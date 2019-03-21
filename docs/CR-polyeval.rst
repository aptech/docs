
polyeval
==============================================

Purpose
----------------

Evaluates polynomials. Can either be one or more scalar polynomials or a single matrix polynomial.

Format
----------------
.. function:: polyeval(x, coefs)

    :param x: , x can either represent K
        separate scalar values at which to evaluate the (scalar) polynomial(s), or it can represent a
        single NxN matrix.
    :type x: 1xK or NxN; that is

    :param c:  If x is 1xK, then c
        must be (P+1)xK. If x is NxN, c must be (P+1)x1.
        That is, if x is a matrix, it can only be
        evaluated at a single set of coefficients.
    :type c: (P+1)xK or (P+1)x1 matrix of coefficients of
        polynomials to evaluate

    :returns: y (*TODO*), Kx1 vector (if c is (P+1)xK) or NxN matrix (if c
        is (P+1)x1 and x is NxN):
        y =( c[1,.].*xp + c[2,.].*x(p-1) + ... + c[p+1,.] )';

Examples
----------------
Scalar example 1

::

    //Evaluate 2^4 + 2^3 + 2^1 + 2^0
    x = 2;
    coefs = { 1, 1, 0, 1, 1 };
    y = polyeval(x,coefs);

The result is 27. Note that this is the decimal value of the binary number 11011.
Scalar example 2

::

    //Evaluate 7*2^3 + 2^1 + 2^0
    x = 2;
    coefs = { 7, 0, 1, 1 };
    y = polyeval(x,coefs);

The result is 59.
Matrix example 1

::

    //Evaluate A*A*A + 2*A
    A = { 2 6,
          4 8 };
    coefs = { 1, 0, 2, 0 };
    A_3 = polyeval(A, coefs);

The above code will set A_3 equal to:

::

    300    660 
       440    960

Matrix example 2

::

    //Evaluate A*A*A*A
    A = { 1.2 3.1,
          1.7 0.8 };
    coefs = 1|zeros(4,1);
    y = polyeval(A,coefs);

You can raise a matrix to the n'th power with the command:

::

    A_n = polyeval(A, 1|zeros(n,1));

A*A*A*A*...*A

Source
++++++

poly.src

.. seealso:: Functions :func:`polymake`, :func:`polychar`, :func:`polymult`, :func:`polyroot`

evaluates polynomial given coefficient
