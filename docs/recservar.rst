
recserVAR
==============================================

Purpose
----------------
Computes a vector autoregressive recursive (VAR) series.

Format
----------------
.. function:: y = recserVAR(x, y0, pi\_)

    :param x: data matrix where :math:`N` is the number of observations and :math:`K` is the number of vectors in the series
    :type x: NxK matrix

    :param y0: :math:`P` is the order of the VAR model, the starting values for each vector in the series.
    :type y0: PxK matrix

    :param pi\_: contains the VAR parameters.
    :type pi\_: KxK matrix

    :return y: contains the series.

    :rtype y: NxK matrix

Examples
----------------

VAR(1) without constant
+++++++++++++++++++++++

::

    // Starting value for the time series
    y0 = { 0 0 };

    // VAR(1) parameter matrix
    pi_ = { 0.6 -0.2,
            -0.4 0.3 };

    // Innovations
    eps = rndn(100, 2);

    // Simulate VAR(1) model
    y = recserVAR(eps, y0, pi_);

VAR(1) with constant
++++++++++++++++++++

::

    // Starting value for the time series
    y0 = { 0 0 0 };

    // VAR(1) parameter matrix
    pi_ = {  0.6 -0.2  0.1,
            -0.4  0.3 0.25,
            0.33 0.15  0.4 };

    // Constant term
    const = { -0.7 1.3 0.5 };

    // Innovations
    eps = rndn(100, 3);

    // Simulate AR(2) model with constant
    y = recserVAR(eps + const, y0, pi_);

Remarks
---------

:func:`recserVAR` currently only supports VAR(1) models.

.. seealso:: Functions :func:`recserar`, :func:`recserrc`, :func:`recsercp`
