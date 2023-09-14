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