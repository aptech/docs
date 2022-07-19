Getting Started with State-Space Modeling in GAUSS
===================================================
This page provides a basic overview of how to implement custom state-space models in GAUSS. It covers everything you need to know to get working with the GAUSS state-space library including:

* Installation and library dependencies.
* Data loading.
* The basics of state-space models.
* Specifying state-space models in GAUSS.
* Fine tuning.
* Post-estimation impulse response functions and forecasting.

Installation
-----------------------------------------------------------
The GAUSS state-space library can be installed and updated using the `GAUSS package manager <https://www.aptech.com/blog/gauss-package-manager-basics/>`_.

	More information about installing the GAUSS package manager is available in our blog, `Installing the GAUSS Package Manager <https://www.aptech.com/blog/installing-gauss-package-manager/>`_.

The state-space library requires:

1.  A working copy of **GAUSS 22+**.
2.  The `Constrained Maximum Likelihood MT library <https://store.aptech.com/gauss-applications-category/constrained-maximum-likelihood-mt.html>`_ for GAUSS.
3.  The `Time Series MT library <https://store.aptech.com/gauss-applications-category/time-series-mt.html>`_ for GAUSS.


In addition, before using the functions created by :class:`sslib` you will need to load the newly created :class:`sslib` library, along with the :class:`cmlmt` and :class:`tsmt`. This can be done in a number of ways:

  *  Navigate to the library tool view window and click the small wrench located next to the :class:`sslib` library. Select `Load Library`.
  *  Enter `library sslib` in the program input/output window.
  *  Put the line `library sslib;` at the beginning of your program files.

It is good practice to begin your state-space program files with the following statements:

::

  new;
  library sslib, tsmt, cmlmt;

Data Loading
--------------------
The preferred method for loading data is the :func:`loadd` procedure. The :func:`loadd` function allows you to load data from:

* Excel (XLS, XLSX)
* CSV or other delimited text files.
* Stata (DTA), SAS (SAS7BDAT), SPSS or GAUSS Datasets (DAT).
* GAUSS Matrix files (FMT), or HDF5 datasets.

The :func:`loadd` function uses two inputs:

* The filename.
* A `formula string <https://docs.aptech.com/gauss/data-management/programmatic-import.html?highlight=formula%20string#gauss-formula-string-basics>`_ .

::

    // Create file name with full path
    dataset = getGAUSSHome() $+ "examples/detroit.sas7bdat";

    // Load two specific variables from the file
    detroit = loadd(dataset, "unemployment + hourly_earn");

The variable name can be used to directly reference individual variables within a loaded `dataframe <https://www.aptech.com/blog/what-is-a-gauss-dataframe-and-why-should-you-care/>`_:

::

  y = detroit[., "unemployment"];


For more information on data loading, cleaning and management in GAUSS see our `GAUSS Data Management Guide <https://docs.aptech.com/gauss/data-management.html>`_.

State-Space Model Specification
---------------------------------------------------
The GAUSS :class:`sslib` library uses the state-space representation of a linear model written as

.. math :: y_t = d + Z\alpha_t + \epsilon_t
.. math :: \alpha_{t+1} = c + T\alpha_t + R\eta_t

where

.. math :: \epsilon_t  \sim N(0, H)
.. math :: \eta_t  \sim N(0, Q)

and

+--------------------+-------------------------+----------------------+
| Object             | Description             | Dimension            |
+====================+=========================+======================+
| :math:`y_t`        | Observed data.          | :math:`p \times 1`   |
+--------------------+-------------------------+----------------------+
| :math:`\alpha_t`   | Unobserved state.       | :math:`m \times 1`   |
+--------------------+-------------------------+----------------------+
| :math:`d`          | Observation intercept.  | :math:`m \times 1`   |
+--------------------+-------------------------+----------------------+
| :math:`Z`          | Design matrix.          | :math:`p \times m`   |
+--------------------+-------------------------+----------------------+
| :math:`H`          | Observation disturbance.| :math:`p \times 1`   |
|                    | covariance matrix.      |                      |
+--------------------+-------------------------+----------------------+
| :math:`c`          | State intercept.        | :math:`m \times 1`   |
+--------------------+-------------------------+----------------------+
| :math:`T`          | Transition matrix.      | :math:`m \times m`   |
+--------------------+-------------------------+----------------------+
| :math:`R`          | Selection matrix.       | :math:`m \times r`   |
+--------------------+-------------------------+----------------------+
| :math:`\eta_t`     | State disturbance       | :math:`r \times 1`   |
+--------------------+-------------------------+----------------------+
| :math:`Q`          | State disturbance       | :math:`r \times r`   |
|                    | covariance matrix.      |                      |
+--------------------+-------------------------+----------------------+

Notice that the current GAUSS :class:`sslib` only supports time-invariant state-space models such that all state-space representation matrices are constant.

