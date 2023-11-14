
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
    :type X: Tx1 dataframe

    :param column: Optional, name or index of the date variable in *X* to get weeks from.
    :type column: Scalar or string
    
    :return weeks: The week components of the dates contained in the column specified by *column*.
    :rtype weeks: Tx1 vector
    

Examples
----------------

::

  // Load data
  fname = getGAUSSHome("examples/yellowstone.csv");
  data = loadd(fname);

  // Get weeks for date column
  weeks = dtWeek(data, "Date");
  
  // Print first five and last five
  // observations of dates
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

.. seealso:: Functions :func:`dtDayofWeek`, :func:`dtDayofMonth`, :func:`dtDayofYear`, :func:`dtMonth`, :func:`dtYear`

