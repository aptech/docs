
cdfMvtce
==============================================

Purpose
----------------
Computes complement (upper tail) of multivariate Student's t cumulative distribution function with error management.

Format
----------------
.. function:: cdfMvtce(ctl, x, corr, nonc, df)

    :param ctl: instance of a :class:`cdfmControl` structure with members

        .. csv-table::
            :widths: auto

            "ctl.maxEvaluations", "scalar, maximum number of evaluations."
            "ctl.absErrorTolerance", "scalar, absolute error tolerance."
            "ctl.relErrorTolerance", "scalar, tolerance."

    :type ctl: struct

    :param x: Lower limits at which to evaluate the complement of the multivariate Student's t cumulative distribution function. If *x* has more than one column, each column will be treated as a separate set of upper limits. K is the dimension of the multivariate Student's t distribution. N is the number of MVT cdf integrals.
    :type x: NxK matrix

    :param corr: correlation matrix.
    :type corr: KxK matrix

    :param nonc: noncentralities.
    :type nonc: Kx1 vector

    :param df: degrees of freedom.
    :type df: scalar

    :returns: **p** (*N x 1 vector*) - Each element in *p* is the complement of the cumulative distribution function of the multivariate Student's t distribution for the corresponding elements in *x*.

    :returns: **err** (*Nx1 vector*) - estimates of absolute error.

    :returns: **retcode** (*Nx1 vector*) - return codes.

        .. csv-table::
            :widths: auto

            "0", "normal completion with :math:`err < ctl.absErrorTolerance`."
            "1", ":math:`err > ctl.absErrorTolerance` and ctl.maxEvaluations exceeded; increase ctl.maxEvaluations to decrease error."
            "2", ":math:`K > 100` or :math:`K < 1`."
            "3", "*R* not positive semi-definite."
            "missing", "*R* not properly defined."

Remarks
------------

-  The central multivariate Student's t upper tail cdf for the i-th row of x is defined by

