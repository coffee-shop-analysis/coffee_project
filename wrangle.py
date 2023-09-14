import pandas as pd
import numpy as np

import matplotlib
import seaborn as sns

import matplotlib.pyplot as plt
import seaborn as sns


import warnings
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', None)


def get_data():
    df = pd.read_csv('201904 sales reciepts.csv')
    return df

def reset_transaction_id(df):
    df.transaction_date = pd.to_datetime(df.transaction_date)
    df.transaction_time = pd.to_datetime(df.transaction_time)
    id = 1
    for current_row in range(len(df)):
        if df.loc[current_row, 'transaction_id'] == 0:
            df.loc[current_row, 'transaction_id'] = id
            for row in range(current_row, len(df)):
                if df.loc[current_row, 'transaction_date'] == df.loc[row, 'transaction_date']:
                    if (df.loc[current_row, 'transaction_time'] == df.loc[row, 'transaction_time'] ) & (df.loc[current_row, 'sales_outlet_id'] == df.loc[row, 'sales_outlet_id']):
                        df.loc[row, 'transaction_id'] = id
                else:
                    break
            id+=1
        else:
            pass
    return df



def data_cleaned(df):
    df.transaction_id = 0
    df = reset_transaction_id(df)
    df.drop(columns=['line_item_id', 'order', 'instore_yn', 'promo_item_yn'], inplace=True)
    df.customer_id = df.customer_id.astype(int)
    df.sales_outlet_id = df.sales_outlet_id.astype(int)
    df.product_id = df.product_id.astype(int)
    df.quantity = df.quantity.astype(int)
    return df