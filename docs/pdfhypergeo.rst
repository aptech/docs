
pdfHyperGeo
==============================================

Purpose
----------------

Computes the probability mass function for the hypergeometric distribution.

Format
----------------
.. function:: p = pdfHyperGeo(x, pop_size, n_marked, n_drawn)

    :param x: The number of marked items drawn. An *x* within 1e-9 (relative) of a whole number is treated as that whole number. Any other non-whole *x* returns 0, as does an *x* that cannot be drawn: below 0 or below *n_drawn* - (*pop_size* - *n_marked*), or above *n_marked* or *n_drawn*.
    :type x: NxK matrix, Nx1 vector or scalar

    :param pop_size: The size of the population from which draws will be made. ExE conformable with *x*. *pop_size* must be at least *n_marked* and *n_drawn*.
    :type pop_size: NxK matrix, Nx1 vector or scalar

    :param n_marked: The number of marked items. ExE conformable with *x*. :math:`n\_marked \geq 0`.
    :type n_marked: NxK matrix, Nx1 vector or scalar

    :param n_drawn: The number of items drawn from the population. ExE conformable with *x*. :math:`0 \leq n\_drawn \leq pop\_size`.
    :type n_drawn: NxK matrix, Nx1 vector or scalar

    :return p: The probability of drawing *x* marked items.

    :rtype p: NxK matrix, Nx1 vector or scalar

Examples
----------------
You are given 50 hard drives, 4 of which are known to be bad. What is the probability of
drawing exactly 1 bad hard drive if you randomly select 6 drives?

::

    p = pdfHyperGeo(1, 50, 4, 6);

After running the code above, *p* is equal to:

::

    0.34504559

Continuing with the example above, what are the probabilities of drawing exactly 2 or exactly 4 bad hard drives?

::

    x = { 2, 4 };
    p = pdfHyperGeo(x, 50, 4, 6);

After running the code above, *p* is equal to:

::

    0.061615284
    6.5132436e-05

Remarks
-------

The probability mass function for the hypergeometric distribution is defined as:

.. math::

    P(X = x \mid m, k, n) = \frac{\binom{k}{x}\binom{m-k}{n-x}}{\binom{m}{n}}

where *m* is *pop_size*, *k* is *n_marked* and *n* is *n_drawn*.

If *pop_size* is negative or smaller than *n_marked* or *n_drawn*, or
*n_marked* or *n_drawn* is negative, :func:`pdfHyperGeo` returns a scalar error code
and :func:`scalerr` returns the position of that argument: 2 for *pop_size*,
3 for *n_marked*, 4 for *n_drawn*. An *x* that
cannot be drawn is not an error: it returns 0. A missing value in any argument
returns a missing value.

.. seealso:: Functions :func:`cdfHyperGeo`, :func:`rndHyperGeo`, :func:`pdfBinomial`
