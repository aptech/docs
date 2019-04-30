
cdfLogNorm
==============================================

Purpose
----------------
Computes the cumulative distribution function of the log-normal distribution.
  

Format
----------------
.. function:: cdfLogNorm(x[, mu, sigma])

    :param x: the limits of integration.
    :type x: matrix or array

    :param mu: Optional input, the mean parameter. Default = 0.
    :type mu: scalar

    :param sigma: Optional input, the standard deviation parameter. Default = 1.
    :type sigma: scalar

    :returns: p (matrix or array), the same dimension as the input *x*, containing
        the cumulative probabilities.

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

Specify 'mu' and 'sigma'
++++++++++++++++++++++++

::

    // Create vector of 'x' values
    x = { 0.1, 1.6, 2 };
    
    mu = 1.5;
    sigma = 2;
    
    // Compute the CDF for the lognormal distribution
    // parameterized by mu = 1.5 and sigma = 2
    p = cdfLogNorm(x, mu, sigma);

After the above, code *p* will equal:

::

    0.028631852 
    0.30327714 
    0.34331728

.. seealso:: Functions :func:`cdfn_cdfNc`, :func:`pdfTruncNorm`, :func:`cdfTruncNorm`, :func:`pdfLogNorm`

