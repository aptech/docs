
cdfPoisson
==============================================

Purpose
----------------
Computes the Poisson cumulative distribution function.

Format
----------------
.. function:: cdfPoisson(x, lambda)

    :param x: Nx1 vector or scalar. x must be a positive whole number.
    :type x: NxK matrix

    :param lambda: ExE conformable with x. The mean parameter.
    :type lambda: TODO

    :returns: p (*NxK matrix*), Nx1 vector or scalar.

Examples
----------------
Suppose that a hospital emergency department sees and average of 200 patients during the Friday 
	evening shift. What is the probability that they will see fewer than 250 patients during any one Friday evening shift.

::

    p = cdfPoisson(250,200);

After running above code,

::

    p = 0.99971538 or 99.715%

.. seealso:: Functions :func:`cdfPoissonInv`, :func:`pdfPoisson`, :func:`cdfBinomial`, :func:`cdfNegBinomial`

poisson cdf cumulative distribution function
