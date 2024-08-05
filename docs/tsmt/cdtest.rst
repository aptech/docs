cdTest
======

Purpose
-------
Runs cross-sectional dependence, CD, tests for panel data. The test
statistics constructed from the mean t-statistic has an asymptotic
standardized normal distribution and tests the null hypothesis that
all series are *I(1)* against the alternative that all series
are *I(0)*

Format
------
.. function:: cd = cdTest(res, model, grp_vector)

   :param res: residuals from panel data regression.
   :type res: Nx1 matrix

   :param model: indicates which test to run\: 1 for Pesaran's test, 2 for Friedman's test, 3 for Frees' test. Note\: the only model appropriate for unbalanced data is model 1. This model will run by default if unbalanced panel data is detected.
   :type model: scalar

   :param grp: group indicator variable.
   :type grp: Nx1 matrix

   :return cd: test statistic
   :rtype cd: matrix

Examples
----------

Example One: Pesaran Test 
+++++++++++++++++++++++++++
::

   new;
   cls;
   library tsmt;

   /*************************************
   //Generate data
   **************************************/
   // Set panel size parameters
   N = 48;
   T = 17;

   // Simulate balanced group vector
   grp = vec(reshape(seqa(1, 1, N), 17, 48));

   // Simulate random stacked residuals
   rndseed 90782;
   y = rndn(T*N, 1);

   /*************************************
   /Run tests
   **************************************/
   // Run pesaran test [model = 1]
   z1 = cdTest(y, 1, grp);

This prints the following results to the **Command Window**:

::

   Test:                                    Pesaran Test (2004) 
   Timespan:                                            Unknown 
   Ho:                             Cross-sectional independence 
   N. Obs:                                                   17 
   N. Groups:                                                48 
   Panel Type:                                         Balanced 
   ============================================================

   CD-stat                                                0.780 
   P-val                                                  0.218 
   ============================================================

   Cannot reject the null hypothesis of cross-sectional 
   independence.

Example Two: Friedman Test 
+++++++++++++++++++++++++++

::

   // Run Friedman test [model = 2]
   z2 = cdTest(y, 2, grp);


   // Run Frees test [model = 3]
   z3 = cdTest(y, 3, grp);

The results printed to screen are

::

  Test:                                        Friedman (1937) 
  Test Variable:                                               
  Timespan:                                            Unknown 
  Ho:                             Cross-sectional independence 
  Number of breaks:                                       None 
  N. Obs:                                                   17 
  N. Groups:                                                48 
  Panel Type:                                         Balanced 
  ============================================================

  CD-stat                                               21.771 
  P-val                                                  0.151 
  ============================================================

  Cannot reject the null hypothesis of cross-sectional 
  independence.

Library
-------
tsmt

Source
------
cdtestbalanced.src

.. seealso:: Functions :func:`cdTestUnbalanced`
