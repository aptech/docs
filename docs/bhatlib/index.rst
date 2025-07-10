BHATLIB Library 
=======================
 The GAUSS BHATLIB provides pre-built support for the flexible estimation of multinomial probit, multivariate ordered-response, and multiple discrete-continuous
models. It also provides a fulle suites of efficient matrix operations and gradient-enabled routines for multivariate distribution evaluation, including Bhat’s (2018) analytic approximation to the multivariate normal cumulative distribution function. These additional tools, in conjunction with GAUSS optimization libraries, support the estimation of a wide range of advanced econometric models.

The library is designed to be flexible and efficient, allowing users to easily estimate complex models with large datasets. It includes a variety of procedures for model estimation, diagnostics, and forecasting, making it a powerful tool for econometric analysis.

Installation
--------------
The BHATLIB library can be directly installed using the `GAUSS Package Manager <https://www.aptech.com/blog/gauss-package-manager-basics/>`_. 

Dependencies
------------------------------
1. Requires `GAUSS/GAUSS Engine v25 <https://www.aptech.com/blog/gauss25/>`_ or higher.
2. Requires `maxlik` library for maximum likelihood estimation. Please `contact Aptech <https://www.aptech.com/contact-us/>` directly to purchase this library

Citation 
------------------------------
If you use the BHATLIB library in your research, please cite the following paper:


Modeling Procedures
------------------------------
The BHATLIB library provides a wide range of procedures for estimating various econometric models. Below is a summary of the key procedures available in the library:
========================== =====================================================================================================================
:func:`linearmdecvfit`       Estimates parameters for the Multiple Discrete-Continuous Extreme Value (MDCEV) model using linear utility for the outside good. Supports input data and specification strings for consumption quantities and explanatory variables.
:func:`mnpfit`           Estimates the Multinomial Probit (MNP) model using analytic gradients and a variety of analytic approximation methods for the multivariate cumulative normal distribution, supporting mixture-of-normals random coefficients and flexible covariance restrictions.
:func:`morpfit`            Estimates a multivariate ordered response probit (MORP) model using flexible correlation structures and efficient maximum likelihood estimation.
:func:`morpATEFit`         Estimates a multivariate ordered response probit (MORP) model with average treatment effects (ATE) using flexible correlation structures and efficient maximum likelihood estimation.`
========================== =====================================================================================================================


Further Reading
-----------------

.. toctree::
    :maxdepth: 2
    :hidden:
    :caption: Constrained Maximum Likelihood 

    user-guide
    command-reference
    bhatlib-examples



