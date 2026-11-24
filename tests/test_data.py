from pathlib import Path

from credit_scoring.data import TARGET, load_data

SAMPLE = Path(__file__).parent / "fixtures" / "sample.csv"


def test_load_data_returns_all_rows():
    df = load_data(SAMPLE)
    assert len(df) == 4


def test_target_is_binary():
    df = load_data(SAMPLE)
    assert set(df[TARGET].unique()) <= {0, 1}


def test_missing_income_is_kept_as_nan():
    df = load_data(SAMPLE)
    assert df["MonthlyIncome"].isna().sum() == 1