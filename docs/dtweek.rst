
dtweek
==============================================

Purpose
----------------

Extracts the week component from a date/time variable as a decimal number (1-53). Monday
is first day of the week.

Format
----------------
.. function:: weeks = dtWeek(X [, columns])

    :param X: data with metadata.
    :type X: NxK Dataframe

    :param columns: Optional, names or indices of the date variable in *X* to get weeks from.
    :type columns: Jx1 Vector or string array
    
    :return weeks: the week components of the dates contained in the Jx1 columns specified by *columns*.
    :rtype weeks: NxJ Vector
    

Examples
----------------

::

  // Load data
  fname = getGAUSSHome("examples/yellowstone.csv");
  data = loadd(fname);

  // Get quarters for date column
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
      
    Name of day:

          Friday 
        Thursday 
       Wednesday 
         Tuesday 
          Sunday

        Saturday 
          Friday 
        Thursday 
         Tuesday 
          Monday 

The abbreviated names can be obtained using the optional *abbreviate* input.

::

  // Get weeks for date column
  weeks = dtWeeks(data, "Date");
  
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
               1
               1 
               1 
               1 
               1 

              48 
              48 
              48 
              48 
              48

.. seealso:: Functions :func:`dtDayofWeek`, :func:`dtDayofMonth`, :func:`dtDayofYear`, :func:`dtMonth`, :func:`dtYear`

