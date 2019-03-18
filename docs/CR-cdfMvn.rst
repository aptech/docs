
cdfMvn
==============================================

Purpose
----------------
Computes multivariate Normal cumulative distribution function.

Format
----------------
.. function:: cdfMvn(ulim, corr)

    :param ulim: abscissae. If ulim has more than one column, each column will be treated as a separate set of upper limits.
    :type ulim: K x 1 vector or K x N matrix

    :param corr: correlation matrix.
    :type corr: K x K matrix

    :returns: p (*N x 1 vector*), :math:`P(X \leq ulim|corr)`. p will have as many elements as the input, ulim, has columns.

Examples
----------------

Uncorrelated variables
++++++++++++++++++++++

::

    //Upper limits of integration
    ulim = { 0, 0 };
    
    //Identity matrix, indicates
    //zero correlation between variables
    corr = { 1 0,
             0 1 };
    
    //Calculate cumulative probability of
    //both variables being ≤ 0
    p = cdfmvn(ulim, corr);
    
    //Calculate joint probablity of two
    //variables with zero correlation,
    //both, being ≤ 0
    p2 = cdfn(0) .* cdfn(0);

After the above code, both p and p2 should be equal to 0.25.

//Upper limits of integration
ulim = { -0.5, 1 };

//Correlation matrix
corr = {   1  0.26,
        0.26     1 };

//Calculate cumulative probability of
//the first variable being ≤ -0.5
//and the second variable being ≤ 1
p = cdfmvn(ulim, corr);
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

After the above code, p should equal: 0.28025. It means :

.. math::
    \Phi = P(-\infty < X_1 \leq -0.5, - \infty < X_2 \leq 1) \approx 0.28025 when the correlation between two variables is 0.26.

Compute the cdf at 3 separate pairs of points
+++++++++++++++++++++++++++++++++++++++++++++

::

    //Upper limits of integration
    //x1 ≤ -1 and x2 ≤ -1.1
    //x1 ≤  0 and x2 ≤ 0.1
    //x1 ≤ 1 and x2 ≤ 1.1
    ulim = {  -1   0    1,
            -1.1 0.1  1.1 };
    
    //Correlation matrix
    corr = {   1 0.31,
            0.31    1 };
    
    //Calculate cumulative probability of
    //each pair of upper limits
    p = cdfmvn(ulim, corr);

After the above code, p should equal:

::

    0.040741382   0.31981965   0.74642007

which means that:

.. math::
    P(x_1 \leq -1 \text{ and } x_2 \leq -1.1) = 0.0407\\
    P(x_1 \leq +0 \text{ and } x_2 \leq +0.1) = 0.3198\\
    P(x_1 \leq 1 \text{ and } x_2 \leq 1.1) = 0.7464

Remarks
+++++++

-  cdfMvn evaluates the *MVN* integral with i-th row of :math:`x` (upper limits), where :math:`1\leqslant i \\leqslant N` -  The correlation matrix :math:`R` is defined by :math:`\Sigma = DRD`, where :math:`D` denotes the diagonal matrix which has the square roots of the
   diagonal entries for covariance matrix :math:`\Sigma` on its diagonal.

Source
++++++

lncdfn.src

.. seealso:: Functions :func:`cdfBvn`, :func:`cdfN`, :func:`lncdfmvn`

multivariate normal cdf cumulative distribution function mvn
