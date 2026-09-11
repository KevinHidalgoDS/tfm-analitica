#!/usr/bin/env python
"""Módulo de procesamiento y comparación de garantías bancarias.

Este módulo proporciona funciones para descargar archivos, conectar a un Key Vault,
generar archivos Excel, comparar textos y realizar diversas operaciones relacionadas
con las garantías bancarias.

Programa: functions.py

Soporte: kevin.hidalgo@globalmvm.com

Versión: 2.0.0

Lenguaje: Python 3.11.9

CD: 20230809

LUD: 20250820

Comentarios:
    * 20250430 Kevin Hidalgo -> PEP8.
    * 20250523 Kevin Hidalgo -> funciones candidatas para reducir complejidad.
    * 20250617 Kevin Hidalgo -> HU 447455
    * 20250820 Kevin Hidalgo -> HU 465025
"""

__authors__ = ["David Imbajoa"]
__contact__ = "david.imbajoa@globalmvm.com"
__copyright__ = "Copyright 2023, MVM ingenieria de software"
__credits__ = ["David Imbajoa"]
__email__ = "david.imbajoa@globalmvm.com"
__status__ = "Desarrollo"
__version__ = "1.0.0"
__date__ = "2023-08-08"

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
