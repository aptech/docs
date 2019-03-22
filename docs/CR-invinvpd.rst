
inv, invpd
==============================================

Purpose
----------------
inv returns the inverse of an invertible matrix.
invpd returns the inverse of a symmetric, positive definite matrix.

Format
----------------
.. function:: inv(x) 
			  invpd(x)

    :param x: 
    :type x: NxN matrix or K-dimensional array where the last two dimensions are NxN

    :returns: y (*NxN matrix or K-dimensional array*) where the last two dimensions are NxN, containing the inverse of x.

Remarks
-------

x can be any legitimate expression that returns a matrix or array that
is legal for the function.

If x is an array, the result will be an array containing the inverses of
each 2-dimensional array described by the two trailing dimensions of x.
In other words, for a 10x4x4 array, the result will be an array of the
same size containing the inverses of each of the 10 4x4 arrays contained
in x

For inv, if x is a matrix, it must be square and invertible. Otherwise,
if x is an array, the 2-dimensional arrays described by the last two
dimensions of x must be square and invertible.

For invpd, if x is a matrix, it must be symmetric and positive definite.
Otherwise, if x is an array, the 2-dimensional arrays described by the
last two dimensions of x must be symmetric and positive definite.

If the input matrix is not invertible by these functions, they will
either terminate the program with an error message or return an error
code which can be tested for with the scalerr function. This depends on
the trap state as follows:

If trap is set to 1, they will return a scalar errorcode:

+--------------------+-------------------------------------------------+
| inv                | invpd                                           |
+--------------------+-------------------------------------------------+
| 50                 | 20                                              |
+--------------------+-------------------------------------------------+

If trap is set to 0, they will terminate with an error message:

+--------------------+-------------------------------------------------+
| inv                | invpd                                           |
+--------------------+-------------------------------------------------+
| "Matrix singular"  | "Matrix not positive definite"                  |
+--------------------+-------------------------------------------------+

If the input to invpd is not symmetric, it is possible that the function
will (erroneously) appear to operate successfully.

Positive definite matrices can be inverted by inv. However, for
symmetric, positive definite matrices (such as moment matrices), invpd
is about twice as fast as inv.


Examples
----------------

::

    n = 4000;
    x1 = rndn(n,1);
    x = ones(n,1)~x1;
    btrue = { 1, 0.5 };
    y = x*btrue + rndn(n,1);
    bols = invpd(x'x)*x'y;

After the code above, bols will be equal to:

::

    1.00237215 
    0.48249445

This example simulates some data and computes the
            ols coefficient estimator using the invpd function.
 First, the number of observations is specified.
 Second, a vector x1 of standard Normal random
 variables is generated and is concatenated with a
 vector of ones(to create a constant term). The true
 coefficients are specified, and the dependent
 variable y is created. Then the ols coefficient
 estimates are computed.
When computing least-squares problems with poorly conditioned matrices, the slash operator "/" and the function olsqr will provide greater accuracy.

inverse matrix positive definite
