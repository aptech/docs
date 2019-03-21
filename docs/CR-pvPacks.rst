
pvPacks
==============================================

Purpose
----------------

Packs symmetric matrix into a structure of type PV.

Format
----------------
.. function:: pvPacks(p1, x, nm)

    :param p1: 
    :type p1: an instance of structure of type PV

    :param x: 
    :type x: MxM symmetric matrix

    :param nm: matrix name.
    :type nm: string

    :returns: p1 (*TODO*), an instance of structure of type PV.

Remarks
-------

pvPacks does not support the packing of arrays.


Examples
----------------

::

    #include pv.sdf
     
    struct PV p1;
    p1 = pvCreate;
     
    x = { 1 2,
          2 1 };
     
    p1 = pvPacks(p1,x, "A");
    p1 = pvPacks(p1, eye(2), "I");

pvUnpack

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

Source
------

pv.src

.. seealso:: Functions :func:`pvPacksm`, :func:`pvUnpack`
