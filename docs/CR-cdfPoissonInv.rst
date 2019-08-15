
cdfPoissonInv
==============================================

Purpose
----------------
Computes the quantile or inverse Poisson cumulative distribution function.

Format
----------------
.. function:: x = cdfPoissonInv(p, lambda)

    :param p: Probabilities at which to compute the Poisson inverse cumulative distribution function. :math:`0 < p < 1`.
    :type p: NxK matrix

    :param lambda: The mean parameter.
    :type lambda: ExE conformable with *p*

    :return x: each value of *x* is the smallest integer such that the Poisson cumulative distribution function is equal to or exceeds the corresponding value of *p*.

    :rtype x: NxK matrix, Nx1 vector or scalar

Remarks
-------

For invalid inputs, :func:`cdfPoissoninv` will return a scalar error code which,
when its value is assessed by function :func:`scalerr`, corresponds to the
invalid input. If the first input is out of range, :func:`scalerr` will return a
1; if the second is out of range, :func:`scalerr` will return a 2; etc.

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

.. seealso:: Functions :func:`cdfPoisson`, :func:`pdfPoisson`, :func:`cdfBinomial`, :func:`cdfNegBinomial`
