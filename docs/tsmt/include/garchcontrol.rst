.. list-table::
   :widths: auto

    * - gctl.density
      - scalar, density of error term:

           =========== ===========================================================================
           0           Normal distribution. (Default)
           1           Student's t-distribution. 
           3           Skew generalized t-distribution.
           =========== ===========================================================================

    * - gctl.asymmetry
      - scalar, if nonzero assymetry terms are added. (Default = 0)
    * - gctl.inmean
      - scalar, GARCH-in-mean, square root of conditional variance is included in the mean equation.
    * - gctl.stConstraintsType
      - scalar, type of enforcement of stationarity requirements:

           =========== =================================================================================
           1           Roots of characteristic polynomial constrained outside unit circle. (Default)
           2           ARCH, GARCH parameters constrained to sum to less than one and greater than zero. 
           3           None.
           =========== =================================================================================

    * - gctl.cvConstraintsType
      - scalar, type of enforcement of nonnegative conditional variances:

            =========== =================================================================================
            0           Direct constraints. (Default)
            1           Nelson & Cao constraints. 
            =========== =================================================================================

    * - gctl.covType
      - scalar, type of covariance matrix of parameters:

            =========== =================================================================================
            1           Maximum Likelihood. (Default)
            2           Quasi-Maximum Likelihood. (Default)
            3           None.
            =========== =================================================================================
    
    * - gctl.sqpsolvemtControlProc
      - function pointer, pointer to a function that updates optimization settings by setting the :class:`sqpsolvemtControl` structure members.
    
    * - gctl.cmlmtControlProc
      - function pointer, pointer to a function that updates optimization settings by setting the :class:`cmlmtControl` structure members.
    
    * - gctl.start
      - PV structure, estimation starting values.
