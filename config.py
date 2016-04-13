
# For sqlite database
databaseName = 'CTR_Prediction.db' # database name
trainingDataTable = 'trainData' # training set table
testingDataTable = 'testData' # testing set table
classTitle = 'click' # class to predict
classLabels = [0,1] # unique list of classes in the training data as list


# For dimension reduction

hasCategoricalColumns = True

# all input columns
dimensionReduction_InputColumns_WithTarget = ['weekday', 'hour', 'userAgent', 'region',  'domain', 'URL',  'adSlot_id', 'city', 'adExchange', 'adSlotWidth', 'adSlotHeight', 'adSlotVisibility', 'adSlotFormat', 'adSlotFloorPrice', 'creative_id', 'keyPageURL', 'click']

# only the categorical columns
dimensionReduction_CategoricalColumns_Encoder = ['userAgent', 'region',  'domain', 'URL',  'adSlot_id', 'city', 'adExchange', 'creative_id', 'keyPageURL', 'click']



# For Classification and cross validation

classification_hasCategoricalColumns = True

# all input columns
classification_InputColumns_WithTarget = ['city', 'adSlot_id', 'weekday', 'hour', 'userAgent', 'region', 'adSlotVisibility', 'adSlotFormat', 'adSlotFloorPrice', 'creative_id', 'click']

# only the categorical columns
classification_CategoricalColumns_Encoder = ['city', 'adSlot_id', 'userAgent', 'region', 'creative_id']

# for train test split
trainPercentage = 0.8




# For prediction - test set

# all input columns
prediction_InputColumns = ['city', 'adSlot_id', 'weekday', 'hour', 'userAgent', 'region', 'adSlotVisibility', 'adSlotFormat', 'adSlotFloorPrice', 'creative_id']

# only the categorical columns
prediction_CategoricalColumns_Encoder = ['city', 'adSlot_id', 'userAgent', 'region', 'creative_id']

# testPercentage = 1 - trainPercentage