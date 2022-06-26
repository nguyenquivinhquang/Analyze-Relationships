import os
import numpy as np
import pandas as pd
from preprocessData import PreprocessData

# Define ROOT directory:
ROOT = "./dataset/DailyClimate"


class DailyClimate(PreprocessData):

    def __init__(self, ROOT, dataset_name="DailyDelhiClimateTrain.csv"):

        self.dataframe = pd.read_csv(os.path.join(ROOT, dataset_name))

        self.cleanup()
        return

    def convert2Year(self, df):
        """
            + Convert format in column "date" from "year-month-date" to "year"
            + Rename column "date" to column "YEAR". 

        Args:
            df (dataframe)
        """

        df['date'] = df['date'].apply(lambda x: x.split('-')[0])

        df.rename(columns={'date': 'YEAR'}, inplace=True)

        return df

    def cleanup(self):
        """
            Preprocess data:
                + Changing format of column "date"
                + Renaming column "date_time" to "Year"
                + Group dataframe by Year with average each colimn
        """
        df = self.convert2Year(self.dataframe)

        df = df.groupby("YEAR").mean().reset_index()
        df = df.astype({'YEAR':'int'})
        self.dataframe = df
        return

  

if __name__ == '__main__':

    Dataframe = DailyClimate(ROOT)
    print(Dataframe.data)