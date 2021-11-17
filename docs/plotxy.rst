
plotXY
==============================================

Purpose
----------------

Graphs X vs. Y using Cartesian coordinates.

Format
----------------
.. function:: plotXY([myPlot, ]x, y)
              plotXY([myPlot, ]df, formula)

    :param myPlot: Optional argument, a :class:`plotControl` structure.
    :type myPlot: struct

    :param x: Each column contains the X values for a particular line.
    :type x: Nx1 or NxM matrix

    :param y: Each column contains the Y values for a particular line.
    :type y: Nx1 or NxM matrix

    :param df: name of the dataframe in memory.
    :type df: dataframe

    :param formula: formula string of the model to be plotted.
        E.g ``"y ~ X1"``, ``y`` is the name of dependent variable to be plotted on the y-axis ``X1`` is the names of the variable to be plotted on the x-axis;

        E.g ``"y ~ X1 + by(X2)"``, ``by(X2)`` specifies that the data should be separated into different lines based on the groups defined by ``X2``.

    :type formula: string
    
Examples
----------------

Basic formula string
++++++++++++++++++++++++++++

  .. figure:: _static/images/plotxy-plasma-fs-1-400x300px.jpg
     :scale: 50 %

  ::

    // Create string with full path to file name
    fname = getGAUSSHome $+ "examples/clotting_time.dat";

    // Load all variables from the dataset
    clotting_time = loadd(fname);

    // Draw plot using formula string to specify variables 
    plotXY(clotting_time, "lot1 ~ plasma");


Create previous plot with indexing and plot customization
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

You can create the same plot from the example above without using a formula string as shown below.

::

    // Create string with full path to file name
    fname = getGAUSSHome $+ "examples/clotting_time.dat";
    
    // Load all variables from the dataset
    clotting_time = loadd(fname);
    
    struct plotControl plt;
    plt = plotGetDefaults("xy");
    
    // Set x and y label text
    plotSetXLabel(&plt, "plasma", "arial", 12);
    plotSetYLabel(&plt, "lot1");
    
    // Draw plot using indexing to specify x and y variables
    plotXY(plt, clotting_time[.,"plasma"], clotting_time[.,"lot1"]);




Formula string with multiple y variables
+++++++++++++++++++++++++++++++++++++++++++++


  .. figure:: _static/images/plotxy-plasma-fs-2-400x300px.jpg
     :scale: 50 %

  ::

    // Create string with full path to file name
    fname = getGAUSSHome $+ "examples/clotting_time.dat";

    // Load all variables from the dataset
    clotting_time = loadd(fname);

    // Draw plot using formula string to specify variables 
    plotXY(clotting_time, "lot1 + lot2 ~ plasma");


Create previous plot with indexing and plot customization
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

You can create the same plot from the example above without using a formula string as shown below.

::

    // Create string with full path to file name
    fname = getGAUSSHome $+ "examples/clotting_time.dat";
    
    // Load all variables from the dataset
    clotting_time = loadd(fname);
    
    struct plotControl plt;
    plt = plotGetDefaults("xy");
    
    // Set x label text and font
    plotSetXLabel(&plt, "plasma", "arial", 12);

    plotSetLegend(&plt, "lot1" $| "lot2");
    
    // Draw plot using indexing to specify x and y variables
    plotXY(plt, clotting_time[.,"plasma"], clotting_time[.,"lot1" "lot2"]);


Remarks
-------

By default missing values in *y* will be represented as gaps
in the line.

.. seealso:: Functions :func:`plotLogX`, :func:`plotLogLog`, :func:`plotScatter`
