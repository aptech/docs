
dummydn
==============================================

Purpose
----------------

Creates a set of dummy (0/1) variables by breaking
up a variable into specified categories. The
highest (rightmost) category is unbounded on the
right, and a specified column of dummies is dropped.

Format
----------------
.. function:: dummydn(x,  v,  p)

    :param x: Nx1 vector of data to be broken up into dummy
        variables.
    :type x: TODO

    :param v: (K-1)x1 vector specifying the K-1 breakpoints
        (these must be in ascending order) that determine the K
        categories to be used. These categories should not
        overlap.
    :type v: TODO

    :param p: positive integer in the range [1,K], specifying
        which column should be dropped in the matrix of
        dummy variables.
    :type p: TODO

    :returns: y (*TODO*), Nx(K-1) matrix containing the K-1 dummy variables.

Examples
----------------

::

    //Set seed for repeatable random numbers
    rndseed 135345;
    
    //Create uniform random integers between 1 and 9
    x = ceil(9*rndu(5,1));
    
    //Set the breakpoints
    v = { 1, 5, 7 };
    
    //Column to drop
    p = 2;
    
    dm = dummydn(x,v,p);

The code above produces four dummies based upon the breakpoints in the vector v:

::

    x < 1
    1 < x < 5
    5 < x < 7
    7 < x

and then remove the pth column which will result in:

::

    0 0 0       2 
         0 0 1       9 
    dm = 0 0 0   x = 4 
         0 1 0       7 
         1 0 0       1

Source
++++++

datatran.src

.. seealso:: Functions :func:`dummy`, :func:`dummybr`, :func:`code`, :func:`recode`, :func:`reclassifyCuts`, :func:`substute`, :func:`rescale`, :func:`reclassify`
