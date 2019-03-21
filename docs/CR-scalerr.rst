
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

Remarks
-------

Error codes in GAUSS are NaN's (Not A Number). These are not just scalar
integer values. They are special floating point encodings that the math
chip recognizes as not representing a valid number. See also error.

scalerr can be used to test for either those error codes that are
predefined in GAUSS or an error code that the user has defined using
error.

If c is an N-dimensional array, y will be an [N-2]-dimensional array,
where each element corresponds to a 2-dimensional array described by the
last two dimensions of c. For each 2-dimensional array in c that does
not contain a scalar error code, its corresponding element in y will be
set to zero. For each 2-dimensional array in c that does contain a
scalar error code, its corresponding element in y will be set to the
value of that error code as an integer. In other words, if c is a
5x5x10x10 array, y will be a 5x5 array, in which each element
corresponds to a 10x10 array in c and contains either a zero or the
integer value of a scalar error code.

If c is an empty matrix, scalerr will return 65535.

Certain functions will either return an error code or terminate a
program with an error message, depending on the trap state. The trap
command is used to set the trap state. The error code that will be
returned will appear to most commands as a missing value code, but the
scalerr function can distinguish between missing values and error codes
and will return the value of the error code.

Following are some of the functions that are affected by the trap state:

+----------+------------+------------------------------+
|          | **trap 1** | **trap 0**                   |
+----------+------------+------------------------------+
| function | error code | error message                |
+----------+------------+------------------------------+
| chol     | 10         | Matrix not positive definite |
+----------+------------+------------------------------+
| invpd    | 20         | Matrix not positive definite |
+----------+------------+------------------------------+
| solpd    | 30         | Matrix not positive definite |
+----------+------------+------------------------------+
| /        | 40         | Matrix not positive definite |
+----------+------------+------------------------------+
|          |            | (second argument not square) |
+----------+------------+------------------------------+
|          | 41         | Matrix singular              |
+----------+------------+------------------------------+
|          |            | (second argument is square)  |
+----------+------------+------------------------------+
| inv      | 50         | Matrix singular              |
+----------+------------+------------------------------+


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
