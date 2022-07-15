cdTestUnbalanced
================

Purpose
-------
Pesaran panel series cross-sectional dependence, CD, test for unbalanced panels. The test statistics constructed from the mean statistic has an asymptotic standardized normal distribution and tests the null hypothesis that all series are *I(1)* against the alternative that all series are\ *I(0* )



Format
------
.. function::  cd = cdTestUnbalanced(res, grp_vector);

  :param res: residuals from panel data regression.
  :type res: Nx1 matrix

  :param grp_vector: group indicator variable.
  :type grp_vector: Nx1 matrix

  :return cd_stat: test statistic.
  :rtype cd_stat: scalar

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
  T={ 8, 9, 6, 7, 5, 5, 5, 6, 9, 7, 7, 9 };
  nobs = sumc(T);

  // Initialize group
  grp = 1*ones(T[1], 1);

  // Simulate unbalanced group vector
  for i(2, 12, 1);
    grp = grp| (i*ones(T[i], 1));
  endfor;

  // Simulate random residual vector
  rndseed 234253;
  residuals = rndn(nobs, 1);

  // Call unbalanced test
  call cdTestUnbalanced(residuals, grp);

The results printed are:

::

  Pesaran's CD Statistic =       0.23127249
  p_value =       0.40855156

Library
-------
tsmt

Source
------
cd_unbalanced.src

.. seealso:: Functions :func:`cdTest`
