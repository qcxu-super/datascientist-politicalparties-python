from pathlib import Path
from typing import List
from urllib.request import urlretrieve

import pandas as pd


class DataLoader:
    """Class to load the political parties dataset"""

    data_url: str = "https://www.chesdata.eu/s/CHES2019V3.dta"

    def __init__(self):
        self.party_data = self._download_data()
        self.non_features = []
        self.index = ["party_id", "party", "country"]

    def _download_data(self) -> pd.DataFrame:
        data_path, _ = urlretrieve(
            self.data_url,
            Path(__file__).parents[2].joinpath(*["data", "CHES2019V3.dta"]),
        )
        return pd.read_stata(data_path)

    def remove_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        """Write a function to remove duplicates in a dataframe"""
        ##### YOUR CODE GOES HERE #####
        df.drop_duplicates(subset=self.index, keep='first', inplace=True)
        df.reset_index(drop=True)
        return df

    def remove_nonfeature_cols(
        self, df: pd.DataFrame, non_features: List[str], index: List[str]
    ) -> pd.DataFrame:
        """Write a function to remove certain features cols and set certain cols as indices
        in a dataframe"""
        ##### YOUR CODE GOES HERE #####
        col = df.columns.difference(non_features)
        df2 = df[col].set_index(index)
        return df2

    def handle_NaN_values(self, df: pd.DataFrame) -> pd.DataFrame:
        """Write a function to handle NaN values in a dataframe"""
        ##### YOUR CODE GOES HERE #####
        empty_ratio = df.isna().sum() / len(df) * 100
        empty_ratio_df = pd.DataFrame(empty_ratio, columns=['empty_ratio'])
        empty_ratio_high_col = list(empty_ratio_df[empty_ratio_df['empty_ratio'] >= 95].index)
        whole_col = df.columns
        df.drop(columns=empty_ratio_high_col, inplace=True)
        df2 = df[whole_col.difference(empty_ratio_high_col)]
        df2.fillna(df2.mean(), inplace=True)
        return df2
    
    def scale_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Write a function to normalise values in a dataframe. Use StandardScaler."""
        ##### YOUR CODE GOES HERE #####
        df_norm = (df - df.min()) / (df.max() - df.min())
        return df_norm


    def preprocess_data(self):
        """Write a function to combine all pre-processing steps for the dataset"""
        ##### YOUR CODE GOES HERE #####
        df2 = self.remove_duplicates(self.party_data)
        df3 = self.remove_nonfeature_cols(df2, self.non_features, self.index)
        df4 = self.handle_NaN_values(df3)
        df5 = self.scale_features(df4)
        return df5
