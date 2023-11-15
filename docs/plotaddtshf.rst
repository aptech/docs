
plotAddTSHF
==============================================

Purpose
----------------
Adds high-frequency and irregularly spaced time series data to an already existing plot.

Format
----------------
.. function:: plotAddTSHF([myPlot, ] date_vec, y)

    :param myPlot: Optional argument, a :class:`plotControl` structure.
    :type myPlot: Struct

    :param date_vec: containing the dates for each observation in the *y* . The dates in *date_vec* are **required** to be:

        - In POSIX time/date format i.e. seconds since Jan 1, 1970.
        - Sorted, increasing.

        However, the dates in *date_vec* **may be**:

        - Irregularly spaced
        - Any frequency which can be represented by DT Scalar format, such as by year, quarter, month, week, day, hour, minute, second or millisecond.

    :type date_vec: Nx1 vector

    :param y: Each column contains the Y values for a particular line.
    :type y: Nx1 or NxM matrix

Examples
----------------

Plot Forex tick data with custom X-tick labels
++++++++++++++++++++++++++++++++++++++++++++++

::

    // Create file name with full path
    file = getGAUSSHome("examples/eurusd_tick.csv");

    // Load dates as a string array from the first column of the file
    dt_psx = loadd(file, "date");
    
    // Use first 20 obs only
    dt_psx = dt_psx[1:20];
    
    // Load bid and ask data 
    y = loadd(file, "bid + ask");
    y = y[1:rows(dt_psx), .];

    // Declare plotControl structure
    // and fill with default settings
    struct plotControl myPlot;
    myPlot = plotGetDefaults("xy");

    // Create an X-tick label every 15 seconds
    // Set the first tick label at:
    // October 31st, 2008 at 45 seconds after midnight
    first_label = strctoposix("2008 10 31 12:52", "%Y %m %d %H:%M");
    plotSetXTicInterval(&myPlot, 15, first_label);

    // Draw bids on graph
    plotTSHF(myPlot, dt_psx, "seconds", y[ ., "bid"]);
    
    // Add asks on graph
    plotAddTSHF(dt_psx, y[., "ask"]);

Remarks
-------

By default missing values in the *y* variable will be represented as gaps in the line.

.. seealso:: Functions :func:`plotTSHF`, :func:`plotSetXTicLabel`, :func:`plotSetXTicInterval`, :func:`plotScatter`, :func:`plotTS`, :func:`plotTSLog`

