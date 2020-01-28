
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

    :return y: or NxK matrix which contains the lowercase equivalent of the data in *x*.

    :rtype y: string

Examples
----------------

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

Remarks
-------

If *x* is a numeric matrix, *y* will contain garbage. No error message will
be generated since GAUSS does not distinguish between numeric and character data in matrices.


.. seealso:: Functions :func:`upper`
