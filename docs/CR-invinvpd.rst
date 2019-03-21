
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

    :returns: y (*TODO*), NxN matrix or K-dimensional array where the last two dimensions are NxN, containing the inverse of x.

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
