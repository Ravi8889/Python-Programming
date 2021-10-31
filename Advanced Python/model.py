import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error ,f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from imblearn.over_sampling import RandomOverSampler 
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
#from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from datetime import datetime 
import warnings
warnings.filterwarnings('ignore', 'statsmodels.tsa.arima_model.ARMA',FutureWarning)
import pickle
## Reading the data set## Feature Engineering Pipeline
df =pd.read_csv(r"adult.csv")
## dealing with the noise data ##(?)
df=df.replace("?",np.nan)
cols =['workclass','occupation','country']
for i in cols:
    df[i].fillna(df[i].mode()[0],inplace=True)
## converting the Categorical data into numerical data
le =LabelEncoder()
for j in df.columns:
    if df[j].dtypes =='object':
        df[j]=le.fit_transform(df[j])
# Split the Data set 
X =df.drop(columns ='salary',axis=1)
Y =df['salary']


#Feature Selection
best_features =SelectKBest(score_func =chi2,k=5)
best_features.fit(X,Y)
dfscores =pd.DataFrame(best_features.scores_)
dfcolumns =pd.DataFrame(X.columns)
df_best_features =pd.concat([dfcolumns,dfscores],axis=1)
df_best_features.columns=['Attributes','Scores']
df_best_features #based on values select the best features
X=X.drop(['fnlwgt','country'],axis=1)

# dealing with the Imbalenced data  set 
resampling =RandomOverSampler(random_state =42)
resampling.fit(X,Y)
reX,ReY =resampling.fit_resample(X,Y)
# Feature Scaling
def norm_data(i):
    x=(i-i.min())/(i.min()-i.max())
    return x
df_norm =norm_data(reX)

# Splitting the Data set into Train and Test for model Creation
X_train,X_test,Y_train,Y_test= train_test_split(reX,ReY,test_size =0.2,random_state=42)

# Final model Creation
model =RandomForestClassifier(n_estimators =40,max_depth= 102,random_state =42)
model  =model.fit(X_train,Y_train)
y_pred =model.predict(X_test)
