.. list-table::
   :widths: auto

   * - fc.mean
     - hx1 vector, forecast of *y* for each period: *mu*, plus the AR terms
       (with earlier forecasts in place of unseen values of *y*), plus
       *x_future* times the regressor coefficients.

   * - fc.variance
     - hx1 vector, conditional variance of the shock in period T+j given the
       data up to T, :math:`\sigma^2_{T+j|T}`.

   * - fc.volatility
     - hx1 vector, square root of *fc.variance*.

   * - fc.total_variance
     - hx1 vector, running sum of *fc.variance*: row j is
       *variance[1]* + ... + *variance[j]*, so row h is the variance of the sum
       of the next h shocks.

   * - fc.y_error_variance
     - hx1 vector, variance of the forecast error of *y*. With AR terms it
       adds the earlier shocks that the AR part carries forward, so it is at
       least *fc.variance*; without AR terms it equals *fc.variance*.

   * - fc.forecast_dates
     - hx1 vector, dates of periods T+1 to T+h when the fit has dates,
       otherwise 1 to h.

   * - fc.freq
     - String, step of *forecast_dates*: ``"annual"``, ``"quarterly"``,
       ``"monthly"``, ``"weekly"``, ``"daily"`` or ``"weekdays"`` (Monday to
       Friday, no holidays); empty when *forecast_dates* are 1 to h.

   * - fc.h
     - Scalar, forecast horizon.

   * - fc.model
     - String, the fitted model, for example ``"GARCH(1,0,1), constant mean, normal errors"``.

   * - fc.status
     - Scalar, 0 when computed, 2 when computed from a fit that did not
       converge; any other value is a refused forecast (``on_error="return"``
       only).

   * - fc.status_message
     - String, empty when *status* is 0; otherwise the warning or refusal message.

   * - fc.warning_message
     - String, empty or the warnings, one per line (AR part not stationary;
       persistence within 1e-6 of 1). Warnings do not change *status*.
