cwTest
======

Purpose
-------
Clark-West test for comparing nested forecast models.

Format
------

.. function:: t = cwTest(e_r, e_u, fc_r, fc_u)
              t = cwTest(e_r, e_u, fc_r, fc_u, quiet=1)

   :param e_r: forecast errors from the restricted (simpler) model.
   :type e_r: Nx1 vector

   :param e_u: forecast errors from the unrestricted (larger) model.
   :type e_u: Nx1 vector

   :param fc_r: point forecasts from the restricted model.
   :type fc_r: Nx1 vector

   :param fc_u: point forecasts from the unrestricted model.
   :type fc_u: Nx1 vector

   :param quiet: Optional keyword, set to 1 to suppress output. Default = 0.
   :type quiet: scalar

   :return t: An instance of a :class:`testResult` structure.
   :rtype t: struct

Examples
--------

::

    new;
    library timeseries;

    // Restricted: AR(1), Unrestricted: VAR(4)
    t = cwTest(e_ar1, e_var4, fc_ar1, fc_var4);
    print "CW statistic:" t.statistic;
    print "p-value:" t.p_value;

Remarks
-------

The standard Diebold-Mariano test is biased in favor of the restricted model
when models are nested (Clark & West 2007). This test adjusts for the noise
in the unrestricted model's parameter estimates.

Model
-----

The Clark-West adjusted statistic adds a correction term for the noise in the
unrestricted model's forecasts:

.. math::

   \tilde{d}_t = (e_{R,t})^2 - \left[(e_{U,t})^2 - (\hat{y}_{R,t} - \hat{y}_{U,t})^2\right]

where :math:`e_R` and :math:`e_U` are forecast errors from the restricted and unrestricted
models, and the squared difference in forecasts corrects for the bias. The test statistic
is the t-statistic of :math:`\bar{\tilde{d}}` with HAC standard errors.


References
----------

- Clark, T.E. and K.D. West (2007). "Approximately normal tests for equal predictive accuracy in nested models." *Journal of Econometrics*, 138(1), 291-311.


Library
-------
timeseries

Source
------
scoring.src

.. seealso:: Functions :func:`dmTest`, :func:`mcsTest`
