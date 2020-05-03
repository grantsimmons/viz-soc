'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates

data = pd.read_csv('sterilization.csv', index_col='state')
print("Original data:\n", data)
#states = data['state'].values




left = 0.125
bottom = 0.11
right = 0.90
top = 0.88
wspace = 0.20
hspace = 0.60

ind = np.arange(30)
width = 0.25

years = ('pre-1943',)
years += tuple('{:04d}'.format(i) for i in range(1943,1964))
print(years)

fig = plt.figure(figsize=(10,10))
plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)
ax = fig.add_subplot(111)
print('indexes:\n',data.index[4:])
print('WI data:\n',data['WI'][4:])
#ax.plot(data.index[4:], data['WI'][4:])
#for state in data:
#    print(data[state][0])
#    ax.plot(data[state][4:])


ind = np.arange(21)
print(data['WI'][4:].values)
print(ind)
chart = ax.bar(ind, data['WI'][4:].values)
print(data.index.values)
plt.xticks(ind, data.index[4:].values)
plt.legend(data)

plt.show()
'''

import geopandas as gpd
from math import ceil
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
import pandas as pd
#%matplotlib inline

data = pd.read_csv('sterilization.csv', index_col='state')
print("Original data:\n", data)
#states = data['state'].values

usa = gpd.read_file('zip://cb_2018_us_state_20m.zip')
#usa = usa.to_crs({'init' :'epsg:4326'})
print(data.index)
merged = pd.merge(usa, data, left_on=usa.STUSPS, right_index=True, how='left').fillna(0, downcast='infer')
merged = merged[(merged.STUSPS != 'PR') & (merged.STUSPS != 'HI') & (merged.STUSPS != 'AK')]
print(merged)

num = 22
per_row = 2

fig, ax = plt.subplots(int(ceil(num / per_row)), figsize=(10,10), ncols=per_row, sharex=True, sharey=True, squeeze=False)
print(ax[0])

for index, year in enumerate(merged.columns[13:]):
    #ax[index] = fig.add_subplot(per_row, 4, index + 1)
    #ax[index].axes.set_aspect('equal')
    print(year)
    merged.plot(ax=ax[int(index / per_row), index % per_row], column=year)
plt.show()
#usa[usa.STUSPS == 'FL'].plot(ax=ax, column='1955')
