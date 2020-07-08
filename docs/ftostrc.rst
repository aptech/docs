
ftostrC
==============================================

Purpose
----------------

Converts a matrix to a string array using a C language format specification.

Format
----------------
.. function:: sa = ftostrC(x, fmt)

    :param x: real or complex.
    :type x: NxK matrix

    :param fmt: format information.
    :type fmt: Kx1 or 1xK or 1x1 string array

    :return sa: contains the contents of *x* converted into a string array.

    :rtype sa: NxK string array

Examples
----------------

Example 1
+++++++++++

::

    grade = 0.937;
    print ftostrC(100 * grade, "Your course grade is: %f");
    print ftostrC(100 * grade, "Your course grade is: %.1f");
    print ftostrC(100 * grade, "Your course grade is: %9.3f");

will return:

::

    Your course grade is: 93.700000
    Your course grade is: 93.7
    Your course grade is:    93.700

Example 2:
+++++++++++

::

    declare string fmtr = { "%6.3lf",
                            "%11.8lf" };

    declare string fmtc = { "(%6.3lf, %6.3lf)",
                            "(%11.8lf, %11.8lf)" };

    xr = rndn(4, 2);
    xc = sqrt(xr')';

    sar = ftostrC(xr, fmtr);
    sac = ftostrC(xc, fmtc);

    print sar;
    print sac;

produces:

::

     -0.166 1.05565441
     -1.590 -0.79283296
      0.130 -1.84886957
      0.789 0.86089687

     ( 0.000, -0.407) ( 1.02745044, 0.00000000)
     ( 0.000, -1.261) ( 0.00000000, -0.89041168)
     ( 0.361, 0.000) ( 0.00000000, -1.35973143)
     ( 0.888, 0.000) ( 0.92784529, 0.00000000)

Remarks
-------

If *fmt* has *K* elements, each column of *sa* can be formatted separately. If
*x* is complex, there must be two format specifications in each element of
*fmt*.


.. seealso:: Functions :func:`strtof`, :func:`strtofcplx`

