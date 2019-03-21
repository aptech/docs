
beta
==============================================

Purpose
----------------

Computes the standard Beta function, also called the Euler integral. The beta function is defined as:

.. math:: B(x,y) = ∫01 tx−1(1−t)y−1dt

.. DANGER:: FIX EQUATION

Format
----------------
.. function:: beta(x,y)

    :param x: may be real or complex
    :type x: scalar or NxK matrix

    :param y: ExE conformable with x.
    :type y: LxM matrix

    :returns: f (NxK matrix)

Remarks
---------------

The Beta function's relationship with the Gamma function is:

.. math:: gamma(x)×gamma(y)gamma(x+y)


.. seealso:: :func:`cdfBeta`, :func:`gamma`, :func:`gammacplx`, :func:`zeta`

