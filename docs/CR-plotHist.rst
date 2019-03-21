
plotHist
==============================================

Purpose
----------------
Computes and graphs a frequency histogram for a vector. The actual frequencies are plotted for each category.

Format
----------------
.. function:: plotHist(myPlot, x, v)plotHist(x, v)

    :param myPlot: 
    :type myPlot: A plotControl structure

    :param x: 
    :type x: Mx1 vector of data

    :param v: the breakpoints to be used to compute the frequencies      - or -scalar, the number of categories
    :type v: Nx1 vector

Examples
----------------

::

    //Create some data to plot
    x = rndn(5000, 1);
    
    //Plot the data
    plotHist(x, 20);

.. seealso:: Functions :func:`plotHistP`, :func:`plotHistF`, :func:`plotBar`
