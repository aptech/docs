
varput
==============================================

Purpose
----------------
Allows a matrix, array, string, or string array to be assigned to a global
symbol whose name is given as a string argument.

Format
----------------
.. function:: y = varput(x, n)

    :param x: data which is to be assigned to the target variable.
    :type x: matrix or array or string or string array

    :param n: the name of the global symbol which will be the target variable
    :type n: string

    :return y: 1 if the operation is successful and 0 if the operation fails.

    :rtype y: scalar

Examples
----------------

::

    source = rndn(2, 2);
    targname = "target";

    if not varput(source, targname);
       print "Symbol table full";
       end;
    endif;

Remarks
-------

*x* and *n* may be global or local. The variable, whose name is in *n*, that *x*
is assigned to is always a global.

If the function fails, it will be because the global symbol table is full.

This function is useful for returning values generated in local
variables within a procedure to the global symbol table.

.. seealso:: Functions :func:`varget`, :func:`typecv`
