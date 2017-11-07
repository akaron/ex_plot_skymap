Here are some examples to plot skymap (RA, DEC). Just personal note.

* `ex_pcolormesh1.py` is a (nearly) minimal working code to add a heatmap on projected
  coordinates
* `ex_pcolormesh2.py` has more controls and styles, especially setting a central
  longitude
* next step: add example which use astropy for coordinates conversion and wrapping


References:

* http://matplotlib.org/gallery/subplots_axes_and_figures/geo_demo.html
* http://docs.astropy.org/en/stable/coordinates/skycoord.html#example-1-plotting-random-data-in-aitoff-projection
* https://stackoverflow.com/questions/46320712/putting-matplotlib-hexbin-into-an-aitoff-projection
* https://stackoverflow.com/questions/7355497/curious-bad-behavior-creating-all-sky-projections-with-matplotlib


Notes:

* Projections aitoff and Mollweide in matplotlib take radian as coordinate unit, range
  from (-pi,pi) and (-pi/2, pi/2).
* astropy can deal with coordinates (deg to and from radian, wrap at 180 deg, ...).
  Probably better than do it manually (but need to import several astropy modules)
* Python package cartopy (which can work with matplotlib) can do similar things and is
  easy to set the central longitude. But cartopy cannot add ticklabels in projections
  other than PlateCarree and Mercator. See https://github.com/SciTools/cartopy/issues/920
  Maybe simply stick with matplotlib
