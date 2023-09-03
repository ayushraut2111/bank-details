# this script is used to load data from csv file to backend

import json
import requests
import os
import csv

headers={'content-type':'application/json'}

url="http://127.0.0.1:8000/bank/"

dir_path = os.path.dirname(os.path.realpath(__file__))
file=dir_path+'/bank_branches.csv'
data=None

count=1
with open(file) as f:
    reader=csv.reader(f)
    for row in reader:
        if count!=1:
            data={'ifsc':row[0],'bank_id':row[1], 'branch':row[2], 'address':row[3], 'city':row[4], 'district':row[5], 'state':row[6], 'bank_name':row[7]}
            json_data=json.dumps(data)
            r=requests.post(url=url,data=json_data,headers=headers)
        count+=1