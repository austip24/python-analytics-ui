"""Load data from database or from files

Functions:
    load_snowflake_data
    load_csv_data
"""


import pandas as pd
from pathlib import Path


def load_snowflake_data() -> pd.DataFrame:
    """This is a template function. The idea for this function is that it would contain
    a query to snowflake or some other database, perform some processing on the data,
    and return the result as a DataFrame

    Returns:
        pd.DataFrame: Query Result
    """
    pass


def load_csv_data(path: Path) -> pd.DataFrame:
    """This is a template function. The idea for this function is that it would read data from
    a csv file, perform some processing on the data, and return the result as a DataFrame

    Args:
        path (Path): path to file

    Returns:
        pd.DataFrame: result
    """
    pass
