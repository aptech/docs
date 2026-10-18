Getting Started with State Space Modeling in GAUSS
===================================================
This page provides a basic overview of how to implement custom state space models with the GAUSS State Space library (``sslib``). It covers:

* Installation and library dependencies.
* Data loading.
* The state space representation used by the library.
* Specifying and estimating a custom model with :func:`ssFit`.
* Fine tuning the estimation.
* Post-estimation impulse response functions, forecasting and smoothing.
* Time-varying-parameter models and the pre-built models.

Installation
-----------------------------------------------------------
The GAUSS state space library can be installed and updated using the `GAUSS package manager <https://www.aptech.com/blog/gauss-package-manager-basics/>`_. More information about installing the GAUSS package manager is available in our blog, `Installing the GAUSS Package Manager <https://www.aptech.com/blog/installing-gauss-package-manager/>`_.

The state space library requires:

1.  A working copy of **GAUSS 26.1.4+**. Version 2.0.0 and later of ``sslib`` use typed
    structure returns and keyword arguments, both of which require GAUSS 26.1.4.
    (Version 1.0.0 remains the **GAUSS 22+** compatible release -- stay on it if
    you need to support GAUSS 22-26.0.)
2.  The `Constrained Maximum Likelihood MT library <https://store.aptech.com/gauss-applications-category/constrained-maximum-likelihood-mt.html>`_ for GAUSS.
3.  The `Time Series MT library <https://store.aptech.com/gauss-applications-category/time-series-mt.html>`_ for GAUSS.

Before using the functions in ``sslib`` you will need to load the ``sslib`` library, along with the ``cmlmt`` and ``tsmt`` libraries. This can be done in a number of ways:

* Navigate to the library tool view window and click the small wrench located next to the ``sslib`` library. Select ``Load Library``.
* Enter ``library sslib, cmlmt, tsmt`` in the program input/output window.
* Put the line ``library sslib, cmlmt, tsmt;`` at the beginning of your program files.

It is good practice to begin your state space program files with the following statements:

::

  new;
  library sslib, cmlmt, tsmt;

Data loading
--------------------
The preferred method for loading data is the :func:`loadd` procedure. The :func:`loadd` function allows you to load data from:

* Excel (XLS, XLSX)
* CSV or other delimited text files.
* Stata (DTA), SAS (SAS7BDAT), SPSS or GAUSS Datasets (DAT).
* GAUSS Matrix files (FMT), or HDF5 datasets.

The :func:`loadd` function uses two inputs:

* The filename.
* An optional `formula string <https://docs.aptech.com/gauss/data-management/programmatic-import.html#gauss-formula-string-basics>`_ selecting the variables to load.

::

    // Create file name with full path
    dataset = getGAUSSHome("examples/detroit.dta");

    // Load two specific variables from the file
    detroit = loadd(dataset, "unemployment + hourly_earn");

The variable name can be used to directly reference individual variables within a loaded `dataframe <https://www.aptech.com/blog/what-is-a-gauss-dataframe-and-why-should-you-care/>`_:

::

  y = detroit[., "unemployment"];

For more information on data loading, cleaning and management in GAUSS see our `GAUSS Data Management Guide <https://docs.aptech.com/gauss/data-management.html>`_.

State Space Model Specification
---------------------------------------------------
The ``sslib`` library uses the state space representation of a linear model written as

.. math:: y_t = d + Z\alpha_t + \epsilon_t

.. math:: \alpha_{t+1} = c + T\alpha_t + R\eta_t

where

.. math:: \epsilon_t \sim N(0, H)

.. math:: \eta_t \sim N(0, Q)

and

