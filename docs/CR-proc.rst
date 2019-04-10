
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



Remarks
-------

A procedure definition begins with the proc statement and ends with the
endp statement.

An example of a procedure definition is:

::

   proc dog(x,y,z); /* procedure declaration */
   local a,b;        /* local variable declarations */
      a = x .* x;
      b = y .* y;
      a = a ./ x;
      b = b ./ y;
      z = z .* z;
      z = inv(z);
      retp(a'b*z);  /* return with value of a'b*z */
   endp;             /* end of procedure definition */

Procedures can be used just as if they were functions intrinsic to the
language. Below are the possible variations depending on the number of
items the procedure returns.

Returns 1 item:

::

   y = dog(i,j,k);

Returns multiple items:

::

   { x,y,z } = cat(i,j,k);

Returns no items:

::

   fish(i,j,k);

If the procedure does not return any items or you want to discard the
returned items:

::

   call
   dog(i,j,k);

Procedure definitions may not be nested.

For more details on writing procedures, see **Procedures and Keywords**,
Chapter 1.

.. seealso:: Functions `keyword`, :func:`call`, `endp`, `local`, `retp`
