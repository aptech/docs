
plotAddHistP
==============================================

Purpose
----------------
Adds a percent histogram to an existing graph.

Format
----------------
.. function:: plotAddHistP(myPlot, x, v)plotAddHistP(x, v)

    :param myPlot: 
    :type myPlot: A plotControl structure

    :param x: 
    :type x: Mx1 vector of data

    :param v: the breakpoints to be used to compute the
        frequencies      - or -scalar, the number of categories.
    :type v: Nx1 vector



Remarks
-------

plotAddHistP may only add a histogram to 2-D graphs.

This function will not change any of the current graph's settings other
than to resize the view as necessary to display the new curve.

