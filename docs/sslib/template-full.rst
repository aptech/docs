
newfoo
==============================================

Purpose
----------------

Solves the nonlinear programming problem.

Format
----------------
.. function:: out = newfoo(&fct, par, y [, ctl])

    :param &fct: pointer to a procedure that computes the function to be minimized. The first input
        to this procedure must be an instance of structure of type :class:`PV`.
    :type &fct: function pointer

    :param par: Contains starting values for parameters to be estimated. This parameter vector is used in the updated function to update the state space system matrices.
    :type par: Vector

    :param y: Observed data.
    :type y: Vector

    :param ctl: Optional input. instance of an :class:`structNameControl` structure. Normally an instance is initialized by calling :func:`structNameControlCreate` and members of this instance can be set to other values by the user. For an instance named *ctl*, the members are:

        .. include:: include/structnamecontrolmembers.rst

    :type ctl: struct

    :return out: an instance of an :class:`structNameout` structure. For an instance named *out*, the members are:

        .. include:: include/structnameoutmembers.rst

    :rtype out: struct

Examples
----------------

    ::

       // Set up procedure for updating SS model
       // structure
       proc (0) = updateSSModel(struct ssModel *ssmod, param);

        // Set up kalman filter matrices
        ssmod->T =  param[1 2]'|(1~0);
        ssmod->Q[1, 1] = param[3];

       endp;

Remarks
-------

.. include:: include/updatefunctionremarks.rst


Source
------

ssmain.src

.. seealso:: Functions :func:`sqpSolveMTControlCreate`, :func:`sqpSolveMTlagrangeCreate`
