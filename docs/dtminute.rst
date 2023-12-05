
dtMinute
==============================================

Purpose
----------------

Extracts the minute component from a date/time variable as a number (0-59).

Format
----------------
.. function:: minutes = dtMinute(X [, column])

    :param X: Data with metadata.
    :type X: TxK dataframe

    :param column: Optional, name or index of the date variable in *X* to get minutes from. Default = first column.
    :type column: Scalar or string

    :return minutes: The minutes of the dates in the column specified by *column*.
    :rtype minutes: Tx1 vector
    

Examples
----------------

Example 1
+++++++++++

::

  // Create a date
  date_df = asDate("2008-02-16 18:36:29", "%Y-%m-%d %H:%M:%S");

  // Get minutes
  dtMinute(date_df);

This extracts the minute component:

::

  36

Example 2
++++++++++++

::

    // Load data and convert TIMESTAMP
    // to a date variable. The %s tells GAUSS
    // that it is stored as seconds since
    // Jan 1, 1970
    fname = getGAUSSHome("examples/usd_cad_2018.dat");
    usd_cad = loadd(fname, "date(TIMESTAMP, %s) + BIDPRICE");
    
    // Select the first 5 rows
    usd_cad = head(usd_cad);
    
    // Convert printing format
    usd_cad[.,"TIMESTAMP"] = setcoldateformats(usd_cad[.,"TIMESTAMP"], "%Y-%m-%d %T");
    
    print usd_cad;

::

           TIMESTAMP         BIDPRICE 
    2018-01-01 17:00        1.2550500 
    2018-01-01 17:03        1.2551500 
    2018-01-01 17:03        1.2551800 
    2018-01-01 17:03        1.2551900 
    2018-01-01 17:04        1.2552000


::

    // Get the number of minutes past the hour
    // for the TIMESTAMP variable
    m = dtMinute(usd_cad, "TIMESTAMP");
    print m;

::

       0.0000000 
       3.0000000 
       3.0000000 
       3.0000000 
       4.0000000


.. seealso:: Functions :func:`dtHour`, :func:`dtSecond`

