svarFit
=======

Purpose
-------
Estimate structural vector autoregressive models.

Format
------
.. function:: rslt = svarFit(Y [, maxlags, const, ctl])

    :param Y: NxM data.
    :type Y: matrix

    :param maxlags: Optional, maximum number of lags to consider for VAR model.
    :type maxlags: scalar

    :param const: Optional, specifying deterministic components of model. 
    :type const: scalar
   
        =========== ===========================================================================
           0           No constant or trend.
           1           Constant. (Default)
           2           Constant and trend.
        =========== ===========================================================================

    :param ctl: Optional, an instance of the :class:`svarControl` structure containing the following members.
    

        .. list-table::
            :widths: auto

            * - ctl.lutStats
              - An indicator specifying to use the Lutkepohl (2005) versions of the information criteria be reported. Default = 1.
            * - ctl.smallDF
              - An indicator specifies that a small-sample degrees-of-freedom adjustment be used when estimating sigma, the error variance–covariance matrix. Specifically, 1/(T - m) is used instead of the large-sample divisor 1/T, where m is the average number of parameters in the functional form for yt over the K equations. Default = 1.
            * - ctl.printVAR
              - An indicator specifying whether to print the results to screen. Default = 1.
            * - ctl.irf
              - An instance of the :class:`irfControl` structure containing the following members.

              .. include:: include/irfcontrol.rst

    :type ctl: struct
    
    :return: An instance of an :class:`svarOut` structure containing the following members.
    

        .. list-table::
            :widths: auto

            * - rslt.b
              - NxM matrix, of final estimates for the SVAR reduced form coefficients, computed by OLS.
            * - rslt.ll
              - Scalar, value of the maximized likelihood function.
            * - rslt.e
              - NxM matrix, residuals.
            * - rslt.vcb
              - KxK matrix, covariance matrix for the SVAR reduced form coefficients.
            * - rslt.aic
              - Scalar, Akaike Information Criterion (AIC).
            * - rslt.sbc
              - Scalar, Schwarz Bayesian Criterion (SBC).
            * - rslt.tsmtDesc
              - An instance of the :class:`tsmtModelDesc` structure containing the following members:

              .. include:: include/tsmtmodeldesc.rst

            * - rslt.sumStats 
              - An instance of the :class:`tsmtSummaryStats` structure containing the following members:
  
              .. include:: include/tsmtsummarystats.rst

        :rtype: struct

Examples
---------

Example One: Short-run restrictions
++++++++++++++++++++++++++++++++++++++++
This example demonstrates the use of short-run restrictions to identify the structural model. It uses the cholesky identification method to determine the structural model. 
This is the default identification method so no :class:`svarControl` structure is necessary.

:: 

    // Load library
    new;
    library tsmt;

    /*
    ** Data import
    */
    lutkepohl2 = loadd(getGAUSShome("pkgs/tsmt/examples/lutkepohl2.dta"));

    // Filter data 
    lutkepohl2 = selif(lutkepohl2, lutkepohl2[., "qtr"] .<= "1978-12-30");

    // Set Y
    y = packr(lutkepohl2[., "qtr" "dln_inv" "dln_inc" "dln_consump"]);
    
    // Set up output structures
    struct svarOut sout;

    // Compute structural VAR model
    sout = svarFit(Y);

This prints the estimates for the reduced for coefficients:

