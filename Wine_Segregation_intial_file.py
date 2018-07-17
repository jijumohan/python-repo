# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 19:21:09 2018

@author: Jijumn
"""

#full cycle of Data science

import pandas as pd
import numpy as np
import pickle

#importing data set and separating Labels & Features

#importing data set and splitting as test and train set

Dataset = pd.read_csv("winequality-red.csv", delimiter=';')
X_train, X_test, y_train, y_test = train_test_split(df.drop('quality', axis=1), df['quality'], test_size=0.25, random_state=1)
#Getting only the column quality

label = Dataset['quality']

#splitting of data into X
X = Dataset.iloc[:, 0:11].values
y = Dataset.iloc[:, 11].values

#getting every column except quality

features = Dataset.drop('quality', axis=1)

#creation of linear model

from sklearn import linear_model

#Defining the linear regression estimator & training with 
regr = linear_model.LinearRegression()


#fitting the regressor to the model
regr.fit(features,label)

#using our trained model to predict fake wine
#print regr.predict([[7.4,0.66,0,1.8,0.075,13,40,0.9978,3.51,0.56.9.4]]).tolist()

#print 

regr.predict([[7.4,0.66,0,1.8,0.075,13,40,0.9978,3.51,0.56,9.4]]).tolist()

#Importing & exporting python model

#serializing our model to a file called model.pkl
#exporting the model

pickle.dump(regr, open("model.p", "wb"))

#loading a model from a file called model.pl

model = pickle.load(open("model.p","rb"))



from flask import Flask
from flask import request

#code which helps to initialize the server
app = Flask(__name__)

#getting trained model from a file we created earlier

model = pickle.load(open("model.p", "rb"))

#defining a /hello route for only post requests
@app.route('/predict', methods=['POST'])
def predict():
    #grabs the data tagged as name
    #name = request.get_json()['name']
    feature_array = request.get_json()['feature_array']
    
    #our model rates wine based on the input array
    prediction = model.predict([feature_array]).tolist()
    
    #preparing a response object and storing the model's prediction
    response = {}
    response['predictions'] = prediction
    
    #sending a hello back to the requester
    #return "Hello " + name

    #sending our response object back as json
    return Flask.jsonify(response)
