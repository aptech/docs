
plotAddScatter
==============================================

Purpose
----------------
Adds a 2-dimensional scatter plot to an existing graph.

Format
----------------
.. function:: plotAddScatter(myPlot, x, y)plotAddScatter(x, y)

    :param myPlot: 
    :type myPlot: A plotControl structure

    :param x:  Each column contains the X values for a particular data point.
    :type x: Nx1 or NxM matrix

    :param y:  Each column contains the Y values for a particular data point.
    :type y: Nx1 or NxM matrix



Remarks
-------

plotAddScatter may only add a scatter plot to 2-D graphs.

This function will not change any of the current graph's settings other
than to resize the view as necessary to display the new curve.

