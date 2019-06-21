
cdfLogNorm
==============================================

Purpose
----------------
Computes the cumulative distribution function of the log-normal distribution.


Format
----------------
.. function:: cdfLogNorm(x[, mu, sigma])

    :param x: Values at which to evaluate the cumulative distribution function for the log-normal distribution.
    :type x: NxK matrix, Nx1 vector or scalar.

    :param mu: Optional input, the mean parameter. Default = 0.
    :type mu: scalar

    :param std: Optional input, the standard deviation parameter. Default = 1.
    :type std: scalar

    :returns: **p** (*NxK matrix, Nx1 vector or scalar*) - Each element in *p* is the cumulative distribution function of the log-normal distribution evaluated at the corresponding element in *x*.

Examples
----------------

Basic Example
+++++++++++++

::

    // Use default 'mu' and 'sigma'
    p = cdfLogNorm(1.7);

After the above, code *p* will equal:

::

    0.70216179

Specify 'mu' and 'std'
++++++++++++++++++++++++

::

    // Create vector of 'x' values
    x = { 0.1, 1.6, 2 };

    // Assign mu value
    mu = 1.5;

    // Assign standard deviation
    std = 2;

    /*
    ** Compute the CDF for the lognormal distribution
    ** parameterized by mu = 1.5 and sigma = 2
    */
    p = cdfLogNorm(x, mu, std);

After the above, code *p* will equal:

::

    0.028631852
    0.30327714
    0.34331728

.. seealso:: Functions :func:`cdfn_cdfNc`, :func:`pdfTruncNorm`, :func:`cdfTruncNorm`, :func:`pdfLogNorm`
