
cdfMvn
==============================================

Purpose
----------------
Computes multivariate Normal cumulative distribution function.

Format
----------------
.. function:: cdfMvn(x, corr)

    :param x: Values at which to evaluate the multivariate normal cumulative distribution function. If *x* has more than one column, each column will be treated as a separate set of upper limits.
    :type x: Kx1 vector or KxN matrix

    :param corr: correlation matrix.
    :type corr: KxK matrix

    :returns: **p** (*Nx1 vector*) - Each element in *p* is the cumulative distribution function of the multivariate Normal distribution for each corresponding columns in *x*. *p* will have as many elements as the input, *x*, has columns.

Remarks
------------

- :func:`cdfMvn` evaluates the *MVN* integral with i-th row of :math:`x` (upper limits),
  where :math:`1\leqslant i \leqslant N`
- The correlation matrix :math:`R` is defined by :math:`\Sigma = DRD`, where :math:`D`
  denotes the diagonal matrix which has the square roots of the diagonal entries for covariance
  matrix :math:`\Sigma` on its diagonal.
- :func:`cdfMvne` is more accurate and faster. Note that :func:`cdfMvne` takes a row vector of upper limits whereas :func:`cdfMvn` takes a column vector of limits.

Examples
----------------

Uncorrelated variables
++++++++++++++++++++++

::

    // Upper limits of integration
    x = { 0, 0 };

    /*
    ** Identity matrix, indicates
    ** zero correlation between variables
    */
    corr = { 1 0,
             0 1 };

    /*
    ** Calculate cumulative probability of
    ** both variables being ≤ 0
    */
    p = cdfmvn(x, corr);

    /*
    ** Calculate joint probablity of two
    ** variables with zero correlation,
    ** both, being ≤ 0
    */
    p2 = cdfn(0) .* cdfn(0);

After the above code, both *p* and *p2* should be equal to 0.25.

Example 2
++++++++++++++

::

    // Upper limits of integration
    x = { -0.5, 1 };

    // Correlation matrix
    corr = {   1  0.26,
            0.26     1 };

    /*
    ** Calculate cumulative probability of
    ** the first variable being ≤ -0.5
    ** and the second variable being ≤ 1
    */
    p = cdfmvn(x, corr);

After the above code, *p* should equal: 0.28025. It means :

.. math::
    \Phi = P(-\infty < X_1 \leq -0.5, - \infty < X_2 \leq 1) \approx 0.28025

when the correlation between two variables is 0.26.

Compute the cdf at 3 separate pairs of points
+++++++++++++++++++++++++++++++++++++++++++++

::

    /*
    ** Upper limits of integration
    ** x1 ≤ -1 and x2 ≤ -1.1
    ** x1 ≤  0 and x2 ≤  0.1
    ** x1 ≤  1 and x2 ≤  1.1
    */
    x = {  -1   0    1,
         -1.1 0.1  1.1 };

    // Correlation matrix
    corr = {   1 0.31,
            0.31    1 };

    /*
    ** Calculate cumulative probability of
    ** each pair of upper limits
    */
    p = cdfmvn(x, corr);

After the above code, p should equal:

::

    0.040741382   0.31981965   0.74642007

which means that:

.. math::
    P(x_1 \leq -1 \text{ and } x_2 \leq -1.1) = 0.0407\\
    P(x_1 \leq +0 \text{ and } x_2 \leq +0.1) = 0.3198\\
    P(x_1 \leq 1 \text{ and } x_2 \leq 1.1) = 0.7464

.. seealso:: Functions :func:`cdfBvn`, :func:`cdfN`, :func:`lncdfmvn`
