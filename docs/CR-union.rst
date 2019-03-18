
union
==============================================

Purpose
----------------

Returns the union of two vectors with duplicates removed.

Format
----------------
.. function:: union(v1,  v2,  flag)

    :param v1: Nx1 vector.
    :type v1: TODO

    :param v2: Mx1 vector.
    :type v2: TODO

    :param flag: 1 if numeric data, 0 if character.
    :type flag: scalar

    :returns: y (*TODO*), Lx1 vector containing all unique values that are in
        v1 and  v2, sorted in ascending order.

Examples
----------------

::

    //Create two column vectors with character data
                    
    let v1 = mary jane linda john;
    let v2 = mary sally;
    
    x = union(v1,v2,0);
    
    //The '$' in front of 'x' tells GAUSS to print 'x' as 
    //character data
    print $x;

The above code will produce the following results:

::

    JANE
     JOHN
    LINDA
     MARY
    SALLY

