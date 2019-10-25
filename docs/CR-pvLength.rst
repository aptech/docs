
pvLength
==============================================

Purpose
----------------

Returns the length of a parameter vector.

Format
----------------
.. function:: n = pvLength(p1)

    :param p1: an instance of structure of type *PV*
    :type p1: struct

    :return n: length of parameter vector in *p1*.

    :rtype n: scalar

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

        pvLength(p1)

Source
------

pv.src
