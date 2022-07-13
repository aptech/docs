
The update function is a required user-provided procedure which specifies how the state space system matrices should be updated with the underlying model parameters.

The update function must always take the same inputs:

  -  The first input is a pointer to a `ssModel` structure which contains the state space system matrices.
  -  The second input is a vector of parameters.

The update function should only specify system matrices which contain parameters, it should not specify fixed system matrices.

For example, we might have the following update function specifying how the parameters of a model should be placed in the state space matrices:

::

   proc (0) = updateSSModel(struct ssModel *ssMod, param);

    // Set up kalman filter matrices
    ssmod->T =  param[1 2]'|(1~0);
    ssmod->Q[1, 1] = param[3];

   endp;
