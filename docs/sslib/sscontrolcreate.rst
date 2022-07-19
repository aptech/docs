
ssControlCreate
==============================================

Purpose
----------------

Creates default ssControl structure.

Format
----------------
.. function:: ssctl = ssControlCreate(k_states, k_endog [, k_posdef])

    :param k_states: Number of states.
    :type k_states:  Scalar

    :param k_endog: Number of endogenous variables.
    :type k_endog: scalar

    :param k_posdef: Optional argument, the dimension of the state innovation with a positive definite covariance matrix.
    :type k_posdef: scalar

    :return ssctl: Instance of :class:`ssControl` struct with members set to default values.

         .. list-table::
            :widths: auto

            * - sctl.param_names
              - String array, parameter names.
            * - sctl.stationary_vars
              - Vector, specifies the index of the variables which should be constrained stationary.
            * - sctl.positive_vars
              - Vector, specifies the index of the variables which should be constrained positive.
            * - sctl.ctl
              - Instance of a :class:`cmlmtControl` structure, used for fine-tuning maximum likelihood estimation. Further information provided in the `cmlmt` documentation.
            * - sctl.ssm
              - Instance of a :class:`ssModel` structure, contains the state space system matrices used in the :func:`kalmanFilter`. Contains the following members:

                .. list-table::
                    :widths: auto

                    * - ssm.Z
                      - k_endog x k_states, transition matrix.
                    * - ssm.d
                      - k_endog x 1, observation intercept.
                    * - ssm.H
                      - k_endog x k_endog, observation disturbance covariance.
                    * - ssm.T
                      - k_states x k_states, design matrix.
                    * - ssm.c
                      - k_states x k_states, state intercept.
                    * - ssm.R
                      - k_states x k_posdef, selection matrix.
                    * - ssm.Q
                      - k_states x k_posdef, state disturbance covariance.
                    * - ssm.a_0
                      - k_states x 1, initial prior state mean.
                    * - ssm.p_0
                      - k_states x k_states, initial prior state covariance.

    :rtype ssctl: struct

Examples
----------------
Since structures are strongly typed in GAUSS, each structure must be declared
before it can be used.

::

    // Declare 'ssctl' as an ssControl structure
    struct ssControl ssctl;

    /*
    ** Model dimensions
    */
    // Number of endogenous variables
    k_endog = 1;

    // Number of states
    k_states = 2;

    // Initialize structure 'ssctl'
    ssctl = ssControlCreate(k_states, k_endog);

Source
------

ssmain.src

.. seealso:: Functions :func:`ssFit`
