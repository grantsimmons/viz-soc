import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates

data = pd.read_csv('sterilization.csv')
states = data['state'].values




left = 0.125
bottom = 0.11
right = 0.90
top = 0.88
wspace = 0.20
hspace = 0.60

ind = np.arange(30)
width = 0.25

fig = plt.figure(figsize=(10,10))
plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)
ax = fig.add_subplot(111)

chart = ax.plot(, value, width, color='lightgray')

