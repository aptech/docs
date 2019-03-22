
pvPacksi
==============================================

Purpose
----------------

Packs symmetric matrix into a PV instance with matrix
name and index.

Format
----------------
.. function:: pvPacksi(p1, x, nm, i)

    :param p1: 
    :type p1: an instance of structure of type PV

    :param x: 
    :type x: MxM symmetric matrix

    :param nm: matrix name.
    :type nm: string

    :param i: index of matrix in lookup table.
    :type i: scalar

    :returns: p1 (*struct*) instance of :class:`PV` struct.

Remarks
-------

pvPacksi does not support the packing of arrays.


Examples
----------------

::

    #include pv.sdf
     
    struct PV p1;
    p1 = pvCreate;
     
    x = { 1 2, 2 1 };
     
    p1 = pvPacksi(p1,x, "A",1);
    p1 = pvPacksi(p1, eye(2), "I",2);

These matrices can be extracted using the pvUnpack command.

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