+--------------------+---------------------------+--------------------------+-------------------------+
| Object             | Description               | Dimension                | ``ssModel`` member      |
+====================+===========================+==========================+=========================+
| :math:`y_t`        | Observed data.            | :math:`p \times 1`       |                         |
+--------------------+---------------------------+--------------------------+-------------------------+
| :math:`\alpha_t`   | Unobserved state.         | :math:`m \times 1`       |                         |
+--------------------+---------------------------+--------------------------+-------------------------+
| :math:`d`          | Observation intercept.    | :math:`p \times 1`       | ``d``                   |
+--------------------+---------------------------+--------------------------+-------------------------+
| :math:`Z`          | Design matrix.            | :math:`p \times m`       | ``Z``                   |
+--------------------+---------------------------+--------------------------+-------------------------+
| :math:`H`          | Observation disturbance   | :math:`p \times p`       | ``H``                   |
|                    | covariance matrix.        |                          |                         |
+--------------------+---------------------------+--------------------------+-------------------------+
| :math:`c`          | State intercept.          | :math:`m \times 1`       | ``c``                   |
+--------------------+---------------------------+--------------------------+-------------------------+
| :math:`T`          | Transition matrix.        | :math:`m \times m`       | ``T``                   |
+--------------------+---------------------------+--------------------------+-------------------------+
| :math:`R`          | Selection matrix.         | :math:`m \times r`       | ``R``                   |
+--------------------+---------------------------+--------------------------+-------------------------+
| :math:`\eta_t`     | State disturbance.        | :math:`r \times 1`       |                         |
+--------------------+---------------------------+--------------------------+-------------------------+
| :math:`Q`          | State disturbance         | :math:`r \times r`       | ``Q``                   |
|                    | covariance matrix.        |                          |                         |
+--------------------+---------------------------+--------------------------+-------------------------+

In the library, :math:`p` is called ``k_endog`` (the number of observed series), :math:`m` is ``k_states`` (the number of states) and :math:`r` is ``k_posdef`` (the dimension of the state disturbance).

:func:`ssFit` estimates models in which every system matrix is constant over time. Models in which some system matrices change from period to period (:math:`Z_t`, :math:`T_t`, and so on) are estimated with :func:`ssFitTVP` instead -- see `Time-varying-parameter models`_ below.

State space representation is a flexible platform for modeling and supports a variety of `time series models <https://www.aptech.com/blog/getting-started-with-time-series-in-gauss/>`_ including ARIMA, SARIMA, VAR, unobserved components, and dynamic factor models.

Example: AR(2)
+++++++++++++++++++++
Consider the :math:`AR(2)` model

.. math:: y_t = \phi_1 y_{t-1} + \phi_2 y_{t-2} + e_t

.. math:: e_t \sim N(0, \sigma^2)

There are a number of ways to transform this model to state space representation. Consider, for example, letting :math:`\alpha_t = (y_t, y_{t-1})'`.

**Transition Equation:**

.. math:: \alpha_{t+1} = \begin{bmatrix} \phi_1 & \phi_2\\ 1 & 0\end{bmatrix} \alpha_t + \begin{bmatrix} 1\\ 0 \end{bmatrix} \eta_t

**Measurement Equation:**

.. math:: y_t = \begin{bmatrix} 1 & 0 \end{bmatrix} \alpha_t

In this representation :math:`p = 1`, :math:`m = 2`, :math:`r = 1`, and the system matrices are:

+--------------------+------------------------------------------------------------------+
| Object             | Specification                                                    |
+====================+==================================================================+
| :math:`d`          | 0                                                                |
+--------------------+------------------------------------------------------------------+
| :math:`Z`          | :math:`\begin{bmatrix} 1 & 0 \end{bmatrix}`                      |
+--------------------+------------------------------------------------------------------+
| :math:`H`          | 0                                                                |
+--------------------+------------------------------------------------------------------+
| :math:`c`          | 0                                                                |
+--------------------+------------------------------------------------------------------+
| :math:`T`          | :math:`\begin{bmatrix} \phi_1 & \phi_2\\ 1 & 0 \end{bmatrix}`    |
+--------------------+------------------------------------------------------------------+
| :math:`R`          | :math:`\begin{bmatrix} 1 \\ 0 \end{bmatrix}`                     |
+--------------------+------------------------------------------------------------------+
| :math:`Q`          | :math:`\sigma^2`                                                 |
+--------------------+------------------------------------------------------------------+

In this model the unknown parameters are :math:`\phi_1`, :math:`\phi_2`, and :math:`\sigma^2`.

Estimation of State Space Models
---------------------------------------------------
The ``sslib`` library relies on two tools for estimating state space models, the Kalman filter and maximum likelihood estimation.

+--------------------+------------------------------------------------------------------+
| Tool               | Purpose                                                          |
+====================+==================================================================+
| Kalman filter      | The Kalman filter uses recursive iteration to estimate the       |
|                    | unknown state.                                                   |
+--------------------+------------------------------------------------------------------+
| Maximum likelihood | Uses the likelihood function generated from the Kalman filter    |
|                    | to estimate the unknown parameters.                              |
+--------------------+------------------------------------------------------------------+

You do not need to call either tool directly when using the GAUSS state space framework: :func:`ssFit` runs the Kalman filter inside a CMLMT maximum likelihood estimation. For more information about either tool please see the following:

