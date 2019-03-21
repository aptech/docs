
intrsectsa
==============================================

Purpose
----------------

Returns the intersection of two string vectors, with duplicates removed. NOTE: This function is deprecated, use intrsect instead.

Format
----------------
.. function:: intrsectsa(sv1, sv2)

    :param sv1: 
    :type sv1: Nx1 or 1xN string vector

    :param sv2: 
    :type sv2: Mx1 or 1xM string vector

    :returns: sy (*Lx1 vector containing all unique strings that are in both  sv1 and  sv2*), sorted in ascending order.

Examples
----------------

::

    vars_a = "age" $| "weight" $| "bmi";
    vars_b = "hdl" $| "ldl" $| "age" $| "bmi" $| "smoking";
    
    shared_vars = intrsectsa(vars_a, vars_b);
    print "Both studies reported the following variables:";
    print shared_vars;

The code above, returns:

::

    Both studies reported the following variables:
                 age              bmi

Source
++++++

intrsect.src

.. seealso:: Functions :func:`intrsect`
