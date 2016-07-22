import sqlite3




def inserter(table, col_to_fix):
    cur.execute('SELECT * FROM {}'.format(table))
    n_rows = len(cur.fetchall())
    for i in range(n_rows - 1):
        try:
            cur.execute('SELECT * FROM {t} where id = {id}'.format(t=table, id=i + 1))
            row = cur.fetchone()
            fixedrow = row[col_to_fix].strip('"').replace('"', '')
            f1 = fixedrow.split('-')
            f2 = '{}-{}-{}'.format(f1[0], int(f1[1]), int(f1[2]))
            print(fixedrow, f1, f2)
            cur.execute("update {t} set {c}=? where id= {id}".format(t=table, c=col_to_fix, id=i + 1), (f2,))
            if i % 10 == 0:
                connection.commit()
                print('{}-th row'.format(i + 1))
        except:
            print('some error in {}-th row'.format(i + 1))
            pass


def inserter2(table, col_to_fix):
    cur.execute('SELECT * FROM {}'.format(table))
    n_rows = len(cur.fetchall())
    for i in range(n_rows - 1):
        try:
            cur.execute('SELECT * FROM {t} where id = {id}'.format(t=table, id=i + 1))
            row = cur.fetchone()
            fixedrow = row[col_to_fix].strip('"').replace('"', '')
            print(fixedrow)
            cur.execute("update {t} set {c}=? where id= {id}".format(t=table, c=col_to_fix, id=i + 1), (fixedrow,))
            if i % 10 == 0:
                connection.commit()
                print('{}-th row'.format(i + 1))
        except:
            print('some error in {}-th row'.format(i + 1))
            pass


def executer(table, col_to_fix):
    cur.execute('SELECT * FROM {}'.format(table))
    n_rows = len(cur.fetchall())
    for i in range(n_rows - 1):
        try:
            cur.execute('SELECT * FROM {t} where id = {id}'.format(t=table, id=i + 1))
            row = cur.fetchone()
            fixedrow = row[col_to_fix].strip('"').replace('"', '')
            print(fixedrow)
            # f1 = fixedrow.split('-')
            # f2 = '{}-{}-{}'.format(f1[0], int(f1[1]), int(f1[2]))
            print(fixedrow)
            cur.execute("update {t} set {c}=? where id= {id}".format(t=table, c=col_to_fix, id=i + 1), (fixedrow,))
            if i % 10 == 0:
                connection.commit()
                print('{}-th row'.format(i + 1))
        except AttributeError:
            print('some error with int in {}-th row'.format(i + 1))
            pass
        except sqlite3.OperationalError:
            print('some error with sqlite in {}-th row'.format(i + 1))
            pass

connection = sqlite3.connect('clear_takeoff_test.db')
connection.row_factory = sqlite3.Row
cur = connection.cursor()

table = 'Weather_subset'
column = 'City_Date'
# inserter(table,'ORIGIN_DATE')
# inserter(table,'DEST_DATE')
# inserter2(table, 'ORIGIN')
inserter(table,column)
# cur.execute('drop table Delays_new')
# cur.execute('drop table Delays_new2')
# cur.execute(
#     'Create table Delays_new as SELECT * FROM Delays JOIN Weather ON Delays.ORIGIN_DATE=Weather.City_Date')
#
# connection.commit()
# cur.execute(
#     'Create table Delays_new2 as SELECT * FROM Delays_new JOIN Weather ON '
#     'Delays_new.DEST_DATE=Weather.City_Date')
connection.commit()

cur.close()
