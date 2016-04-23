import csv

import requests


def get_weath_hist(cities):
    st_date = (1, 1, 2015)
    en_date = (31, 12, 2015)
    for city in cities:
        url = 'https://www.wunderground.com/history/airport/K{c}/{y1}/{m1}/{d1}/CustomHistory.html?dayend={d2}&monthend={m2}&yearend={y2}&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1'.format(
            c=city, d1=st_date[0], m1=st_date[1], y1=st_date[2], d2=en_date[0], m2=en_date[1],
            y2=en_date[2])
        inst = requests.get(url)
        print(url)

        with open("{:02d}_{}.csv".format(cities.index(city), city), "wb") as f:
            f.write(bytes(inst.text, 'UTF-8'))


def parse_airport_IDs(csv_filename):
    with open(csv_filename) as f:
        airport_ids = []
        for line in f:
            source_id = line.split(',')[1].strip('"')[:3]
            airport_ids.append(source_id)
    airport_ids = airport_ids[1:]
    print(airport_ids)
    return (airport_ids)


if __name__ == '__main__':
    # airport_ids=parse_airport_IDs("airport_identifiers_andrew.csv")
    # get_weath_hist(airport_ids)
    pass
