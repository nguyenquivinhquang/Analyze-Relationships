
# Problem:

Analyze the relationship among three pieces of information:

+ [https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india](https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india "https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india")-
+  [https://www.kaggle.com/datasets/mahendran1/weather-data-in-india-from-1901-to-2017](https://www.kaggle.com/datasets/mahendran1/weather-data-in-india-from-1901-to-2017 "https://www.kaggle.com/datasets/mahendran1/weather-data-in-india-from-1901-to-2017") 
+  [https://www.kaggle.com/datasets/hiteshsoneji/historical-weather-data-for-indian-cities](https://www.kaggle.com/datasets/hiteshsoneji/historical-weather-data-for-indian-cities "https://www.kaggle.com/datasets/hiteshsoneji/historical-weather-data-for-indian-cities") 
+ [https://www.kaggle.com/datasets/sumanthvrao/daily-climate-time-series-data](https://www.kaggle.com/datasets/sumanthvrao/daily-climate-time-series-data "https://www.kaggle.com/datasets/sumanthvrao/daily-climate-time-series-data")
+  [https://www.kaggle.com/datasets/lakshyaag/india-trade-data](https://www.kaggle.com/datasets/lakshyaag/india-trade-data "https://www.kaggle.com/datasets/lakshyaag/india-trade-data")


# Solution:


## Preprocessing data:

From the problem above, we have five types of datasets. For each type of dataset, I will explore it by visualization and check if this dataset has a missing value or not. If the dataset has missing values, I will check can I drop the row that has missing values or fill it with 0. Now I will go into detail about each type of dataset.

### Air Quality Data in India (2015 - 2020):
Figure 1 is described the first five rows of the dataset. We can easily see that this dataset has nan value in some rows. Therefore, I need to find that these missing values can negatively affect our dataset. By searching the Kaggle code of this dataset, I see that there exists a notebook that calculates the AQI and AQI_bucket. The AQI(Air quality) is one of our columns in the dataset, and it is calculated based on all the remaining columns (except AQI_bucket). Therefore, I decided that I would fill the nan values with zero, then recalculate the AQI and compare it with the original one. If the accuracy is more than 95%, it is acceptable if I replace the nan value with zero(Except for the AQI and AQI_bucket).


![Figure: 1](https://lh3.googleusercontent.com/LQFYwLOv-sDSpnEQzWd3BeipedVpAKu8ROvmUgijRz9SYz9We-Svd766i854ZyTDD7_E2O1V14ZtjIP_QB8IsT8VrtrNzeUh960Aok-Mvth2XfDQvM3Up0WU01aTil0KZAdYVqvUL0JAXXh8Lw)
