
lower
==============================================

Purpose
----------------

Converts a string or character matrix to lowercase.

Format
----------------
.. function:: lower(x)

    :param x: 
    :type x: string or NxK matrix of character data to be converted to lowercase

    :returns: y (string), or NxK matrix which contains the lowercase
        equivalent of the data in x.

Examples
----------------

::

    x = "MATH 401";
    y = lower(x);
    print y;

::

    math 401

The lower function can be useful when performing case insensitive string comparisons. If you have a program that runs different code depending upon the variable name in a GAUSS dataset or spreadsheet file, you or your colleagues may want to analyze data with inconsistent use of case.

::

    var1 = "Consumption";
    
    if lower(var1) == "gdp";
       //code for gdp branch
    else if lower(var1) == "consumption";
       //code for consumption branch
    endif;

Using the lower function, the code above will operate correctly whether var1 is Consumption, CONSUMPTION or consumption.

.. seealso:: Functions :func:`upper`