state-space representation is a flexible platform for modeling and supports a variety of `time series models <https://www.aptech.com/blog/getting-started-with-time-series-in-gauss/>`_ including ARIMA, SARIMA, VAR, unobserved components, and dynamic factor models.

Example: AR(2)
+++++++++++++++++++++
Consider the :math:`AR(2)` model

.. math :: y_t = \alpha + \phi_1 y_{t-1} + \phi_2 y_{t-2} + e_t
.. math :: e_t \sim N(0, \sigma^2)

There are a number of ways to transform this model to state-space representation. Consider, for example, letting :math:`\alpha_t = (y_t, y_{t-1})'`.

**Transition Equation:**

.. math :: \alpha_t	= \begin{bmatrix} \phi_1 & \phi_2\\ 1 & 0\end{bmatrix} \alpha_t  + \begin{bmatrix} 1\\ 0 \end{bmatrix} \eta_t

**Measurement Equation:**

.. math :: y_t = \begin{bmatrix} 1 & 0 \end{bmatrix} \alpha_t


In this representation the system matrices are:

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
| :math:`T`          |:math:`\begin{bmatrix} \phi_1 & \phi_2\\ 1 & 0 \end{bmatrix}`     |
+--------------------+------------------------------------------------------------------+
| :math:`R`          |:math:`\begin{bmatrix} 1 \\ 0 \end{bmatrix}`                      |
+--------------------+------------------------------------------------------------------+
| :math:`Q`          | :math:`\sigma^2`                                                 |
+--------------------+------------------------------------------------------------------+

In this model our unknown parameters are :math:`\phi_1`, :math:`\phi_2`, and :math:`\sigma^2`

Estimation of State-Space Models
---------------------------------------------------
The GAUSS :class:`sslib` relies on two tools for estimating state-space models, the `Kalman filter <https://docs.aptech.com/gauss/tsmt/kalmanfilter.html>`_ and maximum likelihood estimation.


+--------------------+------------------------------------------------------------------+
|Tool                | Purpose                                                          |
+====================+==================================================================+
| Kalman filter      | The Kalman filter uses recursive iteration to estimate the       |
|                    | unknown state.                                                   |
+--------------------+------------------------------------------------------------------+
| Maximum likelihood | Uses the likelihood function generated from the Kalman filter    |
|                    | to estimate the unknown parameters.                              |
+--------------------+------------------------------------------------------------------+

You will never need to interact with these two tools directly when using the GAUSS state-space framework. However, for more information about either of these please see the following:

1. `Filtering data with the Kalman Filter <https://www.aptech.com/resources/tutorials/tsmt/filtering-data-with-the-kalman-filter/>`_
2. `Beginner's Guide To Maximum Likelihood Estimation <https://www.aptech.com/blog/beginners-guide-to-maximum-likelihood-estimation-in-gauss/>`_
3. `Maximum Likelihood Estimation in GAUSS <https://www.aptech.com/blog/maximum-likelihood-estimation-in-gauss/>`_

State-space Models in GAUSS
---------------------------------------------------
The :class:`sslib` library contains a suite of tools that allows you to specify, estimate, diagnose, and perform post-estimation forecasts. The primary procedure for estimating custom state-space models is the :func:`ssFit` procedure.

Prior to calling :func:`ssFit` there are several simple steps that must be taken:

1. Load the required libraries.
2. Set up parameter vector and start values.
3. Set up control structures.
4. Initialize system matrices.
5. Specify variable constraints.
6. Set up procedure for updating system matrices.

Step One: Loading the required libraries
+++++++++++++++++++++++++++++++++++++++++++
The first step to estimating state-space models in GAUSS is to load the proper libraries:

::

  new;
  library sslib, tsmt, cmlmt;

Step Two: Set up parameter vector and start values
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
If you are estimating a custom state-space model, a vector of parameter starting values is required. The parameter vector should be a column vector which contains a starting value for each unknown parameter. For example, in the :math:`AR(2)` example there are three unknown parameters :math:`\phi_1`, :math:`phi_2`, and :math:`sigma^2`.

::

  /*
  ** Set up parameter vector
  **           and start values
  */

  // Create a dataframe
  param_vec_st = asDF(zeros(3, 1), "param");

  // Starting values for phi_1,
  // phi_2, and sigma2
  param_vec_st[1] = -0.322;
  param_vec_st[2] = 0.433;
  param_vec_st[3] = 0.0025;

Step Three: Set up the control structure
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
The :class:`ssControl` structure is used to:

1. Specify the state-space system matrices.
2. Implement stationarity and non-negativity constraints on parameters.
3. Control modeling features.
3. Specify advanced maximum likelihood controls.

Before using the :class:`ssControl` structure:

* The model dimensions must be specified.
* The controls structure must be initialized.
* The default values must be filled.

Specifying the model dimensions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The model dimensions are defined by three variables:

