
cdfMvte
==============================================

Purpose
----------------
Computes multivariate Student's t cumulative distribution function with error management.

Format
----------------
.. function:: cdfMvte(ctl, x, corr, nonc, df)

    :param ctl: instance of a :class:`cdfmControl` structure with members

        .. csv-table::
            :widths: auto

            "ctl.maxEvaluations", "scalar, maximum number of evaluations."
            "ctl.absErrorTolerance", "scalar, absolute error tolerance."
            "ctl.relErrorTolerance", "scalar, tolerance."

    :type ctl: struct

    :param x: Lower limits at which to evaluate the Student's t cumulative distribution function. If *x* has more than one row, each row will be treated as a separate set of upper limits. K is the dimension of the multivariate Student's t distribution. N is the number of MVT cdf integrals.
    :type x: NxK matrix

    :param corr: correlation matrix.
    :type corr: KxK matrix

    :param nonc: noncentralities.
    :type nonc: Kx1 vector

    :param df: degrees of freedom.
    :type df: scalar

    :returns: **p** (*N x 1 vector*) - Each element in *p* is the cumulative distribution function of the multivariate Student's t distribution for the corresponding elements in *x*.

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

    // Upper limits of integration for K dimensional multivariate Student's t distribution
    x = { 0  0 };

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
    ** both variables being ≤ 0
    */
    { p, err, retcode } = cdfMvte(ctl, x, corr, nonc, df );

    // Calculate joint probablity of two
    // variables with zero correlation,
    // both, being ≤ 0
    p2 = (1 - cdftc(0, df)) .* (1- cdftc(0, df));

After the above code, both *p* and *p2* should be equal to 0.25.

.. math::
    T = P(-\infty <  X_1 \leq 0 \text{ and } - \infty < X_2 \leq 0) \approx 0.25.

Compute the multivariate student's t cdf at 3 separate pairs of upper limits
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    /*
    ** Upper limits of integration
    ** x1 ≤ -1 and x2 ≤ -1.1
    ** x1 ≤ 0 and x2 ≤ 0.1
    ** x1 ≤ 1 and x2 ≤ 1.1
    */
    x = {  -1   -1.1,
            0    0.1,
            1    1.1 };

    // Correlation matrix
    corr = {   1 0.31,
            0.31    1 };

    // Define non-centrality vector
    nonc  = {0, 0};

    // Define degree of freedom
    df  = 3;

    // Define control structure
    struct cdfmControl ctl;
    ctl = cdfmControlCreate();

    /*
    ** Calculate cumulative probability of
    ** each pair of upper limits
    */
    {p, err, retcode}  = cdfMvte(ctl, x, corr, nonc, df);

After the above code, *p* should equal:

::

    0.06752203
    0.31824308
    0.69617932

which means that:

.. math::
    P(x_1 \leq -1 \text{ and } x_2 \leq -1.1) = 0.0675\\
    P(x_1 \leq +0 \text{ and } x_2 \leq +0.1) = 0.3182\\
    P(x_1 \leq 1 \text{ and } x_2 \leq 1.1) = 0.6962

Compute the non central multivariate student's t cdf
++++++++++++++++++++++++++++++++++++++++++++++++++++

::

   /*
   ** Upper limits of integration
   ** x1 ≤ -1 and x2 ≤ -1.1
   ** x1 ≤ 0 and x2 ≤ 0.1
   ** x1 ≤ 1 and x2 ≤ 1.1
   */
    x = {  -1   -1.1,
            0    0.1,
            1    1.1 };

    // Correlation matrix
    corr = {  1 0.31,
           0.31    1 };

    // Define non-centrality vector, Kx1
    nonc = {  1, -2.5 };

    // Define degree of freedom
    df  = 3;

    // Define control structure
    struct cdfmControl ctl;
    ctl = cdfmControlCreate();

    /*
    ** Calculate cumulative probability of
    ** each pair of upper limits
    */
    {p, err, retcode}  = cdfMvte(ctl, x, corr, nonc, df);

After the above code, *p* should equal:

::

    0.03571301
    0.15854358
    0.46919524

which means with non-central vector, the multivariate student's t cdf are:

.. math::
    P(x_1 \leq -1 \text{ and } x_2 \leq -1.1) = 0.0357\\
    P(x_1 \leq +0 \text{ and } x_2 \leq +0.1) = 0.1585\\
    P(x_1 \leq 1 \text{ and } x_2 \leq 1.1) = 0.4692

References
----------------
#. Genz, A. and F. Bretz,''Numerical computation of multivariate
   t-probabilities with application to power calculation of multiple
   contrasts,'' Journal of Statistical Computation and Simulation,
   63:361-378, 1999.

#. Genz, A., ''Numerical computation of multivariate normal
   probabilities,'' Journal of Computational and Graphical Statistics,
   1:141-149, 1992.

.. seealso:: Functions :func:`cdfMvte`, :func:`cdfMvt2e`, :func:`cdfMvnce`
