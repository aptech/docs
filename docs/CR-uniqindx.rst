
uniqindx
==============================================

Purpose
----------------

Computes the sorted index of *x*, leaving out duplicate elements.

Format
----------------
.. function:: index = uniqindx(x, flag)

    :param x: data
    :type x: Nx1 or 1xN vector

    :param flag: 1 if numeric data, 0 if character.
    :type flag: scalar

    :return index: indices corresponding to the
        elements of *x* sorted in ascending order with duplicates removed.

    :type index: Mx1 vector

Remarks
-------

Among sets of duplicates it is unpredictable which elements will be indexed.

Examples
----------------

::

    let x = 5 4 4 3 3 2 1;
    
    // Create a sorted index of all the unique elements in 'x'
    ind = uniqindx(x,1);
    
    // Use the index 'ind' to return all of the unique elements 
    // of 'x' in ascending order
    y = x[ind];

After running the above code, *ind* and *y* are equal to:

::

           7.0000000         1.0000000
           6.0000000         2.0000000
    ind =  4.0000000    y =  3.0000000
           3.0000000         4.0000000
           1.0000000         5.0000000

.. seealso:: Functions :func:`unique`, :func:`uniqindxsa`

