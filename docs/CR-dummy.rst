
dummy
==============================================

Purpose
----------------

Creates a set of dummy (0/1) variables by breaking
up a variable into specified categories. The
highest (rightmost) category is unbounded on the
right.

Format
----------------
.. function:: dummy(x, v)

    :param x: 
    :type x: Nx1 vector of data that is to be broken up
        into dummy variables

    :param v:  These categories should not
        overlap.
    :type v: (K-1)x1 vector specifying the K-1 breakpoints
        (these must be in ascending order) that determine the K
        categories to be used

    :returns: y (*TODO*), NxK matrix containing the K dummy variables.

Examples
----------------

::

    //Set seed for repeatable random numbers
    rndseed 135345;
    
    //Create uniform random integers between 1 and 9
    x = ceil(9*rndu(5,1));
    
    //Set the breakpoints
    v = { 1, 5, 7 };
    
    dm = dummy(x,v);

The code above produces four dummies based upon the breakpoints in the vector v:

::

    x < 1
    1 < x < 5
    5 < x < 7
    7 < x

which look like:

::

    0 1 0 0       2 
         0 0 0 1       9 
    dm = 0 1 0 0   x = 4 
         0 0 1 0       7 
         1 0 0 0       1

Source
++++++

datatran.src

.. seealso:: Functions :func:`dummybr`, :func:`dummydn`, :func:`code`, :func:`recode`, :func:`reclassifyCuts`, :func:`substute`, :func:`rescale`, :func:`reclassify`
