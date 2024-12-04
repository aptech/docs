.. list-table::
   :widths: auto

    * - vmc.rho
      - scalar, number of cointegrating relations. Set to -1 to have GAUSS estimate this value. Default = 0.
    * - vmc.indEquations
      - KxL matrix of zeros and ones. Used to set zero restrictions on the *x* variables to be estimated. Used only if the number of equations, vmc.L, is greater than one. Elements set to one indicate the coefficients to be estimated. If vmc.L = 1, all coefficients will be estimated. If vmc.L > 1 and vmc.indEquations is set to a missing value (the default), all coefficients will be estimated.
    * - vmc.lags
      - scalar, number of lags over which ACF and Diagnostics are calculated. Default = 12.
    * - vmc.start
      - Instance of a PV structure containing starting values. See `VES-Starting Values <VES.7.2-StartingValues.htm>`__ for an example.
    * - vmc.nodet
      - scalar. Set vmc.nodet = 1 to suppress the constant term from the fitted regression and include it in the co-integrating regression; otherwise, set vmc.nodet = 0. Default = 0.
    * - vmc.nwtrunc
      - scalar, the number of autocorrelations to use in calculating the Newey-West correction. If vmc.nwtrunc = 0, GAUSS will use a truncation lag given by Newey and West, vmc.nwtrunc :math:`= 4(T/100)^{2/9}`.
    * - vmc.ctl
      - An instance of an sqpsolvemtControl structure.

        .. list-table::
           :widths: auto

            * - vmc.ctl.covType
              - scalar, if 2, QML standard errors are computed, if 0, none; otherwise Wald-type.
            * - vmc.ctl.printIters
            - scalar, iteration information printed every swc.ctl.printIters-th iteration.

             See documentation for sqpsolvemtControl for further information regarding members of this structure.

    * - vmc.olsqtol
      - scalar, the tolerance used in determining if diagonal elements are approaching zero in olsqrmt. Default = 1e-14.
    * - vmc.output
      - scalar, if nonzero, results are printed to screen. Default = 1.
    * - vmc.row
      - scalar. Specifies how many rows of the dataset are to be read per iteration of the read loop. By default, the number of rows to be read is calculated by ecmFit.
    * - vmc.scale
      - scalar or an Lx1 vector, scales for the time series. If scalar, all series are multiplied by the value. If an Lx1 vector, each series is multiplied by the corresponding element of vmc.scale. Defa ult = 4/standard deviation (found to be best by e xperimentation).
    * - vmc.setConstraints
      - scalar, set to a nonzero value to impose stationarity and invertibility by constraining roots of the AR and MA characteristic equations to be outside the unit circle. Set to zero to estimate an unconstrained model. Default = 1.

     