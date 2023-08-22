from pymongo.mongo_client import MongoClient
import pandas as pd
import json

# uniform resource indentifier
uri = "mongodb+srv://anuj:anuj@cluster0.y4ra03v.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# create database name and collection name
DATABASE_NAME="stores_sales"
COLLECTION_NAME1="sales_train"
COLLECTION_NAME2="sales_test"

# read the data as a dataframe
df_train=pd.read_csv(r"C:\Users\ASUS\Desktop\sales_prediction\notebooks\Data\train.csv")
df_test=pd.read_csv(r"C:\Users\ASUS\Desktop\sales_prediction\notebooks\Data\test.csv")



# Convert the data into json
json_record_train=list(json.loads(df_train.T.to_json()).values())
json_record_test=list(json.loads(df_test.T.to_json()).values())


#now dump the data into the database
client[DATABASE_NAME][COLLECTION_NAME1].insert_many(json_record_train)
client[DATABASE_NAME][COLLECTION_NAME2].insert_many(json_record_test)
