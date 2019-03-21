
cdfHyperGeo
==============================================

Purpose
----------------

Computes the cumulative distribution function for the hypergeometric distribution.

Format
----------------
.. function:: cdfHyperGeo(x, m, k, n)

    :param x: must be a positive number and :math:`< m`
    :type x: NxK matrix or Nx1 vector or scalar

    :param m: The size of the population from which draws will be made. ExE conformable with *x*. *m* must be :math:`> x, k and n`.
    :type m: matrix

    :param k: The number of marked items. ExE conformable with *x*. :math:`0 < prob < 1`.
    :type k: matrix

    :param n: The number of items drawn from the population. ExE conformable with *x*. :math:`0 < k < m`.
    :type n: matrix

    :returns: p (*NxK matrix, Nx1 vector or scalar*), The probability of drawing *x* or fewer marked items. 

Remarks
------------

For invalid inputs, :func:`cdfHyperGeo` will return a scalar error code which,
when its value is assessed by function :func:`scalerr`, corresponds to the
invalid input. If the first input is out of range, :func:`scalerr` will return a
1; if the second is out of range, :func:`scalerr` will return a 2; etc.

Examples
----------------
You are given 120 hard drives, 14 of which are known to be bad. What is the probability of drawing 2 or fewer bad hard drive if you randomly select 12 drives?

::

    p = cdfHyperGeo(2, 120, 14, 12);

After running the code above, *p* is equal to:

::

    0.85284036

Continuing with the example above, what are the probabilities of drawing 4 or fewer bad hard drives if you draw 20 or 40 hard drives?

::

    x = 4;
    n_total = 120;
    n_bad = 14;
    n_draw = { 20, 40 };
    p = cdfHyperGeo(x, n_total, n_bad, n_draw); 
    print p;

After running the code above, p is equal to:

::

    0.94307042 
    0.47070798

.. seealso:: Functions :func:`pdfHyperGeo`, :func:`rndHyperGeo`, :func:`cdfBinomial`

