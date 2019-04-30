
pdfn
==============================================

Purpose
----------------
Computes the standard Normal (scalar) probability density function.

Format
----------------
.. function:: pdfn(x[, mu[, sigma]])

    :param x: data
    :type x: NxK matrix or N-dimensional array.

    :param mu: Optional input, mean parameter.
    :type mu: scalar

    :param sigma: Optional input, standard deviation parameter.
    :type sigma: scalar

    :returns: y (*NxK matrix or N-dimensional array*), containing the standard Normal probability density function of *x*.

Remarks
-------

This does not compute the joint Normal density function. Instead, the
scalar Normal density function is computed element-by-element. *y* could
be computed by the following GAUSS code:

::

   y =(1/sqrt(2*pi))*exp(-(x.*x)/2);


Examples
----------------

Example 1
+++++++++

::

    x = { -3, -2, 0, 2, 3 };
    y = pdfn(x);

After the code above:

::

        0.0044318484 
         0.053990967 
    y  =  0.39894228 
         0.053990967 
         0.004431848

Example 2
+++++++++

    x = 1.5;
    mu = 3;
    sigma = 2; 
    p = pdfn(x, mu, sigma);

After the code above, *p* should equal:

::

    0.15056872

.. seealso:: Functions :func:`pdfTruncNorm`

