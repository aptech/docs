
scalerr
==============================================

Purpose
----------------
Tests for a scalar error code.

Format
----------------
.. function:: scalerr(c)

    :param c: , generally the return argument of a function or procedure call.
    :type c: NxK matrix or sparse matrix or N-dimensional array

    :returns: y (*TODO*), scalar or [N-2]-dimensional array, 0 if the argument
        is not a scalar error code, or the value of the error
        code as an integer if the argument is an error code.

Examples
----------------

::

    trap 1;
    cm = invpd(x);
    trap 0;
    
    if scalerr(cm);
       cm = inv(x);
    endif;

In this example invpd will return a scalar error code if the matrix
x is not positive definite. If scalerr returns with a nonzero
value, the program will use the inv function, which is slower, to
compute the inverse. Since the trap state has been turned off, if
inv fails, the program will terminate with a Matrix singular
error message.

.. seealso:: Functions :func:`error`, :func:`trap`, :func:`trapchk`
