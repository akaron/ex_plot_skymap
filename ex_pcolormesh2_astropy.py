#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Purpose: plot image/heat map on sky coordinates (skymap)
# * Use pcolormesh instead of imshow (see [2])
# * Central longitude can be non-zero
# * Need to shift the data and the xticks
# * also see [3] which use astropy to deal with coordinates
#
# Reference:
# [1] Geographic projections http://matplotlib.org/gallery/subplots_axes_and_figures/geo_demo.html
# [2] https://stackoverflow.com/questions/7355497/curious-bad-behavior-creating-all-sky-projections-with-matplotlib
# [3] Evert's answer at https://stackoverflow.com/questions/46320712/putting-matplotlib-hexbin-into-an-aitoff-projection
#
# Note: this script is similar to ex_pcolormesh2.py, but use astropy units and SkyCoord at a few places
import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.coordinates import SkyCoord
pi = np.pi

# Data: create data between a certain range of RA and DEC
# the full extent is (-180,180)/(-90,90)
RA0 = (np.random.random(10000)*120) * u.degree  # 0 to 120 degrees
DEC = (np.random.random(10000)*90-30) * u.degree  # -30 to 60 degress
c = SkyCoord(ra=RA0, dec=DEC)


def shift_lon(central_longitude, c):
    # center RA at 'lon_cen' degree,
    # return: shifted RA and xtick location and corresponding tick labels

    # RA = (RA0 - central_longitude + 180) % 360 - 180  # without astropy: manually shift and wrap
    RA = (c.ra - central_longitude*u.degree).wrap_at(180*u.deg)  # using astropy to shift and wrap
    xtick_loc_deg = np.arange(-120, 180, 60)  # -120, -60, 0, 60, 120
    xtick_loc_rad = xtick_loc_deg * pi / 180
    # RA should range between 0h and 24h
    xtick_lbl = ['{0:.0f}h'.format(((a+central_longitude) % 360)/15) for a in xtick_loc_deg]
    return RA, xtick_loc_rad, xtick_lbl


# shift the data and obtain the new longitude values
central_longitude = 45  # try 45/255
# central_longitude = 255
RA, xtick_loc_rad, xtick_lbl = shift_lon(central_longitude, c)

# plot
fig = plt.figure(figsize=(10, 6.3))
ax = fig.add_subplot(111, projection='aitoff')  # or aitoff or mollweide

# background image (heat map for example)
hist, xedges, yedges = np.histogram2d(DEC, RA, bins=[90,180], range=([-90,90],[-180,180]))
X, Y = np.meshgrid(np.radians(yedges), np.radians(xedges))
image = ax.pcolormesh(X, Y, hist, cmap=plt.cm.hot)
cb = fig.colorbar(image, orientation='horizontal')

# set shifted xticks
ax.set_xticks(xtick_loc_rad)
ax.set_xticklabels(xtick_lbl, color='cyan')

# title / grid / labels / ...
fig.suptitle(r'Data: RA 0h to 8h; DEC -30 to 60deg. Plot center at lon.={}deg'.format(central_longitude))
ax.grid(True, linestyle='--')  # put this line after pcolormesh to make grid visible
ax.set_xlabel('RA')
ax.set_ylabel('DEC')

plt.show()
