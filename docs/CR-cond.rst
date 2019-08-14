
cond
==============================================

Purpose
----------------

Computes the condition number of a matrix using the singular value decomposition.

Format
----------------
.. function:: c = cond(x)

    :param x: used to compute condition number
    :type x: NxK matrix

    :return c: an estimate of the condition number of *x*.
        This equals the ratio of the largest singular
        value to the smallest. If the smallest singular
        value is zero or not all of the singular values
        can be computed, the return value is 1e300.

    :type c: scalar

Examples
----------------

Basic usage
+++++++++++

::

    x = { 4 2 6,
          8 5 7,
          3 8 9 };

    c = cond(x);

will assign *c* to equal:

::

    c = 9.8436943

Decrease condition number by standardizing variables
++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Set seed for repeatable random numbers
    rndseed 777;
    
    X = rndn(100, 3) ~ rndi(100, 1);
    
    print "cond(X)   = " cond(X);
    
    // Create standardized X
    X_s = X - meanc(X)';
    X_s = X_s ./ stdc(X_s)';
    
    print "cond(X_s) = " cond(X_s);

will create the following output:

::

    cond(X)   =    2.7008906e+09 
    cond(X_s) =        1.2504154 
