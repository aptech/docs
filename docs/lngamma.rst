
lngamma
==============================================

Purpose
----------------

Computes the natural log of the gamma function.

Format
----------------
.. function:: y = lngamma(x)

    :param x: all elements must be positive.
    :type x: NxK matrix or N-dimensional array

    :return y: containing the natural log of the gamma function of each of the elements in *x*.

    :rtype y: NxK matrix

Examples
----------------

::

    x = { 4, 8 };
    y = lngamma(x);

::

    y =   1.7917595
          8.5251614


Remarks
-------

The relation between :func:`lngamma` and :func:`lnfact` is:

::

   lngamma(x) = lnfact(x - 1);


Source
------

.. seealso:: Functions :func:`gamma`, :func:`lnfact`

