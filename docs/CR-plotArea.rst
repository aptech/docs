
plotArea
==============================================

Purpose
----------------

Creates a stacked area plot.

Format
----------------
.. function:: plotArea([myPlot, ]x, y[, base])

    :param myPlot: Optional argument, a :class:`plotControl` structure
    :type myPlot: struct

    :param x:  The X values for a particular line.
    :type x: Nx1 matrix

    :param y: Each column contains the Y values for a particular line. If *y* contains more than
        one column, each column will be stacked on top of the previous column.
    :type y: Nx1 or NxM matrix

    :param base: Optional argument, the height for the base of the area plot. The default value is zero. 
        :func:`plotArea` does not yet support a vector input for base.
    :type base: scalar 

Examples
----------------

::

    x = { 1, 2, 3, 4 };
    y = {   1  1.5  0.9,
          0.8  1.2  1.8,
            1  0.7    2,
          1.2    1  1.2 };
    
    //Draw a cumulative area plot of the columns of 'y'
    plotArea(x, y);

.. seealso:: Functions :func:`plotLogX`, :func:`plotLogLog`, :func:`plotScatter`

