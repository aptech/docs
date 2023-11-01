
dtdayofmonth
==============================================

Purpose
----------------

Extracts the day of the week component from a date/time variable as a decimal number. Default is to start on Sunday (0-6).

Format
----------------
.. function:: dow = dtDayofWeek(X [, columns, startMonday])

    :param X: data with metadata.
    :type X: NxK Dataframe

    :param columns: Optional, names or indices of the date variable in *X* to get days of the week from.
    :type columns: Jx1 Vector or string array
    
    :param startMonday: Optional, indicator variable to start week on Monday (1-7).
    :type startMonday: Scalar
    
    :return dow: the day of the week components of the dates contained in the Jx1 columns specified by *columns*.
    :rtype dow: NxJ Vector
    

Examples
----------------

First find the day of the week components using a Sunday start.

::

  // Load data
  fname = getGAUSSHome("examples/yellowstone.csv");
  data = loadd(fname);

  // Get quarters for date column
  dow = dtDayofWeek(data, "Date");
  
  // Print first five and last five
  // observations of dates
  head(data[., "Date"]);
  tail(data[., "Date"]);
  
  // Print corresponding weeks
  "Day of Week (Sunday start):"
  head(dow);
  tail(dow);

The code above prints the following table, with days ranging from 0-7:

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
      
       Day of Week
    (Sunday Start):
                  5 
                  4 
                  3 
                  2 
                  0

                  6 
                  5 
                  4 
                  2 
                  1 

Now, find the day of the week using a Monday start:

::

   // Get day of the week for date column
  dow = dtDayofWeek(data, "Date", 1);
  
  // Print first five and last five
  // observations of dates
  head(data[., "Date"]);
  tail(data[., "Date"]);
  
  // Print corresponding weeks
  "Day of Week (Monday start):"
  head(dow);
  tail(dow);

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
      
       Day of Week 
   (Monday Start):

                 5 
                 4 
                 3 
                 2 
                 7

                 6 
                 5 
                 4 
                 2 
                 1
                 
.. seealso:: Functions :func:`dtDayofMonth`, :func:`dtDayofYear`, :func:`dtYear`, :func:`dtMonth`, :func:`dtWeek`

