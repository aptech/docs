
ftocv
==============================================

Purpose
----------------

Converts a matrix containing floating point numbers into a matrix containing the decimal character representation of each element.

Format
----------------
.. function:: x_cv = ftocv(x, field, prec)

    :param x: numeric data to be converted
    :type x: NxK matrix

    :param field: minimum field width.
    :type field: scalar

    :param prec: the numbers created will have *prec* places after the decimal point.
    :type prec: scalar

    :return x_cv: contains the decimal character
        equivalent of the corresponding elements in *x* in the format defined by *field* and *prec*.

    :rtype x_cv: NxK character matrix

Remarks
-------

-  To convert numbers to strings, or string arrays, use :func:`ntos` instead.
-  Character vectors, as returned by :func:`ftocv`, can only hold 8 characters.
   Therefore, the *field* and *prec* inputs may not be greater than 8.
-  If a number is narrower than *field*, it will be padded on the left with zeros.
-  If :math:`prec = 0`, the decimal point will be suppressed.


Examples
----------------

Basic examples
++++++++++++++

::

    // Field width for 7 characters (including '.'). Display 5 characters after decimal point
    x = ftocv(1.23456789, 7, 5);

    // Print character vector
    print $x;

The code above will return the following output:

::

    1.23457

::

    x = ftocv(1.23456789, 4, 2);
    print $x;

The code above will return the following output:

::

    1.23

::

    x = ftocv(1.23456789, 6, 3);
    print $x;

The code above will return the following output:

::

    01.235

Combining text with numbers
+++++++++++++++++++++++++++

::

    y = { 6, 7, 8, 9, 10 };

    /*
    ** Combine 'beta' with the vector of numbers in 'y'
    ** Use 2 characters for each number with 0 after the decimal point
    */
    x = 0 $+ "beta" $+ ftocv(y, 2, 0);

    /*
    ** Since the output is a character vector the dollar
    ** sign ($) must be used in front of the variable for printing
    */
    print $x;

results in the following output:

::

          beta06
          beta07
          beta08
          beta09
          beta10

Notice that the ``0 $+`` above was necessary to
force the type of the result to matrix because the
string constant ``"beta"`` would be of type string. The
left operand in an expression containing a ``$+`` operator
controls the type of the result.

.. seealso:: Functions :func:`ftos`, :func:`ntos`
