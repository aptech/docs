
dtYear
==============================================

Purpose
----------------

Extracts the year component from a date/time variable as a decimal number with century included.

Format
----------------
.. function:: year = dtYear(X [, column])

    :param X: Data with metadata.
    :type X: TxK dataframe

    :param columns: Optional, name or index of the date variable in *X* to get years from.
    :type columns: Scalar or string

    :return year: The numeric year components of the dates contained in the column specified by *column*.
    :rtype months: Tx1 vector
    

Examples
----------------

::

  // Load data
  fname = getGAUSSHome("examples/yellowstone.csv");
  data = loadd(fname);

  // Get years for date column
  year = dtYear(data, "Date");
  
  // Print first five and last five
  // observations of dates
  head(data[., "Date"]);
  tail(data[., "Date"]);
  
  // Print corresponding months
     "Years:"
  head(year);
  tail(year);

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
      
          Years:
            2016   
            2015 
            2014 
            2013 
            2012 

            1990 
            1989 
            1988 
            1987 
            1986 

.. seealso:: Functions :func:`dtDayofWeek`, :func:`dtDayofMonth`, :func:`dtDayofYear`, :func:`dtQuarter`, :func:`dtYear`

