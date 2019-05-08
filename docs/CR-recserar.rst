
recserar
==============================================

Purpose
----------------
Computes a vector of autoregressive recursive series.

Format
----------------
.. function:: recserar(x, y0, rho)

    :param x: If simulating an AR process, this would contain the error term and constant if included in the model.
    :type x: NxK matrix

    :param y0: The starting values for the series
    :type y0: PxK matrix

    :param rho: The AR parameters.
    :type rho: PxK matrix

    :returns: y (*NxK matrix*), containing the series.

Examples
----------------

AR(1) without constant
++++++++++++++++++++++

::

    // Starting value for the time series
    y0 = 0;
    
    // AR(1) parameter
    rho = 0.6;
    
    // Innovations
    eps = rndn(10, 1);
    
    // Simulate AR(1) model
    y = recserar(eps, y0, rho);

AR(2) with constant
+++++++++++++++++++

::

    // Starting value for the time series
    y0 = { 0, 0 };
    
    // AR(2) parameters
    rho = { 0.6, -0.3 };
    
    // Constant term
    const = 1.3;
    
    // Innovations
    eps = rndn(10, 1);
    
    // Simulate AR(2) model with constant
    y = recserar(eps + const, y0, rho);


Example 3
+++++++++

::

    n = 10;
    
    sig = { 1 -.3, -.3 1 };
    mu = { 0, 0 };
    e = rndMVn(n,mu,sig);
    
    x = ones(n,1)~rndn(n,3);
    
    b = 1|2|3|4;
    
    rho = { 0.5, 0.3 };
    y0 = zeros(1,2);
    y = recserar(x*b+e,y0,rho);

In this example, two autoregressive series are formed using 
simulated data. The general form of the series can be written:

::

     y[1,t] = rho[1,1]*y[1,t-1] + x[t,.]*b + e[1,t];
     y[2,t] = rho[2,1]*y[2,t-1] + x[t,.]*b + e[2,t];

The error terms (:math:`e[1,t]` and :math:`e[2,t]`) are not individually serially correlated, but 
they are contemporaneously correlated with each other. The variance-covariance matrix is *sig*.

Remarks
-------

:func:`recserar` is particularly useful in dealing with time series.

Typically, the result would be thought of as :math:`K` vectors of length :math:`N`.

*y0* contains the first :math:`P` values of each of these vectors (thus, these are
prespecified). The remaining elements are constructed by computing a Pth
order "autoregressive" recursion, with weights given by *a*, and then by
adding the result to the corresponding elements of *x*. That is, the tth
row of *y* is given by:

::

   y[t,.] = x[t,.] + a[1,.] * y[t-1,.] +...+ a[P,.] * y[t-p,.], t = P + 1,...N

and

::

   y[t,.] = y0[t,.], t = 1,...,P

Note that the first :math:`P` rows of *x* are not used.

.. seealso:: Functions :func:`recserVAR`, :func:`recsercp`, :func:`recserrc`

