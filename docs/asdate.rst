
asDate
==============================================

Purpose
----------------

Converts columns of matrices, string arrays or dataframes to dates, with the option to specify the display format.

Format
----------------
.. function:: x_date = asDate(X [, fmt, columns])

    :param X: data.
    :type X: NxK matrix or dateframe

    :param fmt: Optional input, contains strftime date/time format characters.
    :type fmt: Mx1 string array

    :param columns: Optional input, the names or indices of the date columns in *X* to set format of.
    :type columns: Mx1 scalar or string

    :return x_date: contains metadata assigning the date display format specified by *fmt* to the variables in *x* specified by *columns*.
    :rtype x_date: NxK dataframe


Examples
----------------

Example 1: Convert strings to dates with the default format
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

:func:`asDate` will automatically interpret date strings formatted like this, 2018-02-14 06:31:27. Only the four digit year is required. Any portion of the remaining information may be present as long as all preceding information is also present.

The display format will be set to reflect the input string. For example:

For example:

::

    print asDate("2018-02-14");    

::

           X1
   2018-02-14


::

    // Create two dates with the same date,
    // but different display formats
    dt_1 = asDate("2018-02");    
    dt_2 = asDate("2018-02-01");    

    print "dt_1 = " dt_1;
    print "dt_2 = " dt_2;
    print "dt_1 == dt_1"; (dt_1 == dt_2);


will print the following.

::

    dt_1 = 
                  X1 
             2018-02 
    
    dt_2 = 
                  X1 
          2018-02-01 
    
    dt_1 == dt_1
           1.0000000


::

    // Create a 2x1 string with dates
    // of different precision
    dt_str = "2003-06-17" $| "2003-06-18 09:21:30";
    
    // Convert to a dataframe
    dt_df = asDate(dt_str);
    print dt_df;

The above code will print out:

::

                  X1 
    2003-06-17 00:00 
    2003-06-18 09:21


Example 2: Change the format of a date variable
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Load data
    fname = getGAUSSHome $+ "examples/xle_daily.xlsx";
    xle = loadd(fname, "date(Date) + Volume");

    // Print the first 2 observations
    print "Dates in original format:";
    print xle[1:2,.];

    // Set date format to month/day/Year
    xle_2 = asDate(xle, "%m/%d/%Y", "Date");

    // Print the first 2 observations
    print "";
    print "Dates in new format:";
    print xle_2[1:2,.];


The above code will print out:

::

    Dates in original format:
                Date          Volume
          2017-06-13        15807900
          2017-06-14        30280200

    Dates in new format:
                Date          Volume
          06/13/2017        15807900
          06/14/2017        30280200


Remarks
------------

You can find a list of the available date format specifiers in the Command Reference entry for :func:`posixtostrc`.

.. seealso:: Functions :func:`dfTypes`, :func:`getColDateFormats`, :func:`asdf`
