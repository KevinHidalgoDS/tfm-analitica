#!/usr/bin/env python
"""Cliente HTTP para la orquestación y consumo de la API IA OCR BCT.

Proporciona métodos tipados para interactuar con los endpoints de registro,
análisis de malware y procesamiento de documentos. Implementa inyección
segura de credenciales y políticas de reintento transitorias.

Programa: bct_iaocr_client.py

Soporte: kevin.hidalgo@globalmvm.com

Versión: 1.0.0

Lenguaje: Python 3.11.9

CD: 20260917

LUD: 20260918

Comentarios:
    - 20260917 Kevin Hidalgo -> HU 22665.
"""

import pandas as pd


def clean_transactions(df: pd.DataFrame, threshold: float = 0.0) -> pd.DataFrame:
    """Filtra transacciones por debajo de un umbral monetario y elimina nulos.

    Args:
        df (pd.DataFrame): DataFrame crudo con el historial de transacciones.
        threshold (float): Valor mínimo permitido para la transacción.

    Returns:
        pd.DataFrame: DataFrame limpio y filtrado.

    Raises:
        ValueError: Si la columna 'monto' no existe en el DataFrame.
    """
    if "monto" not in df.columns:
        raise ValueError("El DataFrame debe contener la columna 'monto'")

    return df[df["monto"] >= threshold].dropna()
