
trigamma
==============================================

Purpose
----------------

Computes the trigamma function, which is the second derivative of the log of the gamma function. Commonly used in Newton-Raphson iterations for maximum likelihood estimation of gamma and Dirichlet distribution parameters.

Format
----------------
.. function:: y = trigamma(x)

    :param x: values at which to evaluate the trigamma function. All elements must be positive.
    :type x: MxN matrix or N-dimensional array

    :return y: the trigamma function evaluated element-wise at each value of *x*.

    :rtype y: MxN matrix or N-dimensional array

Remarks
-------

The :func:`trigamma` function is the second derivative of the log of the gamma function with respect to its argument:

.. math::

   \psi_1(x) = \frac{d^2}{dx^2} \ln \Gamma(x)

It is the derivative of the :func:`digamma` function. The trigamma function is defined for positive real numbers and approaches zero as *x* increases.

Examples
----------------

Example 1: Basic evaluation
++++++++++++++++++++++++++++

::

    // Evaluate trigamma at several points
    x = { 0.5, 1, 2, 5, 10 };
    y = trigamma(x);
    print (x~y);

produces:

::

      0.50000000        4.9348022
       1.0000000        1.6449341
       2.0000000       0.64493407
       5.0000000       0.22132296
       10.000000       0.10516634

Note that ``trigamma(1)`` equals :math:`\pi^2/6 \approx 1.6449`, and the values decrease toward zero for larger *x*.

Example 2: Use in Fisher information
++++++++++++++++++++++++++++++++++++++

::

    // For a Gamma(alpha, beta) distribution, the Fisher information
    // for alpha involves the trigamma function:
    // I(alpha) = trigamma(alpha)

    alpha = 3;
    fisher_info = trigamma(alpha);
    print "Fisher information for alpha = " alpha;
    print "I(alpha) = " fisher_info;

produces:

::

    Fisher information for alpha =        3.0000000
    I(alpha) =       0.39493407

.. seealso:: Functions :func:`digamma`, :func:`gamma`, :func:`lnfact`
