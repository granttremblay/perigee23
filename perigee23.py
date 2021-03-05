#!/usr/bin/env python

from astropy.io import ascii

import datetime as dt
import pandas as pd

import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import seaborn as sns
sns.set_theme(context='talk')

ephem = ascii.read('ephem2023.dat')
# Make it a DataFrame
df = ephem.to_pandas()

# Reformat the string dates to the datetimes
df['dates'] = pd.to_datetime(df['dates'], format='%Y:%j:%H:%M:%S.%f')


x = df['orbitephem0_x']
y = df['orbitephem0_y']
z = df['orbitephem0_z']

# these are ECI coordinates, so the Earth-Chandra separation is just
separation = np.sqrt(x**2 + y**2 + z**2) - 6371  # SUBTRACT OFF R_EARTH!!!


fig, ax = plt.subplots()

ax.plot_date(df['dates'], separation)

ax.set_xlabel('Date')
ax.set_ylabel('Earth/Chandra Separation (km)')

# ax.plot_date(df['dates'], df['orbitephem0_y'])


# ax.plot_date(df['dates'], df['orbitephem0_z'])

plt.show()

# fig = plt.figure(figsize=(12, 12))
# ax = fig.add_subplot(111, projection='3d')

# # datetime = dt.datetime.strptime(ephem['dates'], '%Y:%j:%H:%M:%S.%f')

# ax.scatter(ephem['orbitephem0_z'],
#            ephem['orbitephem0_x'], ephem['orbitephem0_y'])

# plt.show()
