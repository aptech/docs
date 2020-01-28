
cdfMvt2e
==============================================

Purpose
----------------
Computes multivariate Student's t cumulative distribution function with error management over :math:`[a, b]`.

Format
----------------
.. function:: { y, err, retcode } = cdfMvt2e(ctl, l_lim, u_lim, corr, nonc, df )

    :param ctl: instance of a :class:`cdfmControl` structure with members

        .. csv-table::
            :widths: auto

            "ctl.maxEvaluations", "scalar, maximum number of evaluations."
            "ctl.absErrorTolerance", "scalar, absolute error tolerance."
            "ctl.relErrorTolerance", "scalar, relative error tolerance."

    :type ctl: struct

    :param l_lim: lower limits. *K* is the dimension of multivariate Student's t distribution. *N* is the number of MVT cdf integrals.
    :type l_lim: NxK matrix

    :param u_lim: upper limits.
    :type u_lim: NxK matrix

    :param corr: correlation matrix.
    :type corr: KxK matrix

    :param nonc: noncentralities.
    :type nonc: Kx1 vector

    :param df: degrees of freedom.
    :type df: scalar

    :return p: Each element in *p* is the cumulative distribution function of the multivariate Student's t distribution for the corresponding columns in *l_lim* and *u_lim*. *p* will have as many elements as the input, *l_lim* and *u_lim*, have rows.

    :rtype p: Nx1 vector

    :return err: estimates of absolute error.

    :rtype err: Nx1 vector

    :return retcode: return codes.

        .. csv-table::
            :widths: auto

            "0", "normal completion with :math:`err < ctl.absErrorTolerance`."
            "1", ":math:`err  >  ctl.absErrorTolerance` and ctl.maxEvaluations exceeded; increase ctl.maxEvaluations to decrease error."
            "2", ":math:`K > 100` or :math:`K < 1`."
            "3", "*R* not positive semi-definite."
            "missing", "*R* not properly defined."

    :rtype retcode: Nx1 vector

Examples
----------------

Uncorrelated variables
++++++++++++++++++++++

::

    // Lower limits of integration for K dimensional multivariate distribution
    l_lim = { -1e4 -1e4 };

    // Upper limits of integration for K dimensional multivariate distribution
    u_lim = { 0 0 };

    /*
    ** Identity matrix, indicates
    ** zero correlation between variables
    */
    corr = { 1 0,
             0 1 };

    // Define non-centrality vector
    nonc  = { 0, 0 };

    // Define degree of freedom
    df  = 3;

    // Define control structure
    struct cdfmControl ctl;
    ctl = cdfmControlCreate();

    /*
    ** Calculate cumulative probability of
    ** both variables being from -1e4 to 0
    */
    { p, err, retcode } = cdfMvt2e(ctl, l_lim, u_lim, corr, nonc, df );

After the above code, both *p* equal to 0.25.

.. math::
    T = P(-\infty <  X_1 \leq 0 \text{ and } - \infty < X_2 \leq 0) \approx 0.25.

Compute the multivariate student's t cdf at 3 separate pairs of upper limits
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    /*
    ** Limits of integration
    ** -5 ≤ x1 ≤ -1 and -8 ≤ x2 ≤ -1.1
    ** -20 ≤ x1 ≤ 0 and -10 ≤ x2 ≤ 0.1
    **  0 ≤ x1 ≤ 1 and 0 ≤ x2 ≤ 1.1
    */
    l_lim = { -5  -8,
             -20 -10,
               0   0 };

    u_lim = { -1 -1.1,
               0  0.1,
               1  1.1 };

    // Correlation matrix
    corr = {   1 0.31,
            0.31   1 };

    // Define non-centrality vector
    nonc  = { 0, 0 };

    // Define degree of freedom
    df  = 3;

    // Define control structure
    struct cdfmControl ctl;
    ctl = cdfmControlCreate();

    /*
    ** Calculate cumulative probability of
    ** both variables being from -1e4 to 0
    */
    { p, err, retcode } = cdfMvt2e(ctl, l_lim, u_lim, corr, nonc, df );

After the above code, *p* should equal:

::

    0.06226091
    0.31743546
    0.12010880

which means that:

.. math::
    P(-5 \leq x_1 \leq -1   \text{ and } -8 \leq  x_2 \leq -1.1) = 0.0623\\
    P(-20 \leq x_1 \leq +0 \text{ and } -10 \leq x_2 \leq +0.1) = 0.3174\\
    P(0 \leq x_1 \leq 1 \text{ and } 0 \leq x_2 \leq 1.1) = 0.1201

Compute the non central multivariate student's t cdf
++++++++++++++++++++++++++++++++++++++++++++++++++++

::

   /*
   ** Limits of integration
   ** -5 ≤ x1 ≤ -1 and -8 ≤ x2 ≤ -1.1
   ** -20 ≤ x1 ≤ 0 and -10 ≤ x2 ≤ 0.1
   **  0 ≤ x1 ≤ 1 and 0 ≤ x2 ≤ 1.1
   */
   l_lim = { -5  -8,
            -20 -10,
              0   0 };

    u_lim = { -1 -1.1,
               0  0.1,
               1  1.1 };

    // Correlation matrix
    corr = {   1 0.31,
            0.31    1 };

    // Define non-centrality vector, Kx1
    nonc  = {  1, -2.5 };

    // Define degree of freedom
    df  = 3;

    // Define control structure
    struct cdfmControl ctl;
    ctl = cdfmControlCreate();

    /*
    ** Calculate cumulative probability of
    ** both variables being from -1e4 to 0
    */
    { p, err, retcode } = cdfMvt2e(ctl, l_lim, u_lim, corr, nonc, df );

After the above code, *p* should equal:

::

    0.02810292
    0.15190018
    0.00092484

which means with non-central vector, the multivariate student's t cdf are:

.. math::
    P(-5 \leq x_1 \leq -1 \text{ and } -8 \leq x_2 \leq -1.1) = 0.0281\\
    P(-20 \leq x_1 \leq +0 \text{ and } -10 \leq x_2 \leq +0.1) = 0.1519\\
    P(0 \leq x_1 \leq 1 \text{ and } 0 \leq x_2 \leq 1.1) = 0.0009


Source
------------

cdfm.src

#. Genz, A. and F. Bretz,''Numerical computation of multivariate
   t-probabilities with application to power calculation of multiple
   contrasts,'' Journal of Statistical Computation and Simulation,
   63:361-378, 1999.

#. Genz, A., ''Numerical computation of multivariate normal
   probabilities,'' Journal of Computational and Graphical Statistics,
   1:141-149, 1992.

.. seealso:: Functions :func:`cdfMvte`, :func:`cdfMvtce`, :func:`cdfMvn2e`
