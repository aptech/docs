
cdfMvtce
==============================================

Purpose
----------------
Computes complement (upper tail) of multivariate Student's t cumulative distribution function with error management.

Format
----------------
.. function:: { y, err, retcode } = cdfMvtce(ctl, x, corr, nonc, df)

    :param ctl: instance of a :class:`cdfmControl` structure with members

        .. csv-table::
            :widths: auto

            "ctl.maxEvaluations", "scalar, maximum number of evaluations."
            "ctl.absErrorTolerance", "scalar, absolute error tolerance."
            "ctl.relErrorTolerance", "scalar, relative error tolerance."

    :type ctl: struct

    :param x: Lower limits at which to evaluate the complement of the multivariate Student's t cumulative distribution function. If *x* has more than one row, each row will be treated as a separate set of upper limits. K is the dimension of the multivariate Student's t distribution. N is the number of MVT cdf integrals.
    :type x: NxK matrix

    :param corr: correlation matrix.
    :type corr: KxK matrix

    :param nonc: noncentralities.
    :type nonc: Kx1 vector

    :param df: degrees of freedom.
    :type df: scalar

    :returns: **p** (*Nx1 vector*) - Each element in *p* is the complement of the cumulative distribution function of the multivariate Student's t distribution for the corresponding elements in *x*.

    :returns: **err** (*Nx1 vector*) - estimates of absolute error.

    :returns: **retcode** (*Nx1 vector*) - return codes.

        .. csv-table::
            :widths: auto

            "0", "normal completion with :math:`err < ctl.absErrorTolerance`."
            "1", ":math:`err > ctl.absErrorTolerance` and ctl.maxEvaluations exceeded; increase ctl.maxEvaluations to decrease error."
            "2", ":math:`K > 100` or :math:`K < 1`."
            "3", "*R* not positive semi-definite."
            "missing", "*R* not properly defined."

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
    p2 =  cdftc(0, df) .* cdftc(0, df);

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
    corr = {  1 0.31,
           0.31    1};

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
    corr = {   1  0.31,
            0.31     1 };

    // Define non-centrality vector, Kx1
    nonc  = {  1, -2.5 };

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
