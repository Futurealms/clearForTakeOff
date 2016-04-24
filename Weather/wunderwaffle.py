import csv

import dataset
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

        with open("{:03d}_{}.csv".format(cities.index(city), city), "wb") as f:
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


def insert_or_update(db_name, db_table, our_dictionary):
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
    table.insert(our_dictionary)
    # print('all done!')


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
            source_2 = source_data[:-7]
            print(source_1)
            # bundle.append(source_1)
            print(source_2)
            bundle.append(source_2)

    return bundle  # airport_ids.append(source_id)
    # airport_ids = airport_ids[1:]
    # print(airport_ids)


def join_history_csv_to_sql():
    cities = parse_airport_IDs('airport_identifiers_andrew.csv')
    # for city in cities:
    city = 'LAX'
    with open("new_{:02d}_{}.csv".format(00, city)) as file:
    # with open("new_{:02d}_{}.csv".format(cities.index(city), city)) as file:
        dict_list = []
        c = 0
        for line in file:
            if c == 0:
                line1 = line.split(',')
                line1[0] = 'Date'
                line1.append('City_Date')
                # print(line1)
                c += 1
            else:
                linec = line.split(',')
                for item in linec:
                    try:
                        linec[linec.index(item)] = int(item)
                    except:
                        pass
                dict = {}
                linec.append(city + '_' + linec[0])
                # print(linec)
                for entry in line1:
                    indexx = line1.index(entry)
                    dict[entry] = linec[indexx]
                dict_list.append(dict)
                c += 1
    db_name = 'sqlite:///clear_takeoff.db'
    db_table = 'Weather_subset'
    for dictionary in dict_list:
        insert_or_update(db_name, db_table, dictionary)
    print('all done for {}!'.format(city))


def delay_csv_to_sql():
    # for andrews csv
    db_name = 'sqlite:///clear_takeoff.db'
    db_table = 'Delays'
    with open("subset.csv") as file:
        # dict_list = []
        c = 0
        for line in file:
            if c == 0:
                line1 = line.split(',')
                line1[0] = 'old_id'
                line1[1] = 'irrel_id'
                line1[3] = 'FL_DATE'
                line1[5] = 'ORIGIN'
                line1[6] = 'DEST'
                line1.append('ORIGIN_DATE')
                line1.append('DEST_DATE')
                # print(line1)
                c += 1
            else:
                linec = line.split(',')
                for item in linec:
                    try:
                        linec[linec.index(item)] = int(item)
                    except:
                        pass
                dict = {}
                linec.append(linec[5].strip('"') + '_' + linec[3].strip('"'))
                linec.append(linec[6].strip('"') + '_' + linec[3].strip('"'))
                # print(linec)
                for entry in line1:
                    indexx = line1.index(entry)
                    dict[entry] = linec[indexx]
                insert_or_update(db_name, db_table, dict)
                print('all done for entry {}!'.format(c))
                # dict_list.append(dict)
                c += 1


def join_query(db_name, table_name1, table_name2, cond1, cond2, res):
    db = dataset.connect(db_name)
    result = db.query('SELECT * FROM {} JOIN {} [ON ({}={})]'.format(table_name1, table_name2, cond1, cond2))
    for row in result:
        print(row)
        db_name[res].insert(row)
    pass

if __name__ == '__main__':
    join_history_csv_to_sql()
    delay_csv_to_sql()
    # delay_csv_to_sql()
    # db = 'sqlite:///clear_takeoff.db'
    # table_name1 = 'Delays'
    # table_name2 = 'Weather'
    # cond1 = 'ORIGIN_DATE'
    # cond2 = 'City_Date'
    # cond11 = 'DEST_DATE'
    # cond22 = 'City_Date'
    # join_query(db, table_name1, table_name2, cond1, cond2, 'result1')
    # join_query(db, table_name1, table_name2, cond1, cond2, 'final_table')
    pass
# SELECT * FROM Delays OUTER JOIN Weather [ON (ORIGIN_DATE=City_Date)]
