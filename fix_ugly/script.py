import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates



#dataset
death = np.array([37000,12000,43000,38000,51000,23000,28000,61000])
hospitalized = np.array([390000,140000,570000,350000,590000,280000,497000,810000])
illness = np.array([21000000,9300000,34000000,30000000,30000000,24000000,39000000,45000000])
combined = np.add(hospitalized, illness)

N = 8
years = ('2010/11','2011/12','2012/13','2013/14','2014/15','2015/16','2016/17','2017/18')
ind = np.arange(N)
ind_y = np.arange(0,50000000, 5000000)
width = 0.75
left = 0.22
bottom = 0.11
right = 0.94
top = 0.88
wspace = 0.20
hspace = 0.20

fig = plt.figure(figsize=(10,10))
plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)
ax = fig.add_subplot(211)
illness_rep = ax.bar(ind, illness, width, color='lightgray')
hosp_rep = ax.bar(ind, hospitalized, width, bottom=illness, color='gray')
death_rep = ax.bar(ind, death, width, bottom=combined, color='black')
ax.set_axisbelow(False) #White lines for grid
ax.yaxis.grid(color='white')
ax.spines['top'].set_visible(False) #Less ink
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.tick_params(axis=u'both', which=u'both',length=0) #Less Ink
ax.axes.margins(0,0)

plt.legend((death_rep, hosp_rep, illness_rep), ("Deaths", "Hospitalizations", "Illnesses"))
plt.title('Estimated U.S. Influenza Burden, By Season')

#Y-Label
ax.set_ylabel('Number Affected\n(Millions)', rotation=0)
ax.yaxis.set_label_coords(-0.175,0.5)
#Y-Ticks
ax.set_yticks(ind_y)
ylabels = [item.get_text() for item in ax.yaxis.get_majorticklabels()]
print(ylabels)
for i, label in enumerate(ylabels):
    ylabels[i] = '{}{}'.format(int(i / 2) if i % 2 == 0 and i is not 0 else '','' if i == 0 else '0' if i % 2 == 0 else '')
print(ylabels)
ax.set_yticklabels(ylabels)
ax.tick_params(axis="y", direction="out", pad=20)

#X-Label
ax.set_xlabel('Flu Season')
#X-Ticks
plt.xticks(ind, years)

bx = fig.add_subplot(223)
#Y-Label
bx.set_ylabel('Number in\nSerious Condition\n(Thousands)', rotation=0)
bx.yaxis.set_label_coords(-0.375,0.5)
ind_y_b = np.arange(0, 900000, 50000)
bx.set_yticks(ind_y_b)
ylabels_b = [item.get_text() for item in bx.yaxis.get_majorticklabels()]
print(ylabels_b)
for i, label in enumerate(ylabels_b):
    ylabels_b[i] = '{}{}'.format(int(i / 2) if i % 2 == 0 and i is not 0 else '','' if i == 0 else '00' if i % 2 == 0 else '')
print(ylabels_b)
bx.set_yticklabels(ylabels_b)
bx.tick_params(axis="y", direction="out", pad=15)
hosp_rep = bx.bar(ind, hospitalized, width, color='gray')
death_rep = bx.bar(ind, death, width, bottom=hospitalized, color='black')
bx.set_axisbelow(False) #White lines for grid
bx.yaxis.grid(color='white')
bx.spines['top'].set_visible(False) #Less ink
bx.spines['right'].set_visible(False)
bx.spines['left'].set_visible(False)
bx.tick_params(axis=u'both', which=u'both',length=0) #Less Ink
bx.axes.margins(0,0)
#X-Label
bx.set_xlabel('Flu Season')
#X-Ticks
plt.xticks(ind, years, rotation=-45, ha='left', rotation_mode='anchor')

cx = fig.add_subplot(224)
#Y-Label
cx.yaxis.set_label_coords(-0.175,0.5)
death_rep = cx.bar(ind, death, width, color='black')
ind_y_c = np.arange(0, 65000, 5000)
cx.set_yticks(ind_y_c)
ylabels_c = [item.get_text() for item in cx.yaxis.get_majorticklabels()]
print(ylabels_c)
for i, label in enumerate(ylabels_c):
    ylabels_c[i] = '{}{}'.format(int(i / 2) if i % 2 == 0 and i is not 0 else '','' if i == 0 else '0' if i % 2 == 0 else '')
print(ylabels_c)
cx.set_yticklabels(ylabels_c)
cx.tick_params(axis="y", direction="out", pad=10)
cx.set_axisbelow(False) #White lines for grid
cx.yaxis.grid(color='white')
cx.spines['top'].set_visible(False) #Less ink
cx.spines['right'].set_visible(False)
cx.spines['left'].set_visible(False)
cx.tick_params(axis=u'both', which=u'both',length=0) #Less Ink
cx.axes.margins(0,0)

#X-Label
cx.set_xlabel('Flu Season')
#X-Ticks
plt.xticks(ind, years, rotation=-45, ha='left', rotation_mode='anchor')
plt.savefig(fname='fluviz.png', format='png', dpi=300)
