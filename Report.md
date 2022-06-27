
# Problem:

Analyze the relationship among three pieces of information:

+ [https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india](https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india "https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india")-
+  [https://www.kaggle.com/datasets/mahendran1/weather-data-in-india-from-1901-to-2017](https://www.kaggle.com/datasets/mahendran1/weather-data-in-india-from-1901-to-2017 "https://www.kaggle.com/datasets/mahendran1/weather-data-in-india-from-1901-to-2017") 
+  [https://www.kaggle.com/datasets/hiteshsoneji/historical-weather-data-for-indian-cities](https://www.kaggle.com/datasets/hiteshsoneji/historical-weather-data-for-indian-cities "https://www.kaggle.com/datasets/hiteshsoneji/historical-weather-data-for-indian-cities") 
+ [https://www.kaggle.com/datasets/sumanthvrao/daily-climate-time-series-data](https://www.kaggle.com/datasets/sumanthvrao/daily-climate-time-series-data "https://www.kaggle.com/datasets/sumanthvrao/daily-climate-time-series-data")
+  [https://www.kaggle.com/datasets/lakshyaag/india-trade-data](https://www.kaggle.com/datasets/lakshyaag/india-trade-data "https://www.kaggle.com/datasets/lakshyaag/india-trade-data")


# Solution:


## Exploring data:

From the problem above, we have five types of datasets. For each type of dataset, I will explore it by visualization and check if this dataset has a missing value or not. If the dataset has missing values, I will check can I drop the row that has missing values or fill it with 0. Now I will go into detail about each type of dataset.

### 1. Air Quality Data in India (2015 - 2020):
Figure 1 is described the first five rows of the dataset. We can easily see that this dataset has nan value in some rows. Therefore, I need to find that these missing values can negatively affect our dataset. By searching the Kaggle code of this dataset, I see that there exists a notebook that calculates the AQI and AQI_bucket. The AQI(Air quality) is one of our columns in the dataset, and it is calculated based on all the remaining columns (except AQI_bucket). Therefore, I decided that I would fill the nan values with zero, then recalculate the AQI and compare it with the original one. If the accuracy is more than 95%, it is acceptable if I replace the nan value with zero(Except for the AQI and AQI_bucket).


![Figure 1](https://lh3.googleusercontent.com/LQFYwLOv-sDSpnEQzWd3BeipedVpAKu8ROvmUgijRz9SYz9We-Svd766i854ZyTDD7_E2O1V14ZtjIP_QB8IsT8VrtrNzeUh960Aok-Mvth2XfDQvM3Up0WU01aTil0KZAdYVqvUL0JAXXh8Lw )


Luckily, the accuracy is 99.814%. Therefore, I will fill all missing values with 0.

### 2. DailyClimate:
The figure below is the first five rows in the dataset.

**![Figure 2 ](https://lh4.googleusercontent.com/ntJVTKochVerd9PyK9iNdSre_uBCoO9rtpSkv26Txf1Hh-09CPblpTaUJQeprPpg-NaV-crdTUOFMfvf_RUiEv_g0u3SjZJXF-XwL7Rb0Pp5TXyzHOrNZ2lNCb_B_CDJyGYcwrOs0Ew_12BLEg)**
 
 Luckily this dataset does not have any missing values. Therefore, I just use this dataset.
**![](https://lh4.googleusercontent.com/iKtUo-DkiX5-qi6Yo4p4MHI20W_kri69kP8lvVpwzQXPP8ZEt36aRwQ0BCoY-cmjQE_a8eKzI-Q7WJMHyf1NoVwvpExw_KHrY_Ja7b1My2AV4KkEXvGyugkcijd6VkjE8mlxFu1Wam0J7t2v2Q)**

### 3. Trade data:
This data includes export and import. The overview of two of these is in the picture below.
**![](https://lh5.googleusercontent.com/Bro6a3OWIUH8fO6wD1DVaCMvTsD5zVaAgO0kxAvzqShMxmzLVq8UG-bERWhtzgNwXe-xob73nx3VezvljY1P03uSvEhJx71UpROhY-I39NIsepeBOgxFKZWtvyOaxPilZN-aMkzZCLBCc1N3VA)**



Both types in this dataset have some Nan values in the Value column and UNSPECIFIED in the country row. For the nan in the value column, with nan value, we cannot keep track of the value that  Commodity is exported to or imported from any country. UNSPECIFIED in the country row also makes us unable to track where Commodity is exported to or imported from. These are why I will drop all the rows that have UNSPECIFIED in the country row or nan in the value column.

### 4	. Historical Weather Data for Indian Cities:

This dataset contains hourly weather data from 01-01-2009 to 01-01-2020. There are 10 cities in this dataset. The data of each city is for more than 10 years.

The picture above is the overview of one of the cities in the dataset.
**![](https://lh6.googleusercontent.com/X0rbaqdITpq1Us9ucOpJBGXyJf4DTF6_j1MOALXx6VlQB0-jOLwqxYuJcrFz5h5hytR_O3hYCAppTimR-n8-cAgXPJgu2ESnZLdW11SChJHi3v6FAIbhUNQmL6nvQHtMSgaWtvPoVp5nlqm7Qw)**

### 5	. Weather Data in India:
This dataset contains mean temperature in India from 1901 to 2017. This dataset is clean, without any missing value.
The picture below is the overview of this dataset.
**![](https://lh3.googleusercontent.com/rzZJo2E4kEgxnsd5wES7KAKyL9E9GpwW0WIwAvWAp4dkee7ctlEiQZiLLHQQloLap6PUvneKKxJBFTjsvFNGkKwK3Rv1hgdeKuD50iw4AqJ_n5LpwuAXX-Q-13bk5sbuBOKewy0EBeYar5TAmA)**

### Viewpoint
After exploring all these datasets, I realize that the time value of all datasets is not the same. It means that some datasets have year only, some have year-month-day, and some have year-moth-day-time. The range year of all datasets does not intersect much. Just only three years: 2015, 2016, and 2017. However, I just need to combine three of five datasets to find the relationship. From my instution, we need to find the relationship of trade data with all remaining values. This means how another attribute affects the trade data throughout each year. Therefore, I will choose the label, or Y is (Year, Commodity), and all remaining attributes is X.
## Preprocessing  data:

+ Air Quality Data: 
	+ Remove column City, AQI_Backet.

	+ Drop row which have nan values in AQI.

	+ Fill missing value with 0.

	+ Change format of column "Date" to "Year".

	+ Group by year with average method.
	+ Rename column Date to YEAR

+ DailyClimate:
	+ Change format of column "Date" to "Year". 
	+ Group by year with average method.
	+ Rename column "Date" to "YEAR".
+ Historical Weather Data for Indian Cities:
	+ Merge dataframe of each city together

	+ Change format of column "date_time"

	+ Rename column "date_time" to "YEAR"

	+ Group dataframe by Year with average each column
+ Weather Data in India:
	+ Create the temperature_mean column by average temperature month in year.
	+ Drop all the column temperate month

I will create the temp dataframe by combining all dataframe above and the index of this dataframe is YEAR COLUMN

+ Trade data:
	+	Grouping export and import into one dataframe
	+	Group by year with sum method
	+	Rename the year column to YEAR

The final dataframe is the combination of  Trade data and temp dataframe.

## Analyze the relationship


My approach to this problem is to find all attributes' relationships with the trade data. It means how other attributes have any affinity for the Commodity.

For example, 
$\text{The import AIRCRAFT, SPACECRAFT, AND PARTS THEREOF} = 1858.6676 * \text{Temperature\_Mean} + 1366.8223 * \text{visibility} + (-4.41e+04) * \text{HeatIndexC} + (4.221e+04)* \text{FeelsLikeC} + -0.0506 * \text{ Difference}+ -256.3637 * \text{mintempC} + 1 * (1.212e+04)$


The problem is to analyze the relationship between three pieces of information. The first is Trade_data. Therefore two remainings are the combination of two of the other dataset. With three datasets, I will choose Trade_data to work like $Y$ and another work like $X$. It means that I predict $Y$ based on $X$ by using regression.

With a set of $X$, I will find $X$'s most petite subset attributes that can work well to predict $Y$. When having the most petite subset, I use F-test to conclude that the input model has a relationship with the output. In other words, $Y$ is related to all independent variables in subset $X$.

The explanation of my work is in file: ```f-test.ipynb```

## Result

With the pair dataset: trade_data,  Weather Data in India, Historical Weather Data for Indian Cities:

| |      Import|  Export|
|:----------|:-------------:|:------:|
| Has relationship|  96 | 93|
| Has not relationship |    2|   5 |


With the pair dataset: trade_data,  DailyClimate, Historical Weather Data for Indian Cities:

| |      Import|  Export|
|:----------|:-------------:|:------:|
| Has relationship|  95 | 95|
| Has not relationship |    5|   3 |


The actual relationship and parameter is store in ```Output/```


## Conclusion:

All the thing in this report is everything I've done in the past three days. This field is a new field for me. That's why my solution can have some naive errors. I would be happy if you could tell me those mistakes. In the future, I need to find another way to solve some Commodity with no relationship and find another approach for this kind of problem.