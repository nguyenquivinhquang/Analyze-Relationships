import os
import numpy as np
import pandas as pd
from preprocessData import PreprocessData

# Define ROOT directory:
ROOT = "./dataset/WeatherData/"


class WeatherCountry(PreprocessData):

    def __init__(self, ROOT, data_name="Weather_Data_India_1901_2017.csv"):
        self.ROOT = ROOT

        # Loading dataset
        self.dataframe = pd.read_csv(os.path.join(ROOT, data_name))

        # Removing the first index column
        self.dataframe = self.dataframe.iloc[:, 1:]

        # preprocess data
        self.cleanup()

    def cleanup(self):
        # Creating the new  Temperature_Mean which is average temperature of 12 months
        self.dataframe["Temperature_Mean"] = self.dataframe.apply(
            lambda row: (row.JAN + row.FEB + row.MAR + row.APR + row.MAY + row.JUN + row.JUL + row.
                         AUG + row.SEP + row.OCT + row.NOV + row.DEC) / 12,
            axis=1)

        # Renaming the columns, just add the "_Temp" at each name
        self.dataframe.rename(columns={
            'JAN': 'JAN_Temp',
            'FEB': 'FEB_Temp',
            'MAR': 'MAR_Temp',
            'APR': 'APR_Temp',
            'MAY': 'MAY_Temp',
            'JUN': 'JUN_Temp',
            'JUL': 'JUL_Temp',
            'AUG': 'AUG_Temp',
            'OCT': 'OCT_Temp',
            'NOV': 'NOV_Temp',
            'SEP': 'SEP_Temp',
            'DEC': 'DEC_Temp'
        },
                              inplace=True)

        # Filter year >= 2010
        self.dataframe = self.dataframe[self.dataframe.YEAR >= 2005].reset_index()

        # Removing the first column which is the old index column
        self.dataframe = self.dataframe.iloc[:, 1:]

        self.dataframe = self.dataframe.astype({'YEAR': 'int'})

        # Drop month temp
        self.dataframe = self.dataframe.drop([
            'JAN_Temp', 'FEB_Temp', 'MAR_Temp', 'APR_Temp', 'MAY_Temp', 'JUN_Temp', 'JUL_Temp',
            'AUG_Temp', 'OCT_Temp', 'NOV_Temp', 'SEP_Temp', 'DEC_Temp'
        ],
                                             axis=1)
        return


class WeatherCities(PreprocessData):

    def __init__(self, ROOT, folder="cities"):

        self.ROOT = os.path.join(ROOT, folder)

        self.dataframe = dict()

        for filename in os.listdir(self.ROOT):
            data = pd.read_csv(os.path.join(self.ROOT, filename))

            data = data.drop(['moonrise', 'moonset', 'sunrise', 'sunset'], axis=1)
            self.dataframe[filename.split('.')[0]] = data

        self.cleanup()
        return

    def convert2Year(self, df):
        """
            + Convert format in column date_time from "year-month-date times" to "year"
            + Rename column date_time to column year. 

        Args:
            df (dataframe)
        """

        df['date_time'] = df['date_time'].apply(lambda x: x.split('-')[0])

        df.rename(columns={'date_time': 'YEAR'}, inplace=True)

        return df

    def cleanup(self):
        """
            Preprocess data:
                + Merge dataframe of each city together
                + Changing format of column "date_time"
                + Renaming column "date_time" to "Year"
                + Group dataframe by Year with average each colimn
        """
        df = self.convert2Year(self.dataframe["bombay"])

        for dataframeName in self.dataframe:
            if dataframeName == "bombay":
                continue
            df = pd.concat([df, self.convert2Year(self.dataframe[dataframeName])], axis=0)

        df = df.groupby("YEAR").mean().reset_index()

        self.dataframe = df

        self.dataframe = self.dataframe.astype({'YEAR': 'int'})

        return


if __name__ == '__main__':
    weatherDataframe = WeatherCountry(ROOT)

    dataframe = weatherDataframe.data
    print(dataframe.head(-1))

    weatherCities = WeatherCities(ROOT)
    dataframeCities = weatherCities.data
    print(dataframeCities.head(5))