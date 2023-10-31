
dtmonth
==============================================

Purpose
----------------

Extracts the month component from a date/time variable as a decimal number(1-12).

Format
----------------
.. function:: months = dtMonth(X [, columns])

    :param X: data with metadata.
    :type X: NxK Dataframe

    :param columns: Optional, names or indices of the date variable in *X* to get quarters from.
    :type columns: Jx1 Vector or string array

    :return months: the numeric month (1-12) components of the dates contained in the Jx1 columns specified by *columns*.
    :rtype months: NxJ Vector
    

Examples
----------------

::

  // Load data
  fname = getGAUSSHome("examples/yellowstone.csv");
  data = loadd(fname);

  // Get months for date column
  months = dtMonth(data, "Date");
  
  // Print first five and last five
  // observations of dates
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

