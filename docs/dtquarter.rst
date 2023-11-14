
dtQuarter
==============================================

Purpose
----------------

Extracts the quarter from a date/time variable (1-4).

Format
----------------
.. function:: qtrs = dtQuarter(X [, column])

    :param X: Data with metadata.
    :type X: TxK dataframe

    :param column: Optional, name or index of the date variable in *X* to get quarters from.
    :type column: Scalar or string

    :return qtrs: The numeric quarter (1-4) components of the dates contained in the column specified by *columns*.
    :rtype qtrs: Tx1 vector
    

Examples
----------------

::

  // Load data
  fname = getGAUSSHome("examples/yellowstone.csv");
  data = loadd(fname);

  // Get quarters for date column
  qtrs = dtQuarter(data, "Date");
  
  // Print first five and last five observations
  head(data[., "Date"]);
  tail(data[., "Date"]);
  
  // Print corresponding quarters
  "Quarters:";
  head(qtrs);
  tail(qtrs);

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
         
       Quarters:
               1 
               1 
               1 
               1 
               1 

               4 
               4 
               4 
               4
               4 

.. seealso:: Functions :func:`dtDayofWeek`, :func:`dtDayofMonth`, :func:`dtDayofYear`, :func:`dtMonth`, :func:`dtYear`

