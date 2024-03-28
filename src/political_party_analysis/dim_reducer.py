import pandas as pd
from sklearn.decomposition import PCA


class DimensionalityReducer:
    """Class to model a dimensionality reduction method for the given dataset.
    1. Write a function to convert the high dimensional data to 2 dimensional.
    """

    def __init__(self, data: pd.DataFrame, n_components: int = 2):
        self.n_components = n_components
        self.data = data
        self.feature_columns = data.columns

    ##### YOUR CODE GOES HERE #####
    def reduce_dimensionality(self) -> pd.DataFrame:
        estimator = PCA(n_components=self.n_components)
        x_pca = estimator.fit_transform(self.data)
        data2 = self.data.reset_index(drop=False)
        df_main = data2[["party_id", "party", "country"]]
        df_pca = pd.DataFrame(x_pca)
        df = pd.merge(df_main, df_pca, left_index=True, right_index=True)
        df.set_index(["party_id", "party", "country"], inplace=True)
        return df