+--------------------+------------------------------------------------------------------+
|Variable            | Description                                                      |
+====================+==================================================================+
| `k_endog`          | Number of endogenous variables.                                  |
+--------------------+------------------------------------------------------------------+
| `k_states`         | Number of state variables.                                       |
+--------------------+------------------------------------------------------------------+
| `k_posdef`         | Optional, dimension of the state innovation with                 |
|                    | a positive definite covariance matrix.                           |
|                    | Default = k_states.                                              |
+--------------------+------------------------------------------------------------------+

For the AR(2) model we have one endogenous variable and two state variables:

::

  /*
  ** Declare shape
  */
  // Number of endogenous variables
  k_endog = 1;

  // Number of states
  k_states = 2;


Initialize control structure and system matrices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
After specifying the model dimensions, the :class:`ssControl` structure and the system matrices should be initialized using the :func:`ssControlCreate` procedure.

::

  // Declare and instance of control structure
  struct ssControl ssctl;

  // Fill the controls structure with defaults
  // and sets up the system matrices.
  ssCtl = ssControlCreate(k_states, k_endog);


The :func:`ssControlCreate` procedure initiates the state-space system matrices in a :class:`ssModel` structure. The matrices are all set to zeroes in the following dimensions:

+--------------------+------------------------------------------------------------------+
| Object             | Specification                                                    |
+====================+==================================================================+
| :math:`ssm.d`      | :math:`k_{endog} \times 1`                                       |
+--------------------+------------------------------------------------------------------+
| :math:`ssm.Z`      | :math:`k_{endog} \times k_{states}`                              |
+--------------------+------------------------------------------------------------------+
| :math:`ssm.H`      | :math:`k_{endog} \times k_{endog}`                               |
+--------------------+------------------------------------------------------------------+
| :math:`ssm.c`      | :math:`k_{states} \times k_{states}`                             |
+--------------------+------------------------------------------------------------------+
| :math:`ssm.T`      | :math:`k_{states} \times k_{states}`                             |
+--------------------+------------------------------------------------------------------+
| :math:`ssm.R`      | :math:`k_{states} \times k_{posdef}`                             |
+--------------------+------------------------------------------------------------------+
| :math:`ssm.Q`      | :math:`k_{posdef} \times k_{posdef}`                             |
+--------------------+------------------------------------------------------------------+

Step Four: Set up fixed system matrices
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
The fixed system matrices should be specified using GAUSS after initializing the system matrices. In this step, any elements of the system matrices that do not contain parameters to be estimated should be specified using `GAUSS matrix notation <https://www.aptech.com/blog/gauss-basics-3-introduction-to-matrices/>`_.

For example, in the AR(2) example above, the transition matrix, :math:`Z`, is given by

.. math :: \begin{bmatrix} 1 & 0 \end{bmatrix}

and the selection matrix, :math:`R`, is given by

.. math :: \begin{bmatrix} 1 \\ 0 \end{bmatrix}

These matrices have no relationship to the model parameters and should be specified before calling the :func:`ssFit` procedure:

::

  /*
  ** Step four: Set up fixed system
  **            matrices
  **
  ** The system matrices are stored in the
  ** control structure in ssModel structure ssm:
  **
  */

  // Set fixed parameters of model
  ssctl.ssm.Z = { 1 0 };
  ssctl.ssm.R[1, 1] = 1;

Step Five: Set up parameter constraints
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Step Six: Set procedure for updating the SS model structure with parameters
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
The final step before calling the :func:`ssFit` procedure is to specify the relationship between the state-space system matrices and the model parameters using a :class:`updateSSModel` `procedure <https://www.aptech.com/blog/basics-of-gauss-procedures/>`_.

The :class:`updateSSModel` function should always include twp input parameters:

+--------------------+------------------------------------------------+
| Object             | Specification                                  |
+====================+================================================+
| :code:`*ssmod`     | A pointer to the :class:`ssmod` structure.     |
+--------------------+------------------------------------------------+
| :code:`param`      | The parameter vector.                          |
+--------------------+------------------------------------------------+

The :class:`updateSSModel` should always:

1. Begin with a procedure declaration

::

  proc (0) = updateSSModel(struct ssModel *ssmod, param);

2. Contain a procedure body which relations system matrices to model parameters.

::

  // Set up kalman filter matrices
  ssmod->T =  param[1 2]'|(1~0);
  ssmod->Q[1, 1] = param[3];

3. End with a procedure end statement.

::

  endp;

All together, the :class:`updateSSModel` for the AR(2) model is:

::

  /*
  ** Step five: Set up procedure for updating SS model
  ** structure.
  **
  */
  proc (0) = updateSSModel(struct ssModel *ssmod, param);

    // Set up kalman filter matrices
    ssmod->T =  param[1 2]'|(1~0);
    ssmod->Q[1, 1] = param[3];

  endp;
