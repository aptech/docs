
plotAddVLine
==============================================

Purpose
----------------
Adds a vertical line to an existing plot.

Format
----------------
.. function:: plotAddVLine([myPlot, ]x)

    :param myPlot: Optional argument. An instance of a :class:`plotControl` structure.
    :type myPlot: struct

    :param x: the X coordinate(s) specifying where the vertical lines should be added.
    :type x: scalar or Nx1 vector


Examples
----------------

This example creates a scatter plot of two variables and adds vertical lines representing the 95% quantiles for the X variable.

.. figure:: _static/images/plotaddvline-cr-1.jpg
   :scale: 50 %

::

    // Create file name with full path
    fname = getgausshome()$+"examples/auto2.dta";
    
    // Load specified variables
    auto = loadd(fname, "weight + mpg");
    
    // Declare plotControl structure and
    // fill with default settings for scatter
    struct plotControl plt;
    plt = plotGetDefaults("scatter");
    
    plotSetXLabel(&plt, "Weight (lbs)");
    plotSetYLabel(&plt, "Miles Per Gallon");
    
    // Draw scatter plot
    plotScatter(plt, auto[.,"weight"], auto[.,"mpg"]);
    
    /*
    ** Add vertical line at the median weight
    */
    
    // Compute percentiles of 'weight' variable
    pct = quantile(auto[.,"weight"], 0.025 | 0.975);
    
    // Set line to be gray, 1 pixel wide
    // and to have 'dot'=3 style
    plotSetLinePen(&plt, 1, "gray", 3);
    
    // Draw line
    plotAddVLine(plt, pct);


Remarks
-------

Please note that :func:`plotAddVLine` will add arrows to existing graphs, it
will not create a new graph if one does not exist. :func:`plotAddVLine` is not
yet supported for surface plots.


.. seealso:: Functions :func:`plotAddHLine`, :func:`plotAddVBar`
