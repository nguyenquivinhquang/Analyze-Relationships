import pandas as pd
import numpy as np
import os
import aqi_city
import daily_climate
import trade_data
import weather_India_data
import warnings

warnings.filterwarnings('ignore')
# Define root
ROOT = './dataset'

# Declare class
aqi_data = aqi_city.AIQCity(os.path.join(ROOT, "AirQuality"), "city_day.csv")
climate_data = daily_climate.DailyClimate(os.path.join(ROOT, "DailyClimate"))
trade_data = trade_data.TradeData(os.path.join(ROOT, "TradeData"))
weather_country_data = weather_India_data.WeatherCountry(os.path.join(ROOT, "WeatherData"))
weather_cities_data = weather_India_data.WeatherCities(os.path.join(ROOT, "WeatherData"))

# Merge  dataframes in to a list
dataframes = [weather_country_data, weather_cities_data]

# Output filename
filename = "datasettrade-weatherCities-weatherIndian_v2.csv"

# Find the range of year that all dataset all have

lower_year, upper_year = 0, 20000

for dataframe in dataframes:
    min_year, max_year = 20000, -1
    for year in dataframe.data["YEAR"].tolist():
        min_year = min(year, min_year)
        max_year = max(year, max_year)
    lower_year = max(lower_year, min_year)
    upper_year = min(upper_year, max_year)
print(lower_year, upper_year)

# Filter Year, just keep row in range [lower_year, upper_year]
for dataframe in dataframes:
    dataframe.filter_in_range(lower_year, upper_year)

# Merge all data to one and get the final dataframes
df = dataframes[0].data

for i in range(1, len(dataframes)):
    for col in dataframes[i].data:
        if col == 'YEAR':
            continue
        df[col] = dataframes[i].data[col].copy()

# Remove the column index
df = df.drop(['index'], axis=1)

finalDataframe = trade_data.data
print(df.head())

finalDataframe[df.columns.tolist()[1:]] = pd.DataFrame([np.zeros(len(df.columns.tolist()[1:]))],
                                                       index=df.index)
rownames = df.columns.tolist()[1:]
finalDataframe = finalDataframe[finalDataframe.YEAR.between(max(lower_year, 2010),
                                                            min(upper_year, 2018))].reset_index()
finalDataframe = pd.DataFrame(finalDataframe)

# Save the index of a column name
rehash = {}
for (idx, colName) in enumerate(finalDataframe):
    rehash[colName] = idx

for (idx, rowTrade) in enumerate(finalDataframe.itertuples()):
    tempRow = df[df.YEAR == rowTrade.YEAR]
    for (y, value) in enumerate(rownames):
        finalDataframe.iat[idx, rehash[value]] = tempRow[value]

finalDataframe = finalDataframe.drop(['index'], axis=1)

# save
print(os.path.join(ROOT, "datasetGenerate") + filename)
finalDataframe.to_csv("datasetGenerate/" + filename)
