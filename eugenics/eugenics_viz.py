import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates

data = pd.read_csv('sterilization.csv', index_col='state')
data = data.T
print(data.T)
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
ax.plot(data.index[4:], data['WI'][4:])


plt.show()

