# Analyze-Relationships
The purpose of this respo is to analyze the relationship among three pieces of information in below datasets:

- https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india
- https://www.kaggle.com/datasets/mahendran1/weather-data-in-india-from-1901-to-2017
- https://www.kaggle.com/datasets/hiteshsoneji/historical-weather-data-for-indian-cities
- https://www.kaggle.com/datasets/sumanthvrao/daily-climate-time-series-data
- https://www.kaggle.com/datasets/lakshyaag/india-trade-data

## Prepare

+ Download dataset from:
    [Link](https://drive.google.com/drive/folders/1lVzvGCXYRYtXJq1lmTtwXPqTGJV7y19M?usp=sharing)
+ Put the dataset downloaded into the forder ```/dataset```

+ Install environment:

    ```pip install -r requirements.txt```

## Preprocess data:

+ Run the following code:

    ```python preProcess/preprocess.py```

+ For edit the pair, go to line 22 which comment is # Merge  dataframes in to a list in file ```preProcess/preprocess.py```

+ The dataset after preprocessing is located at ```datasetGenerate/```
## Find the feature:

+ Run the following code:

    ```f-test.py```
+ The output will store at:
    
    ```Output/```
