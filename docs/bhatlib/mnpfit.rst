mnpFit
==============================================

Purpose
----------------

Estimates the Multinomial Probit (MNP) model using analytic gradients and a variety of analytic approximation methods for the multivariate cumulative normal distribution, supporting mixture-of-normals random coefficients and flexible covariance restrictions.

Format
----------------

.. function:: beta_hat = mnpFit(fname, dvunordname, davunordname, ivunord, var_unordnames [, mix, ranvars, mCtl])

    :param fname: Name of dataset in CSV format containing the data for estimation.
    :type fname: string

    :param dvunordname: Names of dependent variables indicating chosen alternatives. The number of entries should equal the number of alternatives.
    :type dvunordname: string array

    :param davunordname: Names indicating the availability of alternatives.
    :type davunordname: string array

    :param ivunord: Independent variable specifications for each alternative (and segment if applicable). Rows correspond to alternatives, columns to variables.
    :type ivunord: string matrix

    :param var_unordnames: Names of independent variables for output reporting. Must match the number of columns in *ivunord*.
    :type var_unordnames: string array

    :param mix: Optional input. Indicates if random coefficients are included.
        :0: No random coefficients (default).
        :1: Random coefficients included.
    :type mix: scalar

    :param ranvars: Optional input. Names of variables (in *var_unordnames*) with random coefficients when *mix = 1*.
    :type ranvars: string array

    :param mCtl: Optional input. An instance of :class:`mnpControl` structure containing the following members:

        .. list-table::
            :widths: auto

            * - mCtl.nseg
              - Number of segments. Default = 1.
            * - mCtl.mix
              - Indicates random coefficients present. Default = 0.
            * - mCtl.randdiag
              - Diagonal restriction on random coefficients covariance. Default = 0.
            * - mCtl.want_covariance
              - Computes covariance matrix of estimates. Default = 1.
            * - mCtl.IID_first
              - If 1, forces IID kernel as starting values. Default = 0.
            * - mCtl.IID
              - Forces IID covariance structures. Default = 0.
            * - mCtl.heteronly
              - Controls heteroskedasticity restrictions in differenced covariance. Default = 0.
            * - mCtl.spherical
              - Parameterization type for Cholesky decomposition. 1 = spherical, 0 = radial. Default = 0.
            * - mCtl.scal
              - Scale matrix for spherical/radial parameterizations. Default = 1.
            * - mCtl.seed10
              - Seed for `"SSJ"`` method. Default = 70000000 if method is `"SSJ"`.
            * - mCtl.perms
              - Permutations for `"SSJ"` method. Default = 1 if method is `"SSJ"`.
            * - mCtl.method
              - Analytic approximation method. Default = `"OVUS"`.

    :type mCtl: struct

    :return beta_hat: Estimated parameters including fixed coefficients, random coefficients (if applicable), kernel/correlation parameters, and scale parameters.
    :rtype beta_hat: column vector

Remarks
------------

- Supports a variety of analytic methods for multivariate normal approximation:
  
    ==========  ======================================================
    Method      Description
    ==========  ======================================================
    "SSJ"       Switzer, Solow, and Joe method
    "TG"        Trinh and Genz's univariate conditioning
    "ME"        Matrix-based LDLT approach
    "OVUS"      One-variate univariate screening
    "OVBS"      One-variate bivariate screening
    "TGBME"     Trinh and Genz's bivariate conditioning
    "BME"       Bivariate ME approach
    "TVBS"      Two-variate bivariate screening
    ==========  ======================================================

- Uses the :func:`maxlik` framework for maximum likelihood estimation with analytic gradients.
- Random coefficients (mixture-of-normals) are supported when *mix = 1* with variable names specified in *ranvars*.

Examples
----------------

Basic usage without random coefficients
+++++++++++++++++++++++++++++++++++++++++++++

::

    // Set up the workspace 
    new;
    cls;

    // Load the libraries
    library bhatlib, maxlik;

    // Specify the dataset file
    fname = __FILE_DIR $+ "TRAVELMODE.csv";
    
    // Specify the dependent variables alternatives
    string dvunordname = { "Alt1_ch" "Alt2_ch" "Alt3_ch" };
    
    // Specify availability restrictions 
    string davunordname = "none";

    // Specify independent variables for each alternative
    string ivunord = {
        "sero" "sero" "AGE45" "sero" "IVTT_DA" "OVTT_DA" "COST_DA",
        "uno"  "sero" "sero"  "AGE45" "IVTT_SR" "OVTT_SR" "COST_SR",
        "sero" "uno"  "sero"  "sero" "IVTT_TR" "OVTT_TR" "COST_TR"
    };

    // Specify variable names for output reporting
    string var_unordnames = { "CON_SR" "CON_TR" "AGE45_DA" "AGE45_SR" "IVTT" "OVTT" "COST" };

    // Estimate the model
    beta_hat = mnpFit(fname, dvunordname, davunordname, ivunord, var_unordnames);

Usage with random coefficients
+++++++++++++++++++++++++++++++++++++++++++++

::

    // Set up the workspace
    new;
    cls;

    // Load the libraries
    library bhatlib, maxlik;

    // Specify the dataset file
    fname = __FILE_DIR $+ "TRAVELMODE.csv";
    
    //  Specify the dependent variables alternatives
    string dvunordname = { "Alt1_ch" "Alt2_ch" "Alt3_ch" };
    
    // Specify availability restrictions
    string davunordname = "none";

    // Specify independent variables for each alternative
    string ivunord = {
        "sero" "sero" "AGE45" "sero" "IVTT_DA" "OVTT_DA" "COST_DA",
        "uno"  "sero" "sero"  "AGE45" "IVTT_SR" "OVTT_SR" "COST_SR",
        "sero" "uno"  "sero"  "sero" "IVTT_TR" "OVTT_TR" "COST_TR"
    };

    // Specify variable names for output reporting
    string var_unordnames = { "CON_SR" "CON_TR" "AGE45_DA" "AGE45_SR" "IVTT" "OVTT" "COST" };

    // Turn on random coefficients
    mix = 1;

    // Specify random coefficients variables
    ranvars = "OVTT";

    beta_hat = mnpFit(fname, dvunordname, davunordname, ivunord, var_unordnames, mix, ranvars);

Source
------

bhatlib.src

