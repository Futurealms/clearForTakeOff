import csv

import requests

cities=['DFW','JFK','MSY','SJC']

for city in cities:
    inst = requests.get(
        'https://www.wunderground.com/history/airport/K{}/2014/1/23/CustomHistory.html?dayend=23&monthend=12&yearend=2014&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1'.format(city))
    with open("{}.csv".format(city), "wb") as f:
        f.write(bytes(inst.text, 'UTF-8'))