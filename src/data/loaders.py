# src/data/loaders.py
from pathlib import Path
from typing import Union
import pandas as pd

def read_csv(path: Union[str, Path], **kwargs) -> pd.DataFrame:
    """CSV loader with UTF-8 default and Path safety."""
    return pd.read_csv(Path(path), encoding=kwargs.pop("encoding", "utf-8"), **kwargs)
