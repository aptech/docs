
plotAddTS
==============================================

Purpose
----------------

Adds a curve of time series data to an existing time series plot.

Format
----------------
.. function:: plotAddTS(myPlot, dtstart, frequency, y)plotAddTS(dtstart, frequency, y)

    :param myPlot: 
    :type myPlot: A plotControl structure

    :param dtstart: starting date in DT scalar format.
    :type dtstart: Scalar

    :param frequency: frequency of the data per year. Valid options include:
    :type frequency: Scalar

    .. csv-table::
        :widths: auto

        "1", "Yearly"
        "4", "Quarterly"
        "12", "Monthly"

    :param y:  Each column contains the Y values for a particular line.
    :type y: Nx1 or NxM matrix

Examples
----------------

//Create some data to plot
y = rndn(100, 1);

//The first input starts the series in January of 1982
//The second input specifies the data to be monthly
plotTS(1982, 12, y);

y2 = rndu(28, 1);

//Add the data from 'y2' as quarterly data
//starting in Q2 of 1980
plotAddTS(198004, 4, y2);
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Remarks
+++++++

You may only add time series graphs to other time series graphs. For
more information on time series graphs, see **Time Series Plots in
GAUSS**, Section 1.1.

By default missing values in the y variable will be represented as gaps
in the line.

.. seealso:: Functions :func:`plotSetXTicLabel`, :func:`plotSetXTicInterval`, :func:`plotTS`
