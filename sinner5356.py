import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pycaret
import sklearn
from sklearn.model_selection import train_test_split
from pycaret.classification import *
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv('C:/Users/User/Desktop/Learing_Money/Class/Python/Final_ML/1million/spotify_data.csv')
data.head()

columns_to_drop = ['Unnamed: 0', 'artist_name', 'track_name', 'track_id', 'year', 'genre']
df = data.drop(columns_to_drop, axis=1)

X = pd.DataFrame(df[['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature']])
y = pd.DataFrame(df[['popularity']])
X.head()

X_train, X_test, y_train, y_test = train_test_split(X, y)

regressor = xgb.XGBRegressor(
    n_estimators=100,
    reg_lambda=1,
    gamma=0,
    max_depth=3
)

regressor.fit(X_train, y_train)

pd.DataFrame(regressor.feature_importances_.reshape(1, -1))

y_pred = regressor.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print('r2: {}'.format(r2))
print('mse: {}'.format(mse))