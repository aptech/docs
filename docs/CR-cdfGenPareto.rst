
cdfGenPareto
==============================================

Purpose
----------------
Computes the cumulative distribution function for the Generalized Pareto distribution.

Format
----------------
.. function:: cdfGenPareto(x, a, o, k)

    :param x: 
    :type x: NxK matrix or Nx1 vector or scalar

    :param a: Location parameter, ExE conformable with *x*.
    :type a: NxK matrix or Nx1 vector or scalar

    :param o: Scale parameter, ExE conformable with *x*. *o* must be greater than 0.
    :type o: NxK matrix or Nx1 vector or scalar

    :param k: Shape parameter, ExE conformable with *x*.
    :type k: NxK matrix or Nx1 vector or scalar

    :returns: y (*NxK matrix or Nx1 vector or scalar*)


Remarks
-------

The cumulative distribution function for the Generalized Pareto
distribution is defined as:

.. math:: 

    f(x,\mu,\sigma,k) = 
    \begin{cases} 1 - (1 + k\frac{x-\mu}{\sigma})^{\frac{-1}{k}},& k \ne 0\\
    1 - exp(-\frac{x-\mu}{\sigma}), & k = 0
    \end{cases}

.. DANGER:: FIx equation missing here.

Examples
---------

::

    mu = 0;
    sigma = 2;
    k = 5;

    p = cdfGenPareto(3, mu, sigma, k);

After the above code, `p` is equal to

::

     0.3482


.. seealso:: :func:`pdfGenPareto`

