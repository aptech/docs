
pdfn
==============================================

Purpose
----------------
Computes the standard Normal (scalar) probability density function.

Format
----------------
.. function:: pdfn(x, mu, sigma)

    :param x: or N-dimensional array.
    :type x: NxK matrix

    :param mu: scalar, mean parameter.
    :type mu: Optional input

    :param sigma: scalar, standard deviation parameter.
    :type sigma: Optional input

    :returns: y (*NxK matrix*), or N-dimensional array, containing the standard Normal
        probability density function of x.

Examples
----------------

x = { -3, -2, 0, 2, 3 };
y = pdfn(x);
+++++++++++++++++++++++++++++++++++++

After the code above:

::

    0.0044318484 
         0.053990967 
    y  =  0.39894228 
         0.053990967 
        0.0044318484

x = 1.5;
mu = 3;
sigma = 2; 
p = pdfn(x, mu, sigma);
++++++++++++++++++++++++++++++++++++++++++++++++++++

After the code above, p should equal:

::

    0.15056872

.. seealso:: Functions :func:`pdfTruncNorm`
