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
    # print(airport_ids)
    return (airport_ids)


def insert_or_update(db_name, db_table, entry_list):
    '''
    Бере список фільмів і закидає їх у таблицю бази даних.
    Оновлює запис (або створює новий) у базі даних.
    :param db_name:     назва бази даних (створить нову, якщо нема)
    :param db_table:    назва таблиці у базі даних (створить нову, якщо нема)
    :param entry_list:  список назв фільмів, дані яких треба закинути у таблицю
    :return:
    '''
    import dataset
    db = dataset.connect(db_name)
    table = db[db_table]
    # existed_id = table.find_one(imdb_id=dict_by_title['imdb_id'])
    # if existed_id != None:
    # print(existed_id, 'funn')
    # if table.find_one(imdb_id=dict_by_title['imdb_id'])['imdb_id'] == dict_by_title['imdb_id']:
    #     table.update(dict_by_title, ['imdb_id'])
    # print('\nentry updateted')
    # else:
    table.insert(entry_list)
    print('all done!')


def clearoff_rb_on_csv(csv_filename):
    # for list in dictlist[1:0]:
    with open(csv_filename) as f:
        airport_ids = []
        bundle = []
        for line in f:
            source_data = line
            # source_id = line.split(',')[5].strip('"')
            # print(source_data)
            source_1 = source_data[:-7].split(',')
            source_2=source_data[:-7]
            print(source_1)
            # bundle.append(source_1)
            print(source_2)
            bundle.append(source_2)

    return bundle  # airport_ids.append(source_id)
    # airport_ids = airport_ids[1:]
    # print(airport_ids)

if __name__ == '__main__':
    # airport_ids=parse_airport_IDs("airport_identifiers_andrew.csv")
    # get_weath_hist(airport_ids)

    # with open("{:02d}_{}.csv".format(cities.index(city), city), "wb") as f:
    # with open("_{:02d}_{}.csv".format(0, city), "wb") as f:
    #     for list in dictlist[1:0]:
    #         f.write(bytes(list, 'UTF-8'))
    cities = parse_airport_IDs('airport_identifiers_andrew.csv')
    for city in cities:
        dictlist = clearoff_rb_on_csv('{:02d}_{}.csv'.format(cities.index(city), city))
        # print(dictlist[1:])
        with open("new_{:02d}_{}.csv".format(cities.index(city), city), "wb") as file_new:
            for item in dictlist[1:]:
                # print(item+'\n')
                # file_new.write(bytes(source_data[:-7].join('\n'), 'UTF-8'))
                file_new.write(bytes(item+'\n', 'UTF-8'))
    pass
