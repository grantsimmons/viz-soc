import geopandas as gpd
from math import ceil
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
import pandas as pd
from math import ceil

data = pd.read_csv('sterilization.csv', index_col='state')

usa = gpd.read_file('zip://cb_2018_us_state_20m.zip')
#usa = usa.to_crs({'init' :'epsg:4326'})
merged = pd.merge(usa, data, left_on=usa.STUSPS, right_index=True, how='left').fillna(0, downcast='infer')
merged = merged[(merged.STUSPS != 'PR') & (merged.STUSPS != 'HI') & (merged.STUSPS != 'AK')]

left = 0.13
bottom = 0.11
right = 0.90
top = 0.88
wspace = 0.00
hspace = 0.64

num = 22
per_row = 4

fig, ax = plt.subplots(ceil(num/per_row), figsize=(10,10), ncols=per_row, sharex=True, sharey=True, squeeze=False)
fig.suptitle('Relative Popularity of Compulsory Sterilization in the United States')
plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)

for index, year in enumerate(merged.columns[13:]):
    merged.plot(ax=ax[int(index / per_row), index % per_row], column=year, cmap='binary', edgecolor='black', alpha=.9) #legend=True
    ax[int(index / per_row), index % per_row].set_xlabel(year)

for index in range(ceil(num/per_row) * per_row):
    xy = (int(index / per_row), index % per_row)
    ax[xy].spines['top'].set_visible(False) #Less ink
    ax[xy].spines['right'].set_visible(False)
    ax[xy].spines['left'].set_visible(False)
    ax[xy].spines['bottom'].set_visible(False)
    ax[xy].tick_params(
    axis='both',
    which='both',
    bottom=False,
    top=False,
    left=False,
    right=False,
    labelbottom=False)
    ax[xy].set_yticklabels([])

    
plt.savefig(fname='choropleth.png', format='png', dpi=300)
#plt.show()


fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
regions = { 'southeast' : {},
            'southwest' : {},
            'west' : {},
            'northeast' : {},
            'midwest' : {}   }
lines = {}
for key in regions:
    region_data = data.loc[data['region'] == key]
    for index, year in enumerate(region_data.columns[4:]):
        for row_index, row in region_data.iterrows():
            try:
                regions[key][year] += row[year]
            except:
                regions[key][year] = row[year]
    lines[key] = plt.plot(list(regions[key].keys()), list(regions[key].values()))
    ax.annotate(key, xy=(0.98,(regions[key]['1963']/825)), xytext=(0.98,(regions[key]['1963']/825)), horizontalalignment='left', verticalalignment='center', textcoords='axes fraction', color=lines[key][0].get_color())
ax.set_title('Compulsory Sterilization (By Region)')
ax.set_ylabel('Number of\nPeople\nSterilized', rotation=0)
ax.yaxis.set_label_coords(-0.1,0.5)
ax.set_xlabel('Year')
ax.spines['top'].set_visible(False) #Less ink
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.xaxis.grid(color='gainsboro', linestyle='dashed')
ax.yaxis.grid(color='whitesmoke', linestyle='dashed')
plt.ylim((-2,825))
plt.xticks(list(regions[key].keys()), rotation=-90, va='center', ha='left', rotation_mode='anchor')

plt.savefig(fname='sterilization.png', format='png', dpi=300)
plt.show()
