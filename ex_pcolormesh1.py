#!/usr/bin/env python
# -*- coding: utf-8 -*-
# plot image/heatmap in skymap in RA, DEC coordinate, project to mollweide or aitoff projections
# refer: from https://stackoverflow.com/questions/7355497/curious-bad-behavior-creating-all-sky-projections-with-matplotlib
import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# the full extent of projected image is (-180,180)/(-90,90)
RA = np.random.random(10000)*60  # 0 to 60 degrees (on purpose)
DEC = np.random.random(10000)*90-30  # -30 to 60 degress (on purpose)

# plot
fig = plt.figure(figsize=(10, 6.3))
ax = fig.add_subplot(111, projection='mollweide')  # or aitoff

hist, xedges, yedges = np.histogram2d(DEC, RA, bins=[90,180], range=([-90,90],[-180,180]))
X, Y = np.meshgrid(np.radians(yedges), np.radians(xedges))
image = ax.pcolormesh(X, Y, hist)
cb = fig.colorbar(image, orientation='horizontal')

# more about plot
ax.grid(True)  # put this line after pcolormesh to make grid visible
ax.set_xlabel('RA')
ax.set_ylabel('DEC')
plt.show()
