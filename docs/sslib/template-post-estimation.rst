
newfoo
==============================================

Purpose
----------------

Solves the nonlinear programming problem.

Format
----------------
.. function:: out = newfoo(out)

    :param out: an instance of an :class:`structNameout` structure. For an instance named *out*, the members are:

        .. include:: include/structnameoutmembers.rst

    :type out: struct

    :return out: an updated instance of an :class:`structNameout` structure. For an instance named *out*, the updated members are:

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

.. include:: include/postestimationremarks.rst

Source
------

ssmain.src

.. seealso:: Functions :func:`sqpSolveMTControlCreate`, :func:`sqpSolveMTlagrangeCreate`
