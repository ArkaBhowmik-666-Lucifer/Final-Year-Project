from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn import tree
import warnings

warnings.filterwarnings('ignore')
import pickle
df=pd.read_excel('Crop_Recommendation_West_Bengal.xlsx')
print(df.head())
print()
print(df.tail())
print()
print(df.columns)
print()
print(df.shape)
print()
print(df.nunique())
print()
print(df.dtypes)
print()
print(df['Label'].value_counts())
#Seperating features and target label
features = df[['Temperature', 'Humidity', 'pH', 'Rainfall']]
target = df['Label']
labels = df['Label']
# Initializing empty lists to append all model's name and corresponding name
acc = []
model = []
 #Splitting into train and test data
from sklearn.model_selection import train_test_split
Xtrain, Xtest, Ytrain, Ytest = train_test_split(features,target,test_size = 0.2,random_state =2)
#Random Forest
from sklearn.ensemble import RandomForestClassifier
RF = RandomForestClassifier(n_estimators=20, random_state=0)
RF.fit(Xtrain,Ytrain)
predicted_values = RF.predict(Xtest)
x = metrics.accuracy_score(Ytest, predicted_values)
acc.append(x)
model.append('RF')
print("RF's Accuracy is: ", x)
print(classification_report(Ytest,predicted_values))
#Saving trained Random Forest model
import pickle

# Dump the trained Naive Bayes classifier with Pickle
RF_pkl_filename = 'RandomForest.pkl'

# Open the file to save as pkl file
RF_Model_pkl = open(RF_pkl_filename, 'wb')
pickle.dump(RF, RF_Model_pkl)

# Close the pickle instances
RF_Model_pkl.close()

data = np.array([[45, 88, 7.6, 400]])
prediction = RF.predict(data)
print(prediction)
data = np.array([[12, 43, 7.6, 100]])
prediction = RF.predict(data)
print(prediction)
data = np.array([[43,10,6,4000]])
prediction = RF.predict(data)
print(prediction)
data = np.array([[38,20,5,1200]])
prediction = RF.predict(data)
print(prediction)