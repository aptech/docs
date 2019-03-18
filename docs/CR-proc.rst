
proc
==============================================

Purpose
----------------

Begins the definition of a multi-line recursive procedure. Procedures are user-defined
functions with local or global variables.

Format
----------------
.. function:: name(arglist) 
			  proc name(arglist)

    :param nrets: number of objects returned by the procedure.
        If  nrets is not explicitly given, the default is 1. Legal values
        are 0 to 1023. The retp statement is used to return values from a
        procedure.
    :type nrets: constant

    :param name: name of the procedure. This name will be a
        global symbol.
    :type name: literal

    :param arglist: separated by commas, to be used
        inside the procedure to refer to the arguments that are passed to the
        procedure when the procedure is called. These will always be local
        to the procedure, and cannot be accessed from outside the procedure
        or from other procedures.
    :type arglist: a list of names

