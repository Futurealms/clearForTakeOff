import csv
from pymongo import MongoClient
import os
db_name = 'delays'
csv_list = [i for i in os.listdir(os.path.dirname(__file__)) if i[-3:] == 'csv']
print(csv_list)
mongo_client = MongoClient()
db = mongo_client.nodelay
db[db_name].drop()
for name in csv_list:
    csv_reader = open(name, 'r')
    reader = csv.DictReader(csv_reader, delimiter=' ')
    header = reader.fieldnames
    print(header)
    for each in reader:
        row = {}
        for field in header:
            if field[0] == '.':
                field = field[1:]
            try:
                row[field] = int(each[field])
            except ValueError:
                row[field] = each[field]
        print(row)
        db[db_name].insert(row)


