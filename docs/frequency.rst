
frequency
==============================================

Purpose
----------------

Generate frequency table.

Format
----------------
.. function:: frequency(x, varlist [, sort])

    :param x: Data.
    :type x: NxK dataframe

    :param varlist: Names or indices of variables to be counted. If names, should be entered as a formula string e.g ``"rep78 + foreign"``. For two-way tables, 
    the variable left of the `"~"` will be reported on rows and variables listed to the right of the 
    table will be reported on columns. E.g ``"df ~ df2 + df3"``, ``"df1"`` categories will be reported in rows, separate columns will be returned for each category in ``"df1"`` and ``"df2"``.
    
    :type varlist: Vector or string
    
    :param sort: Optional, indicator to sort from most frequent to least frequent categories. Set to 1 to sort. Default = 0.
    :type sort: scalar


Examples
----------------

Single one-way table
+++++++++++++++++++++

The simplest use of :func:`frequency` is a single one-way table:

::

  // Load data
  fname = getGAUSSHome $+ "examples/auto2.dta";
  auto2 = loadd(fname);

  // Create frequency table for the 'rep78' variable in 'auto2'
  frequency(auto2, "rep78");

This code prints the following tables:

::

      Label     Count   Total %    Cum. %
       Poor         2     2.899     2.899
       Fair         8     11.59     14.49
    Average        30     43.48     57.97
       Good        18     26.09     84.06
  Excellent        11     15.94       100
      Total        69       100

Sorted one-way tables
++++++++++++++++++++++

The one-way table can be sorted from most frequent to least frequent category using the optional *sort* input:

::

  // Indicator for sorting
  sort = 1;
  
  // Create frequency table for the 'rep78' variable in 'auto2'
  frequency(auto2, "rep78", sort);

This code prints the following tables:

::

       Label      Count   Total %    Cum. % 
     Average         30     43.48     43.48 
        Good         18     26.09     69.57 
   Excellent         11     15.94     85.51 
        Fair          8     11.59      97.1 
        Poor          2     2.899       100 
       Total         69       100      


Multiple one-way tables
+++++++++++++++++++++++++

Adding mutiple RHS variables to the formula string results in multiple one-way tables:

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

Creating two-way tables
+++++++++++++++++++++++++

To create a two-way table, a variable is added on the LHS of the formula string in front of the ``"~"``:

::

    // Load data
    tips2 = loadd(getGAUSSHome("examples/tips2.dta"));
  
    // Get two-way table of 'sex' vs. 'smoker'
    frequency(tips2, "sex ~ smoker");
    
::

      ========================================
         sex               smoker       
      ========================================
                        No       Yes     Total


      Female            55        33        88 
      Male              99        60       159 

      Total            154        93       247
      
.. seealso:: Functions :func:`plotFreq`, :func:`plotHist`, :func:`plotHistP`, :func:`plotHistF`, :func:`tabulate`