1. `Beginner's Guide To Maximum Likelihood Estimation <https://www.aptech.com/blog/beginners-guide-to-maximum-likelihood-estimation-in-gauss/>`_
2. `Maximum Likelihood Estimation in GAUSS <https://www.aptech.com/blog/maximum-likelihood-estimation-in-gauss/>`_

:func:`ssKalmanFilter` is also available for running the Kalman filter on a model whose parameters are already known.

State Space Models in GAUSS
---------------------------------------------------
The ``sslib`` library contains a suite of tools that allows you to specify, estimate, diagnose, and perform post-estimation forecasts. The primary procedure for estimating custom state space models is the :func:`ssFit` procedure.

Estimating a custom model takes six steps:

1. Load the required libraries and data.
2. Set up the parameter vector and start values.
3. Set up the control structure.
4. Set the fixed system matrices and parameter constraints.
5. Write a procedure that places the parameters in the system matrices.
6. Call :func:`ssFit`.

The steps below estimate the :math:`AR(2)` example above.

Step One: Load the required libraries and data
+++++++++++++++++++++++++++++++++++++++++++++++++
::

  new;
  library sslib, cmlmt, tsmt;

  // Simulated AR(2) data shipped with TSMT
  fname = getGAUSSHome("pkgs/tsmt/examples/enders_sim2.dat");
  y = loadd(fname, "ar2");

Step Two: Set up the parameter vector and start values
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
A custom state space model needs a column vector containing a starting value for each unknown parameter. In the :math:`AR(2)` example there are three unknown parameters, :math:`\phi_1`, :math:`\phi_2`, and :math:`\sigma^2`.

::

  // Create a dataframe
  param_vec_st = asDF(zeros(3, 1), "param");

  // Starting values for phi_1, phi_2 and sigma2
  param_vec_st[1] = -0.322;
  param_vec_st[2] = 0.433;
  param_vec_st[3] = 0.0025;

Step Three: Set up the control structure
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
The :class:`ssControl` structure is used to:

1. Specify the state space system matrices.
2. Implement stationarity and non-negativity constraints on parameters.
3. Control modeling features such as the Kalman filter initialization.
4. Specify advanced maximum likelihood controls.

The model dimensions are defined by three variables:

+--------------------+------------------------------------------------------------------+
| Variable           | Description                                                      |
+====================+==================================================================+
| ``k_endog``        | Number of endogenous (observed) variables, :math:`p`.            |
+--------------------+------------------------------------------------------------------+
| ``k_states``       | Number of state variables, :math:`m`.                            |
+--------------------+------------------------------------------------------------------+
| ``k_posdef``       | Dimension of the state disturbance, :math:`r`. Optional; it      |
|                    | defaults to ``k_states``.                                        |
+--------------------+------------------------------------------------------------------+

:func:`ssControlCreate` returns an :class:`ssControl` structure filled with default values, with every system matrix in ``ssctl.ssm`` set to zeros of the correct size. Because :func:`ssControlCreate` declares its return type, no preceding ``struct ssControl ssctl;`` declaration is needed:

::

  // Model dimensions
  k_endog = 1;
  k_states = 2;
  k_posdef = 1;

  // Control structure with default values
  ssctl = ssControlCreate(k_states, k_endog, k_posdef);

Step Four: Set the fixed system matrices and constraints
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
System matrices that do not depend on any parameter are set once, directly on ``ssctl.ssm``. In the :math:`AR(2)` example, :math:`Z` and :math:`R` are fixed; :math:`d`, :math:`H` and :math:`c` are zero, which is already their default:

::

  // Fixed system matrices
  ssctl.ssm.Z = { 1 0 };
  ssctl.ssm.R = { 1, 0 };

  // Parameter names used in the printed output
  ssctl.param_names = "phi1"$|"phi2"$|"sigma2";

Parameters can be constrained by listing their positions in the parameter vector. ``ssctl.stationary_vars`` constrains the listed parameters to be stationary, and ``ssctl.positive_vars`` constrains the listed parameters to be positive:

::

  // phi1 and phi2 stationary, sigma2 positive
  ssctl.stationary_vars = 1|2;
  ssctl.positive_vars = 3;

Step Five: Write the update procedure
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
The update procedure places the current parameter values in the system matrices that depend on them. It always takes two inputs: a pointer to an :class:`ssModel` structure and the parameter vector. Members of the structure are set with the arrow (``->``) notation:

::

  proc (0) = updateSSModel(struct ssModel *ssmod, param);
      ssmod->T = param[1 2]'|(1~0);
      ssmod->Q = param[3];
  endp;

