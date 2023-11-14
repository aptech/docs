
dtDayName
==============================================

Purpose
----------------

Extracts the day component from a date/time variable as a string name.

Format
----------------
.. function:: day_names = dtDayName(X [, columns, abbreviate])

    :param X: Data with metadata.
    :type X: TxK dataframe

    :param column: Optional, name or index of the date variable in *X* to get day names from.
    :type column: Scalar or string array

    :param abbreviate: Optional, indicator variable to abbreviate months. Set to 1 to abbreviate names. Default = 0.
    :type abbreviate: Scalar
    
    :return day_names: the name of the day components of the dates contained in the Jx1 columns specified by *columns*.
    :rtype day_names: Tx1 string array
    

Examples
----------------

::

  // Load data
  fname = getGAUSSHome("examples/yellowstone.csv");
  data = loadd(fname);

  // Get day of the week names for date column
  day_names = dtDayName(data, "Date");
  
  // Print first five and last five
  // observations of dates
  head(data[., "Date"]);
  tail(data[., "Date"]);
  
  // Print corresponding days of the week
  "Name of day:"
  head(day_names);
  tail(day_names);

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

  // Get day names for date column
  day_names = dtDayName(data, "Date", 1);
  
  // Print first five and last five
  // observations of dates
  head(data[., "Date"]);
  tail(data[., "Date"]);
  
  // Print corresponding days of the week
  "Name of day:"
  head(day_names);
  tail(day_names);

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
             Fri 
             Thu 
             Wed 
             Tue 
             Sun 

             Sat 
             Fri 
             Thu 
             Tue 
             Mon

.. seealso:: Functions :func:`dtDayofWeek`, :func:`dtDayofMonth`, :func:`dtMonthName`, :func:`dtDayofYear`, :func:`dtMonth`, :func:`dtYear`

