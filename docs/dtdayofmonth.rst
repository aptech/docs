
dtDayofMonth
==============================================

Purpose
----------------

Extracts the day of the month component from a date/time variable as a decimal number (1-31).

Format
----------------
.. function:: dom = dtDayofMonth(X [, column])

    :param X: Data with metadata.
    :type X: TxK dataframe

    :param column: Optional, name or index of the date variable in *X* to get days of the months from.
    :type column: Scalar or string
    
    :return dom: The day of the month components of the dates contained in the column specified by *column*.
    :rtype dom: Tx1 vector
    

Examples
----------------

::

  // Load data
  fname = getGAUSSHome("examples/yellowstone.csv");
  data = loadd(fname);

  // Get day of the month for date column
  dom = dtDayofMonth(data, "Date");
  
  // Print first five and last five
  // observations of dates
  head(data[., "Date"]);
  tail(data[., "Date"]);
  
  // Print corresponding weeks
  "Day of Month:"
  head(dom);
  tail(dom);

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
      
    Day of Year:

               1 
               1 
               1 
               1 
               1

               1 
               1 
               1 
               1 
               1 

.. seealso:: Functions :func:`dtDayofWeek`, :func:`dtDayofYear`, :func:`dtYear`, :func:`dtMonth`, :func:`dtWeek`

