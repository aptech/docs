
beta
==============================================

Purpose
----------------

Computes the standard Beta function, also called the Euler integral. The beta function is defined as:

.. math:: B(x, y) = \int_{0}^{1} t^{x−1}(1−t)^{y−1}dt

Format
----------------
.. function:: f = beta(x,y)

    :param x: may be real or complex
    :type x: scalar or NxK matrix

    :param y: ExE conformable with x.
    :type y: LxM matrix

    :return f: 

    :rtype f: NxK matrix

Examples
----------------

::

    // Set x
    x = 9;

    // Set y
    y = 3;

    // Call beta function
    f = beta(x, y);

    After the code above:

::

    f = 0.0020202020
    
Remarks
---------------

The Beta function's relationship with the Gamma function is:

.. math:: B(x,y) = \frac{\Gamma(x)×\Gamma(y)}{\Gamma(x+y)}

.. seealso:: :func:`cdfBeta`, :func:`gamma`, :func:`gammacplx`, :func:`zeta`
