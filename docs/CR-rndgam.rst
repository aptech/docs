
rndgam
==============================================

Purpose
----------------

Computes pseudo-random numbers with gamma distribution.

.. NOTE:: :func:`rndgam` is deprecated and should be replaced with :func:`rndGamma`.

Format
----------------
.. function:: rndgam(r, c, alpha)

    :param r: number of rows of resulting matrix.
    :type r: scalar

    :param c: number of columns of resulting matrix.
    :type c: scalar

    :param alpha: ExE conformable with r x c resulting matrix, shape parameters for gamma distribution.
    :type alpha: MxN matrix

    :returns: x (*r x c matrix*), gamma distributed pseudo-random numbers.

Remarks
-------

The properties of the pseudo-random numbers in *x* are:

.. DANGER:: fix equation

.. math::

   E(x) = alphaVar(x) = alphax > 0alpha > 0

Source
------

random.src

.. seealso:: Functions :func:`rndGamma`

