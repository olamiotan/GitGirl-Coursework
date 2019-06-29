#A model to predict if a passenger survived the sinking of the Titanic or not. 
#For each in the test set, a 0 or 1 value is given to predict the variable.

#Import libraries
import numpy as np 
import pandas as pd 
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


#Reading csv file
train_data = pd.read_csv('C://Users/Olamiotan/Desktop/train.csv') 
test_data = pd.read_csv('C://Users/Olamiotan/Desktop/test.csv')


# Using one label encoding on categorival column Sex where male -> 1 and female -> 0
train_data["Sex"] = train_data["Sex"].astype('category')
train_data["Sex"] = train_data["Sex"].cat.codes

test_data["Sex"] = test_data["Sex"].astype('category')
test_data["Sex"] = test_data["Sex"].cat.codes


#Set the "X" and "Y" dataframe values (X = [sex], Y = [survived]) using traindata
X = train_data[['Sex']]
Y = train_data[['Survived']]
 
 
#Trains AI
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=0,)


#Fits the data with the Scikit-Learn Logistic Regression model
model = LogisticRegression(random_state=0, solver='lbfgs')
model.fit(X_train, y_train.values.ravel())


#Tests the model's prediction; [1:10] denotes the first 10 rows
predictions = model.predict_proba(X_test)
print (predictions[1:10])  

predictions = model.predict(X_test)
print (predictions[1:10]) 


#Testing model accuracy
print("Report : ", classification_report(y_test,predictions))
   
    
#Evaluating the Algorithm
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, predictions))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, predictions))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))      
    
    
#Predicting the results using the test data
Z = test_data[['Sex']]
survival = model.predict(Z)
print('Survival array: ', survival)


#Creating a new column Survived to save predictions
test_data['Survived'] = survival
print('Test data with new predicted column Survived: ', test_data())

#Prediction of survival is 0 for male and 1 for female
