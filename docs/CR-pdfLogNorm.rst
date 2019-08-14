
pdfLogNorm
==============================================

Purpose
----------------
Computes the probability density function of the log-normal distribution.
  

Format
----------------
.. function:: p = pdfLogNorm(x[, mu[, sigma]])

    :param x: data
    :type x: matrix or array

    :param mu: Optional input, the mean parameter. Default = 0.
    :type mu: scalar

    :param sigma: Optional input, the standard deviation parameter. Default = 1.
    :type sigma: scalar

    :returns: p (*matrix or array*) of the same dimension as the input *x*, containing the probabilities.

Examples
----------------

Basic Example
+++++++++++++

::

    // Use default 'mu' and 'sigma'
    p = pdfLogNorm(3.1);

After the above, code *p* will equal:

::

    0.067855420

Specify 'mu' and 'sigma'
++++++++++++++++++++++++

::

    // Create vector of 'x' values
    x = { 0.1, 1.6, 2 };
    
    mu = 1.5;
    sigma = 2;
    
    // Compute the PDF for the lognormal distribution
    // parameterized by mu = 1.5 and sigma = 2
    p = pdfLogNorm(x, mu, sigma);

After the above, code *p* will equal:

::

     0.32727408 
     0.10918617 
    0.091940897

.. seealso:: Functions :func:`cdfn_cdfNc`, :func:`pdfTruncNorm`, :func:`cdfTruncNorm`, :func:`cdfLogNorm`

