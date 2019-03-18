
lnfact
==============================================

Purpose
----------------

Computes the natural log of the factorial function and can be used to compute log gamma.

Format
----------------
.. function:: lnfact(x)

    :param x: NxK matrix or N-dimensional array, all elements must be positive.
    :type x: TODO

    :returns: y (*TODO*), NxK matrix containing the natural log of the factorial of each of the elements in x.

Examples
----------------

::

    let x = 100 500 1000;
    y = lnfact(x);

::

    363.73938 
    y = 2611.3305 
        5912.1282

Source
++++++

lnfact.src

.. seealso:: Functions :func:`gamma`

Technical Notes
+++++++++++++++

For x > 1, Stirling's formula is used.

For 0 < x <= 1, ln(gamma(x+1)) is used.

| 

natural logarithm log factorial function