.. math:: T(x_i; \Sigma, \nu) = \frac{\Gamma(\frac{\nu+K}{2})}{\Gamma(\frac{\nu}{2})\sqrt{|\Sigma|(\nu\pi)^K}}\int_{x_{i1}}^{\infty}\int_{x_{i2}}^{\infty}\ldots\int_{x_{iK}}^{\infty} \Big( 1 + \frac{z'\Sigma^{-1}z}{\nu} \Big)^{-\frac{\nu+K}{2}} dz\\
\equiv \frac{2^{1 -  \frac{\nu}{2}}}{\Gamma(\frac{\nu}{2})}\int_0^{\infty}s^{\nu-1}e^{-\frac{s^2}{2}}\Phi\Big(\frac{sx_i}{\sqrt{\nu}},\infty; \Sigma \Big) ds

   where :math:`\nu \in \mathbb{R^+}` is a scale (or degree of freedom) parameter, :math:`z` is
   a K-dimensional Student's t multivariate distribution, and

.. math:: \phi(x_i; \Sigma) = \frac{1}{\sqrt{|\Sigma|(2\pi)^K}}\int_{x_{i1}}^{\infty}\int_{x_{i2}}^{\infty}\ldots\int_{x_{iK}}^{\infty} e^{-\frac{1}{2}z'\Sigma^{-1}z} dz

   For the non-central multivariate Student's t distribution cdf, we have

.. math:: T(x_i, \Sigma, \nu, \delta) = \frac{\Gamma(\frac{\nu+K}{2})}{\Gamma(\frac{\nu}{2})\sqrt{|\Sigma|(\nu\pi)^K}}\int_{x_{i1}}^{\infty}\int_{x_{i2}}^{\infty}\ldots\int_{x_{iK}}^{\infty} \Big( 1  \frac{(z-\delta)'\Sigma^{-1}(z-\delta)}{\nu} \Big)^{-\frac{\nu+K}{2}} dz

   where :math:`\delta` denotes the :math:`K \times 1` non-centrality vector with :math:`-\infty< \delta_k < \infty`. Another form of non-central multivariate Student's t distribution cdf is

.. math:: T(x_i, \Sigma, \nu, \delta) = \frac{2^{1 - \frac{\nu}{2}}}{\Gamma(\frac{\nu}{2})}\int_0^{\infty}s^{\nu-1}e^{-\frac{s^2}{2}}\Phi\Big(\frac{sx_i}{\sqrt{\nu}}-\delta; \Sigma \Big) ds

-  The correlation matrix :math:`R` is defined by covariance matrix :math:`\Sigma`, :math:`\Sigma = DRD`, where :math:`D` denotes the diagonal matrix which has the square roots of the
   diagonal entries for :math:`\Sigma` on its diagonal.

Examples
----------------

Uncorrelated variables
++++++++++++++++++++++

::

    // Lower limits of integration for K dimensional multivariate Student's t distribution
    x = { 0  0 };

    /*
    ** Identity matrix, indicates
    ** zero correlation between variables
    */
    corr = { 1 0,
          0 1 };

    // Define non-centrality vector
    nonc  = {0, 0};

    // Define degree of freedom
    df  = 3;

    // Define control structure
    struct cdfmControl ctl;
    ctl = cdfmControlCreate();

    /*
    ** Calculate cumulative probability of
    ** both variables being ≥ 0
    */
    { p, err, retcode } = cdfMvtce(ctl, x, corr, nonc, df);

    /*
    ** Calculate joint probablity of two
    ** variables with zero correlation,
    ** both, being ≥ 0
    */
    p2 =  cdftc(0, v) .* cdftc(0, v);

After the above code, both p and p2 should be equal to 0.25.

.. math::
    T = P(0 \leq  X_1 < \infty   \text{ and } 0 \leq X_2 < \infty) \approx 0.25.

Compute the upper tail of multivariate student's t cdf at 3 separate pairs of lower limits
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    /* Lower limits of integration
    ** x1 ≥ -1 and x2 ≥ -1.1
    ** x1 ≥ 0 and x2 ≥ 0.1
    ** x1 ≥ 1 and x2 ≥ 1.1
    */
    x = {  -1   -1.1,
            0    0.1,
            1    1.1 };

    // Correlation matrix
    corr = { 1  0.31,
          0.31  1};

    // Define non-centrality vector
    nonc  = { 0, 0 };

    // Define degree of freedom
    df  = 3;

    // Define control structure
    struct cdfmControl ctl;
    ctl = cdfmControlCreate();

    /*
    ** Calculate cumulative probability of
    ** each pair of lower limits
    */
    { p, err, retcode }  = cdfMvtce(ctl, x, corr, nonc, df);

After the above code, p should equal:

::

    0.69617932
    0.28156926
    0.06752203

which means that:

.. math::
    P(x_1 \geq -1 \text{ and } x_2 \geq -1.1) = 0.6962\\
    P(x_1 \geq +0 \text{ and } x_2 \geq +0.1) = 0.2816\\
    P(x_1 \geq 1 \text{ and } x_2 \geq 1.1) = 0.0675

Compute the upper tail of non central multivariate student's t cdf
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

  /* Lower limits of integration
  ** x1 ≥ -1 and x2 ≥ -1.1
  ** x1 ≥ 0 and x2 ≥ 0.1
  ** x1 ≥ 1 and x2 ≥ 1.1
  */
    x = { -1   -1.1,
           0    0.1,
           1    1.1 };

    // Correlation matrix
    corr = {    1  0.31,
          0.31     1 };

    // Define non-centrality vector, Kx1
    nonc  = {  1,
         -2.5 };

    // Define degree of freedom
    df  = 3;

    // Define control structure
    struct cdfmControl ctl;
    ctl = cdfmControlCreate();

    /*
    ** Calculate cumulative probability of
    ** each pair of lower limits
    */
    { p, err, retcode }  = cdfMvtce(ctl, x, corr, nonc, df);

After the above code, *p* should equal:

::

    0.08623943
    0.00468427
    0.00049538

which means with non-central vector, the multivariate student's t cdf are:

.. math::
    P(x_1 \geq -1 \text{ and } x_2 \geq -1.1) = 0.0862\\
    P(x_1 \geq +0 \text{ and } x_2 \geq +0.1) = 0.0047\\
    P(x_1 \geq 1 \text{ and } x_2 \geq 1.1) = 0.0005


References
------------

#. Genz, A. and F. Bretz,''Numerical computation of multivariate
   t-probabilities with application to power calculation of multiple
   contrasts,'' Journal of Statistical Computation and Simulation,
   63:361-378, 1999.
#. Genz, A., ''Numerical computation of multivariate normal
   probabilities,'' Journal of Computational and Graphical Statistics,
   1:141-149, 1992.

.. seealso:: Functions :func:`cdfMvt2e`, :func:`cdfMvte`, :func:`cdfMvne`
