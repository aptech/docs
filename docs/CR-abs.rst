
abs
==============================================

Purpose
----------------

Returns the absolute value or complex modulus of *x*.

Format
----------------
.. function:: abs(x)

    :param x: 
    :type x: NxK matrix or sparse matrix or N-dimensional array

    :returns: y (NxK matrix or sparse matrix or N-dimensional array) 
        containing absolute values of *x*.

Examples
----------------

::

    // Set random number generator seed for  
    // repeatable random numbers
    rndseed 929212;
    
    x = rndn(2,2);
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


