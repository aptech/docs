
lncdfn2
==============================================

Purpose
----------------

Computes natural log of interval of Normal cumulative distribution function.

Format
----------------
.. function:: y = lncdfn2(x, dx)

    :param x: values at which to evaluate the cumulative distribution function.
    :type x: MxN matrix

    :param dx: ExE conformable with *x*, intervals used to compute the upper bound, *x + dx*.
    :type dx: KxL matrix

    :return lnp: the log of the integral from *x* to *x+dx* of the Normal distribution, i.e.,

        .. math:: ln\ Pr(x < X < x+dx)

    :rtype lnp: max(M,K) x max(N,L) matrix

Remarks
-------

The relative error is:

.. csv-table::
    :widths: auto


    ":math:`\|x\| < 1`", "and", ":math:`dx < 1`", "±1e-14"
    ":math:`1 < \|x\| < 37`", "and", ":math:`\|dx\| < 1/\|x\|`", "±1e-13"
    ":math:`min(x,x+dx) > -37`", "and", ":math:`y > -690``", "±1e-11 or better"

A relative error of ±1e-14 implies that the answer is accurate to better
than ±1 in the 14th digit after the decimal point.

Examples
----------------

::

    // Set x
    x = -10;

    // Set interval
    dx = 29;

    print
    lncdfN2(x, dx);

::

    -7.6198530241605269e-24

::

    // Set x
    x = 0;

    // Set interval
    dx = 1;

    print
    lncdfN2(x, dx);

::

    -1.0748623268620716e+00

::

  // Set x
  x = 5;

  // Set interval
  dx = 1;

  print
  lncdfN2(x, dx);

::

    -1.5068446096529453e+01

Source
------

lncdfn.src

.. seealso:: Functions :func:`cdfn2`
