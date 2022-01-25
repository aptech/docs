
Estimation methods
===========================


Standard estimation methods
-------------------------------

These functions perform paramter estimation, diagnostics and print reports.

=========================          ====================================================
:doc:`../glm`                      Solves the generalized linear model problems.
:doc:`../gmmfit`                   Estimate parameters using generalized method of moments.
:doc:`../gmmfitiv`                 Estimate instrumental variables model using the generalized method of moments.
:doc:`../olsmt`                    Computes a least squares regression.
:doc:`../quantilefit`              Perform linear quantile regression.
:doc:`../quantilefitloc`           Perform local linear or quadratic quantile regression.
=========================          ====================================================


Standard error methods
-----------------------

====================          ====================================================
:doc:`../clusterse`           Computes the White cluster-robust standard errors.
:doc:`../robustse`            Computes the Huber-White heteroscedastic robust standard errors. The procedure uses the “sandwich” variance-covariance estimator with a small sample correction of :math:`(n)/(n−1)`.
====================          ====================================================

Lower level estimation
-------------------------

.. note:: Use the slash operator :math:`b = y / X` to compute least-squares estimates.

==================           ====================================================
:doc:`../ldlsol`             Computes the solution to a system of linear equations given a factorized matrix returned by the function :doc:`../ldlp` and one or more right hand sides.
:doc:`../lusol`              Computes the solution of :math:`LUx=b` where :math:`L` and :math:`U` are matrix factors returned by :doc:`../lu`.
:doc:`../olsqr`              Computes OLS coefficients using :math:`QR` decomposition.
:doc:`../olsqr2`             Computes OLS coefficients, residuals, and predicted values using the :math:`QR` decomposition.
:doc:`../solpd`              Solves a set of positive definite linear equations.
==================           ====================================================
