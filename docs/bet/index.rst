Bayesian Estimation Tools (BET)
=========================================
A suite of tools for bayesian estimation and analysis of a pre-packaged models, including univariate and multivariate linear models, autoregressive models, structural VAR models, and dynamic factor models, in **GAUSS**.

Description
----------------
The **Bayesian Estimation Tools** package provides a suite of tools for estimation and analysis of a number of pre-packaged models. The internal Bayesian models provide quickly accessible, full-stage modeling including data generation, estimation, and post-estimation analysis. Modeling flexibility is provided through control structures for setting modeling parameters, such as burn-in periods, total iterations and others.


Installation
--------------
Please `contact us <https://www.aptech.com/contact-us>`_ with to request pricing and installation information.

If you already own **BET** , you can use the `GAUSS Package Manager <https://www.aptech.com/blog/gauss-package-manager-basics/>`_ to install **BET**.

Key Features
------------------------------

Data generation tools for building hypothetical data sets
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

* Univariate and multivariate linear models
* Autoregressive error terms (AR)
* Hierarchical Bayes (HB)
* Probit and logit data

Supported models for Markov Chain Monte Carlo (MCMC) Estimation
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

* Univariate and multivariate linear models
* Autoregressive error terms (AR)
* Hierarchical Bayes (HB)
* Probit model
* Dynamic two-factor model
* Structural vector autoregressive (SVAR)

Flexible, user defined MCMC estimation parameters including
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

* Number of saved iterations
* Skipped iterations
* Burn-in iterations
* Total number of iterations
* Inclusion of intercept
* Optional graph and results output
* Elective maximum likelihood estimation (MLE) initialization

Thorough computations including
+++++++++++++++++++++++++++++++

* Draws for all parameters at each iteration
* Posterior mean of parameters
* Posterior standard deviation of parameters
* Predicted variable values and residuals
* Correlation matrix between observed and predicted data
* PDF values and corresponding PDF graphs
* Log-likelihood values (when applicable)

.. toctree::
    :maxdepth: 2
    :hidden:
    :caption: Bayesian Estimation Tools

    command-reference
    bet-examples