"""Data processing in preparation for figure/table creation. When querying a database,
these methods are meant to be called on DataFrames at some point AFTER the query has been received.

Functions
    transform_measurement

Variables:
    sample_data
"""

import pandas as pd


def transform_measurement(input_df: pd.DataFrame) -> pd.DataFrame:
    """This is a template function, meant to perform processing on some DataFrame

    Args:
        input_df (pd.DataFrame): DataFrame to process

    Returns:
        pd.DataFrame: Resulting DataFrame after processing
    """
    pass


# dummy data
sample_data = pd.DataFrame({
    "Dates": ["01-Jan-2023", "02-Jan-2023", "03-Jan-2023", "04-Jan-2023", "05-Jan-2023", "06-Jan-2023", "07-Jan-2023"],
    "Sales": [2054, 1533, 1741, 1832, 1476, 1759, 1799]
})
