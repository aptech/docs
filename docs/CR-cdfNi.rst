
cdfni
==============================================

Purpose
----------------
Computes quantiles, or the inverse of the cdf of the Normal distribution.

Format
----------------
.. function:: x = cdfni(p)

    :param p: Normal probability levels, :math:`0 <= p <= 1`.
    :type p: NxK real matrix

    :return x: each value of *x* is the value such that the normal cumulative distribution function is equal to the corresponding value of *p*. :code:`cdfn(x) = p`

    :rtype x: NxK real matrix

Examples
-------

Basic Example
+++++++++++++

::

    print cdfni(0.75);

The code above will print

::

    0.67448975

Example with vector input
++++++++++++++++++++++++

::

    // Create 3x1 vector of probabilities
    p = { 0.05, 0.5, 0.95 };

    x = cdfni(p);

After the code above, *x* will equal

::

      -1.6448536 
       0.0000000 
       1.6448536

.. seealso:: :func:`cdfn`
