
local
==============================================

.. _local:
.. index:: local

Purpose
----------------

Declare variables that are to exist only inside a procedure.

Format
----------------

::

    local x, y, f:proc;

Examples
-------------------

::

  proc (1) = myProc(y);
    local x1, x2;

    x1 = y;
    x2 = 2*x1;

    retp(x1);
  endp;

Remarks
-------

The statement in the format section would place the names *x*, *y*, and *f* in the local
symbol table for the current procedure being compiled. This statement is
legal only between the `proc` statement and the `endp` statement of a
procedure definition.

These symbols cannot be accessed outside of the procedure.

The symbol *f* in the statement above will be treated as a procedure
whenever it is accessed in the current procedure. What is actually
passed in is a pointer to a procedure.

See **Procedures and Keywords**, Chapter 1.


.. seealso:: Functions `proc`
