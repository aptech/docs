
cdfHyperGeo
==============================================

Purpose
----------------

Computes the cumulative distribution function for the hypergeometric distribution.

Format
----------------
.. function:: cdfHyperGeo(x, m, k, n)

    :param x: class="BodyD-Column2-Body1">NxK matrix, Nx1 vector or scalar. x must be a positive number and < m
    :type x: TODO

    :param m: The size of the population from which draws will be made. ExE conformable with x. m must be > x, k and n.
    :type m: TODO

    :param k: The number of marked items. ExE conformable with x. 0 < prob < 1.
    :type k: TODO

    :param n: The number of items drawn from the population. ExE conformable with x. 0 < k < m.
    :type n: TODO

    :returns: p (*TODO*), The probability of drawing x or fewer marked items. NxK matrix, Nx1 vector or scalar.

Examples
----------------
You are given 120 hard drives, 14 of which are known to be bad. What is the probability of drawing 2 or fewer bad hard drive if you randomly select 12 drives?

::

    p = cdfHyperGeo(2, 120, 14, 12);

After running the code above, p is equal to:

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

Remarks
+++++++

For invalid inputs, cdfHyperGeo will return a scalar error code which,
when its value is assessed by function scalerr, corresponds to the
invalid input. If the first input is out of range, scalerr will return a
1; if the second is out of range, scalerr will return a 2; etc.

.. seealso:: Functions :func:`pdfHyperGeo`, :func:`rndHyperGeo`, :func:`cdfBinomial`

hypergeometric cdf cumulative distribution function
