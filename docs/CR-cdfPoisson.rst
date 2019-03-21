
cdfPoisson
==============================================

Purpose
----------------
Computes the Poisson cumulative distribution function.

Format
----------------
.. function:: cdfPoisson(x, lambda)

    :param x: must be a positive whole number.
    :type x: NxK matrix or Nx1 vector or scalar

    :param lambda: The mean parameter.
    :type lambda: ExE conformable with *x*

    :returns: p (*NxK matrix or Nx1 vector or scalar*)

Remarks
-------

For invalid inputs, :func:`cdfPoisson` will return a scalar error code which,
when its value is assessed by function :func:`scalerr`, corresponds to the
invalid input. If the first input is out of range, :func:`scalerr` will return a
1; if the second is out of range, :func:`scalerr` will return a 2; etc.

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

