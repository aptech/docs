
abs
==============================================

Purpose
----------------

Returns the absolute value or complex modulus of *x*.

Format
----------------
.. function:: y = abs(x)

    :param x:
    :type x: NxK matrix or sparse matrix or N-dimensional array

    :return y: containing absolute values of *x*.

    :rtype y: NxK matrix or sparse matrix or N-dimensional array

Examples
----------------

::

    /*
    ** Set random number generator seed for
    ** repeatable random numbers
    */
    rndseed 929212;

    x = rndn(2, 2);
    y = abs(x);

The code above assigns the variables as follows:

::

    x =  -0.23061709      0.054931120
          0.88863202     -0.82246522

    y =   0.23061709      0.054931120
          0.88863202      0.82246522

In this example, a 2x2 matrix of Normal random
numbers is generated and the absolute value of the
matrix is computed.
