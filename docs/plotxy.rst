
plotXY
==============================================

Purpose
----------------

Graphs X vs. Y using Cartesian coordinates.

Format
----------------
.. function:: plotXY([myPlot, ]x, y [, title={}, xlabel={}, ylabel={}, xlim={}, ylim={}, colors={}, legend={}, legend_location={}, line_width={}, line_style={}, marker={}, grid={}, font_name={}, font_scale={}])
              plotXY([myPlot, ]df, formula [, title={}, xlabel={}, ylabel={}, xlim={}, ylim={}, colors={}, legend={}, legend_location={}, line_width={}, line_style={}, marker={}, grid={}, font_name={}, font_scale={}])

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
    
Plot keywords
++++++++++++++++++++++++

Named settings override the corresponding settings on a copy of ``myPlot``.
Omit a keyword or use ``{}`` to use the control or plot defaults.
Named labels take precedence over labels generated from the data.

.. list-table::
    :header-rows: 1
    :widths: 25 75

    * - Keyword
      - Meaning
    * - ``title``
      - Plot title. Use ``""`` to clear it.
    * - ``xlabel``
      - X-axis label. Use ``""`` to clear it.
    * - ``ylabel``
      - Y-axis label. Use ``""`` to clear it.
    * - ``xlim``
      - Two numbers, ``min | max`` or ``min ~ max``, for a numeric X axis.
    * - ``ylim``
      - Two numbers, ``min | max`` or ``min ~ max``, for a numeric Y axis.
    * - ``colors``
      - Color names or RGB values as accepted by :func:`plotSetLineColor`.
    * - ``legend``
      - One string label per series. Use ``""`` to clear the legend.
    * - ``legend_location``
      - Up to three words from ``top``, ``vcenter`` (or ``middle``), ``bottom``, ``left``, ``hcenter``, ``right``, ``inside`` and ``outside``. ``center`` fills an unspecified direction, or both when used alone.
    * - ``line_width``
      - A nonnegative numeric width, or a vector of widths.
    * - ``line_style``
      - Style numbers 1 through 5, or ``solid``, ``dash``, ``dot``, ``dashdot`` and ``dashdotdot``. Also accepts ``dashed``, ``dotted``, ``dash-dot``, ``dash-dot-dot``, ``-``, ``--``, ``:`` and ``-.``.
    * - ``marker``
      - Symbol numbers −1 through 14 and names from :func:`plotSetLineSymbol`, with shortcuts ``o``, ``s``, ``d``, ``^``, ``v``, ``+``, ``x``, ``*`` and ``h``.
    * - ``font_name``
      - A font family for the title, axis labels, tick labels and legend. If the family is unavailable, the system substitutes a font.
    * - ``font_scale``
      - A positive number that multiplies each of these point sizes. For example, ``1.5`` scales an 11-point label to 16.5 points. The default is ``1``.
    * - ``grid``
      - ``0`` (off), ``1`` (major grid), ``"major"``, ``"minor"`` or ``"both"``.

Keywords in a plot call
++++++++++++++++++++++++

::

    years = 2020:2025;
    growth = { 1.2, 2.1, 1.5, 2.4, 1.9, 2.3 };
    plotXY(years, growth, title="GDP growth", xlabel="Year",
        ylabel="Percent", line_style="--", marker="o", grid=1, xlim=2020|2025);


Examples
----------------

Basic formula string
++++++++++++++++++++++++++++

  .. figure:: _static/images/plotxy-plasma-fs-1-400x300px.jpg
     :scale: 50 %

::

    // Create string with full path to file name
    fname = getGAUSSHome("examples/clotting_time.dat");

    // Load all variables from the dataset
    clotting_time = loadd(fname);

    // Draw plot using formula string to specify variables 
    plotXY(clotting_time, "lot1 ~ plasma");


Create previous plot with indexing and plot customization
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

You can create the same plot from the example above without using a formula string as shown below.

::

    // Create string with full path to file name
    fname = getGAUSSHome("examples/clotting_time.dat");
    
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
    fname = getGAUSSHome("examples/clotting_time.dat");

    // Load all variables from the dataset
    clotting_time = loadd(fname);

    // Draw plot using formula string to specify variables 
    plotXY(clotting_time, "lot1 + lot2 ~ plasma");


Create previous plot with indexing and plot customization
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

You can create the same plot from the example above without using a formula string as shown below.

::

    // Create string with full path to file name
    fname = getGAUSSHome("examples/clotting_time.dat");
    
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

See :func:`plotSetXTicInterval` for an example of a time series plot using :func:`plotXY`.

.. seealso:: Functions :func:`plotLogX`, :func:`plotLogLog`, :func:`plotScatter`
