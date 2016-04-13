from config import *
from sqlite3Connection import *
from encoder import *
import pandas as pd
import numpy as np
from sklearn import linear_model

# sample count per class
samplesCountList = []
for label in classLabels:
	queryString = "SELECT COUNT("+str(classTitle)+") FROM "+str(trainingDataTable)+" WHERE "+str(classTitle)+" = "+str(label)+";"
	count = loadDataFrame(queryString)['COUNT('+str(classTitle)+')'].tolist()[0]
	samplesCountList.append(count)

samplesCount = min(samplesCountList)

# balanced dataframe for training

df = pd.DataFrame()
for label in classLabels:
	queryString = "SELECT * FROM "+str(trainingDataTable)+" WHERE "+str(classTitle)+" = "+str(label)+" ORDER BY RANDOM() LIMIT "+str(samplesCount)+";"
	tempDF = loadDataFrame(queryString)
	df = pd.concat([df, tempDF])
	
dfLength =  len(df)

# subset with columns specified in the config file
subsetDF = df[classification_InputColumns_WithTarget]


# encoding of categorical variables
if classification_hasCategoricalColumns == True:
	subsetDF_Encoded = MultiColumnLabelEncoder(columns = classification_CategoricalColumns_Encoder).fit_transform(subsetDF)
else:
	subsetDF_Encoded = subsetDF

	

dfLength = len(subsetDF_Encoded)


# get splitting indicies
trainLen = int(dfLength*trainPercentage)
#testLen  = int(dfLength*(1-trainPercentage))

# to shuffle the rows in the dataframe
subsetDF_Encoded = subsetDF_Encoded.sample(frac=1).reset_index(drop=True)


# get training and test sets
training = subsetDF_Encoded[:trainLen]
testing = subsetDF_Encoded[trainLen:]


featureNames = [col for col in subsetDF_Encoded.columns if col != classTitle]

trainFeatures = training[ featureNames ].values
trainClasses  = training[ classTitle   ].values

testFeatures = testing[ featureNames ].values
testClasses  = testing[ classTitle   ].values


#classifier = linear_model.SGDClassifier()
classifier = linear_model.LogisticRegression()
#classifier = SVC(kernel="linear")
classifier.fit(trainFeatures, trainClasses)


# scoring for evaluation
score = classifier.score(testFeatures, testClasses)
print score
