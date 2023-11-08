# Welcome to My Ds Babel
***

## Task
Your mission will be to help translate from one format to another.

We will work with two popular formats: SQL and CSV.

## Description
Firstly I create a function that convert sql to csv and then i wrote a function for conterting csv file to sql
## Installation
python my_ds_babel.py
## Usage
print(sql_to_csv('sourse_all_fault_line.db','fault_lines'))

csv_content = open("sourse_list_volcano.csv")
csv_to_sql(csv_content, 'list_volcanos.db','volcanos')
