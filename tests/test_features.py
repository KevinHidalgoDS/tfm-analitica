#!/usr/bin/env python
"""Tests para el módulo OCR.

Este módulo contiene pruebas unitarias para las funciones del módulo OCR, incluyendo la lectura de
documentos en memoria y la interacción con la API de reconocimiento de formularios de Azure.

Tema: Pruebas unitarias para OCR
Programa: test_ocr.py
Soporte: kevin.hidalgo@globalmvm.com
versión: 2.0.0
lenguaje: Python 3.11
CD: 20230809
LUD: 20250523
Comentarios:
20250523 Kevin Hidalgo -> corrección e incremento de cobertura.
"""

import pandas as pd
import pytest
from src.features import clean_transactions


def test_clean_transactions_filters_by_threshold_and_removes_nulls() -> None:
    """Debe filtrar montos inferiores al umbral y eliminar valores nulos."""
    df = pd.DataFrame(
        {
            "monto": [100.0, 50.0, 200.0, 25.0],
            "descripcion": ["A", "B", None, "D"],
        }
    )

    result = clean_transactions(df, threshold=50.0)

    expected = pd.DataFrame(
        {
            "monto": [100.0, 50.0],
            "descripcion": ["A", "B"],
        },
        index=[0, 1],
    )

    pd.testing.assert_frame_equal(result, expected)


def test_clean_transactions_uses_zero_as_default_threshold() -> None:
    """Debe utilizar cero como umbral cuando no se proporciona."""
    df = pd.DataFrame(
        {
            "monto": [-10.0, 0.0, 100.0],
            "descripcion": ["A", "B", "C"],
        }
    )

    result = clean_transactions(df)

    expected = pd.DataFrame(
        {
            "monto": [0.0, 100.0],
            "descripcion": ["B", "C"],
        },
        index=[1, 2],
    )

    pd.testing.assert_frame_equal(result, expected)


def test_clean_transactions_raises_value_error_without_monto() -> None:
    """Debe lanzar ValueError si no existe la columna monto."""
    df = pd.DataFrame(
        {
            "descripcion": ["A", "B"],
        }
    )

    with pytest.raises(
        ValueError,
        match="El DataFrame debe contener la columna 'monto'",
    ):
        clean_transactions(df)

# Para ejecutar las pruebas desde la línea de comandos
if __name__ == '__main__':
    # Usar unittest.main() para descubrir y ejecutar todos los tests
    # `argv=['first-arg-is-ignored']` y `exit=False` son buenas prácticas para
    # permitir la ejecución dentro de IDEs o scripts sin que unittest.main()
    # intente procesar los argumentos del script principal y cause un SystemExit.
    # unittest.main(argv=['first-arg-is-ignored'], exit=False)
    pytest.main()
    # exit_code = pytest.main(['-v', 'tests/'])
    # raise SystemExit(exit_code)
