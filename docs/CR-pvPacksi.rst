
pvPacksi
==============================================

Purpose
----------------

Packs symmetric matrix into a :class:`PV` instance with matrix name and index.

Format
----------------
.. function:: p1 = pvPacksi(p1, x, nm, i)

    :param p1: an instance of structure of type :class:`PV`
    :type p1: struct

    :param x: data
    :type x: MxM symmetric matrix

    :param nm: matrix name.
    :type nm: string

    :param i: index of matrix in lookup table.
    :type i: scalar

    :return p1: instance of :class:`PV` struct.

    :rtype p1: struct

Remarks
-------

:func:`pvPacksi` does not support the packing of arrays.


Examples
----------------

::

    #include pv.sdf
     
    struct PV p1;
    p1 = pvCreate;
     
    x = { 1 2, 2 1 };
     
    p1 = pvPacksi(p1,x, "A",1);
    p1 = pvPacksi(p1, eye(2), "I",2);

These matrices can be extracted using the :func:`pvUnpack` command.

::

    print
    pvUnpack(p1,1);

::

    1.000 2.000
    2.000 1.000

::

    print
    pvUnpack(p1,2);

::

    1.000 0.000
    0.000 1.000

.. seealso:: Functions :func:`pvPacks`, :func:`pvUnpack`

