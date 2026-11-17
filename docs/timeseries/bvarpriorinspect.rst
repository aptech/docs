bvarPriorInspect
================

Purpose
-------
Inspect the resolved Minnesota coefficient prior before fitting a BVAR.

Format
------

.. function:: info = bvarPriorInspect(y, ctl={}, residual_variances={}, residual_variances_values={})

   :param y: Data, one column per variable. A single date column is excluded from the model.
   :type y: matrix or dataframe

   :param ctl: A :class:`bvarControl` from :func:`bvarControlCreate`. Set *ctl.p* to a positive integer lag order before calling. There is no ``p=`` keyword or implicit lag order. Only this control type or ``{}`` is accepted; omitting it leaves the required lag unset. *ctl.const* must be 0 or 1.
   :type ctl: struct

   :param residual_variances: Optional keyword, ``"ar_p"`` or ``"ar_1"``; overrides the control's residual-variance method and clears inherited variance values. A :func:`bvarChoose` mark is refused.
   :type residual_variances: string

   :param residual_variances_values: Optional keyword, positive residual variances, one per variable. Overrides the method and inherited values. A :func:`bvarChoose` mark is refused.
   :type residual_variances_values: vector

   :return info: A ``bvarPriorInfo`` structure. The main fields are:

       .. list-table::
          :widths: auto

          * - coefficient_prior_mean
            - Kxm matrix of prior coefficient means, with equations in columns.
          * - omega_diag
            - Kx1 vector, diagonal of the coefficient prior row covariance factor.
          * - coefficient_prior_sd_sigma_mean
            - Kxm matrix of coefficient standard deviations with the error covariance fixed at its prior mean.
          * - coefficient_names
            - Kx1 string array of coefficient row labels.
          * - residual_variances, residual_variances_values
            - Resolved method and the mx1 residual-variance vector.

   :rtype info: struct

Examples
--------

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv");
    data = loadd(fname, "date + gdp_growth + inflation + fed_funds");
    struct bvarControl ctl;
    ctl = bvarControlCreate();
    ctl.p = 2;
    // Growth is centered at 0; persistent inflation and the funds rate at 1.
    ctl.lag1_prior_mean = { 0, 1, 1 };
    info = bvarPriorInspect(data, ctl=ctl);
    print info.coefficient_prior_mean;

Remarks
-------

Rows are the constant (when present), lag 1 through lag p in variable order,
then exogenous regressors in *ctl.xreg* column order. The procedure resolves
the base Minnesota prior only; it does not fit a posterior or draw samples.
Sum-of-coefficients and single-unit-root dummy contributions are not included
in these tables. *ctl.n_draws*, *ctl.seed* and *ctl.quiet* do not affect them.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`bvarControlCreate`, :func:`bvarFit`
