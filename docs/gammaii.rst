
gammaii
==============================================

Purpose
----------------

Computes the inverse incomplete gamma function.

Format
----------------
.. function:: g_ii = gammaii(a, p)

    :param a: exponents.
    :type a: MxN matrix

    :param p: incomplete gamma values.
    :type p: KxL matrix or ExE conformable with *a*

    :return g_ii: the inverse incomplete gamma function evaluate at *p*.

    :rtype g_ii: max(M,K) by max(N,L) matrix

Examples
----------------

::

    /*
    ** Create sequence from 0
    ** to 0.9 with a 0.001
    ** increment
    */
    p = seqa(0, 0.001, 0.9/0.001);

    // Find inverse incomplete gamma
    g_ii = gammaii(3, p);

    //  Plot results
    plotXY(p, g_ii);

Globals
-------

`\_ginvinc`, `\__macheps`

inverse incomplete gamma
Source
------

cdfchii.src
