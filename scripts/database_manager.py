# Importing module
import os
import pandas as pd
from mysql.connector import Error
import mysql.connector as cu

def DBConnect(dbName=None):
    mydb = cu.connect(host='localhost', user='root',
                      password='localhost',
                         database=dbName, buffered=True)
    cursor = mydb.cursor()
    return mydb, cursor


def createDB(dbName: str) -> None:
    mydb, cursor = DBConnect()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {dbName};")
    mydb.commit()
    cursor.close()
    
def createTables(dbName: str, schema) -> None:
    mydb, cursor = DBConnect(dbName)
    sqlFile = schema
    fd = open(sqlFile, 'r')
    readsqlFile = fd.read()
    fd.close()
    sqlCommands = readsqlFile.split(';')
    for command in sqlCommands:
        try:
            result = cursor.execute(command)
        except Exception as e:
            print('command skipped: ', command)
            print(e)
    mydb.commit()
    cursor.close()
    
def preprocess_df(df: pd.DataFrame) -> pd.DataFrame:
    try:
        df = df.fillna(0)
    except KeyError as e:
        print('Error: ', e)
    
    return df
        
def insert_into_table(dbName: str, df: pd.DataFrame, table_name: str) -> None:
    mydb, cursor = DBConnect(dbName)
    df = preprocess_df(df)
    for _, col in df.iterrows():
        sqlQuery = f"""INSERT INTO {table_name} 
        (user_id, engagement_score, experience_score, satisfaction_score)
              VALUES(%s, %s, %s, %s);"""
       
        data = (col[0], col[1], col[2], col[3])
        try:
            cursor.execute(sqlQuery, data)
            mydb.commit()
            print('Data inserted successfully')
        except Exception as e:
            mydb.rollback()
            print('Error: ', e)
            
def fetch_data(table_name):
    mydb, cursor= DBConnect()
    column = []
    query = "SELECT * FROM "+table_name
    value = cursor.execute(query)
    for items in cursor.description:
        column.append(items[0])
        mydb.commit()
        df = pd.DataFrame(value, columns=column)
        cursor.close()
        return df
            
if __name__=="__main__":
    createDB(dbName='tweets')
    df = pd.read_csv('processed_tweet_data.csv')
    createTables(dbName='tweets')
    insert_into_table(dbName = 'tweets', df = df, table_name='TweetInformation')