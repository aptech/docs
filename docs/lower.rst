
lower
==============================================

Purpose
----------------

Converts a string or character matrix to lowercase.

Format
----------------
.. function:: y = lower(x)

    :param x: data to be converted to lowercase
    :type x: string or NxK matrix

    :return y: which contains the lowercase equivalent of the data in *x*.

    :rtype y: string or NxK matrix

Examples
----------------

::

    // Load example dataframe
    rep78 = loadd(getGAUSSHome("examples/auto2.dta"), "rep78");

    print rep78[1:4];

::

           rep78 
         Average 
         Average 
               . 
         Average


::

   rep78_u = lower(rep78);
   print rep78_u[1:4];

::

           rep78 
         average 
         average 
               . 
         average

::

::

    x = "MATH 401";
    y = lower(x);
    print y;

::

    math 401

The :func:`lower` function can be useful when performing case insensitive string comparisons.
If you have a program that runs different code depending upon the variable name in a GAUSS dataset
or spreadsheet file, you or your colleagues may want to analyze data with inconsistent use of case.

::

    var1 = "Consumption";

    if lower(var1) == "gdp";
       // code for gdp branch
    else if lower(var1) == "consumption";
       // code for consumption branch
    endif;

Using the :func:`lower` function, the code above will operate correctly whether *var1* is ``Consumption``, ``CONSUMPTION`` or ``consumption``.

.. seealso:: Functions :func:`upper`
