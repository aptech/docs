
cdfLogistic
==============================================

Purpose
----------------
Computes the cumulative distribution function for the logistic distribution.

Format
----------------
.. function:: cdfLogistic(x, a, b)

    :param x: 
    :type x: NxK matrix or Nx1 vector or scalar.

    :param a: Location parameter, ExE conformable with *x*.
    :type a: NxK matrix or Nx1 vector or scalar

    :param b: Scale parameter, ExE conformable with *x*. *b* must be greater than 0.
    :type b: NxK matrix or Nx1 vector or scalar

    :returns: y (*NxK matrix or Nx1 vector or scalar*)

Remarks
-------

The cumulative distribution function for the logistic distribution is
defined as:

.. math::

    f(x, \mu, \sigma) = \frac{1}{1 + exp(-z)}

.. DANGER:: Define missing equation

where

.. math::

    z = \frac{x - \mu}{\sigma}

.. DANGER:: Define missing equation

Examples
--------

::

    x = { 1, 2, 3 };
    p = cdfLogistic(x, 0, 2);

After the above code, `p` will equal:

::

    0.6225 
    0.7311 
    0.8176 

.. seealso:: :func:`pdfLogistic`

