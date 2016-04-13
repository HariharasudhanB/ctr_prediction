from config import *
from sqlite3Connection import *
from encoder import *
import pandas as pd
import numpy as np
from sklearn.ensemble import ExtraTreesClassifier

from sklearn import linear_model
from sklearn.cross_validation import StratifiedKFold
from sklearn.feature_selection import RFECV

# the below portion get the min count of classes sample

samplesCountList = []
for label in classLabels:
	queryString = "SELECT COUNT("+str(classTitle)+") FROM "+str(trainingDataTable)+" WHERE "+str(classTitle)+" = "+str(label)+";"
	count = loadDataFrame(queryString)['COUNT('+str(classTitle)+')'].tolist()[0]
	samplesCountList.append(count)

samplesCount = min(samplesCountList)

# to get the balanced dataset for training from the db as a dataframe

df = pd.DataFrame()
for label in classLabels:
	queryString = "SELECT * FROM "+str(trainingDataTable)+" WHERE "+str(classTitle)+" = "+str(label)+" ORDER BY RANDOM() LIMIT "+str(samplesCount)+";"
	tempDF = loadDataFrame(queryString)
	df = pd.concat([df, tempDF])
	
dfLength =  len(df)


# subsetting the df with only the mentioned columns in the config file
subsetDF = df[dimensionReduction_InputColumns_WithTarget]


# encodind the categorical columns
if hasCategoricalColumns == True:
	subsetDF_Encoded = MultiColumnLabelEncoder(columns = dimensionReduction_CategoricalColumns_Encoder).fit_transform(subsetDF)
else:
	subsetDF_Encoded = subsetDF


featureNames = [col for col in subsetDF_Encoded.columns if col != classTitle]
X = subsetDF_Encoded[ featureNames ].values
y  = subsetDF_Encoded[ classTitle   ].values


# fit an Extra Trees model to the data
model = ExtraTreesClassifier(n_estimators=2000)
model.fit(X, y)

# display the relative importance of each attribute
print subsetDF_Encoded.columns
print featureNames
print(model.feature_importances_)

importances = model.feature_importances_
std = np.std([tree.feature_importances_ for tree in model.estimators_], axis=0)
indices = np.argsort(importances)[::-1]

# Print the feature ranking
print("Feature ranking:")

for f in range(X.shape[1]):
    print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

print 'Variable importance obtained'

# estimator for rfecv
est = linear_model.LogisticRegression()

# fit rfecv
rfecv = RFECV(estimator=est, step=1, cv=StratifiedKFold(y, 10), scoring='accuracy')
rfecv.fit(X, y)

print rfecv.support_ 
print rfecv.ranking_
print 'score = ', rfecv.score(X, y)

print("Optimal number of features : %d" % rfecv.n_features_)
