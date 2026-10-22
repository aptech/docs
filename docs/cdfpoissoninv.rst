
cdfPoissonInv
==============================================

Purpose
----------------
Computes the quantile or inverse Poisson cumulative distribution function.

Format
----------------
.. function:: x = cdfPoissonInv(p, lambda)

    :param p: Probabilities at which to compute the Poisson inverse cumulative distribution function. :math:`0 \leq p \leq 1`.
    :type p: NxK matrix

    :param lambda: The mean parameter. :math:`lambda \geq 0`.
    :type lambda: ExE conformable with *p*

    :return x: each value of *x* is the smallest integer such that the Poisson cumulative distribution function is equal to or exceeds the corresponding value of *p*.

    :rtype x: NxK matrix, Nx1 vector or scalar

Examples
----------------
Suppose that a hospital emergency department sees an average of 200 patients during the Friday evening shift.
If the hospital wants to have enough staff on hand to handle the patient load on 95% of Friday evenings, how
many patients do they need staff on hand for?

::

    // Probability
    p = 0.95;

    // The average observations
    lambda = 200;

    // Call cdfPoissonInv
    x = cdfPoissonInv(p, lambda);

After running above code, the hospital should expect to see 224 or few patients on 95% of Friday evenings.

::

    x = 224

Remarks
-------

The number of events has no upper limit, so *p* = 1 returns +INF (unless
*lambda* = 0, when every result is 0).

If *p* is outside [0, 1] or *lambda* is below 0, :func:`cdfPoissonInv` returns
a scalar error code and :func:`scalerr` returns the position of that argument: 1
for *p*, 2 for *lambda*. A missing value in either argument returns a missing
value.

.. seealso:: Functions :func:`cdfPoisson`, :func:`pdfPoisson`, :func:`cdfBinomial`, :func:`cdfNegBinomial`
