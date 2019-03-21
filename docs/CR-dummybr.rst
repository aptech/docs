
dummybr
==============================================

Purpose
----------------

Creates a set of dummy (0/1) variables. The highest (rightmost) category is bounded on the right.

Format
----------------
.. function:: dummybr(x, v)

    :param x: 
    :type x: Nx1 vector of data that is to be broken up
        into dummy variables

    :param v:  These categories should not
        overlap.
    :type v: Kx1 vector specifying the K breakpoints (these
        must be in ascending order) that determine the K
        categories to be used

    :returns: y (*TODO*), NxK matrix containing the K dummy variables.
        Each row will have a maximum of one 1.

Examples
----------------

::

    //Set seed for repeatable random numbers
    rndseed 135345;
    
    //Create uniform random integers between 1 and 9
    x = ceil(9*rndu(5,1));
    
    //Set the breakpoints
    v = { 1, 5, 7 };
    
    dm = dummybr(x,v);

The code above produces three dummies based upon the breakpoints in the vector v:

::

    x < 1
    1 < x < 5
    5 < x < 7

which look like:

::

    0 1 0       2 
         0 0 0       9 
    dm = 0 1 0   x = 4 
         0 0 1       7 
         1 0 0       1

Source
++++++

datatran.src

.. seealso:: Functions :func:`dummydn`, :func:`dummy`, :func:`code`, :func:`recode`, :func:`reclassifyCuts`, :func:`substute`, :func:`rescale`, :func:`reclassify`
