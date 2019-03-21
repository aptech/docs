
cdfLaplace
==============================================

Purpose
----------------
Computes the cumulative distribution function for the Laplace distribution.

Format
----------------
.. function:: cdfLaplace(x, a, b)

    :param x: 
    :type x: NxK matrix or Nx1 vector or scalar.

    :param a: Location parameter, ExE conformable with *x*.
    :type a: NxK matrix or Nx1 vector or scalar

    :param b: Scale parameter; ExE conformable with *x*. *b* must be greater than 0.
    :type b: NxK matrix or Nx1 vector or scalar

    :returns: y (*NxK matrix or Nx1 vector or scalar*)

Remarks
-------

The cumulative distribution function for the Laplace distribution is
defined as

.. DANGER:: ADd missing equation here

.. seealso:: :func:`cdfLaplaceInv`

