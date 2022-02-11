import csv
import os
import pandas as pd

files = os.listdir("./CSV/")
vals = ""
for f in files:
    print('./CSV/'+f)
    file = open('./CSV/'+f)
    csvreader = csv.reader(file)
    next(csvreader)
    
    for row in csvreader:
        r = row[0].split(";")
        vals = vals + "("+r[0]+", '"+r[2]+"', "+r[3]+", "+r[4]+", NULL"+", NULL"+", NULL"+", NULL"+", NULL"+", "+r[0]+"),\n"

with open('./stations.txt', 'w') as f:
    f.write(vals)