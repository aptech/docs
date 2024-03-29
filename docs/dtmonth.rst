
dtMonth
==============================================

Purpose
----------------

Extracts the month component from a date/time variable as a decimal number (1-12).

Format
----------------
.. function:: months = dtMonth(X [, column])

    :param X: Data with metadata.
    :type X: TxK dataframe

    :param columns: Optional, name or index of the date variable in *X* to get months from.  Default = first column.
    :type columns: Scalar or string

    :return months: The numeric month (1-12) of the dates in the column specified by *column*.
    :rtype months: Tx1 vector
    

Examples
----------------

::

  // Load data
  fname = getGAUSSHome("examples/yellowstone.csv");
  data = loadd(fname);

  // Get months for date column
  months = dtMonth(data, "Date");
  
  // Print first and last five dates
  head(data[., "Date"]);
  tail(data[., "Date"]);
  
  // Print corresponding months
  "Months:"
  head(months);
  tail(months);

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
      
         Months:
               1 
               1 
               1 
               1 
               1 

              12 
              12 
              12 
              12 
              12 

.. seealso:: Functions :func:`dtDayofWeek`, :func:`dtDayofMonth`, :func:`dtDayofYear`, :func:`dtQuarter`, :func:`dtYear`

