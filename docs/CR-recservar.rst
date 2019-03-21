
recserVAR
==============================================

Purpose
----------------
Computes a vector autoregressive recursive (VAR) series.

Format
----------------
.. function:: recserVAR(x, y0, pi_)

    :param x: where N is the number of observations and K is the number of vectors in the series
    :type x: NxK matrix

    :param y0: where P is the order of the VAR model, the starting values for each vector in the series.
    :type y0: PxK matrix

    :param pi_: containing the VAR parameters.
    :type pi_: KxK matrix

    :returns: y (*NxK matrix*), containing the series.

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

See Also
recserar, recserrc,
            recsercp