Step Six: Estimate the model
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
:func:`ssFit` takes a pointer to the update procedure, the starting values, the data and the control structure. It estimates the parameters, computes the parameter covariance, residual diagnostics and model summary statistics, and prints the results:

::

  sOut = ssFit(&updateSSModel, param_vec_st, y, ssctl);

The returned :class:`ssOut` structure holds the estimates (``sOut.final_params``), the system matrices at the estimates (``sOut.ssmFinal``), the Kalman filter results (``sOut.kfResults``), and the diagnostics. See :func:`ssFit` for the full list of members.

Fine tuning
---------------------------------------------------
Several members of the :class:`ssControl` structure change how the model is estimated. The most commonly used are:

+------------------------------+--------------------------------------------------------------+
| Member                       | Purpose                                                      |
+==============================+==============================================================+
| ``ssctl.init``               | Kalman filter initialization: ``"diffuse"`` (the default,    |
|                              | exact diffuse initialization), ``"stationary"`` or           |
|                              | ``"mixed"``.                                                 |
+------------------------------+--------------------------------------------------------------+
| ``ssctl.stationary_states``  | With ``ssctl.init = "mixed"``, the states initialized at     |
|                              | their stationary distribution.                               |
+------------------------------+--------------------------------------------------------------+
| ``ssctl.gradproc``           | Pointer to a procedure supplying an analytic gradient.       |
+------------------------------+--------------------------------------------------------------+
| ``ssctl.ctl``                | An instance of a :class:`cmlmtControl` structure, passed to  |
|                              | CMLMT to control the maximum likelihood estimation.          |
+------------------------------+--------------------------------------------------------------+

See :func:`ssFit` for details of each.

Post-estimation
---------------------------------------------------
After estimation, the filled :class:`ssOut` structure can be used to compute impulse responses, forecasts with their standard errors, and smoothed states:

::

  // Impulse responses of y to the first state disturbance,
  // over 20 periods
  irf = ssIRF(sOut.ssmFinal, 20, 1);

  // 20 out-of-sample forecasts (the default) and their standard errors
  forecasts = ssPredict(sOut, y);
  se = ssPredictSE(sOut, y);

  // Forecasts through 8 periods past the end of the sample
  forecasts8 = ssPredict(sOut, y, end_pred=rows(y)+8);

  // Smoothed states, reusing the Kalman filter results from ssFit
  { a_smooth, p_smooth } = ssKalmanSmooth(sOut.ssmFinal, sOut.kfResults);

See :func:`ssIRF`, :func:`ssPredict`, :func:`ssPredictSE` and :func:`ssKalmanSmooth` for details.

Time-varying-parameter models
---------------------------------------------------
:func:`ssFitTVP` estimates models in which some system matrices change over time. It follows the same steps as :func:`ssFit`, with three differences:

* Pass the number of observations as the fourth argument to :func:`ssControlCreate`, ``ssControlCreate(k_states, k_endog, k_posdef, nobs)``. This allocates ``ssctl.tvp``, a :class:`tvpModel` structure, instead of ``ssctl.ssm``.
* Each system matrix in ``ssctl.tvp`` is an array with one page per period. A scalar is applied to every period automatically; any other matrix must be supplied as a full nobs-page array.
* The update procedure takes a pointer to a :class:`tvpModel` instead of an :class:`ssModel`.

Post-estimation uses :func:`ssIRFTVP`, :func:`ssPredictTVP`, :func:`ssPredictSETVP` and :func:`ssKalmanSmoothTVP`. See :func:`ssFitTVP` for a complete example.

Pre-built models
---------------------------------------------------
Several common models can be estimated without writing an update procedure:

* :func:`ssARIMA` and :func:`ssSARIMA` estimate ARIMA and seasonal ARIMA models.
* :func:`ssStructuralTS` estimates structural time series (unobserved-components) models, and :func:`ssStructuralComponents` decomposes the fit into its trend, seasonal, cycle and regression components.
* :func:`ssDFM` estimates dynamic factor models for nowcasting monthly and quarterly series, and :func:`ssDFMPredict` forecasts from them.

For example:

::

  // Monthly airline passengers, 1949-1960, in logs
  fname = getGAUSSHome("pkgs/sslib/examples/airline.dat");
  passengers_ln = loadd(fname, "ln(passengers)");

  // Local linear trend with a monthly seasonal component
  sOut_sts = ssStructuralTS(passengers_ln, trend="trend", seasonal_period=12);
