
lncdfn2
==============================================

Purpose
----------------

Computes natural log of interval of Normal cumulative distribution function.

Format
----------------
.. function:: y = lncdfn2(x, r)

    :param x: abscissae.
    :type x: MxN matrix

    :param r: ExE conformable with *x*, intervals.
    :type r: KxL matrix

    :return y: the log of the integral from *x* to *x+dx* of the Normal distribution, i.e., 
        
        .. math:: ln\ Pr(x < X < x+dx)

    :rtype y: max(M,K)xmax(N,L) matrix

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

    print
    lncdfN2(-10,29);

    -7.6198530241605269e-24

::

    print
    lncdfN2(0,1);

    -1.0748623268620716e+00

::

    print
    lncdfN2(5,1);

    -1.5068446096529453e+01

Source
------

lncdfn.src

.. seealso:: Functions :func:`cdfn2`

