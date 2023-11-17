
dtMonthName
==============================================

Purpose
----------------

Extracts the month component from a date/time variable as a string name.

Format
----------------
.. function:: month_names = dtMonthName(X [, column, abbreviate])

    :param X: Data with metadata.
    :type X: TxK dataframe

    :param column: Optional, name or index of the date variable in *X* to get months from.  Default = first column.
    :type column: Scalar or string

    :param abbreviate: Optional, indicator variable to abbreviate months. Set to 1 to abbreviate names. Default = 0.
    :type abbreviate: Scalar
    
    :return month_names: The names of the months of the dates in the column specified by *column*.
    :rtype month_names: Tx1 string array
    

Examples
----------------

::

  // Load data
  fname = getGAUSSHome("examples/yellowstone.csv");
  data = loadd(fname);

  // Get month names for date column
  month_names = dtMonthName(data, "Date");
  
  // Print first and last five dates
  head(data[., "Date"]);
  tail(data[., "Date"]);
  
  // Print corresponding months
  "Month Names:"
  head(month_names);
  tail(month_names);

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
      
    Month Names:
    
         January 
         January 
         January 
         January
         January

         December 
         December 
         December 
         December 
         December 

The abbreviated names can be obtained using the optional *abbreviate* input.

::

  // Get month names for date column
  month_names = dtMonthName(data, "Date", 1);
  
  // Print corresponding months
  "Month Names:"
  head(month_names);
  tail(month_names);

The code above prints the following table:

::

    Month Names:
    
             Jan 
             Jan 
             Jan 
             Jan 
             Jan 

             Dec 
             Dec 
             Dec 
             Dec 
             Dec

.. seealso:: Functions :func:`dtDayofWeek`, :func:`dtDayofMonth`, :func:`dtDayofYear`, :func:`dtMonth`, :func:`dtYear`

