
pvPacksmi
==============================================

Purpose
----------------

Packs symmetric matrix into a PV instance with a mask, 
matrix name, and index.

Format
----------------
.. function:: pvPacksmi(p1, x, nm, mask, i)

    :param p1: 
    :type p1: an instance of structure of type PV

    :param x: 
    :type x: MxM symmetric matrix

    :param nm: matrix name.
    :type nm: string

    :param mask: symmetric mask matrix of zeros and ones.
    :type mask: MxM matrix

    :param i: index of matrix in lookup table.
    :type i: scalar

    :returns: p1 (*TODO*), an instance of structure of type PV.

Examples
----------------

::

    #include pv.sdf
     
    struct PV p1;
    p1 = pvCreate;
     
    x = { 1 2 4,
          2 3 5,
          4 5 6};
     
    mask = { 1 0 1,
             0 1 0,
             1 0 1 };
     
    p1 = pvPacksmi(p1,x, "A",mask,1);
     
    print pvUnpack(p1,1);

::

    1.000 2.000 4.000
      2.000 3.000 5.000
      4.000 5.000 6.000

::

    p2 = pvGetParVector(p1);
     
    print p2;

::

    1.000
      3.000
      4.000
      6.000

::

    p3 = { 10, 11, 12, 13 };
    p1 = pvPutParVector(p1,p3);
     
    print pvUnpack(p1,1);

::

    10.000  2.000 12.000
       2.000 11.000  5.000
      12.000  5.000 13.000

.. seealso:: Functions :func:`pvPacksm`, :func:`pvUnpack`
