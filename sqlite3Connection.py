# connecting to sqlite3Connection
import pandas as pd
from config import *

try:
	import sqlite3 as lite
except:
	print "No sqlite3 instance found. Copy sqlite3.exe in the working directory"

# Read sqlite query results into a pandas DataFrame
connection = lite.connect(databaseName)

def loadDataFrame(queryString):
	df = pd.read_sql_query(queryString, connection)
	return df