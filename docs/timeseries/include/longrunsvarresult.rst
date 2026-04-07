.. list-table::
   :widths: auto

   * - lr.impact
     - mxm matrix, structural impact matrix :math:`B_0`. Column j gives the contemporaneous effect of structural shock j on all variables.

   * - lr.irf
     - An instance of an :class:`irfResult` structure containing orthogonalized impulse responses identified via long-run restrictions. See :func:`irfCompute` for the :class:`irfResult` layout.

   * - lr.m
     - Scalar, number of endogenous variables.

   * - lr.p
     - Scalar, lag order.

   * - lr.n_ahead
     - Scalar, number of forecast horizons.

   * - lr.var_names
     - Mx1 string array, variable names.
