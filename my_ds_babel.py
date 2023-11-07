import pandas as pd
import csv
import sqlite3
import warnings
warnings.filterwarnings('ignore')

def sql_to_csv(database, table_name):
 
    # # Create a connection and get a cursor
    connection = sqlite3.connect(database)
    sql_query = pd.read_sql_query('select * from ' + table_name, connection) # here, the 'conn' is the variable that contains your database connection information from step 2

    df = pd.DataFrame(sql_query)
    df.to_csv (r'list_fault_line.csv', index = False) # place 'r' before the path name
    
    with open('list_fault_line.csv', 'r') as df1:
        return ''.join([i for i in df1][:-1])





def csv_to_sql(csv_content, database, table_name):
    df = pd.read_csv(csv_content)
    df = df.drop_duplicates()
    connection = sqlite3.connect(database)
    df.to_sql(table_name, con = connection, if_exists = 'replace', index = False)

print(sql_to_csv('all_fault_line.db','fault_lines'))

csv_content = open("list_volcano.csv")
csv_to_sql(csv_content, 'list_volcanos.db','volcanos')