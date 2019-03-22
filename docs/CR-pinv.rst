
pinv
==============================================

Purpose
----------------
Computes the Moore-Penrose pseudo-inverse of a matrix, using the singular value decomposition. This pseudo-inverse is one particular type of generalized inverse. 

Format
----------------
.. function:: pinv(x)

    :param x: 
    :type x: NxM matrix

    :returns: y (*MxN matrix*) that satisfies the 4 Moore-Penrose
        conditions:

    .. csv-table::
        :widths: auto

        "xyx = x"
        "yxy = y"
        "xy is symmetric"
        "yx is symmetric"

Examples
----------------
pinv can be used to solve an undertermined least squares problem.

::

    //Create an underdetermined system of equations 'A'
    A = rndn(4, 5);
    
    //Create a right hand side
    b = rndn(4,1);
    
    if rank(A) < cols(A);
       print "A does not have full rank, using pinv to solve";
       Api = pinv(A);
       x = Api*b;
    else;
       print "A has full rank, solve with '/' operator";
       x = b/A;
    endif;

Least squares problems with full rank can also be solved with the GAUSS
functions: ols, olsqr and olsqr2.

Source
------

svd.src

Moore-Penrose generalized pseudo-inverse


Global Input
------------

+-----------------+-----------------------------------------------------+
| \_svdtol        | scalar, any singular values less than \_svdtol are  |
|                 | treated as zero in determining the rank of the      |
|                 | input matrix. The default value for \_svdtol is     |
|                 | 1.0e-13.                                            |
+-----------------+-----------------------------------------------------+

