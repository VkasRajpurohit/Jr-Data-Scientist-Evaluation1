import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder


class DataPreprocessing:
    """This class will preprocess the data.
       Written by : Vikram Singh
       Date: 04/29/2022"""

    def __init__(self):
        pass

    def basic_info(self, data):
        """Method Name: basic_info
           Description: It will display basic information about the data like shape of data,
           column present & other general summary information."""
        try:
            print('Shape of the dataset: ', data.shape)
            print('\nColumns present: {} \n'.format(data.columns))
            data.info()  # data summary
        except Exception as e:
            print('Unable to process request: ', e)

    def convert_date_time(self, data):
        """Method Name: convert_date_time
           Description: It will convert datetime object columns to pandas datetime"""
        try:
            data['Date'] = pd.to_datetime(data['Date'])
            data['Date of Last Description Change'] = pd.to_datetime(data['Date of Last Description Change'])
            new_data = data
            return new_data
        except Exception as e:
            print('Unable to process request: ', e)

    def is_null_present(self, data):
        """Method Name: is_null_present
           Description: It will check the null values present in data for each column"""
        null_present = False
        try:
            null_counts = data.isna().sum()  # check for the count of null values per column
            for i in null_counts:
                if i > 0:
                    null_present = True
                    break
            if (null_present):  # see which columns have null values
                dataframe_with_null = pd.DataFrame()
                dataframe_with_null['columns'] = data.columns
                dataframe_with_null['missing values count'] = np.asarray(data.isna().sum())
                print(dataframe_with_null)
            return null_present
        except Exception as e:
            print('Unable to process request: ', e)

    def cat_feature_unique_values(self, data):
        """Method Name: cat_feature_unique_values
           Description: It will display categorical/object features with unique values count."""
        print('Unique values for categorical features --')
        try:
            for col in data.columns:
                if data[col].dtype == object:
                    print('{} : {}'.format(col, data[col].nunique()))
        except Exception as e:
            print('Unable to process request: ', e)

    def label_encoder(self, data):
        """Method Name: label_encoder
           Description: It will convert categorical features into numeric using LabelEncoder"""
        # from sklearn.preprocessing import LabelEncoder
        le = LabelEncoder()
        try:
            cat_features = data.columns[data.dtypes == object].tolist()
            data[cat_features] = data[cat_features].apply(lambda cols: le.fit_transform(cols))
            new_data = data
            return new_data
        except Exception as e:
            print('Unable to process request: ', e)


class DisplayCorrelation:
    """This class will display correlation for the data.
       Written by : Vikram Singh
       Date: 04/29/2022"""

    def __init__(self):
        pass

    def corr_heatmap(self, data):
        """Method Name: corr_heatmap
           Description: It will display correlation with heatmap for the data"""
        try:
            corr = data.corr(method='spearman')
            plt.figure(figsize=(15, 6))
            plt.title('Checking correlation with heatmap', fontsize=22, fontweight='bold')
            sb.heatmap(corr, annot=True, cmap='Accent', linecolor='black', linewidths=0.05,
                       xticklabels=corr.columns, yticklabels=corr.columns, cbar=True)
            plt.show()
        except Exception as e:
            print('Unable to process request: ', e)