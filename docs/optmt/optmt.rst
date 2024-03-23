optmt
==============================================

Purpose
----------------

Solve the optimization problem with or without simple bounds.

Format
----------------
.. function:: out = optmt(&modelProc, par [,..., c1])

    :param &modelProc: Pointer to a procedure that computes the function to be minimized.
    :type &modelProc: pointer

    :param par: An instance of a PV structure. The par instance is passed to the user-provided procedure pointed to by &fct. par is constructed using the "pack" functions.
    :type par: struct

    :param ...: Optional input arguments. They can be any set of structures, matrices, arrays, strings required to compute the function. Can include GAUSS data types or a DS structure for dataset manipulation. Specific usage depends on the requirements of the `modelProc`.
    :type ...: various

    :param c1: Optional input. Instance of a :class:`optmtControl` structure containing the following members:

        .. include:: include/optmtcontrolstruct.rst

    :type c1: struct

    :return out: An instance of a :class:`optmtResults` structure. Contains the results of the nonlinear programming problem solution, including parameter estimates, function evaluations, and detailed information about constraints handling and optimization process. The :class:`optmtResults` structure includes:

        .. include:: include/optmtresultsstruct.rst

    :rtype out: struct

Examples
----------------


Remarks
-------

- There is one required user-provided procedure, the one computing the objective function and optionally the first and/or second derivatives, and four other optional procedures, one each for computing the equality constraints, the inequality constraints, the Jacobian of the equality constraints, and the Jacobian of the inequality constraints.

- The main procedure, computing the objective function and optionally the first and/or second derivatives: 
    - Requires a vector of parameters or an instance of a PV structure containing the parameters as the first input.
    - Any number of optional arguments including structures, matrices, arrays, strings, required to compute the objective function.
    - A last input named `ind`. 

- The remaining optional procedures take just two arguments: the parameters and any optional arguments that were passed to :func:`optmt`.

- The instance of the PV structure is set up using the PV pack procedures, :func:`pvPack`, :func:`pvPackm`, :func:`pvPacks`, and :func:`pvPacksm`. These procedures allow for setting up a parameter vector in a variety of ways.

- The optional arguments passed to the user-provided objective function procedure are untouched. This allows you to pass into your function any information it needs.

