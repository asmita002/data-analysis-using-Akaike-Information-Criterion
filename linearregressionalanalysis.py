import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from scipy import stats
import seaborn as sns
%matplotlib inline
sns.set()
df = pd.read_excel(r"/Users/anup/Desktop/puredataset.csv") 
df.dropna(inplace=True)
print(df)
df.head(10)

dfa = df.iloc[1:]
x = dfa.drop(["Unnamed: 0"], axis=1).values
y = dfa["Unnamed: 0"].values
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3, random_state=0)

ml=LinearRegression()
ml.fit(x,y)
y_pred = ml.predict(x)
print(y_pred)

plt.figure(figsize = (10, 9))
plt.scatter(y, y_pred)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted')

fitted_data, fitted_lambda = stats.boxcox(y)
fitted_lambda = round(fitted_lambda, 2)
print(fitted_lambda)
