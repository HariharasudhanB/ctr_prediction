from config import *
from sqlite3Connection import *
from encoder import *
import pandas as pd
import numpy as np
from sklearn import linear_model


samplesCountList = []
for label in classLabels:
	queryString = "SELECT COUNT("+str(classTitle)+") FROM "+str(trainingDataTable)+" WHERE "+str(classTitle)+" = "+str(label)+";"
	count = loadDataFrame(queryString)['COUNT('+str(classTitle)+')'].tolist()[0]
	samplesCountList.append(count)

samplesCount = min(samplesCountList)


df = pd.DataFrame()
for label in classLabels:
	queryString = "SELECT * FROM "+str(trainingDataTable)+" WHERE "+str(classTitle)+" = "+str(label)+" ORDER BY RANDOM() LIMIT "+str(samplesCount)+";"
	tempDF = loadDataFrame(queryString)
	df = pd.concat([df, tempDF])
	
subsetDF = df[classification_InputColumns_WithTarget]


if classification_hasCategoricalColumns == True:
	subsetDF_Encoded = MultiColumnLabelEncoder(columns = classification_CategoricalColumns_Encoder).fit_transform(subsetDF)
else:
	subsetDF_Encoded = subsetDF

featureNames = [col for col in subsetDF_Encoded.columns if col != classTitle]

trainFeatures = subsetDF_Encoded[ featureNames ].values
trainClasses  = subsetDF_Encoded[ classTitle   ].values

# build classiier and fit
classifier = linear_model.LogisticRegression()
classifier.fit(trainFeatures, trainClasses)

print 'Classifier fitted and saved as a pkl file with name : model.pkl'

from sklearn.externals import joblib
joblib.dump(classifier, 'model.pkl') 
