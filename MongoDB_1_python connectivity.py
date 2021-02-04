# import library to support driver which is pymong

from pymongo import MongoClient

#Create client
client=MongoClient('mongodb://127.0.0.1:27017/')

#create database
mydb = client['Employee']

# create collection
information=mydb.empinform

#create record which is json file
record ={
    'first':'Abhi',
    'last':'Gowda',
    'depart':'Data science'}

# insert one record
information.insert_one(record)

# insert multiple records
records=[
        {
    'first':'Abhi1',
    'last':'Gowda1',
    'depart':'Data science1'},
    {
    'first':'Abhi2',
    'last':'Gowda2',
    'depart':'Data science2'},
    {
    'first':'Abhi3',
    'last':'Gowda3',
    'depart':'Data science3'}]

information.insert_many(records)

