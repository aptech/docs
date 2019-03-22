
plotXY
==============================================

Purpose
----------------

Graphs X vs. Y using Cartesian coordinates.

Format
----------------
.. function:: plotXY(myPlot, x, y)plotXY(x, y)

    :param myPlot: 
    :type myPlot: A plotControl structure

    :param x:  Each column contains the X values for a particular line.
    :type x: Nx1 or NxM matrix

    :param y:  Each column contains the Y values for a particular line.
    :type y: Nx1 or NxM matrix



Remarks
-------

By default missing values in the y variable will be represented as gaps
in the line.

.. seealso:: Functions :func:`plotLogX`, :func:`plotLogLog`, :func:`plotScatter`
