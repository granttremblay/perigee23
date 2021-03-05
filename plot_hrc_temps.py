#!/usr/bin/env python

import matplotlib.pyplot as plt
from Ska.engarchive import fetch

from hrcsentinel import hrccore as hrc
from cxotime import CxoTime

from astropy import units as u
from astropy import constants as c
import datetime as dt

import seaborn as sns
sns.set_theme(context='talk')

fetch.data_source.set('cxc')

dat = fetch.MSIDset(['Dist_SatEarth', '2FHTRMZT'], start='1999:204', stat='5min').interpolate(copy=True)


# plot 1

fig, ax = plt.subplots(figsize=(12,12))
ax.plot(dat['2FHTRMZT'].midvals, dat['Dist_SatEarth'].midvals / 1000, marker='o', markersize=1.8)

ax.set_xlabel('HRC FEA Temperature (C), 5min stats')
ax.set_ylabel('Chandra distance from Earth center (km), 5min stats')


# orbit plot

fig, ax = plt.subplots(figsize=(12,6))
ax.plot_date(hrc.convert_chandra_time(dat['Dist_SatEarth'].times), dat['Dist_SatEarth'].mins / 1000, marker='o', markersize=0.5)
ax.set_ylabel('Chandra distance from Earth center (km)')

# 

last_closeappraoch = CxoTime(['2012:001', '2013:001'])
last_closeappraoch.cxcsec

fig, ax = plt.subplots(figsize=(12,6))
ax.scatter(dat['Dist_SatEarth'].times, dat['Dist_SatEarth'].mins / 1000, c=dat['2FHTRMZT'].maxes)

ax.set_xlim(last_closeappraoch.cxcsec)


fig, ax = plt.subplots(figsize=(16,6))
ax.plot_date(hrc.convert_chandra_time(dat['Dist_SatEarth'].times), dat['Dist_SatEarth'].mins / 1000, marker='o', markersize=1.8)
ax.set_ylabel('Chandra distance from Earth center (km), 5min stats')

xmin = dt.datetime(1999, 7, 23)
xmax = dt.datetime(1999,10, 20)

# xmin = dt.datetime(2012, 4, 1)
# xmax = dt.datetime(2012, 9, 1)


ax.set_xlim(xmin,xmax)
# ax.set_ylim(0, 20000)




fig, ax = plt.subplots(figsize=(12,12))

y = dat['Dist_SatEarth'].means / 1000.0
x = dat['2FHTRMZT'].means

ax.set_xlabel('Daily Mean HRC FEA Temperature (C)')
ax.set_ylabel('Daily Minimum Chandra distance from Earth (km)')

ax.set_xlim(10, 30)

sns.kdeplot(x=x, y=y, fill=True, cmap='mako', levels=100)



plt.show()
