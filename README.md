# About
Just a few personal notes in how to use matplotlit to plot skymap (RA, DEC).

* `ex_pcolormesh1.py` is a (nearly) minimal working code to add a heatmap on projected coordinates
* `ex_pcolormesh2.py` has more controls and styles, especially setting a central longitude
* `ex_pcolormesh2_astropy.py` is similar to previous one, but use astropy to wrap the coordinates
* `ex_astropy.py` and `ex_using_astropy.ipynb`: another example which use astropy units and
  SkyCoords.  Both are basically the same.


# References

1. [Geographic Projections (matplotlib)](http://matplotlib.org/gallery/subplots_axes_and_figures/geo_demo.html)
2. [Example 1: Plotting random data in Aitoff projection (astropy)](http://docs.astropy.org/en/stable/coordinates/skycoord.html#example-1-plotting-random-data-in-aitoff-projection)
3. https://stackoverflow.com/questions/46320712/putting-matplotlib-hexbin-into-an-aitoff-projection
4. https://stackoverflow.com/questions/7355497/curious-bad-behavior-creating-all-sky-projections-with-matplotlib


# Notes

* Projections aitoff and Mollweide in matplotlib take radian as coordinate unit, range from
  `(-pi,pi)` and `(-pi/2, pi/2)`.
* astropy can deal with coordinates (deg to and from radian, wrap at 180 deg, ...).  Probably better
  than do it manually (but need to import several astropy modules)
* Python package cartopy (which can work with matplotlib) can do similar things and is easy to set
  the central longitude. But cartopy cannot add ticklabels in projections other than PlateCarree and
  Mercator. See [issue #920 of cartopy](https://github.com/SciTools/cartopy/issues/920).
