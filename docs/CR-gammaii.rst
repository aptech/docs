
gammaii
==============================================

Purpose
----------------

Computes the inverse incomplete gamma function.

Format
----------------
.. function:: gammaii(a, p)

    :param a: exponents.
    :type a: MxN matrix

    :param p: incomplete gamma values.
    :type p: KxL matrix or ExE conformable with *a*

    :returns: x (*max(M,K) by max(N,L) matrix*) , abscissae.

Globals
-------

`\_ginvinc`, `\__macheps`

inverse incomplete gamma
Source
------

cdfchii.src

