
union
==============================================

Purpose
----------------

Returns the union of two vectors with duplicates removed.

Format
----------------
.. function:: y = union(v1, v2, flag)

    :param v1: data
    :type v1: Nx1 vector

    :param v2: data
    :type v2: Mx1 vector

    :param flag: 1 if numeric data, 0 if character.
    :type flag: scalar

    :return y: containing all unique values that are in *v1* and *v2*, sorted in ascending order.

    :rtype y: Lx1 vector

Remarks
-------

The combined elements of *v1* and *v2* must fit into a single vector.


Examples
----------------

::

    // Create two column vectors with character data
                    
    let v1 = mary jane linda john;
    let v2 = mary sally;
    
    x = union(v1,v2,0);
    
    // The '$' in front of 'x' tells GAUSS to print 'x' as 
    // character data
    print $x;

The above code will produce the following results:

::

    JANE
     JOHN
    LINDA
     MARY
    SALLY

