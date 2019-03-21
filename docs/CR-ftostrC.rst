
ftostrC
==============================================

Purpose
----------------

Converts a matrix to a string array using a C language format specification.

Format
----------------
.. function:: ftostrC(x, fmt)

    :param x: real or complex.
    :type x: NxK matrix

    :param fmt: 1xK or 1x1 string array containing format information.
    :type fmt: Kx1

    :returns: sa (*TODO*), NxK string array.

Examples
----------------

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

.. seealso:: Functions :func:`strtof`, :func:`strtofcplx`
