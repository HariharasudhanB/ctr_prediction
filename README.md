# ctr_prediction
This project has the python scripts for ctr prediction

Place all the files in the same folder

First call the .bat from that folder as directory to create sqlite db from the train.txt and test.txt file

All the py scripts work from db

call dimensionReduction.py to get results on dimension reduction (see config file for mentioning columns to consider)

call the modelEveluation.py to get the score for the model built and evaluated using the mentioned dimensions (mention in config file)

call the fitting.py to fit a classifier with the mentioned columns as inputs and save the classifier as a pickle file named model.pkl

call the prediction.py to get the predictions for the test set saved as table in db and save predictions in a csv file with name predictions.csv


