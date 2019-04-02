
gamma
==============================================

Purpose
----------------

Returns the value of the gamma function.

Format
----------------
.. function:: gamma(x)

    :param x: 
    :type x: NxK matrix or N-dimensional array

    :returns: y (*NxK matrix or N-dimensional array*)

Remarks
-------

For each element of *x* this function returns the integral

.. math::

   ∫0⧜t(x−1)⁢e−tdt

.. DANGER:: FIX Equation

All elements of *x* must be positive and less than or equal to 169. Values
of *x* greater than 169 will cause an overflow.

The natural log of :func:`gamma` is often what is required and it can be
computed without the overflow problems of :func:`gamma` using :func:`lnfact`.


Examples
----------------

::

    y = gamma(2.5);

After the code above:

::

    y = 1.329340

.. seealso:: Functions :func:`cdfchic`, :func:`cdfbeta`, :func:`cdffc`, :func:`cdfnc`, :func:`cdftc`, :func:`erf`, :func:`erfc`, :func:`lnfact`

