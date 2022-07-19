lsdvFit
=======

Purpose
-------
Estimates coefficients of a regression model with autoregressive errors of any specified order.

Format
------
.. function:: lout1 = lsdvFit(y, x, series_length, n_lags[, lsc])
              lout1 = lsdvFit(dataset, formula, series_length, n_lags[, lsc])

   :param y: data.
   :type y: Nx1 vector

   :param x: independent data.
   :type x: Nxk vector

   :param dataset: name of data set or null string.
   :type dataset: string

   :param formula: formula string of the model. E.g. "y ~ X1 + X2" 'y' is the name of dependent variable, 'X1' and 'X2' are names of independent variables; E.g. "y ~ ." , '.' means including all variables except dependent variable 'y';
   :type formula: string

   :param series_length: number of time periods for each case or instance.
   :type series_length: scalar

   :param num_lags: number of lagged values of the dependent variable.
   :type num_lags: scalar

   :param lsc: Optional input, an instance of a lsdvmtControl structure. The following members of lsc are referenced within this routine:

      .. list-table::
         :widths: auto

         * - lsc.Constrain
           - scalar, if nonzero constraints will be applied to the autoregression coefficients. Default = 1.
         * - lsc.scale
           - scalar, if nonzero, data are scaled.
         * - lsc.output
           - scalar, determines the output to be printed.
         * - lsc.title
           - string, title to be printed at top of header.

   :type lsc: struct

   :return out: An instance of an lsdvOutstructure. The following members of out are referenced within this routine:

      .. list-table::
         :widths: auto

         * - autoCoefficients
           - Jx1 vector, uncorrected autoregression coefficients.
         * - regCoefficients
           - Kx1 vector, uncorrected regression coefficients.
         * - autoCoefficientsCorr
           - Jx1 vector, bias corrected autoregression coefficients.
         * - regCoefficientsCorr
           - Kx1 vector, bias corrected regression coefficients.
         * - autoStderrs
           - Jx1 vector, autoregression coefficient standard errors.
         * - regStderrs
           - Kx1 vector, regression coefficient standard errors.
         * - covPar
           - KxK matrix, covariance matrix of parameters
         * - SSresidual
           - scalar, residual sums of squares.
         * - SStotal
           - scalar, total sums of squares.
         * - SSexplained
           - scalar, explained sums of squares.
         * - SSpooledResidual
           - scalar, pooled residual sums of squares.
         * - biasCorr
           - K+Jx1 vector, bias corrections.
         * - lagrange
           - Jx2 matrix, Lagrangeans for constraints.
         * - numCases
           - scalar, number of cases.
         * - numMissing
           - scalar, number of observations with missing data.
         * - numDF
           - scalar, number of degrees of freedom.
         * - numObservations
           - scalar, number of observations.
         * - numParameters
           - scalar, number of parameters.
         * - numPeriods
           - scalar, number of periods in time series.

   :rtype out: struct

Examples
--------

Dataset and formula
++++++++++++++++++++
::

   new;
   library tsmt;

   // Declare lsdvmt control structure
   struct lsdvmtControl c0;
   c0 = lsdvmtControlCreate();

   // Turn screen output on
   c0.output = 1;

   // Scale data before running
   c0.scale = 0;

    // Declare output structure
   struct lsdvmtOut out;

   // Call lsdvmt function 
   out = lsdvFit(getGAUSSHome() $+ "pkgs/tsmt/examples/lsdv.dat", "Y~X1+X2+X3", 50, 2, c0);

Data matrices
++++++++++++++

::

   new;
   library tsmt;

   //Load data
   data = loadd( getGAUSSHome() $+ "pkgs/tsmt/examples/lsdv.dat");

   //Dependent variable
   y = data[., 1];

   //Independent variable
   x = data[., 2:4];

   //Declare lsdvmt control structure
   struct lsdvmtControl c0;
   c0 = lsdvmtControlCreate();

   //Turn screen output on
   c0.output = 1;

   //Scale data before running
   c0.scale = 0;

    //Declare output structure
   struct lsdvmtOut out;

   //Call lsdvmt function
   out = lsdvFit(y, x, 50, 2, c0);

Remarks
-------
The data must be contained in a GAUSS dataset cross-sectional unit by
cross-sectional unit, with one variable containing an index for the
units. From each cross-sectional unit all observations must be
grouped together. For example, for the first cross-sectional unit
there may be 10 rows in the dataset, for the second cross-sectional
unit there may be another 10 rows, and so on. Each row in the dataset
contains measurements on the endogenous and exogenous variables
measured for each observation along with the index identifying the
cross-sectional unit.

The index variable must be a series of integers. While all
observations for each cross-sectional unit must be grouped together,
they do not have to be sorted according to the index.


Library
-------
tsmt

Source
------
lsdvmt.src
