import pickle

import pandas
import sqlite3

sql_connection = sqlite3.connect('delaysAndWeather.db')
sql_connection_test = sqlite3.connect('test_pands.db')
#   load from sql to dataframes:
delays = pandas.read_sql(con=sql_connection, sql='SELECT * FROM Delays_2nd_0 LIMIT 10')
weather = pandas.read_sql(con=sql_connection, sql='SELECT * FROM Weather LIMIT 10')

print(delays.head().to_string())


delays["ORIGIN_DATE"] = delays["ORIGIN"] + '_' + delays["FL_DATE"]
delays["DEST_DATE"] = delays["DEST"] + '_' + delays["FL_DATE"]
print('delays: ')
print(delays.head().to_string())

print('weather: ')
print(weather.head().to_string())
#   dump to pickle
# pickle.dump(datafr, open('sql_pickle.p', 'wb'))

print(delays.columns.values)


delays['DEST_DATE'].map(str)
delays.loc['ORIGIN_DATE'].map(str)
weather['City_Date'].map(str)

merged_first = pandas.merge(delays, weather, on=["DEST_DATE", 'City_Date'])

# print('weather + delay #1: ')
# print(merged_first.head().to_string())

# datafr['FL_DATE'].apply()
# datafr.to_sql('test_pandas',sql_connection_test,)



#   check pickled file:
# df = pickle.load(open('sql_pickle.p', 'rb'))
# print(df.head().to_string())

