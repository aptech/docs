
plotAddHLine
==============================================

Purpose
----------------
Adds a horizontal line to an existing plot.

Format
----------------
.. function:: plotAddHLine([myPlot, ]y)

    :param myPlot: Optional argument. An instance of a :class:`plotControl` structure.
    :type myPlot: struct

    :param y: the Y coordinate(s) specifying where the horizontal lines should be added.
    :type y: scalar or Nx1 vector


Examples
----------------

This example creates a scatter plot of two variables and adds horizontal lines representing the 95% confidence interval and the median for the Y variable.

.. figure:: _static/images/plotaddhline-cr-1.jpg
   :scale: 50 %

::

    // Create file name with full path
    dataset = getGAUSSHome() $+ "examples/nba_ht_wt.xls";
    
    // Load variables from the Excel file
    nba = loadd(dataset, "Height + Weight");
    
    // Declare plotControl structure and 
    // fill with default settings
    struct plotControl plt;
    plt = plotGetDefaults("scatter");
    
    plotSetTitle(&plt, "NBA Player Size", "Arial", 14);
    
    plotSetXLabel(&plt, "Weight (lbs)", "Arial", 12);
    plotSetYLabel(&plt, "Height (inches)");
    
    // No legend item for initial scatter plot.
    // Set legend text for horizontal line we add later
    legend_text = "" $| "Median Height";
    plotSetLegend(&plt, legend_text, "top left inside");
    
    // Turn off legend border
    plotSetLegendBorder(&plt, "white", 0);
    
    // Draw scatter plot
    plotScatter(plt, nba[.,"Weight"], nba[.,"Height"]);
    
    // Compute median height and add to plot
    med_ht = median(nba[.,"Height"]);
    plotAddHLine(med_ht);


Remarks
-------

Please note that :func:`plotAddHLine` will add arrows to existing graphs, it
will not create a new graph if one does not exist. :func:`plotAddHLine` is not
yet supported for surface plots.


.. seealso:: Functions :func:`plotAddVLine`, :func:`plotAddHBar`
