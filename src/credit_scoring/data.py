from pathlib import Path

import pandas as pd

TARGET = "SeriousDlqin2yrs"
DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "cs-training.csv"


def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    """Carga el dataset de crédito usando la primera columna como índice."""
    return pd.read_csv(path, index_col=0)
