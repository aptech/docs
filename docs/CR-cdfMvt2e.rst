
cdfMvt2e
==============================================

Purpose
----------------
Computes multivariate Student's t cumulative distribution function with error management over :math:`[a, b]`.

Format
----------------
.. function:: cdfMvt2e(ctl, a, b, R, m, v)

    :param ctl: instance of a :class:`cdfmControl` structure with members

        .. csv-table::
            :widths: auto
    
            "ctl.maxEvaluations", "scalar, maximum number of evaluations."
            "ctl.absErrorTolerance", "scalar absolute error tolerance."
            "ctl.relErrorTolerance", "tolerance."

    :type ctl: struct

    :param a: lower limits. *K* is the dimension of multivariate Student's t distribution. *N* is the number of MVT cdf integrals.
    :type a: NxK matrix

    :param b: upper limits.
    :type b: NxK matrix

    :param R: correlation matrix.
    :type R: KxK matrix

    :param m: noncentralities.
    :type m: Kx1 vector

    :param v: degrees of freedom.
    :type v: scalar

    :returns: y (*Nx1 vector*), a :math:`Pr(X ≥ a and X ≤ b|R,m)`.

    :returns: err (*Nx1 vector*), estimates of absolute error.

    :returns: retcode (*Nx1 vector*), return codes.

        .. csv-table::
            :widths: auto
    
            "0", "normal completion with err < ctl.absErrorTolerance."
            "1", "err  >  ctl.absErrorTolerance and ctl.maxEvaluations exceeded; increase ctl.maxEvaluations to decrease error."
            "2", ":math:`K > 100` or :math:`K < 1`."
            "3", "*R* not positive semi-definite."
            "missing", "*R* not properly defined."

Remarks
------------

-  The central multivariate Student's t cdf for the i-th row of *a* and *b*
   is defined by where :math:`\nu \\in \\mathbb{R^+}` is a scale (or degree of freedom) 
   parameter, :math:`z` is a K-dimensional Student's t multivariate distribution, and


   For the non-central Student's t multivariate distribution cdf, we
   have


   where

   
   denotes the :math:`K \\times 1` non-centrality vector with :math:`-\infty< \\delta_k < \\infty` .

   Another form of non-central multivariate Student's t distribution cdf
   is

.. DANGER:: FIX EQUATIONS


-  The correlation matrix :math:`R` is defined by covariance matrix :math:`\Sigma`, :math:`\Sigma = DRD`, where :math:`D` denotes the diagonal matrix which has the square roots of the
   diagonal entries for :math:`\Sigma` on its diagonal.

Examples
----------------

Uncorrelated variables
++++++++++++++++++++++

::

    // Lower limits of integration for K dimensional multivariate distribution
    a = { -1e4 -1e4 };
    
    // Upper limits of integration for K dimensional multivariate distribution
    b = { 0 0 };		
    
    // Identity matrix, indicates
    // zero correlation between variables
    R = { 1 0,
          0 1 };
    				
    // Define non-centrality vector 
    m  = { 0, 0 };
    				
    // Define degree of freedom 
    v  = 3;        		
    						
    // Define control structure				
    struct cdfmControl ctl;
    ctl = cdfmControlCreate();
    
    // Calculate cumulative probability of
    // both variables being from -1e4 to 0
    { p, err, retcode } = cdfMvt2e(ctl, a, b, R, m, v );

After the above code, both *p* equal to 0.25.

.. math::
    T = P(-\infty <  X_1 \leq 0 \text{ and } - \infty < X_2 \leq 0) \approx 0.25.

Compute the multivariate student's t cdf at 3 separate pairs of upper limits
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Limits of integration
    //-5 ≤ x1 ≤ -1 and -8 ≤ x2 ≤ -1.1
    //-20 ≤ x1 ≤ 0 and -10 ≤ x2 ≤ 0.1
    // 0 ≤ x1 ≤ 1 and 0 ≤ x2 ≤ 1.1
    a = { -5  -8,
         -20 -10,
           0   0 };
    b = {  -1 -1.1,
            0  0.1,
            1  1.1 };
    
    // Correlation matrix
    R = {    1 0.31,
          0.31    1};
    				
    // Define non-centrality vector 
    m  = { 0, 0 };
    				
    // Define degree of freedom 
    v  = 3;      
    				      				
    // Define control structure
    struct cdfmControl ctl;
    ctl = cdfmControlCreate();
    				
    // Calculate cumulative probability of
    // each pair of limits
    { p, err, retcode }  = cdfMvt2e(ctl, a, b, R, m, v);

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

    // Limits of integration
    //-5 ≤ x1 ≤ -1 and -8 ≤ x2 ≤ -1.1
    //-20 ≤ x1 ≤ 0 and -10 ≤ x2 ≤ 0.1
    // 0 ≤ x1 ≤ 1 and 0 ≤ x2 ≤ 1.1
    a = {   -5  -8,
           -20 -10,
             0   0 };
    b = {  -1 -1.1,
            0  0.1,
            1  1.1 };
    
    // Correlation matrix
    R = { 1    0.31,
          0.31    1 };
    				
    // Define non-centrality vector, Kx1
    m  = {  1, 
         -2.5 };
    				
    // Define degree of freedom 
    v  = 3;    
    				         				
    // Define control structure
    struct cdfmControl ctl;
    ctl = cdfmControlCreate();
    				
    // Calculate cumulative probability of
    // each pair of limits
    { p, err, retcode } = cdfMvt2e(ctl, a, b, R, m, v);

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

