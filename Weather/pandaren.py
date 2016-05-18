import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.mpl_style', 'default') # Make the graphs a bit prettier
csv_handle = pd.read_csv('new_321_WYS.csv')
print(csv_handle[' Max Gust SpeedKm/h'])
plt.figure()
csv_handle[' Max Gust SpeedKm/h'].plot(figsize=(15, 10))
plt.show()