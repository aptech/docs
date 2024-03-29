GAUSS State-Space Modeling (SSLIB)
==============================================

Description
----------------
This package provides tools for estimating and evaluating time-invariant state-space models. In addition to providing the tools for custom state space models, it provides pre-built functions for state-space modeling of:

* ARIMA packages
* SARIMA packages

Installation
--------------
The GAUSS State Space library can be installed and updated directly in GAUSS using the `GAUSS Package Manager <https://www.aptech.com/blog/gauss-package-manager-basics/>`_. It requires a working copy of GAUSS 22+.

  For more information on installing the GAUSS Package Manager please see our video blog, `Installing the GAUSS Package Manager <https://www.aptech.com/blog/installing-gauss-package-manager/>`_.

Dependencies
--------------
This library requires the installation of the following GAUSS libraries:

* `Time Series MT <https://store.aptech.com/gauss-applications-category/time-series-mt.html>`_
* `Constrained Maximum Likelihood MT <https://store.aptech.com/gauss-applications-category/constrained-maximum-likelihood-mt.html>`_

Usage
-------------
Estimating custom state-space models using the `sslib` library requires:

* Loading data
* Setting up the state-space representation
* Calling the estimation function `ssFit`

A complete guide to getting started with the state-space estimation in GAUSS is available `here <./getting-started-with-state-space-gauss.rst>`_.

Commands
------------------------------

Estimating custom models
+++++++++++++++++++++++++++++++

========================== ===========================================================================================================
:func:`ssFit`              Estimates parameters of a state-space model using Kalman filtering and maximum likelihood estimation.
:func:`ssIRF`              Computes the impulse response functions based on the final estimated parameters.
:func:`ssPredict`          Computes in sample predictions or out-of-sample forecasts based on the final estimated parameters.
:func:`ssKalmanSmooth`		 Performs the Rauch-Tung-Striebel backward recursion smoother for state variables and state covariances.
========================== ===========================================================================================================

Pre-built models
+++++++++++++++++++++++++++

========================== =================================================================================================================================================================
:func:`ssARIMA`            Estimates parameters of a state-space model ARIMA(p, d, q) model using Kalman filtering and maximum likelihood estimation.
:func:`ssSARIMA`           Estimates parameters of a state-space model SARIMA(p, d, q)(p_s, d_s, q_s) model using Kalman filtering and maximum likelihood estimation.
========================== =================================================================================================================================================================


Model evaluation
+++++++++++++++++++++

================================  =======================================================================================================================================================
:func:`ssgetAIC`                  Computes Akaike's information criterion from loglikelihood.
:func:`ssgetAICC`                 Computes the corrected Akaike's information criterion from loglikelihood.
:func:`ssgetBIC`                  Computes the Schwarz’ Bayesian information criterion from loglikelihood.
:func:`ssgetHQIC`                 Computes the Hannan–Quinn information criterion from loglikelihood.
:func:`ssHeteroskedasticityTest`  Tests the null hypothesis of no heteroskedasticity by comparing the sum-of-squares of the first third of the sample to the sum-of-squares of last third of the sample. Analogous to a Goldfeld-Quandt test.
:func:`ssJarqueBera`              Performs the Jarque-Bera goodness-of-fit test on model residuals.
:func:`ssLjungBox`                Computes the Ljung-Box test for autocorrelation.
:func:`ssSkewness`                Computes the sample skewness.
:func:`ssKurtosis`                Compute the sample kurtosis.
================================  =======================================================================================================================================================



Further Reading
-----------------


.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: State-space modeling

    ssarima
    sscontrolcreate
    ssfit
    ssgetaic
    ssgetaicc
    ssgetbic
    ssgethqic
    ssheteroskedasticitytest
    ssirf
    ssjarquebera
    sskalmansmooth
    sskurtosis
    ssljungbox
    sspredict
    sssarima
    ssskewness
