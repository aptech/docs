
Estimation methods
===========================


Standard estimation methods
-------------------------------

These functions perform paramter estimation, diagnostics and print reports.

================          ====================================================
:doc:`glm`                Solves the generalized linear model problems.
:doc:`gmmFit`             Estimate parameters using generalized method of moments.
:doc:`gmmFitIV`           Estimate instrumental variables model using the generalized method of moments.
:doc:`olsmt`              Computes a least squares regression.
:doc:`quantileFit`        Perform linear quantile regression.
:doc:`quantileFitLoc`     Perform local linear or quadratic quantile regression.
================          ====================================================


Standard error methods
-----------------------

================          ====================================================
:doc:`clusterSE`          Computes the White cluster-robust standard errors.
:doc:`robustSE`           Computes the Huber-White heteroscedastic robust standard errors. The procedure uses the “sandwich” variance-covariance estimator with a small sample correction of :math:`(n)/(n−1)`.
================          ====================================================

Lower level estimation
-------------------------

================          ====================================================
:doc:`ldlsol`             Computes the solution to a system of linear equations given a factorized matrix returned by the function :doc:`ldlp` and one or more right hand sides.
:doc:`lusol`              Computes the solution of :math:`LUx=b` where L and U are matrix factors returned by :doc:`lu`.
:doc:`olsqr`              Computes OLS coefficients using QR decomposition.
:doc:`olsqr`2             Computes OLS coefficients, residuals, and predicted values using the QR decomposition.
:doc:`solpd`              Solves a set of positive definite linear equations.
================          ====================================================
