
cdfHyperGeo
==============================================

Purpose
----------------

Computes the cumulative distribution function for the hypergeometric distribution.

Format
----------------
.. function:: p = cdfHyperGeo(x, pop_size, n_marked, n_items)

    :param x: must be a positive number and :math:`0 < x < pop\_size`
    :type x: NxK matrix, Nx1 vector or scalar

    :param pop_size: The size of the population from which draws will be made. ExE conformable with *x*. :math:`pop\_size > x,\:\ n\_marked\:\ and\:\ n\_items`.
    :type pop_size: matrix

    :param n_marked: The number of marked items. ExE conformable with *x*. :math:`0 < n\_marked`.
    :type n_marked: matrix

    :param n_drawn: The number of items drawn from the population. ExE conformable with *x*. :math:`0 < n\_drawn < pop\_size`.
    :type n_drawn: matrix

    :return p: The probability of drawing *x* or fewer marked items.

    :rtype p: NxK matrix, Nx1 vector or scalar

Examples
----------------
You are given 120 hard drives, 14 of which are known to be bad. What is the probability of drawing 2 or fewer bad hard drive if you randomly select 12 drives?

::

    // Value of interest
    x = 2;

    // Total population
    pop_size = 120;

    // Marked items
    n_marked = 14;

    // Number drawn
    n_drawn = 12;

    // Call cdfHyperGeo
    p = cdfHyperGeo(x, pop_size, n_marked, n_drawn);

After running the code above, *p* is equal to:

::

    0.85284036

Continuing with the example above, what are the probabilities of drawing 4 or fewer bad hard drives if you draw 20 or 40 hard drives?

::

    // Value of interest
    x = 4;

    // Total population
    pop_size = 120;

    // Marked items
    n_marked = 14;

    // Number drawn
    n_drawn = { 20, 40 };

    p = cdfHyperGeo(x, pop_size, n_marked, n_drawn);
    print p;

After running the code above, *p* is equal to:

::

    0.94307042
    0.47070798

Remarks
------------

For invalid inputs, :func:`cdfHyperGeo` will return a scalar error code which,
when its value is assessed by function :func:`scalerr`, corresponds to the
invalid input. If the first input is out of range, :func:`scalerr` will return a
1; if the second is out of range, :func:`scalerr` will return a 2; etc.

.. seealso:: Functions :func:`pdfHyperGeo`, :func:`rndHyperGeo`, :func:`cdfBinomial`
