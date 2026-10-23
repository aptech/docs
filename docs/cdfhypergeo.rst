
cdfHyperGeo
==============================================

Purpose
----------------

Computes the cumulative distribution function for the hypergeometric distribution.

Format
----------------
.. function:: p = cdfHyperGeo(x, pop_size, n_marked, n_drawn)

    :param x: The number of marked items drawn. A fractional *x* is rounded down. An *x* below 0 returns 0 and an *x* above *n_marked* or *n_drawn* returns 1.
    :type x: NxK matrix, Nx1 vector or scalar

    :param pop_size: The size of the population from which draws will be made. ExE conformable with *x*. *pop_size* must be at least *n_marked* and *n_drawn*.
    :type pop_size: matrix

    :param n_marked: The number of marked items. ExE conformable with *x*. :math:`n\_marked \geq 0`.
    :type n_marked: matrix

    :param n_drawn: The number of items drawn from the population. ExE conformable with *x*. :math:`0 \leq n\_drawn \leq pop\_size`.
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

If *pop_size* is negative or smaller than *n_marked* or *n_drawn*, or
*n_marked* or *n_drawn* is negative, :func:`cdfHyperGeo` returns a scalar error code
and :func:`scalerr` returns the position of that argument: 2 for *pop_size*,
3 for *n_marked*, 4 for *n_drawn*. An *x* outside
the range is not an error: it returns 0 or 1. A missing value in any argument
returns a missing value.

.. seealso:: Functions :func:`pdfHyperGeo`, :func:`rndHyperGeo`, :func:`cdfBinomial`
