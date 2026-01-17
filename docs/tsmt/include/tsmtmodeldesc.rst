.. list-table::
   :widths: auto

   * - tsmtDesc.depvar
     - Kx1 string array, names of endogenous variables.
   * - tsmtDesc.indvars
     - Mx1 string array, names of exogenous variables.
   * - tsmtDesc.timespan
     - 2x1 string array, range of the time series. Available if date vector is passed as part of a dataframe input.
   * - tsmtDesc.ncases
     - Scalar, number of observations.
   * - tsmtDesc.df
     - Scalar, degrees of freedom.
   * - tsmtDesc.model_name
     - String, model name.