::

    =====================================================================================================
    Model:                      SVAR(2)                               Number of Eqs.:                   3
    Time Span:              1960-04-01:                               Valid cases:                     73
                            1978-10-01                                                                   
    Log Likelihood:             606.307                               AIC:                        -24.632
                                                                    SBC:                        -24.067
    =====================================================================================================
    Equation                             R-sq                  DW                 SSE                RMSE

    dln_inv                           0.12856             2.01020             0.14056             0.04615 
    dln_inc                           0.11419             1.75766             0.00906             0.01172 
    dln_consump                       0.25128            -1.84234             0.00589             0.00944 
    =====================================================================================================
    Results for reduced form equation dln_inv
    =====================================================================================================
            Coefficient            Estimate           Std. Err.             T-Ratio          Prob |>| t
    -----------------------------------------------------------------------------------------------------

                Constant            -0.01672             0.01723            -0.97073             0.33523 
            dln_inv L(1)            -0.31963             0.12546            -2.54775             0.01318 
            dln_inc L(1)             0.14599             0.54567             0.26754             0.78989 
        dln_consump L(1)             0.96123             0.66431             1.44696             0.15264 
            dln_inv L(2)            -0.16055             0.12491            -1.28537             0.20316 
            dln_inc L(2)             0.11460             0.53457             0.21438             0.83091 
        dln_consump L(2)             0.93440             0.66509             1.40491             0.16474 
    =====================================================================================================
    Results for reduced form equation dln_inc
    =====================================================================================================
            Coefficient            Estimate           Std. Err.             T-Ratio          Prob |>| t
    -----------------------------------------------------------------------------------------------------

                Constant             0.01577             0.00437             3.60427             0.00060 
            dln_inv L(1)             0.04393             0.03186             1.37891             0.17258 
            dln_inc L(1)            -0.15273             0.13857            -1.10219             0.27438 
        dln_consump L(1)             0.28850             0.16870             1.71014             0.09194 
            dln_inv L(2)             0.05003             0.03172             1.57726             0.11952 
            dln_inc L(2)             0.01916             0.13575             0.14116             0.88817 
        dln_consump L(2)            -0.01020             0.16890            -0.06039             0.95203 
    =====================================================================================================
    Results for reduced form equation dln_consump
    =====================================================================================================
            Coefficient            Estimate           Std. Err.             T-Ratio          Prob |>| t
    -----------------------------------------------------------------------------------------------------

                Constant             0.01293             0.00353             3.66626             0.00049 
            dln_inv L(1)            -0.00242             0.02568            -0.09437             0.92510 
            dln_inc L(1)             0.22481             0.11168             2.01305             0.04819 
        dln_consump L(1)            -0.26397             0.13596            -1.94153             0.05646 
            dln_inv L(2)             0.03388             0.02556             1.32534             0.18963 
            dln_inc L(2)             0.35491             0.10941             3.24398             0.00185 
        dln_consump L(2)            -0.02223             0.13612            -0.16329             0.87079 
    =====================================================================================================

The IRFs for the model are stored in the *irf* member of the :class:`svarOut` output structure. This member is 3-dimensional array, with each plane containing the response to shocks to a different endogenous variable. The planes house a MxH matrix of responses with each row containg the responses from different response variable, and each column representing a different horizon.

For example, let's preview the response of our three endogenous variables to, *dln_inv*, *dln_inc*, and *dln_consump*, to a shock in the first variable, *dln_inv*.

::

    // Index of shock variable 
    shk_indx = 1;

    // Get matrix of responses to dln_inv
    res_to_dln_inv = getMatrix(sout.irf, shk_indx);

    // Print first five responses
    res_to_dln_inv[., 1:3];

::

    0.046147884     -0.011956777      -0.0009900109 
    0.001551898      0.002560746       0.0012599300 
    0.002670542     -0.000467869       0.0027831146

Example Two: Long-run restrictions
++++++++++++++++++++++++++++++++++++++++
This example demonstrates the use of long-run restrictions to identify the structural model. This is done using the *ctl.irf.ident* member of the :class:`svarControl` structure. 

:: 

    // Load library
    new;
    library tsmt;

    /*
    ** Data import
    */
    lutkepohl2 = loadd(getGAUSShome("pkgs/tsmt/examples/lutkepohl2.dta"));

    // Filter data 
    lutkepohl2 = selif(lutkepohl2, lutkepohl2[., "qtr"] .<= "1978-12-30");

    // Set up output structures
    struct svarOut sout;

    // Declare controls structure
    // Fill with defaults
    struct svarControl ctl;
    ctl = svarControlCreate();

    // Use long-run restrictions for
    // structural identification
    ctl.irf.ident = "long"; 

    // Set Y
    y = packr(lutkepohl2[., "qtr" "dln_inv" "dln_inc" "dln_consump"]);

    // Run model
    maxlags = 8;
    const = 1;

    // Check structural VAR model
    sout = svarFit(Y, maxlags, const, ctl);

