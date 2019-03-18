
stof
==============================================

Purpose
----------------
Converts a string to floating point.

Format
----------------
.. function:: stof(x)

    :param x: string or NxK matrix containing character elements to be converted.
    :type x: TODO

    :returns: y (*matrix*), the floating point equivalents of the ASCII numbers in x.

Examples
----------------

x = stof("3.14");
+++++++++++++++++

After the above code, x will be a 1x1 matrix equal to 3.14.

x = stof(".");

//If 'x' is a 1x1 missing value
if scalmiss(x);
    print "'x' is a missing value";
endif;
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

After the above code, x will be a 1x1 missing value (.) and the code will print the message 
"'x' is a missing value".

x = stof("1 2 3");
++++++++++++++++++

After the above code, x will be a 3x1 vector, conaining

::

    1
    2
    3

Remarks
+++++++

-  To convert string arrays to floating point numeric values, or to
   convert strings representing complex data, use strtof.
-  If x is a null string (""), stof will return a 0.
-  This uses the same input conversion routine as loadm and let. It will
   convert character elements and missing values. stof also converts
   complex numbers in the same manner as let.

.. seealso:: Functions :func:`ftos`, :func:`ftocv`, :func:`chrs`, :func:`strtof`
