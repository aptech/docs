
dtDayofYear
==============================================

Purpose
----------------

Extracts the day of the year component from a date/time variable as a decimal number (1-366). 

Format
----------------
.. function:: doy = dtDayofYear(X [, column])

    :param X: Data with metadata.
    :type X: TxK dataframe

    :param column: Optional, name or index of the date variable in *X* to get days of the year from.
    :type column: Scalar or string
    
    :return doy: The day of the year components of the dates contained in the column specified by *column*.
    :rtype doy: Tx1 vector
    

Examples
----------------

::

  // Load data
  fname = getGAUSSHome("examples/yellowstone.csv");
  data = loadd(fname);

  // Get day of the year for date column
  doy = dtDayofYear(data, "Date");
  
  // Print first five and last five
  // observations of dates
  head(data[., "Date"]);
  tail(data[., "Date"]);
  
  // Print corresponding weeks
  "Day of Year:"
  head(doy);
  tail(doy);

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

             335 
             335 
             336 
             335 
             335 

.. seealso:: Functions :func:`dtDayofWeek`, :func:`dtDayofMonth`, :func:`dtYear`, :func:`dtMonth`, :func:`dtWeek`

