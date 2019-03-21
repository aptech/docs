
xy
==============================================

Purpose
----------------
Graphs X vs. Y using Cartesian coordinates. NOTE: This function is for the deprecated PQG graphics.

Format
----------------
.. function:: xy(x, y)

    :param x:  Each column contains the X values for a particular line.
    :type x: Nx1 or NxM matrix

    :param y:  Each column contains the Y values for a particular line.
    :type y: Nx1 or NxM matrix



Remarks
-------

Missing values are ignored when plotting symbols. If missing values are
encountered while plotting a curve, the curve will end and a new curve
will begin plotting at the next non-missing value.



Source
------

pxy.src

