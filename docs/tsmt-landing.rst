Time Series MT (TSMT)
==============================================

Description
----------------
Provides tools for comprehensive treatment of time series models, including model diagnostics, MLE and state-space estimation, and forecasts. Time Series MT also includes tools for managing panel series data and estimating and diagnosing panel series models, including random effects and fixed effects.

Installation
--------------
Please visit our `product page <https://store.aptech.com/gauss-applications-category/time-series-mt.html>`_ to contact us about obtaining TSMT.

Commands
------------------------------
Univariate Time Series Models
+++++++++++++++++++++++++++++++
Conditional mean models
^^^^^^^^^^^^^^^^^^^^^^^^
========================== ================================================================================================================================================
:func:`arimaFit`           Estimates autoregressive integrated moving average models.
:func:`sarimaSS`           Estimates seasonal autoregressive integrated moving average models.
========================== ================================================================================================================================================

Conditional variance models
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
========================== ================================================================================================================================================
:func:`garchFit`           Estimates parameters of a generalized autoregressive conditional heteroskedasticity model.
:func:`igarchFit`          Estimates parameters of an integrated generalized autoregressive conditional heteroskedasticity model.
:func:`garchjrFit`         Estimates parameters of an asymmetric generalized autoregressive conditional heteroskedasticity model.
:func:`garchMFit`          Estimates parameters of an integrated generalized autoregressive conditional heteroskedasticity in mean model.
========================== ================================================================================================================================================

Multivariate Time Series Models
++++++++++++++++++++++++++++++++
Conditional mean models
^^^^^^^^^^^^^^^^^^^^^^^^
========================== ================================================================================================================================================
:func:`varmaFit`           Estimates parameters of a vector autoregressive integrated moving average models.
:func:`svarmamt`           Estimates parameters of a seasonal vector autoregressive integrated moving average models.
:func:`ecmFit`             Estimates parameters of an error correction model.
========================== ================================================================================================================================================

Panel data and other models
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
========================== ================================================================================================================================================
:func:`tscsFit`            Estimates panel data fixed effects, pooled OLS, and random effects models.
:func:`lsdvFit`            Computes bias-corrected coefficients and covariance matrix of coefficients of the Least Squares Dummy Variable model for unbalanced panel data.
:func:`kalmanFilter`       Data filtering algorithm.
========================== ================================================================================================================================================

Nonlinear Time Series Model
++++++++++++++++++++++++++++++++
========================== ================================================================================================================================================
:func:`switchFit`          Estimates a switching time series model.
:func:`sbreak`             Estimates the m-break structural break model.
:func:`tarTest`            Estimates a p-order threshold autoregression and tests the hypothesis of a linear autoregression.
========================== ================================================================================================================================================

Further Reading
-----------------

* `Introduction to the Fundamentals of Time Series Data and Analysis <https://www.aptech.com/blog/introduction-to-the-fundamentals-of-time-series-data-and-analysis/>`_
* `Introduction to the Fundamentals of Vector autoregressive Models <https://www.aptech.com/blog/introduction-to-the-fundamentals-of-vector-autoregressive-models/>`_
* `The Structural VAR Model at Work: Analyzing Monetary Policy <https://www.aptech.com/blog/the-structural-var-model-at-work-analyzing-monetary-policy/>`_
* `How to Conduct Unit Root Tests in GAUSS <https://www.aptech.com/blog/how-to-conduct-unit-root-tests-in-gauss/>`_
* `A Guide to Conducting Cointegration Tests <https://www.aptech.com/blog/a-guide-to-conducting-cointegration-tests/>`_
* `Unit Root Tests with Structural Breaks <https://www.aptech.com/blog/unit-root-tests-with-structural-breaks/>`_
* `Introduction to Structural Breaks <https://www.aptech.com/structural-breaks/>`_
