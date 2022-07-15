autoregFit
==========

Purpose
-------
Estimates coefficients of a regression model with autoregressive errors of any specified order.

Format
------
.. function:: aro = autoregFit(y, x, lagvars, order[, arc])
              aro = autoregFit(dataset, formula, lagvars, order[, arc])

   :param y: data.
   :type y: Nx1 vector

   :param x: independent data.
   :type x: Nxk vector

   :param dataset: name of data set or null string.
   :type dataset: string

   :param formula: formula string of the model. E.g. ``"y ~ X1 + X2"`` 'y' is the name of dependent variable, 'X1' and 'X2' are names of independent variables; E.g. ``"y ~ ."`` , ``.`` means including all variables except dependent variable 'y';
   :type formula: string

   :param lagvars: the number of periods to lag the variables inindvars. If there are no lagged variables, set to scalar 0. The variables in indvars will be lagged the number of periods indicated in the corresponding entries inlagvars. The dependent variable in depvar can be included in indvars can be repeated if each corresponding entry in lagvars is a different value.
   :type lagvars: Kx1 vector

   :param order: order of the autoregressive process; must be greater than 0 and less than the number of observations.
   :type order: scalar

   :param arc: Optional input. Instance of an :class:`automtControl` structure. The following members of arc are referenced within this routine:

      .. list-table::
         :widths: auto

         * - arc.const
           - scalar. If 1, constant will be used in model; else not. Default = 1.
         * - arc.header
           - string, specifies the format for the output header. arc.header can contain zero or more of the following characters:

             .. list-table::
                :widths: auto

                * - t
                  - title is to be printed.
                * - l
                  - lines are to bracket the title.
                * - d
                  - a date and time is to be printed.
                * - v
                  - version number of program is to be printed.
                * - f
                  - file name of program is to be printed

             Example:

             ::

               arc.header = "tld";

             If :code:`arc.header = ""`, no header is printed. Default = ``"tldvf"``.

         * - arc.init
           - scalar. If 1, only initial estimates will be computed. Default = 0.
         * - arc.iter
           - scalar. If 0, iteration information will not be printed. If 1, iteration information will be printed (arc.outputmust be nonzero). Default = 0.
         * - arc.maxvec
           - scalar, the maximum number of elements allowed in any one matrix. Default = 20000.
         * - arc.output
           - scalar, if nonzero, results are printed to screen. Default = 1.
         * - arc.title
           - string, a title to be printed at the top of the output header (see arc.header). By default, no title is printed (``arc.title=""``).
         * - arc.tol
           - scalar, convergence tolerance. Default = 1e-5.

   :type arc: struct

   :return aro: An instance of an :class:`automtOut` structure containing the following members:

      .. list-table::
         :widths: auto

         * - aro.acor
           - (L+1)x1 vector, autocorrelations.
         * - aro.acov
           - (L+1)x1 vector, autocovariances.
         * - aro.chisq
           - scalar, -2\* log-likelihood.
         * - aro.coefs
           - Kx1 vector, estimated regression coefficients.
         * - aro.phi
           - Lx1 vector, lag coefficients.
         * - aro.rsq
           - scalar, explained variance.
         * - aro.sigsq
           - scalar, variance of white noise error.
         * - aro.tobs
           - scalar, number of observations.
         * - aro.vcb
           - KxK matrix, covariance matrix of estimated regression coefficients.
         * - aro.vcphi
           - LxL matrix, covariance matrix of *phi*.
         * - aro.vsig
           - scalar, variance of aro.sigsq (variance of the variance of white noise error).

   :rtype aro: struct


Examples
--------

Data matrices
++++++++++++++++++++++++++++++

::

   new;
   cls;
   library tsmt;

   //Load data
   data = loadd(getGAUSSHome() $+ "pkgs/tsmt/examples/autoregmt.dat");
   y = data[., 1];
   x = data[., 2 3];

   //Lag of independent variables
   lag_vars = 0;

   //Autoregressive order
   order = 3;

   //Initialized automtOut structure
   struct automtOut aro;

   //Call autoregFit function
   aro = autoregFit(y, x, lag_vars, order);

The final results are:

::

  DEPENDENT VARIABLE:  Y
                Number of Observations:     200
                             R-squared:     0.710
            Standard Error of Estimate:     1.524
  Variance of White Noise Error (sigsq):     0.913
                     Variance of sigsq:     0.008
                    -2*log(likelihood):   548.000

                COEFFICIENTS OF INDEPENDENT VARIABLES (beta)

  Variable        Coef           Std. Error     t-Ratio       P-Value
  -------------------------------------------------------------------
  CONSTANT       -0.266678       0.516473      -0.516344       0.606
  X1              0.503195       0.060327       8.341081       0.000
  X2              0.592405       0.059390       9.974846       0.000

                      AUTOREGRESSIVE PARAMETERS (Phi)

  Lag         Phi            Std. Error     T-Ratio        P-Value
  ----------------------------------------------------------------
  1           0.246131       0.065740       3.744029       0.000
  2           0.263760       0.065397       4.033229       0.000
  3           0.368323       0.065740       5.602763       0.000

                   AUTOCORRELATIONS AND AUTOCOVARIANCES

            Lag           Autocovariances      Autocorrelations
            ----------------------------------------------------
            0             2.322667             1.000000
            1             1.563621             0.673201
            2             1.573401             0.677411
            3             1.655176             0.712619

Dataset and formula string
++++++++++++++++++++++++++++++++++++++++++++

::

   new;
   cls;
   library tsmt;

   //Lag of independent variables
   lag_vars = 0;

   //Autoregressive order
   order = 3;

   //Initialized automtOut structure
   struct automtOut aro;

   //Call autoregFit function
   aro = autoregFit(getGAUSSHome() $+ "pkgs/tsmt/examples/autoregmt.dat", "Y ~ X1 + X2", lag_vars, order);

The results printed to screen are:

::

  DEPENDENT VARIABLE:  Y
                Number of Observations:     200
                             R-squared:     0.710
            Standard Error of Estimate:     1.524
  Variance of White Noise Error (sigsq):     0.913
                     Variance of sigsq:     0.008
                    -2*log(likelihood):   548.000

                COEFFICIENTS OF INDEPENDENT VARIABLES (beta)

 Variable        Coef           Std. Error     t-Ratio       P-Value
 -------------------------------------------------------------------
 CONSTANT       -0.266678       0.516473      -0.516344       0.606
 X1              0.503195       0.060327       8.341081       0.000
 X2              0.592405       0.059390       9.974846       0.000

                      AUTOREGRESSIVE PARAMETERS (Phi)

 Lag         Phi            Std. Error     T-Ratio        P-Value
 ----------------------------------------------------------------
 1           0.246131       0.065740       3.744029       0.000
 2           0.263760       0.065397       4.033229       0.000
 3           0.368323       0.065740       5.602763       0.000

                   AUTOCORRELATIONS AND AUTOCOVARIANCES

            Lag           Autocovariances      Autocorrelations
            ----------------------------------------------------
            0             2.322667             1.000000
            1             1.563621             0.673201
            2             1.573401             0.677411
            3             1.655176             0.712619

Remarks
-------
This program will handle only datasets that fit in memory.

All autoregressive parameters are estimated up to the specified lag.
You cannot estimate only the first and fourth lags, for instance.

The algorithm will fail if the model is not stationary at the
estimated parameters. Thus, in that sense it automatically tests for
stationarity.


Library
-------
tsmt

Source
------
autoregmt.src

.. seealso:: Functions :func:`arimaFit`, :func:`arimaSS`, :func:`arimaControlCreate`
