
cdfPoissonInv
==============================================

Purpose
----------------
Computes the quantile or inverse Poisson cumulative distribution function.

Format
----------------
.. function:: cdfPoissonInv(p, lambda)

    :param p: Nx1 vector or scalar. 0 < p < 1.
    :type p: NxK matrix

    :param lambda: ExE conformable with p. The mean parameter.
    :type lambda: TODO

    :returns: x (*NxK matrix*), Nx1 vector or scalar.

Examples
----------------
Suppose that a hospital emergency department sees an average of 200 patients during the Friday evening shift. 
If the hospital wants to have enough staff on hand to handle the patient load on 95% of Friday evenings, how 
many patients do they need staff on hand for?

::

    x = cdfPoissonInv(.95,200);

After running above code, the hospital should expect to see 224 or few patients on 95% of Friday evenings.

::

    x = 224

Remarks
+++++++

For invalid inputs, cdfPoissoninv will return a scalar error code which,
when its value is assessed by function scalerr, corresponds to the
invalid input. If the first input is out of range, scalerr will return a
1; if the second is out of range, scalerr will return a 2; etc.

.. seealso:: Functions :func:`cdfPoisson`, :func:`pdfPoisson`, :func:`cdfBinomial`, :func:`cdfNegBinomial`

inverse poisson cdf cumulative distribution function
