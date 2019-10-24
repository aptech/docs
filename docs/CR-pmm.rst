
pmm
==============================================

Purpose
----------------

Replaces missing values with imputed values using predictive mean matching.

Format
----------------
.. function:: y_imputed = __pmm(y, x[, iCtl]])

    :param y: data vector with missing values.
    :type y: Nx1 vector

    :param x: matrix of variables to be used to impute the missing values. Should not contain any missing values.
    :type x: NxK matrix

    :param iCtl: an instance of an :class:`imputeControl` structure. The following members of *iCtl* are referenced within the :func:`pmm` routine:

      .. list-table::
          :widths: auto

        * - *iCtl.numberSeries*
          - Scalar, number of series to be imputed.  Default = 1.
        * - *iCtl.numberDonors*
          - Scalar, number of donors to be considered  for PMM and LRD methods if *dMax* member is
          set to zero. If the *dMax* member is nonzero the *numberDonors* member will be used to determine candidate donors only if no potential donors meet the maximum distance criteria. Default = 5.
        * - *iCtl.dMax*
          - Scalar, maximum distance cutoff to be used to determine candidate donors. If set to zero, the *numberDonors* member will be used to determine candidate donors. If non-zero and *adaptiveDmax* is set to one, the *numberDonors* member will be used to determine candidate donors only if no donor meet the maximum distance criteria. Default = 0.
        * - *iCtl.matchingType*
          - Integer, the type of matching to be used in the predictive mean matching. Default = 1.
            Acceptable values:

              :0: Type 0 matching. Ignores variability in estimated betas and OLS beta is used for predicting in both the missing and observed cases.
              :1: Type 1 matching. Uses OLS beta for predicting for observed cases and a beta drawn from the posterior distribution for prediction in the missing cases.
              :2: Type 2 matching. Uses same beta drawn from the posterior distribution for predicting in both the missing and observed cases.
              :3: Type 3 matching. Uses same different betas drawn from the same posterior distribution for predicting in the missing and observed cases.
        * - *iCtl.linearMethod*
          - String, the prediction method used for LRD or linear prediction. Default = :code:`"bayes"`
            Acceptable values:

              :"predict": OLS :math:`beta` is used for predicting in missing cases.
              :"noise": OLS :math:`beta` is used for predicting in missing cases and a random disturbance drawn from :math:`N(0, \hat{\sigma})` is added to the prediction.
              :"bayes": Uses :math:`\dot{\beta}` drawn from the posterior distribution for predicting missing cases and a random disturbance drawn from :math:`N(0, \dot{\sigma})` is added to the prediction. :math:`\dot{\sigma}` is drawn from the posterior distribution.
              :"bootstrap": Coefficient and sigma are the least squares estimates calculated from a bootstrap sample taken from the observed data. A random disturbance is drawn from :math:`N(0, \dot{sigma})` is added to the prediction.
        * - *iCtl.adaptiveDmax*
          - Scalar, indicator variable, either one or zero. When set to one uses an adaptive method that uses the *numberDonors* member to determine the number of potential candidates when no potential donors meet the max distance criteria. When set to zero missing values will be kept in dataset if no potential candidates meet the max distance criteria. Default = 0.
        * - *iCtl.k*
          - Scalar, ridge parameter used evade singular matrices when computing Bayesian and Bootstrap posterior distributions. Default = 0.00001.

    :type iCtl: struct

    :return y_imputed: original *y* with imputed values where the missing values originally occurred.
    :rtype y_imputed: Kx1 matrix

Examples
--------------

::

  rndseed 189790;

  // Create a 18x1 matrix with missing values
  y = { 1.27  .  3.7,
        .  5.23  .,
        7.12  8.99  .,
        .  10.1 11.09,
        2.8 9.1 2.03,
        . 0.9 .};

  y = vec(y);

  x = rndn(18, 5);

  // First test default cases
  y_imp = pmm(y, x);

  // Now use control structure
  struct imputeControl iCtl;
  iCtl = imputeControlCreate();

  // Change matching type to type 2
  // instead of default type 1
  iCtl.matchingType = 0;
  y_imp0 = pmm(y, x, iCtl);


  // Change linear prediction type to
  // predict instead of bayes
  struct imputecontrol iCtl;
  iCtl = imputeControlCreate();

  icTl.linearMethod = "predict";
  y_imp_predict = pmm(y, x, iCtl);

  // Use dmax method
  struct imputeControl iCtl;
  iCtl = imputeControlCreate();

  icTl.dmax = 4.5;
  y_imp_dmax = pmm(y, x, iCtl);

  // Turn off adaptiveDmax
  // Note that this leaves missing values
  // in imputed dataset
  icTl.adaptiveDmax = 0;
  y_imp_dmax_noadapt = pmm(y, x, iCtl);

  print "y-matrix ~ y_imp_default ~ y_imp_type0 ~ y_imp_linear ~ y_imp_dmax ~ y_imp_dmax_noadapt";
  y~y_imp~y_imp0~y_imp_predict~y_imp_dmax~y_imp_dmax_noadapt;

After the code

::

  y-matrix ~ y_imp_default ~ y_imp_type0 ~ y_imp_linear ~ y_imp_dmax ~ y_imp_dmax_noadapt

       1.2700000        1.2700000        1.2700000        1.2700000        1.2700000        1.2700000
               .       -1.2308107       0.80802246       0.80802158        1.0745335                .
       7.1200000        7.1200000        7.1200000        7.1200000        7.1200000        7.1200000
               .       0.80802246       -1.1697303       -2.1980657       -2.1979831       -2.1979831
       2.8000000        2.8000000        2.8000000        2.8000000        2.8000000        2.8000000
               .       0.80802246       -1.1697303       0.80802158        1.0745335        1.9460724
               .       0.80802246       0.80802246       -2.1980657       -1.1697303       -1.1697303
       5.2300000        5.2300000        5.2300000        5.2300000        5.2300000        5.2300000
       8.9900000        8.9900000        8.9900000        8.9900000        8.9900000        8.9900000
       10.100000        10.100000        10.100000        10.100000        10.100000        10.100000
       9.1000000        9.1000000        9.1000000        9.1000000        9.1000000        9.1000000
      0.90000000       0.90000000       0.90000000       0.90000000       0.90000000       0.90000000
       3.7000000        3.7000000        3.7000000        3.7000000        3.7000000        3.7000000
               .        1.0745335        1.0745335       0.80802158       -2.1979831        4.7229624
               .        5.3760367       0.80802246       0.80802158       -1.1697303                .
       11.090000        11.090000        11.090000        11.090000        11.090000        11.090000
       2.0300000        2.0300000        2.0300000        2.0300000        2.0300000        2.0300000
               .       -1.2308107        4.7229624       0.80802158       -1.1697303                .

.. seealso:: Functions :func:`pmm`, :func:`impute`, :func:`imputePredict`