The reduced for estimates for this model are the same as the first model, because identification restrictions have no impact on the reduced form estimates. 

However, if we look at the IRFS using these restrictions:

::

    // Index of shock variable 
    shk_indx = 1;

    // Get matrix of responses to dln_inv
    res_to_dln_inv = getMatrix(sout.irf, shk_indx);

    // Print first five responses
    res_to_dln_inv[., 1:3];

::

    0.041667833    -0.0067978789     0.0016807041 
    0.0056614147     0.0026748073     0.0013125032 
    0.0059236730   -0.00039186770     0.0040106258



Example Three: Sign restrictions
++++++++++++++++++++++++++++++++++++++++
The sign-restrictions option implements identification based on the theoretically anticipated direction of the IRFs. For example, consider a VAR model which includes real (GDP), the personal consumption expenditure price index (PCEPI), and the federal funds rate (FFR).   

We can use sign-restricted IRFs to model the theory that real GDP and the PCEPI should initially respond with negatively to a monetary policy shock.

To start we import and transform the data:

:: 

    new;
    rndseed 908098;

    library tsmt;

    // Data files
    fname = getGAUSSHome("pkgs/tsmt/examples/sign_restrictions_data.csv");

    // Load data from .csv file
    // and take ln of GDPC1 and PCEp1
    data = loadd(__FILE_DIR $+ fname, "ln(GDPC1) + ln(PCEPI) + FEDFUNDS");

    // Renaming columns 
    data = asDF(data, "l_gdp"$|"l_pce"$|"ffr");

    // Remove missing values
    reg_data = packr(data);

Next we implement the sign restrictions using the :class:`svarControl` structure. This requires specifying:
* The use of sign-restrictions for identification by setting the :class:`svarControl` structure member *ctl.irf.ident* to ``"sign"``.
* Which shocks to restrict using the *ctl.irf.restrictedShock* control structure member. 
* The horizons whose responses are restricted using the *ctl.irf.restrictionHorizon* control structure member. 
* The direction of the restrictions using the *ctl.irf.signrestrictions* control structure member. This matrix should have a row for each restricted shock and a column for each response variable. A value of `-1` restricts a shock to be negative, a value of `1` restricts a shock to be positive, and a value of `0` indicates no restrictions.
  
:: 

    // Declare controls structure
    // Fill with defaults
    struct svarControl ctl;
    ctl = svarControlCreate();

    // Specify to use sign restrictions
    ctl.irf.ident = "sign";

    // Specify which shock variable is restricted
    ctl.irf.restrictedShock = 3;

    // Set up restrictions horizon
    ctl.irf.restrictionHorizon = 1;

    /* Specify sign restrictions 
    ** GDP response to monetary shock must < 0 (-1)
    ** PCE response to monetary shock must < 0 (-1)
    ** FFR response to monetary shock must > 0 (1)
    */
    ctl.irf.signRestrictions = { -1  -1  1 };

Finally, we run the model using :func:`svarFit`.

::

    /*
    ** Setup VAR estimation
    */
    // Maximum lags
    maxlags = 8;

    // Use constant in model
    const = 1;

    // Check structural VAR model
    struct svarOut sOut;
    sout = svarFit(reg_data, maxlags, const, ctl);


Remarks
-------
The procedure :func:`svarFit` is designed to provide flexibility in estimating SVAR models by allowing users to specify various options for the deterministic components, number of lags, and control settings for model estimation and impulse response analysis. The inclusion of bootstrapping methods and sign restrictions further enhances the robustness and interpretability of the resulting SVAR model.

.. seealso:: Functions :func:`arimaFit`, :func:`plotIRF`, :func:`svarControlCreate`, :func:`plotFEVD`

