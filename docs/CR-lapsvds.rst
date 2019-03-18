
lapsvds
==============================================

Purpose
----------------

Computes the singular values of a real or complex rectangular matrix

Format
----------------
.. function:: lapsvds(x)

    :param x: real or complex rectangular matrix.
    :type x: MxN matrix

    :returns: s (*TODO*), min(M,N)x1 vector, singular values.

Examples
----------------

::

    x = { 2.143 4.345 6.124,
          1.244 5.124 3.412,
          0.235 5.657 8.214 };
     
    va = lapsvds(x);
    print va';

::

    13.895868 2.1893939 1.4344261

::

    xi = { 4+1 3+1 2+2,
           1+2 5+3 2+2,
           1+1 2+1 6+2 };
     
    ve = lapsvds(xi);
    print ve';

::

    10.352877 4.0190557 2.3801546

Note the transpose operator (') at the end of the print statements. This causes the output of these column vectors to be printed as a row vector.

.. seealso:: Functions :func:`lapsvdcusv`, :func:`lapsvdusv`

singular values real complex rectangular matrix
