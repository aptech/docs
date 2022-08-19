Example: Simple Time Invariant Models
=======================================
This example uses generated data to demonstrate how to estimate a simple state-space model.

Data Generation
-------------------
The data generating process follows

========================== ========================================================
State Equation             :math:`\alpha_t = 0.3 \alpha_{t-1} + \eta_t`
Measurement Equation       :math:`y_t = \alpha_t + 0.1 \epsilon_t`
========================== ========================================================

We will first generate the :math:`AR(1)` using the :func:`simarmamt` function from the TSMT library.

::

  new;

  /*
  ** Load required libraries
  */
  library cmlmt, tsmt, sslib;

  /*
  ** Step one: Data generation
  */
  seed = 8971;

  // Number of observations
  T = 150;

  // AR coefficient
  phi = 0.3;

  // AR order
  p = 1;

  // MA order
  q = 0;

  // Deterministic components
  const = 0;
  trend = 0;

  // Number of replications
  k = 1;

  // Standard deviation of error process
  std = 1;

  // Generate data
  alpha = simarmamt(phi, p, q, const, trend, T, k, std, seed);

The alpha series can then be used to generate the observed series, :math:`y_t` using the :func:`rndn`:

::

  // Generate observation
  y = alpha + 0.1*rndn(T,1);

Estimating the state-space model
-------------------------------------
Using the generate series, :math:`y`, let's estimate the state-space model assuming the underlying parameters, :math:`\phi`, :math:`\sigma_2`, and :math:`\sigma_2`, are unknown:

========================== ========================================================
State Equation             :math:`\alpha_t = \phi \alpha_{t-1} + \sigma_1 \eta_t`
Measurement Equation       :math:`y_t = \alpha_t + \sigma_2 \epsilon_t`
========================== ========================================================

Step one: Specify the starting values
+++++++++++++++++++++++++++++++++++++++++
The parameter vector has three unknowns so our vector of starting parameters should be a :math:`3 x 1` vector.

::

  /*
  ** Set up parameter vector
  ** and start values
  */
  param_vec_st = asDF(zeros(3, 1), "param");

  param_vec_st[1] = 0.5;
  param_vec_st[2] = 0.9;
  param_vec_st[3] = 0.2;

Step two: Setting up the control structure and model matrices
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
The GAUSS :class:`sslib` library uses the state-space representation of a linear model written as

.. math:: y_t = d + Z\alpha_t + \epsilon_t
.. math:: \alpha_t = c + T\alpha_{t-1} + R\eta_t

where

.. math:: \epsilon_t  \sim N(0, H)
.. math:: \eta_t  \sim N(0, Q)

For the model in this example, we specify the following system matrices:

+--------------------+-------------------------+----------------------+
| Object             | Description             | Specification        |
+====================+=========================+======================+
| :math:`d`          | Observation intercept.  | 0                    |
+--------------------+-------------------------+----------------------+
| :math:`Z`          | Design matrix.          | 1                    |
+--------------------+-------------------------+----------------------+
| :math:`H`          | Observation disturbance | :math:`\sigma_2`     |
|                    | covariance matrix.      |                      |
+--------------------+-------------------------+----------------------+
| :math:`c`          | State intercept.        | 0                    |
+--------------------+-------------------------+----------------------+
| :math:`T`          | Transition matrix.      | :math:`\phi`         |
+--------------------+-------------------------+----------------------+
| :math:`R`          | Selection matrix.       | 1                    |
+--------------------+-------------------------+----------------------+
| :math:`Q`          | State disturbance       | :math:`\sigma_1`     |
|                    | covariance matrix.      |                      |
+--------------------+-------------------------+----------------------+

The first step to specifying this model is to initialize the system using the `ssControl` structure and the model dimensions. This model has 1 endogenous variable and 1 state variable:

::

  /*
  ** Declare shape
  ** Three dimensions:
  **     k_endog               Required, number of
  **                           endogenous variables.
  **
  **     k_states              Required, number of
  **                           states.
  **
  **     k_posdef              Optional argument, scalar, the dimension
  **                           of the state innovation with
  **                           a positive definite covariance matrix.
  */
  // Number of endogenous variables
  k_endog = 1;

  // Number of states
  k_states = 1;

  // Declare and instance of control structure
  struct ssControl ssctl;

  // Fill the controls structure with defaults
  // and sets up the system matrices.
  ssCtl = ssControlCreate(k_states, k_endog);

  // Parameter names
  ssCtl.param_names = "phi"$|"sigma1"$|"sigma2";

Step three: Constrained variables
+++++++++++++++++++++++++++++++++++++++++
In this model we need to constrain :math:`phi` to be stationary and :math:`sigma_1` and `sigma_2` to be positive.

::

  /*
  ** This stationary_vars member
  ** indicates which variables should be
  ** constrained to stationarity.
  */
  // Set the first and second parameters in
  // the parameter vector to be stationary
  ssCtl.stationary_vars = 1;

  /*
  ** This positive_vars member
  ** indicates which variables should be
  ** constrained to positive.
  */
  // Set the third parameter in
  // the parameter vector to be positive
  ssCtl.positive_vars = 2|3;

Step four: Specify the fixed matrices in the model
++++++++++++++++++++++++++++++++++++++++++++++++++++
In this state-space model the :math:`Z` and :math:`R` matrices are independent of the unknown parameters and should be specified outside of the `update` function:

::

  // Set fixed parameters of model
  ssctl.ssm.Z = 1;
  ssctl.ssm.R = 1;

Step five: Set up procedure for updating SS model
++++++++++++++++++++++++++++++++++++++++++++++++++++
We also need to specify the function for updating the system matrices with the unknown parameters.

::

  /*
  ** The updateSSModel function should always include the
  ** input parameters
  **
  **   *ssmod
  **
  **   param           The parameter vector.
  **
  **  To set a member in the ssmod structure use the arrow notation:
  **
  **   ssmod->T = param[1 2]'|(1~0);
  */
  proc (0) = updateSSModel(struct ssModel *ssmod, param);

    // Set up kalman filter matrices
    ssmod->T =  param[1];
    ssmod->Q  = param[2];
    ssmod->H  = param[3];
 endp;

Step six: Estimate the model
++++++++++++++++++++++++++++++++++++++++++++++++++++
Finally, we are ready to estimate the model using the :func:`ssFit` procedure.

::

  /*
  ** Call the ssFit procedure.
  **            This will:
  **              1. Estimate model parameters.
  **              2. Estimate inference statistics (se, t-stats).
  **              3. Perform model residual diagnostics.
  **              4. Compute model diagnostics and summary statistics.
  */
  struct ssOut sOut;
  sOut = ssFit(&updateSSModel, param_vec_st, y, ssctl);

The model estimates are both stored in the `sOut` output structure and printed to screen:

::

  Return Code:                                                             0
  Log-likelihood:                                                     -210.6
  Number of Cases:                                                       149
  AIC:                                                                 427.2
  AICC:                                                                427.4
  BIC:                                                                 436.2
  HQIC:                                                                  426
  Covariance Method:                                    ML covariance matrix
  ==========================================================================

        Parameters         Estimates         Std. Err.            T-stat
  ---------------------------------------------------------------------------
               phi            0.5912            0.2972            1.9890
            sigma1            0.1937            0.2385            0.8120
            sigma2            0.6184            0.2346            2.6357
