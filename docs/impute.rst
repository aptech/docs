
impute
==============================================

Purpose
----------------
Replaces missing values in the columns of a matrix by a specified imputation method.


Format
----------------
.. function:: x_full = impute(x[, method [, indvars [, iCtl]]])

    :param x: Data matrix which has missing values to be imputed. If no missing values, original matrix will be returned.
    :type x: NxK matrix

    :param method: Optional input. Specifies which imputation method to use.

        **Valid options:**

        .. list-table::
            :widths: auto

            * - "bfill"
              - Replace missing values with the next valid observation (backward fill).
            * - "ffill"
              - Replace missing values with the most recent previous valid observation (forward fill).
            * - "mean"
              - Replace missing values with the mean of the column (default).
            * - "median"
              - Replace missing values with the median of the column.
            * - "mode"
              - Replace missing values with the mode of the column.
            * - "pmm"
              - Replace missing values using predictive mean matching.
            * - "lrd"
              - Replace missing values using local residual draws.
            * - "predict"
              - Replace missing values using linear regression prediction.

    :type method: string

    :param indvars: Optional input, matrix of variables to be used to impute the missing values. Should not contain any missing values. Must be specified if using the "pmm", "lrd", or "predict" methods.
    :type indvars: NxK matrix

    :param iCtl: Optional input, an instance of an :class:`imputeControl` structure. The following members of *iCtl* are referenced within the :func:`impute` "pmm", "lrd", and "predict" routines:

      .. list-table::
          :widths: auto

          * - *iCtl.numberSeries*
            - Scalar, number of series to be imputed.  Multiple series only valid for Nx1 *x* vector. Default = 1.
          * - *iCtl.numberDonors*
            - Scalar, number of donors to be considered  for PMM and LRD methods if *dMax* member is
              set to zero. If the *dMax* member is nonzero the *numberDonors* member will be used to determine candidate donors only if no potential donors meet the maximum distance criteria. Default = 5.
          * - *iCtl.dMax*
            - Scalar, maximum distance cutoff to be used to determine candidate donors. If set to zero, the *numberDonors* member will be used to determine candidate donors. If non-zero and *adaptiveDmax* is set to one, the *numberDonors* member will be used to determine candidate donors only if no donor meet the maximum distance criteria. Default = 0.
          * - *iCtl.matchingType*
            - Integer, the type of matching to be used in the predictive mean matching. Default = 1.
              Acceptable values:

                :0: Type 0 matching. Ignores variability in estimated betas and OLS beta is used for predicting in both the missing and observed cases.
                :1: Type 1 matching. Uses OLS :math:`\beta` for predicting for observed cases and a beta drawn from the posterior distribution for prediction in the missing cases.
                :2: Type 2 matching. Uses same :math:`\beta` drawn from the posterior distribution for predicting in both the missing and observed cases.
                :3: Type 3 matching. Uses same different :math:`\beta` drawn from the same posterior distribution for predicting in the missing and observed cases.

          * - *iCtl.linearMethod*
            - String, the prediction method used for LRD or linear prediction. Default = :code:`"bayes"`
              Acceptable values:

                :"predict": OLS :math:`\beta` is used for predicting in missing cases.
                :"noise": OLS :math:`\beta` is used for predicting in missing cases and a random disturbance drawn from :math:`N(0, \hat{\sigma})` is added to the prediction.
                :"bayes": Uses :math:`\dot{\beta}` drawn from the posterior distribution for predicting missing cases and a random disturbance drawn from :math:`N(0, \dot{\sigma})` is added to the prediction. :math:`\dot{\sigma}` is drawn from the posterior distribution.
                :"bootstrap": Coefficient and sigma are the least squares estimates calculated from a bootstrap sample taken from the observed data. A random disturbance is drawn from :math:`N(0, \dot{sigma})` is added to the prediction.

          * - *iCtl.adaptiveDmax*
            - Scalar, indicator variable, either one or zero. When set to one uses an adaptive method that uses the *numberDonors* member to determine the number of potential candidates when no potential donors meet the max distance criteria. When set to zero missing values will be kept in dataset if no potential candidates meet the max distance criteria. Default = 0.
          * - *iCtl.k*
            - Scalar, ridge parameter used evade singular matrices when computing Bayesian and Bootstrap posterior distributions. Default = 0.00001.

    :type iCtl: struct

    :return x_full: the input matrix with the missing values from each column filled in by the specified imputation method.

    :rtype x_full: matrix

Examples
----------------

Basic examples
+++++++++++++++

::

    // Create 3x3 matrix with a missing value
    x = { 1    2    3,
          4    .    5,
          7    8    9,
         10   11    . };

    // Replace missing values with column mean
    x_default = impute(x);

    // Replace missing values with column median
    x_median = impute(x, "median");

    // Replace missing values with column mean
    x_mean = impute(x, "mean");

The above code will make the following assignments:

::

                   1    2    3
    x_default =    4    7    5
                   7    8    9
                  10   11    5.67

                   1    2    3
    x_median  =    4    8    5
                   7    8    9
                  10   11    5

                   1    2    3
    x_mean    =    4    7    5
                   7    8    9
                  10   11    5.67


Time series forward-fill example
++++++++++++++++++++++++++++++++

::

    // Create a date sequence
    dates = seqaposix("2023-01-01", 1, "months", 12);
  
    // Create a random normal sequence with missing values
    rndseed 43243;
    values = rndn(rows(dates), 1);
  
    values[3 5 7] = miss();
  
    // Combine variables into a dataframe
    df = asdf(dates ~ values, "date", "value");
  
    print df;

::

            date            value
      2023-01-01      -0.20449596
      2023-02-01        1.8492699
      2023-03-01                .
      2023-04-01       0.35370459
      2023-05-01                .
      2023-06-01       -1.4505849
      2023-07-01                .
      2023-08-01      -0.70050827
      2023-09-01       -1.5805357
      2023-10-01       0.21287644
      2023-11-01      -0.94837545
      2023-12-01       0.38238763

::

    // Fill missing observations of the 'value' column
    // with the most recent valid observation
    df[.,"value"] = impute(df[.,"value"], "ffill");
   
    print df;

::

            date            value
      2023-01-01      -0.20449596
      2023-02-01        1.8492699
      2023-03-01        1.8492699
      2023-04-01       0.35370459
      2023-05-01       0.35370459
      2023-06-01       -1.4505849
      2023-07-01       -1.4505849
      2023-08-01      -0.70050827
      2023-09-01       -1.5805357
      2023-10-01       0.21287644
      2023-11-01      -0.94837545
      2023-12-01       0.38238763


Remarks
-------

-  If all elements of a column passed to :func:`impute` are missing values,
   every element of the corresponding column returned will contain
   missing values.
-  To replace the missing values in each column with a constant value,
   use :func:`missrv`. It will allow you to specify one constant for the entire
   matrix, or a separate constant for each column.
-  Use the :func:`miss` function to replace specific values (for example 999)
   with GAUSS missing values.
-  The :func:`packr` function will remove all rows which contain one or more
   missing values (listwise deletion).

.. seealso:: Functions :func:`missrv`, :func:`miss`, :func:`reclassify`, :func:`packr`
