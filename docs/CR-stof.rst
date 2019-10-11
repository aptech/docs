
stof
==============================================

Purpose
----------------
Converts a string to floating point.

Format
----------------
.. function:: y = stof(x)

    :param x: character elements to be converted
    :type x: string or NxK matrix

    :return y: the floating point equivalents of the ASCII numbers in *x*.

    :rtype y: matrix

Examples
----------------

Basic string to floating point number
+++++++++++++++++++++++++++++++++++++

::

    x = stof("3.14");

After the above code, *x* will be a 1x1 matrix equal to 3.14.

Convert a string "." to a missing value
+++++++++++++++++++++++++++++++++++++++

::

    x = stof(".");
    
    //If 'x' is a 1x1 missing value
    if scalmiss(x);
        print "'x' is a missing value";
    endif;

After the above code, *x* will be a 1x1 missing value (``.``) and the code will print the message 
"'x' is a missing value".

Convert a string containing space separated numbers to a vector.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    x = stof("1 2 3");

After the above code, *x* will be a 3x1 vector, containing

::

    1
    2
    3

Remarks
-------

-  To convert string arrays to floating point numeric values, or to
   convert strings representing complex data, use :func:`strtof`.
-  If *x* is a null string (""), :func:`stof` will return a 0.
-  This uses the same input conversion routine as `loadm` and `let`. It will
   convert character elements and missing values. :func:`stof` also converts
   complex numbers in the same manner as `let`.

.. seealso:: Functions :func:`ftos`, :func:`ftocv`, :func:`chrs`, :func:`strtof`

