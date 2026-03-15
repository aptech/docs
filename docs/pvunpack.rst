
pvUnpack
==============================================

Purpose
----------------

Unpacks matrices stored in a structure of type :class:`PV`.

Format
----------------
.. function:: x = pvUnpack(p1, m)

    :param p1: an instance of structure of type :class:`PV`
    :type p1: struct

    :param m: name of matrix, or integer, index of matrix.
    :type m: string

    :return x: MxN general matrix or MxM symmetric matrix or N-dimensional array

    :rtype x: matrix or array

Examples
--------

::

    // Create and populate a PV structure
    struct PV p1;
    p1 = pvCreate;
    p1 = pvPack(p1, 1|2|3, "beta");
    p1 = pvPack(p1, 0.5~0.8, "gamma");

    // Unpack matrices by name
    beta = pvUnpack(p1, "beta");
    gamma = pvUnpack(p1, "gamma");
    print beta;
    print gamma;

Source
------

pv.src
