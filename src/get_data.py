# get_data.py
import requests
import csv
import json
import pandas as pd
import io
from collections import defaultdict

''' Request Loading Errors:

_csv.Error: iterator should return strings, not bytes (did you open the file in text mode?)

https://stackoverflow.com/questions/1035340/reading-binary-file-and-looping-over-each-byte

https://requests.kennethreitz.org//en/latest/user/quickstart/#json-response-content
https://stackoverflow.com/questions/6862770/let-json-object-accept-bytes-or-let-urlopen-output-strings


url = 'https://docs.google.com/spreadsheets/d/1tMeTHBpdw3kDuEcJbZA4G98fhbuJfo-MBKKBDVXxcA4/edit#gid=1801354196'
r = requests.get(url)
# text = r.iter_lines()
# reader = csv.reader(text, delimiter=',')
# commented code gets the above request loading error; to work around this i downloaded csv from google spreadsheets

'''
# UPLOAD DATA FROM CSV FILE
# headers = id, name, identity, alignment, orientation, status,
# appearances, introduced, introduced_month, eyes, hair, gender

def load_data(file):
    with open(file) as csv_file:
        reader = csv.reader(csv_file)
        mydict = defaultdict(dict)
        for key, rows in enumerate(reader):
            mydict[key]['id'] = rows[0]
            mydict[key]['name'] = rows[1]
            mydict[key]['identity'] = rows[2]
            mydict[key]['alignment'] = rows[3]
            mydict[key]['orientation'] = rows[4]
            mydict[key]['status'] = rows[5]
            mydict[key]['appearances'] = rows[6]
            mydict[key]['introduced'] = rows[7]
            mydict[key]['introduced_month'] = rows[8]
            mydict[key]['eyes'] = rows[9]
            mydict[key]['hair'] = rows[10]
            mydict[key]['gender'] = rows[11]
    return mydict
