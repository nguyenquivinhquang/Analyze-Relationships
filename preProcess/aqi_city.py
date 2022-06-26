import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from preprocessData import PreprocessData
ROOT = './dataset/AirQuality'


class AIQCity(PreprocessData):

    def __init__(self, ROOT, dataset_name):
        self.dataframe = pd.read_csv(os.path.join(ROOT, dataset_name))

        self.cleanup()
        return

    def convert2Year(self, df):
        """
            + Convert format in column "Date" from "year-month-date" to "year"
            + Rename column "date" to column "YEAR". 

        Args:
            df (dataframe)
        """

        df['Date'] = df['Date'].apply(lambda x: x.split('-')[0])

        df.rename(columns={'Date': 'YEAR'}, inplace=True)

        return df

    def cleanup(self):
        """
            Preprocessing data:
                + Remove column City, AQI_Backet
                + Drop row which have nan values in AQI 
                + Fill missing value with 0
                + Change format of row "Date" to "Year"
                + Group by year 
        """
        # Drop rows that has NaN values on AQI
        df = self.dataframe.dropna(subset=['AQI'])

        # Drop columns City and AQI_Bucket
        df = df.drop(columns=['City', 'AQI_Bucket'])

        # Fill nan with 0:
        df = df.fillna(0)

        # Change format and rename column Date
        df = self.convert2Year(df)

        # Group by year and calculate mean
        df = df.groupby("YEAR").mean().reset_index()

        df = df.astype({'YEAR':'int'})

        self.dataframe = df
        return

    @property
    def data(self):
        return self.dataframe


if __name__ == "__main__":
    dataframe = AIQCity(ROOT, "city_day.csv")

    print(dataframe.data.isna().all())
    print(dataframe.data)