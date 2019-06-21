
cdfMvnce
==============================================

Purpose
----------------
Computes the upper tail of the multivariate Normal cumulative distribution function with error management.

Format
----------------
.. function:: cdfMvnce(ctl, x, corr, nonc)

    :param ctl: instance of a :class:`cdfmControl` structure with members

        .. csv-table::
            :widths: auto

            "ctl.maxEvaluations", "scalar, maximum number of evaluations."
            "ctl.absErrorTolerance", "scalar, absolute error tolerance."
            "ctl.relative", "scalar, error tolerance."

    :type ctl: struct

    :param x: Lower limits at which to evaluate the complement of the multivariate normal cumulative distribution function. If *x* has more than one column, each column will be treated as a separate set of upper limits.
    :type x: NxK matrix

    :param corr: correlation matrix.
    :type corr: KxK matrix

    :param nonc: non-centrality vector.
    :type nonc: Kx1 vector

    :returns: **p** (*Nx1 vector*) - :math:`Pr(X ≥ x|corr, nonc)`. The probability in the upper tail of the multivariate normal cumulative distribution function for each corresponding set of limits in *x*.

    :returns: **err** (*Nx1 vector*) - estimates of absolute error.

    :returns: **retcode** (*Nx1 vector*) - return codes.

        .. csv-table::
            :widths: auto

            "0", "normal completion with :math:`err < ctl.absErrorTolerance`."
            "1", ":math:`err > ctl.absErrorTolerance` and ctl.maxEvaluations exceeded; increase *ctl.maxEvaluations* to decrease error."
            "2", ":math:`K > 100` or :math:`K < 1`"
            "3", "*R* not positive semi-definite."
            "missing", "*R* not properly defined."

Remarks
------------

-  The :func:`cdfMvnce` evaluates the upper tail of *MVN* integral, where :math:`1\leqslant i \leqslant N` For the non-central *MVN*, we have where :math:`z` denotes :math:`K` -dimensional multivariate normal distribution, :math:`\delta` denotes the :math:`K \times 1` non-centrality vector with :math:`-\infty<\:\ \delta_k <\:\ \infty`.

-  The correlation matrix :math:`R` is defined by :math:`\Sigma = DRD`, where :math:`D` denotes the diagonal matrix which has the square roots of the diagonal entries for covariance matrix :math:`\Sigma` on its diagonal.

Examples
----------------

Uncorrelated variables
++++++++++++++++++++++

::

    // Lower limits of integration for K dimensional multivariate distribution
    x = { 0  0 };

    /*
    ** Identity matrix, indicates
    ** zero correlation between variables
    */
    corr = { 1 0,
          0 1 };

    // Define non-centrality vector
    nonc  = { 0, 0};

    // Define control structure
    struct cdfmControl ctl;
    ctl = cdfmControlCreate();

    /*
    ** Calculate cumulative probability of
    ** both variables being ≥ 0
    */
    { p, err, retcode } = cdfMvnce(ctl, x, corr, nonc);

    /*
    ** Calculate joint probability of two
    ** variables with zero correlation,
    ** both, being ≥ 0
    */
    p2 = cdfnc(0) .* cdfnc(0);

After the above code, both *p* and *p2* should be equal to 0.25.

.. math::
    \Phi = P(0 \leq  X_1 < \infty \text{ and } 0 \leq X_2 < \infty) \approx 0.25.

Compute the upper tail of multivariate normal cdf at 3 separate pairs of lower limits
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    /*
    ** Lower limits of integration
    ** x1 ≥ -1 and  x2 ≥ -1.1
    ** x1 ≥ 0 and x2 ≥ 0.1
    ** x1 ≥ 1 and x2 ≥ 1.1
    */
    x = {  -1   -1.1,
            0    0.1,
            1    1.1 };

    // Correlation matrix
    corr = {   1  0.31,
         0.31     1 };

    // Define non-centrality vector
    nonc  = { 0, 0 };

    // Define control structure
    struct cdfmControl ctl;
    ctl = cdfmControlCreate();

    /*
    ** Calculate cumulative probability of
    ** each pair of lower limits
    */
    { p, err, retcode }  = cdfMvnce(ctl, x, corr, nonc);

After the above code, *p* should equal:

::

    0.74642007
    0.27999181
    0.04074138

which means that:

.. math::
    P(x_1 \geq -1 \text{ and } x_2 \geq -1.1) = 0.7464\\
    P(x_1 \geq +0 \text{ and } x_2 \geq +0.1) = 0.2800\\
    P(x_1 \geq 1 \text{ and } x_2 \geq 1.1) = 0.0407

Compute the upper tail of noncentral multivariate normal cdf
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    /* Lower limits of integration
    ** x1 ≥ -1 and x2 ≥ -1.1
    ** x1 ≥ 0 and  x2 ≥ 0.1
    ** x1 ≥ 1 and x2 ≥ 1.1
    */
    x = { -1   -1.1,
           0    0.1,
           1    1.1 };

    // Correlation matrix
    corr = {    1  0.31,
          0.31     1 };

    // Define non-centrality vector, Kx1
    nonc  = {   1,
          -2.5 };

    // Define control structure
    struct cdfmControl ctl;
    ctl = cdfmControlCreate();

    /*
    ** Calculate cumulative probability of
    ** each pair of lower limits
    */
    { p, err, retcode } = cdfMvnce(ctl, x, corr, nonc);

After the above code, p should equal:

::

    0.08046686
    0.00455354
    0.00014231

which means with non-central vector, the multivariate normal cdf are:

.. math::
    P(x_1 \geq -1 \text{ and } x_2 \geq -1.1) = 0.0805\\
    P(x_1 \geq +0 \text{ and } x_2 \geq +0.1) = 0.0046\\
    P(x_1 \geq 1 \text{ and } x_2 \geq 1.1) = 0.0001

References
------------

#. Genz, A. and F. Bretz,''Numerical computation of multivariate
   t-probabilities with application to power calculation of multiple
   contrasts'', Journal of Statistical Computation and Simulation,
   63:361-378, 1999.

#. Genz, A., ''Numerical computation of multivariate normal
   probabilities'', Journal of Computational and Graphical Statistics,
   1:141-149, 1992.

.. seealso:: Functions :func:`cdfMvn2e`, :func:`cdfMvnce`, :func:`cdfMvte`
