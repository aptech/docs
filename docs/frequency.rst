
frequency
==============================================

Purpose
----------------

Generate frequency table.

Format
----------------
.. function:: frequency(x, varlist)

    :param x: Data.
    :type x: NxK dataframe

    :param varlist: Names or indices of variables to be counted. If names, should be entered as a formula string e.g `"rep78 + foreign"`
    :type varlist: Vector or string
    
    :param sort: Optional, indicator to sort from most frequent to least frequent categories. Set to 1 to sort. Default = 0.
    :type sort: scalar


Examples
----------------

::

  // Load data
  fname = getGAUSSHome $+ "examples/auto2.dta";
  auto2 = loadd(fname);

  // Create frequency table for the 'rep78' and 'foreign' variable in 'auto2'
  frequency(auto2, "rep78 + foreign");

This code prints the following tables:

::

      Label     Count   Total %    Cum. %
       Poor         2     2.899     2.899
       Fair         8     11.59     14.49
    Average        30     43.48     57.97
       Good        18     26.09     84.06
  Excellent        11     15.94       100
      Total        69       100


      Label     Count   Total %    Cum. %
   Domestic        52     70.27     70.27
    Foreign        22     29.73       100
      Total        74       100

.. seealso:: Functions :func:`plotFreq`, :func:`plotHist`, :func:`plotHistP`, :func:`plotHistF`
