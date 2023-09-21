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


def split_data(df):
    train =  df[df.transaction_date < '2019-04-22']
    test = df[df.transaction_date >= '2019-04-22']
    return train, test


def get_store_sales(df):
    stores_grouped = df.groupby('sales_outlet_id')['line_item_amount'].sum().reset_index()
    plt.figure(figsize=(12, 6))
    sns.barplot(data=stores_grouped, x='sales_outlet_id', y='line_item_amount')
    plt.title('Sales by store for first 3 weeks')
    plt.ylabel('Amount')
    plt.show()
    
    
    
def daily_company_sales(df):
    daily_sales = df.groupby('transaction_date')['line_item_amount'].sum().reset_index()
    plt.figure(figsize=(12, 6))
    plt.title('Daily company sales for 3 weeks')
    sns.lineplot(data=daily_sales, x='transaction_date', y='line_item_amount', marker='o')
    plt.xticks(daily_sales.transaction_date, rotation=90)
    plt.ylabel('Amount')
    plt.show()
    
    
def daily_store_sales(df):
    daily_store_sales = df.groupby(['transaction_date', 'sales_outlet_id'])['line_item_amount'].sum().reset_index()
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=daily_store_sales, x='transaction_date', y='line_item_amount', marker='o', hue='sales_outlet_id')
    plt.xticks(daily_store_sales.transaction_date, rotation=90)
    plt.title('Daily Sales by Store')
    plt.ylabel('Amount')
    plt.show()
    
    
def best_sell_product(df):
    product_grouped = df.groupby('product_id')['line_item_amount'].sum().reset_index()
    products = pd.read_csv('product.csv')
    product_grouped = pd.merge(product_grouped, products, on='product_id')
    product_grouped = product_grouped.sort_values('line_item_amount', ascending=False)
    plt.figure(figsize=(15, 6))
    sns.barplot(data=product_grouped, x='product', y='line_item_amount')
    plt.xticks(rotation=90)
    plt.title('Products by Revenue')
    plt.ylabel('Amount')
    plt.show()
    
    
def best_sell_group(df):
    products = pd.read_csv('product.csv')
    product_grouped = df.groupby('product_id')['line_item_amount'].sum().reset_index()
    product_grouped = pd.merge(product_grouped, products, on='product_id')
    product_grouped = product_grouped.sort_values('line_item_amount', ascending=False)
    group_sums = product_grouped.groupby('product_group')['line_item_amount'].sum().reset_index()
    plt.figure(figsize=(15, 6))
    sns.barplot(data=group_sums, x='product_group', y='line_item_amount')
    plt.ylabel('Amount')
    plt.show()