
pvPacks
==============================================

Purpose
----------------

Packs symmetric matrix into a structure of type :class:`PV`.

Format
----------------
.. function:: p1 = pvPacks(p1, x, nm)

    :param p1: an instance of structure of type :class:`PV`
    :type p1: struct

    :param x: data
    :type x: MxM symmetric matrix

    :param nm: matrix name.
    :type nm: string

    :return p1: instance of :class:`PV` struct.

    :rtype p1: struct

Examples
----------------

::

    struct PV p1;
    p1 = pvCreate;

    x = { 1 2,
          2 1 };

    p1 = pvPacks(p1, x, "A");
    p1 = pvPacks(p1, eye(2), "I");

These matrices can be extracted using the :func:`pvUnpack` command:

::

    print pvUnpack(p1, "A");

::

     1.000 2.000
     2.000 1.000

::

    print pvUnpack(p1, "I");

::

     1.000 0.000
     0.000 1.000

Remarks
-------

:func:`pvPacks` does not support the packing of arrays.


Source
------

pv.src

.. seealso:: Functions :func:`pvPacksm`, :func:`pvUnpack`
