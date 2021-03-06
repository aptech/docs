
uniqindxsa
==============================================

Purpose
----------------
Computes the sorted index of a string vector, omitting duplicate elements.

Format
----------------
.. function:: ind = uniqindxsa(sv)

    :param sv: data
    :type sv: Nx1 or 1xN string vector

    :return ind: indices corresponding to the
        elements of *sv* sorted in ascending order with duplicates removed.

    :rtype ind: Mx1 vector

Examples
----------------

::

    //  String vector
    string sv = {"mary", "linda", "linda", "jane",
                 "jane", "cindy", "betty"};

    // Find indices of sorted string vector
    ind = uniqindxsa(sv);

    // Sort string vector
    y = sv[ind];

The above code assigns the variables ``ind`` and ``y`` as follows:

::

           7       betty
           6       cindy
    ind  = 4   y =  jane
           2       linda
           1        mary

Remarks
-------

Among sets of duplicates it is unpredictable which elements will be indexed.


Source
------

uniquesa.src

.. seealso:: Functions :func:`unique`, :func:`uniquesa`, :func:`uniqindx`
