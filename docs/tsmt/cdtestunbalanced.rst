================
cdTestUnbalanced
================

10.0.13cdTestUnbalanced
=======================

Purpose
-------
Pesaran panel series cross-sectional dependence, CD, test for
   unbalanced panels. The test statistics constructed from the mean
   t-statistic has an asymptotic standardized normal distribution and
   tests the null hypothesis that all series are *I(1)* against the
   alternative that all series are\ *I(0* )

Library
-------
tsmt

Format
------
cd = cdTestUnbalanced(res, grp_vector);

Input
-----
========== =================================================
   res        Nx1 matrix, residuals from panel data regression.
   grp_vector N x 1 matrix, group indicator variable.
   ========== =================================================

Output
------
== ===============
   cd test statistic.
   == ===============

Example
-------
::

new;
cls;
library tsmt;

/*************************************
//Generate data
**************************************/
// Set panel size parameters
N = 12;

// Generate grp vector
T={8, 9, 6, 7, 5, 5, 5, 6, 9, 7, 7, 9};
nobs = sumc(T);

// Initialize group
grp = 1*ones(T[1], 1);

// Simulate balanced group vector
for i(2, 12, 1);
    grp = grp| (i*ones(T[i], 1));
endfor;

// Simulate random residual vector
rndseed 234253;
residuals = rndn(nobs, 1);

// Call unbalanced test
call cdTestUnbalanced(residuals, grp);

Source
------
cd_unbalanced.src
