
uniqindxsa
==============================================

Purpose
----------------
Computes the sorted index of a string vector, omitting duplicate  elements.

Format
----------------
.. function:: uniqindxsa(sv)

    :param sv: Nx1 or 1xN string vector.
    :type sv: TODO

    :returns: ind (*Mx1 vector*), indices corresponding to the
        elements of  sv sorted in ascending order with
        duplicates removed.

Examples
----------------

::

    string sv = {"mary", "linda", "linda", "jane",
                 "jane", "cindy", "betty"};
    ind = uniqindxsa(sv);
    y = sv[ind];

The above code assigns the variables ind and y as follows:

::

    7       betty
           6       cindy
    ind  = 4   y =  jane
           2       linda
           1        mary

Source
++++++

uniquesa.src

.. seealso:: Functions :func:`unique`, :func:`uniquesa`, :func:`uniqindx`
