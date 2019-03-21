
plotTSLog
==============================================

Purpose
----------------

Creates a graph of time series data with the Y-axis on a log scale.

Format
----------------
.. function:: plotTSLog(myPlot, dtstart, frequency, y)plotTSLog(dtstart, frequency, y) 
			   
			  plotTSLog(myPlot, date_vec, label_unit, y)plotTSLog(date_vec, label_unit, y)

    :param myPlot: 
    :type myPlot: A plotControl structure

    :param dtstart: starting date in DT scalar format. This input is used when the data is evenly spaced and yearly, quarterly or monthly.
    :type dtstart: Scalar

    :param frequency: frequency of the data per year. NOTE: This option is only used with the scalar dtstart input. Valid options include:
    :type frequency: Scalar

    .. csv-table::
        :widths: auto

        "1", "Yearly"
        "4", "Quarterly"
        "12", "Monthly"

    :param date_vec: containing the dates for each observation in the y . The dates in date_vec are required to be:
        In DT Scalar format.Sequential.
        However, the dates in date_vec may be:
        
        Irregularly spaced
        Any freqency which can be represented by DT Scalar format, such as by year, quarter, month, week, day, hour, minute and second.
    :type date_vec: Nx1 vector

    :param label_unit: containing the frequency with which to display the X axis tick labels.
        NOTE: This input is only used with a full length date_vec vector. Valid options include:
    :type label_unit: String

    .. csv-table::
        :widths: auto

        ""seconds"", ""
        ""minutes"", ""
        ""hours"", ""
        ""days"", ""
        ""months"", ""
        ""quarters"", ""
        ""years"", ""

    :param y:  Each column contains the Y values for a particular line.
    :type y: Nx1 or NxM matrix

Examples
----------------

Basic time series plot with start date
++++++++++++++++++++++++++++++++++++++

::

    // Create an exponential curve with some random noise
    y = abs(rndn(30, 1) + exp(seqa(0.1, 0.1, 30)));
    
    // The first input starts the series in January of 1982
    // The second input specifies the data to be monthly
    plotTSLog(1982, 12, y);

T-bill plot with scalar start date
++++++++++++++++++++++++++++++++++

::

    // Create file name with full path
    file = getGAUSSHome() $+ "examples/tbill_3mo.xlsx";
    
    // Load scalar starting date
    date_1 = xlsReadM(file, "A2:A2");
    
    // Load the T-bill data
    y = loadd(file, "tbill_3m");
    
    // Specify the data is monthly
    freq = 12;
    
    // Draw the time series plot
    plotTSLog(date_1, freq, y);

T-bill plot with full date vector
+++++++++++++++++++++++++++++++++

::

    // Create file name with full path
    file = getGAUSSHome() $+ "examples/tbill_3mo.xlsx";
    
    // Load date vector and tbill data
    x = loadd(file, "obs_date + tbill_3m");
    
    // Separate date vector and tbill data
    date_vec = x[ ., 1 ];
    y = x[ ., 2 ];
    
    // Specify that tick labels should be
    // on years, even though the data is monthly
    label_unit = "years";
    
    // Draw the time series plot
    plotTSLog(date_vec, label_unit, y);

Daily data with full date vector
++++++++++++++++++++++++++++++++

::

    // Fully pathed file name
    fname = getGAUSSHome() $+ "examples/xle_daily.xlsx";
    
    // Load all observations from variables,
    // 'Date' and 'Adj Close'
    data = loadd(fname, "Date + Adj Close");
    
    // Select the first 150 observations
    // from the date vector and the adjusted close
    nobs = 150;
    date_vec = data[ 1:nobs, 1 ];
    closing_price = data[ 1:nobs, 2 ];
    
    
    // Draw plot of this daily data, specifying
    // that the X-tick labels should be set in
    // terms of months
    plotTSLog(date_vec, "months", closing_price);

Time Series Plot With Custom X-tics
+++++++++++++++++++++++++++++++++++

::

    // Create file name with full path
    file = getGAUSSHome() $+ "examples/tbill_3mo.xlsx";
    
    // Load date of observation 20 (header is row 1)
    date_1 = xlsReadM(file, "A21:A21");
    
    // Load 28 observations
    y = xlsReadM(file, "B21:B49");
    
    // Declare 'myPlot' to be a plotControl structure
    // and fill it with 'xy' default settings
    struct plotControl myPlot;
    myPlot = plotGetDefaults("xy");
    
    // Place first 'X' tick mark at 1984 month 1 and draw one every 6 months
    plotSetXTicInterval(&myPlot, 6, 1984);
    
    // Display only 4 digit year on 'X' tick labels
    plotSetXTicLabel(&myPlot, "YYYY-QQ");
    
    // Draw time series plot, using settings in 'myPlot'
    plotTSLog(myPlot, date_1, 12, y);

In DT Scalar format, quarters are represented by supplying the first month of the quarter for
the sixth and seventh leading digits. As we see below, 200504 represents April of 2005, but it
also represents the second quarter of April 2005.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // The first input starts the series in the second quarter of 2005
    // The second input specifies the data to be quarterly
    plotTSLog(200504, 4, y);

Remarks
+++++++

Formatting for the X-tick labels can be set with the function
plotSetXTicLabel. If a plotControl structure is not passed in to
plotTSLog, or the format specifier is not set with plotSetXTicLabel the
default formatting: for annual data is "YYYY", for quarterly data
"YYYY-QQ" and for monthly data is "YYYY-MO".

By default missing values in the y variable will be represented as gaps
in the line.

.. seealso:: Functions :func:`plotTS`, :func:`plotTSHF`, :func:`plotSetXTicLabel`, :func:`plotSetXTicInterval`, :func:`plotScatter`
