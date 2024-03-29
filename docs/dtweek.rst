
dtWeek
==============================================

Purpose
----------------

Extracts the week component from a date/time variable as a decimal number (0-53). Monday
is first day of the week.

Format
----------------
.. function:: weeks = dtWeek(X [, column])

    :param X: Data with metadata.
    :type X: Txk dataframe

    :param column: Optional, name or index of the date variable in *X* to get weeks from.  Default = first column.
    :type column: Scalar or string
    
    :return weeks: The week of the dates in the column specified by *column*.
    :rtype weeks: Tx1 vector
    

Examples
----------------

::

  // Load data
  fname = getGAUSSHome("examples/yellowstone.csv");
  data = loadd(fname);

  // Get weeks for date column
  weeks = dtWeek(data, "Date");
  
  // Print first and last five dates
  head(data[., "Date"]);
  tail(data[., "Date"]);
  
  // Print corresponding weeks
  "Weeks:"
  head(weeks);
  tail(weeks);

The code above prints the following table:

::

            Date 
      2016/01/01 
      2015/01/01 
      2014/01/01 
      2013/01/01 
      2012/01/01
      
            Date 
      1990/12/01 
      1989/12/01 
      1988/12/01 
      1987/12/01 
      1986/12/01 
      
          Weeks:

               0 
               0 
               0 
               0 
               0

              48 
              48
              48 
              48 
              48 

Remarks
------------

- Days before the first Monday of the year will be returned as week 0.


.. seealso:: Functions :func:`dtDayofWeek`, :func:`dtDayofMonth`, :func:`dtDayofYear`, :func:`dtMonth`, :func:`dtYear`

