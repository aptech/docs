
What is GAUSS?
==============

GAUSS is a matrix programming language designed for computationally intensive tasks in statistics, econometrics, and data analysis. Developed by Aptech Systems since 1984, it combines the speed of compiled code with the flexibility of an interpreted environment.

Who Uses GAUSS?
---------------

GAUSS is used by:

- **Central banks** for forecasting, policy analysis, and financial stability research
- **Academic economists** for econometric research and teaching
- **Financial institutions** for risk modeling and quantitative analysis
- **Transportation researchers** for discrete choice modeling
- **Government agencies** for economic forecasting

Why Choose GAUSS?
-----------------

**Purpose-built for econometrics.** Unlike general-purpose languages, GAUSS was designed from the start for matrix mathematics and statistical computing. This means:

- Matrix operations are first-class citizens, not library add-ons
- Statistical functions work the way econometricians expect
- Time series, panel data, and limited dependent variable tools are available out of the box or through specialized add-ons

**Speed.** GAUSS compiles to native code and uses optimized numerical libraries. For computationally intensive work—Monte Carlo simulations, bootstrapping, large-scale optimization—this matters.

**40 years of reliability.** Code written in GAUSS in the 1990s still runs today. When you build research infrastructure in GAUSS, it lasts.

**Interactive and batch modes.** Explore data interactively in the IDE, then run production jobs in batch mode on servers.

What Can You Do with GAUSS?
---------------------------

**Time series analysis:**

- ARIMA, GARCH, VAR/VECM models
- State-space models and Kalman filtering
- Forecasting with multiple methods

**Econometric estimation:**

- OLS, GLS, IV, GMM
- Maximum likelihood estimation
- Bayesian methods (MCMC)

**Panel data:**

- Fixed and random effects
- Dynamic panels
- Clustered standard errors

**Discrete choice:**

- Logit, probit, multinomial models
- Mixed logit with simulation
- Nested logit structures

**General computation:**

- Matrix algebra and linear algebra
- Numerical optimization
- Simulation and Monte Carlo

Core Concepts
-------------

**Everything is a matrix.** In GAUSS, scalars are 1×1 matrices, vectors are Nx1 or 1xN matrices, and multi-dimensional data lives in matrices or dataframes.

**Dataframes** extend matrices with column names, types (numeric, string, date, category), and metadata—similar to dataframes in R or pandas.

**Procedures** are user-defined functions. GAUSS ships with hundreds of built-in procedures; you can write your own or use add-on packages.

**Libraries** group related procedures. Load them with ``library libname;`` to access specialized functionality.

GAUSS vs. Other Tools
---------------------

=============== =============== =============== ===============
Aspect          GAUSS           MATLAB          Stata/EViews
=============== =============== =============== ===============
Primary focus   Econometrics    Engineering     Statistics/Econ
Matrix syntax   Native          Native          Command-based
Speed           Fast            Fast            Moderate
Custom code     Easy            Easy            Limited
Time series     Strong (TSMT)   Moderate        Strong
GUI workflow    IDE + code      IDE + code      GUI-centric
=============== =============== =============== ===============

See our "Coming from..." guides for detailed comparisons on the `GAUSS documentation website <https://docs.aptech.com/gauss/coming-to-gauss/>`__:

- `Introduction to GAUSS for Stata Users <https://docs.aptech.com/gauss/coming-to-gauss/intro-gauss-for-stata-users.html>`__
- `Introduction to GAUSS for EViews Users <https://docs.aptech.com/gauss/coming-to-gauss/intro-gauss-for-eviews-users.html>`__
- `Introduction to GAUSS for MATLAB Users <https://docs.aptech.com/gauss/coming-to-gauss/intro-gauss-for-matlab-users.html>`__
- `Introduction to GAUSS for R Users <https://docs.aptech.com/gauss/coming-to-gauss/intro-gauss-for-r-users.html>`__
- `Introduction to GAUSS for Python Users <https://docs.aptech.com/gauss/coming-to-gauss/intro-gauss-for-python-users.html>`__

Getting Started
---------------

Ready to try GAUSS?

1. :doc:`quickstart` — Run your first GAUSS code in 10 minutes
2. :doc:`running-existing-code` — If you have existing GAUSS code to run
3. :doc:`absolute-basics` — If you're new to programming

.. seealso::

    `Aptech Systems <https://www.aptech.com>`_ — Company website, downloads, support
