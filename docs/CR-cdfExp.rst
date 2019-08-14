
cdfExp
==============================================

Purpose
----------------
Computes the cumulative distribution function for the exponential distribution.

Format
----------------
.. function:: y = cdfExp(x, loc, m)

    :param x: Values at which to evaluate the exponential cdf. :math:`x > 0`.
    :type x: NxK matrix, Nx1 vector or scalar.

    :param loc: Location parameter, ExE conformable with *x*. :math:`loc < x`.
    :type loc: NxK matrix, Nx1 vector or scalar

    :param m: Mean parameter, ExE conformable with *x*. *m* is the inverse of the rate parameter which is often called :math:`\lambda`. :math:`m > 0`.
    :type m: NxK matrix, Nx1 vector or scalar

    :return p: Each element in *p* is the exponential cdf value evaluated at the corresponding element in *x*.

    :type p: NxK matrix, Nx1 vector or scalar

Examples
----------------

::

  // Vector of values
  x = seqa(0, 1, 5);

  // Location parameter
  loc = 0;

  // Mean parameter
  m = 1/1.5~1~2;

  // Call cdfExp
  p = cdfExp(x, loc, m);
  print "p = " p;

After above code,

::

  p =
    0.0000   0.0000   0.0000
    0.7769   0.6321   0.3935
    0.9502   0.8647   0.6321
    0.9889   0.9502   0.7769
    0.9975   0.9817   0.8647

Remarks
-------

The cumulative distribution function for the exponential distribution is defined as

.. math:: 1−exp⁡(− \frac{x−loc}{m})

.. seealso:: Function :func:`pdfExp`
