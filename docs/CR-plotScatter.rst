
plotScatter
==============================================

Purpose
----------------
Creates a 2-dimensional scatter plot.

Format
----------------
.. function:: plotScatter(myPlot, x, y) 
			              plotScatter(x, y)

    :param myPlot: A plotControl structure.
    :type myPlot: TODO

    :param x: Nx1 or NxM matrix. Each column contains the X values for a particular data point.
    :type x: TODO

    :param y: Nx1 or NxM matrix. Each column contains the Y values for a particular data point.
    :type y: TODO

Examples
----------------

::

    //Create random normal data
    x = rndn(50, 1);
         
    //Reverse the order of 'x' and set it to be the 'y' value
    y = rev(x);
         
    //Plot the data
    plotScatter(x, y);

.. seealso:: Functions :func:`plotXY`, :func:`plotLogLog`, :func:`plotBox`, :func:`plotHistP`
