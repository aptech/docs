
cdfMvn2e
==============================================

Purpose
----------------
Computes the multivariate normal cumulative distribution function with error management over the range :math:`[a,b]`.

Format
----------------
.. function:: { y, err, retcode } = cdfMvn2e(ctl, l_lim, u_lim, corr, nonc)

    :param ctl: instance of a :class:`cdfmControl` structure with members

        .. csv-table::
            :widths: auto

            "ctl.maxEvaluations", "scalar, maximum number of evaluations."
            "ctl.absErrorTolerance", "scalar, absolute error tolerance."
            "ctl.relErrorTolerance", "scalar, error tolerance."

    :type ctl: struct

    :param l_lim: lower limits.
    :type l_lim: NxK matrix

    :param u_lim: upper limits.
    :type u_lim: NxK matrix

    :param corr: correlation matrix.
    :type corr: KxK matrix

    :param nonc: non-centrality vector.
    :type nonc: Kx1 vector

    :return p: Each element in *p* is the cumulative distribution function of the multivariate normal distribution for each corresponding columns in *x*. *p* will have as many elements as the inputs, *u_lim* and *l_lim*, have rows. :math:`Pr(X ≥ l\_lim \text{ and } X ≤ u\_lim|corr, nonc)`.

    :rtype p: Nx1 vector

    :return err: estimates of absolute error.

    :rtype err: Nx1 vector

    :return retcode: return codes.

        .. csv-table::
            :widths: auto

            "0", "normal completion with :math:`err < ctl.absErrorTolerance`."
            "1", ":math:`err > ctl.absErrorTolerance` and *ctl.maxEvaluations* exceeded; increase *ctl.maxEvaluations* to decrease error."
            "2", ":math:`K > 100` or :math:`K < 1`."
            "3", "*corr* not positive semi-definite."
            "missing", "*corr* not properly defined."

    :rtype retcode: Nx1 vector

Examples
----------------

Uncorrelated variables
++++++++++++++++++++++

::

    // Lower limits of integration for K dimensional multivariate distribution
    a = {-1e4 -1e4};

    // Upper limits of integration for K dimensional multivariate distribution
    b = {0 0};

    /*
    ** Identity matrix, indicates
    ** zero correlation between variables
    */
    corr = { 1 0,
             0 1 };

    // Define non-centrality vector
    nonc  = {0, 0};

    // Define control structure
    struct cdfmControl ctl;
    ctl = cdfmControlCreate();

    /*
    ** Calculate cumulative probability of
    ** both variables being from -1e4 to  0
    */
    { p, err, retcode } = cdfMvn2e(ctl, a, b, corr, nonc);

After the above code, both *p* equal to 0.25.

.. math::
    \Phi = P(-10000 \leq  X_1 \leq 0 \text{ and } -10000 \leq X_2 \leq 0) \approx 0.25.

Compute the multivariate normal cdf at 3 separate pairs of upper limits
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    /*
    ** Limits of integration
    ** -5 ≤ x1 ≤ -1 and -8 ≤ x2 ≤ -1.1
    ** -10 ≤ x1 ≤ 0 and -10 ≤ x2 ≤ 0.1
    ** 0 ≤ x1 ≤ 1 and 0 ≤ x2 ≤ 1.1
    */
    a = {  -5  -8,
          -20 -10,
            0   0 };

    b = {  -1 -1.1,
            0  0.1,
            1  1.1 };

    // Correlation matrix
    corr = {   1 0.31,
            0.31    1};

    // Define non-centrality vector
    nonc  = {0, 0};

    // Define control structure
    struct cdfmControl ctl;
    ctl = cdfmControlCreate();

    /*
    ** Calculate cumulative probability of
    ** each pair of limits
    */
    { p, err, retcode }  = cdfMvn2e(ctl, a, b, corr, nonc);

After the above code, *p* should equal:

::

    0.04074118
    0.31981965
    0.13700266

which means that:

.. math::
    P(-5 \leq x_1 \leq -1   \text{ and } -8 \leq  x_2 \leq -1.1) = 0.0407\\
    P(-20 \leq x_1 \leq 0 \text{ and } -10 \leq x_2 \leq 0.1) = 0.3198\\
    P(0 \leq x_1 \leq 1 \text{ and } 0 \leq x_2 \leq 1.1) = 0.1370

Compute the non central multivariate normal cdf
+++++++++++++++++++++++++++++++++++++++++++++++

::

    /*
    ** Limits of integration
    ** -5 ≤ x1 ≤ -1 and -8 ≤ x2 ≤ -1.1
    ** -10 ≤ x1 ≤ 0 and -10 ≤ x2 ≤ 0.1
    ** 0 ≤ x1 ≤ 1 and 0 ≤ x2 ≤ 1.1
    */
    a = { -5  -8,
         -20 -10,
           0   0 };

    b = {  -1 -1.1,
            0  0.1,
            1  1.1 };

    // Correlation matrix
    corr = {   1  0.31,
            0.31     1 };

    // Define non-centrality vector, Kx1
    nonc  = {   1,
             -2.5 };

    // Define control structure
    struct cdfmControl ctl;
    ctl = cdfmControlCreate();

    /*
    ** Calculate cumulative probability of
    ** each pair of upper limits
    */
    { p, err, retcode } = cdfMvn2e(ctl, a, b, corr, nonc);

After the above code, *p* should equal:

::

    0.02246034
    0.15854761
    0.00094761

which means with non-central vector, the multivariate normal cdf are:

.. math::
    P(-5 \leq x_1 \leq -1 \text{ and } -8 \leq x_2 \leq -1.1) = 0.0225\\
    P(-20 \leq x_1 \leq 0 \text{ and } -10 \leq x_2 \leq 0.1) = 0.1585\\
    P(0 \leq x_1 \leq 1 \text{ and } 0 \leq x_2 \leq 1.1) = 0.0009

Remarks
------------

- :func:`cdfMvn2e` evaluates the following non-central *MVN* integral, where :math:`1\leqslant i \leqslant N` where :math:`z` denotes :math:`K` -dimensional multivariate normal distribution, :math:`\delta` denotes the :math:`K \times 1` non-centrality vector with :math:`-\infty<\:\ \delta_k <\:\ \infty` .

- The correlation matrix :math:`R` is defined by :math:`\Sigma = DRD`, where :math:`D` denotes the diagonal matrix which has the square roots of the diagonal entries for covariance matrix :math:`\Sigma` on its diagonal.

References
------------

#. Genz, A. and F. Bretz,''Numerical computation of multivariate
   t-probabilities with application to power calculation of multiple
   contrasts,'' Journal of Statistical Computation and Simulation,
   63:361-378, 1999.

#. Genz, A., ''Numerical computation of multivariate normal
   probabilities,'' Journal of Computational and Graphical Statistics,
   1:141-149, 1992.

.. seealso:: Functions :func:`cdfMvne`, :func:`cdfMvnce`, :func:`cdfMvt2e`
