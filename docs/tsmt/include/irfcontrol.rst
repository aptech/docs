.. list-table::
   :widths: auto

   * - ctl.irf.nsteps
     - Scalar, the number of horizons for IRF computations. Default = 20.
   * - ctl.irf.ident
     - String, the identification method. Options include:
     
        =========== ===========================================================================
        "short"     Zero short-run restrictions.
        "long"      Zero long-run restrictions.
        "sign"      Sign restrictions.
        =========== ===========================================================================
     
    * - ctl.irf.ndraws
      - Scalar, number of draws for bootstrapping IRFs. Default = 10000.
    * - ctl.irf.cl
      - Scalar, confidence level for IRF bootstrap confidence intervals. Default = 0.95.
    * - ctl.irf.bootMethod
      - String, method for bootstrapping the IRF confidence intervals. Default = "bs".
    * - ctl.irf.signRestrictions
      - Matrix, specifies restrictions for sign restricted identification.  There should be a single row for each restricted shock and a column for and a single column for each endogenous variable. 0 specifies that no restrictions are placed on a variable, -1 specifies that the sign should be negative, 1 specifies that the sign should be positive.
    * - ctl.irf.restrictionHorizon
      - Matrix, specifies the number of horizons over which the restrictions hold.
    * - ctl.irf.restrictedShockNames
      - String array, specifies which shock has restricted impulses using variable names. Must be specified if the number of restricted shocks is less than the number of endogenous variables and ctl.irf.restrictedShock index is not specified.
    * - ctl.irf.restrictedShock
      - Matrix, specifies which shock has restricted impulses using an index. Must be specified if the number of restricted shocks is less than the number of endogenous variables and ctl.irf.restrictedShockNames is not specified.
