import os
import numpy as np
import pandas as pd
from preprocessData import PreprocessData
# Define ROOT directory:
ROOT = "./dataset/TradeData/"


# Loading dataset
class TradeData(PreprocessData):

    def __init__(self,
                 ROOT,
                 import_name="2018-2010_import.csv",
                 export_name="2018-2010_export.csv"):
        self.ROOT = ROOT

        # Loading dataset
        self.data_import = pd.read_csv(os.path.join(ROOT, import_name))
        self.data_export = pd.read_csv(os.path.join(ROOT, export_name))

        self.preprocess()

    def cleanup(self, dataset):
        """This function will drop the row has:
            + column country equal to UNSPECIFIED
            + column has Nan value

        Args:
            dataset (dataframe): The dataframe need to be clean

        Returns:
            dataframe: The dataframe after cleaned
        """
        #setting country UNSPECIFIED to nan
        dataset['country'] = dataset['country'].apply(lambda x: np.NaN if x == "UNSPECIFIED" else x)
        #ignoring where import value is 0 .
        dataset = dataset[dataset.value != 0]
        dataset.dropna(inplace=True)
        dataset.year = pd.Categorical(dataset.year)
        dataset.drop_duplicates(keep="first", inplace=True)
        return dataset

    def preprocess(self):

        # Cleaning data
        data_import = self.cleanup(self.data_import)
        data_export = self.cleanup(self.data_export)

        # Grouping data by year
        import_sum = data_import.groupby(['year', "Commodity"]).agg({'value': 'sum'}).reset_index()
        export_sum = data_export.groupby(['year', "Commodity"]).agg({'value': 'sum'}).reset_index()

        # Merge Import, Export, Difference columns into 1 dataframe
        data = import_sum.copy()
        data.rename(columns={'value': 'Import', "year": "YEAR"}, inplace=True)
        data['Export'] = export_sum["value"]
        data['Difference'] = export_sum["value"] - import_sum["value"]
        data = data.astype({'YEAR': 'int'})
        self.dataframe = data
        return

    @property
    def data(self):
        return self.dataframe


if __name__ == '__main__':
    tradeDataframe = TradeData(ROOT)

    dataframe = tradeDataframe.data
    print(dataframe.head(-1))