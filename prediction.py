from config import *
from sqlite3Connection import *
from encoder import *
import pandas as pd
import numpy as np
from sklearn import linear_model

# load pkl file to classifier
from sklearn.externals import joblib
classifier = joblib.load('model.pkl') 

# get the test set from sqlite
queryString = "SELECT * FROM "+str(testingDataTable)
testDF = loadDataFrame(queryString)

# filter columns from config file mentioned input columns
subsetTestDF = testDF[prediction_InputColumns]

# encode categorical values
if classification_hasCategoricalColumns == True:
	subsetTestDF_Encoded = MultiColumnLabelEncoder(columns = prediction_CategoricalColumns_Encoder).fit_transform(subsetTestDF)
else:
	subsetTestDF_Encoded = subsetTestDF

# features to pass for prediction
testFeatures = subsetTestDF_Encoded.values

result = classifier.predict(testFeatures)

final = pd.DataFrame(result, columns=['predictions']).to_csv('predictions.csv')
print 'predictions are saved in the file named : predictions.csv'
