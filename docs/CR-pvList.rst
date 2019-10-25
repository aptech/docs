
pvList
==============================================

Purpose
----------------

Retrieves names of packed matrices in structure of type :class:`PV`.

Format
----------------
.. function:: n = pvList(p1)

    :param p1: an instance of structure of type :class:`PV`
    :type p1: struct

    :return n: names of packed matrices.

    :rtype n: Kx1 string vector

Examples
----------------

::

        // Declare 'p1' as an instance of a 'PV' structure
        struct PV p1;

        // Initialize 'p1' with default values
        p1 = pvCreate;

        x = { 1 2,
              3 4 };

        // 1's indicate elements to pack into 'p1' parameter vector
        mask = { 1 1,
                0 0 };

        p1 = pvPackm(p1, x, "X", mask);

        pvList(p1)

Source
------

pv.src
