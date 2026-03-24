
pvGetIndex
==============================================

Purpose
----------------

Gets row indices of a matrix in a parameter vector.

Format
----------------
.. function:: id = pvGetIndex(p1, nm1)

    :param p1: an instance of structure of type :class:`PV`
    :type p1: struct

    :param nm1: name or row number of matrix 
    :type nm1: string or scalar

    :return id: row indices of matrix described by *nm1* in parameter vector.

    :rtype id: Kx1 vector

Examples
--------

::

    // Create and populate a PV structure
    struct PV p1;
    p1 = pvCreate;
    p1 = pvPack(p1, 1|2|3, "beta");
    p1 = pvPack(p1, 0.5~0.8, "gamma");

    // Get the row indices of "beta" in the parameter vector
    id = pvGetIndex(p1, "beta");
    print id;

Source
------

pv.src

