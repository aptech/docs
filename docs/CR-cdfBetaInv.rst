
cdfBetaInv
==============================================

Purpose
----------------
Computes the quantile or inverse of the Beta cumulative distribution function.

Format
----------------
.. function:: cdfBetaInv(p,a,b)

    :param p: Nx1 vector or scalar. 0 < p < 1.
    :type p: NxK matrix

    :param a: ExE conformable with p. 0 < a.
    :type a: TODO

    :param b: ExE conformable with p. 0 < b.
    :type b: TODO

    :returns: x (*NxK matrix*), Nx1 vector or scalar.

Examples
----------------

::

    y = { 0.14228251, 0.20662575, 0.26057158, 0.31087052 };
    a = 0.5;
    b = 0.3;
    p = cdfBeta(y,a,b);
    print "p = "	p;

After running above code,

::

    p =
    	0.1
    	0.2
    	0.3
    	0.4

.. seealso:: Functions :func:`cdfBeta`, :func:`cdfBinomial`, :func:`cdfNegBinomial`

cdf quantile inverse beta cumulative distribution function
