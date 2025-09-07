from pymongo.mongo_client import MongoClient
import pandas as pd
import json

uri = 'mongodb+srv://padmalochanroutray:Kanha000@cluster0.udbzwiw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
client = MongoClient(uri)

DATABASE_NAME = 'pwskills'
COLLECTION_NAME = 'waferfault'

df = pd.read_csv('D:\SENSORPROJECT\notebooks\wafer_23012020_041211.csv')
df.drop('Unnamed: 0', axis=1,inplace=True)

json_record = list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)