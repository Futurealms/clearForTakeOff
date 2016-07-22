import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlite3
from rpy2.robjects import pandas2ri, r
import matplotlib


# pandas2ri.activate()


def parse_csv_with_DatesAndIDs(csv_filename):
    with open(csv_filename) as f:
        airport_ids = []
        for line in f:
            source_data = line.split(',')[3].strip('"')
            source_id = line.split(',')[5].strip('"')
            print(source_id, source_data)
            # airport_ids.append(source_id)
    # airport_ids = airport_ids[1:]
    # print(airport_ids)
    return (airport_ids)


def inserter(connection, table, col_to_fix):
    connection.row_factory = sqlite3.Row
    cur = connection.cursor()
    cur.execute('SELECT * FROM {}'.format(table))
    n_rows = len(cur.fetchall())
    for i in range(n_rows - 1):
        try:
            cur.execute('SELECT * FROM {t} where id = {id}'.format(t=table, id=i + 1))
            row = cur.fetchone()
            fixedrow = row[col_to_fix].strip('"').replace('"', '')
            f1 = fixedrow.split('-')
            f2 = '{}-{:02}-{:02}'.format(f1[0], int(f1[1]), int(f1[2]))
            # print(fixedrow, f1, f2)
            if fixedrow == f2:
                continue
            cur.execute("update {t} set {c}=? where id= {id}".format(t=table, c=col_to_fix, id=i + 1), (f2,))
            if i % 200 == 0:
                connection.commit()
                print('{}-th row'.format(i + 1))
            connection.commit()
        except:
            print('some error in {}-th row'.format(i + 1))
            pass


# https://www.periscope.tv/w/1zqJVkndBnZxB

def pandas_load(name):
    '''
    loads .rdata file (R dataframe file) and returns it as Pandas dataframe.
    :param name: .rdata filename (eg: 'subset.Rdata')
    :return: pandas dataframe object
    '''
    pandas2ri.activate()
    r.load(name)  # name = 'subset.fcuk.Rdata'
    # name_without_ext = r['.'.join(name.split('.')[-2::-1][::-1])]
    # print(r.ls())  # ls() - list of active objects in R env
    df = pandas2ri.ri2py(r[r.ls()[0]])
    return df


def pandas_load_by_parts(r, i):
    '''
    loads .rdata file (R dataframe file) and returns it as Pandas dataframe.
    :param r: r connection
    :param i: субсет
    :return: pandas dataframe object
    '''
    # pandas2ri.activate()
    # r.load(name)  # name = 'subset.fcuk.Rdata'
    # name_without_ext = r['.'.join(name.split('.')[-2::-1][::-1])]
    print(r.ls())  # ls() - list of active objects in R env
    print(r('dim(df)'))  # ls() - list of active objects in R env
    print(r('diablo <- df[{}:{},]'.format(i * 10000, i * 10000 + 10000)))  # ls() - list of active objects in R env
    print(type(r.ls()))
    # df = pandas2ri.ri2py(r[r.ls()[0]])
    df = pandas2ri.ri2py(r['diablo'])
    print(type(df))
    # print(df)
    return df


def prelude2_sql(connection):
    '''
    Злиття sql в одну табличку
    :param connection:
    :return:
    '''
    connection.row_factory = sqlite3.Row
    cur = connection.cursor()
    i = 1
    try:
        while True:
            cur.execute('Insert into Delays_2nd_0 select * from Delays_2nd_{}'.format(i))
            print('table "Delays_2nd_{}" added...'.format(i))
            i += 1
            pass
    except sqlite3.OperationalError as erry:
        print(erry)
    finally:
        connection.commit()
        print('adding completed')


def prelude3_sql(connection):
    '''

    :param connection:
    :return:
    '''
    connection.row_factory = sqlite3.Row
    cur = connection.cursor()
    cur.execute('select * from Delays_2nd_0')
    bulk = cur.fetchall()
    print(len(bulk))

def prelude4_sql(connection):
    '''
    Злиття sql в одну табличку
    :param connection:
    :return:
    '''
    connection.row_factory = sqlite3.Row
    cur = connection.cursor()
    i = 1
    try:
        while True:
            cur.execute('drop table Delays_2nd_{}'.format(i))
            print('table "Delays_2nd_{}" dropped...'.format(i))
            i += 1
            pass
            # if i==10: break
    except sqlite3.OperationalError as erry:
        print(erry)
    finally:
        connection.commit()
        print('dropping completed')

def prelude1_Rdata(connection):
    # print(parse_csv_with_DatesAndIDs('subset.csv'))
    # виправляю weather прямо в sql (один раз :) ):
    # inserter(con_in,'Weather','City_date')
    # завантажую датасети:
    connection.row_factory = sqlite3.Row
    cur = connection.cursor()
    r.load('flights.Rdata')  # name = 'subset.Rdata'
    # r('diablo <- df[1350500:5819079, ]')
    for i in range(5819079 // 10000 + 1):  # 5819079 5819 79
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Delays{}".format(i))

        delays = pandas_load_by_parts(r, i)
        # weather = pd.read_sql('select * from Weather', con_in)
        # корегую імена колонок:
        # di = {}
        # for item in weather.axes[1]:
        #     di[item] = item.strip()
        #     print(item.strip())
        # weather.rename(columns=di, inplace=True)
        # записую в sql:
        # weather.to_sql('Weather', con_out)
        delays.to_sql('Delays_2nd_{}'.format(i), connection)
def _zeros_from_weather

if __name__ == '__main__':
    pandas2ri.activate()
    # підключаю бази даних:
    con_in = sqlite3.connect('clear_takeoff_test.db')
    con_out = sqlite3.connect('Data.db')
    con_test = sqlite3.connect('test.db')
    # prelude2_sql(con_test)
    # prelude1_Rdata(con_test)
    # prelude3_sql(con_test)
    prelude4_sql(con_test)
