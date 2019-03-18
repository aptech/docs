
unionsa
==============================================

Purpose
----------------

Returns the union of two string vectors with duplicates removed.

Format
----------------
.. function:: unionsa(sv1,  sv2)

    :param sv1: Nx1 or 1xN string vector.
    :type sv1: TODO

    :param sv2: Mx1 or 1xM string vector.
    :type sv2: TODO

    :returns: y (*TODO*), Lx1 vector containing all unique values that
        are in  sv1 and  sv2, sorted in ascending
        order.

Examples
----------------

::

    string sv1 = { "mary", "jane", "linda", "john" };
    string sv2 = { "mary", "sally" };
    y = unionsa(sv1,sv2);
    print y;

The above code produces the following output:

::

    jane
     john
    linda
     mary
    sally

Source
++++++

unionsa.src

.. seealso:: Functions :func:`union`
