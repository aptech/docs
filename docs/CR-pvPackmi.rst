
pvPackmi
==============================================

Purpose
----------------

Packs general matrix or array into a PV instance with
a mask, name, and index.

Format
----------------
.. function:: pvPackmi(p1, x, nm, mask, i)

    :param p1: 
    :type p1: an instance of structure of type PV

    :param x: 
    :type x: MxN matrix or N-dimensional array

    :param nm: matrix or array name.
    :type nm: string

    :param mask: ,
        mask of zeros and ones.
    :type mask: MxN matrix or N-dimensional array

    :param i: index of matrix or array in lookup table.
    :type i: scalar

    :returns: p1 (*TODO*), an instance of structure of type PV.

Examples
----------------

::

    #include pv.sdf
     
    struct PV p1;
    p1 = pvCreate;
     
    x = { 1 2,
          3 4 };
     
    mask = { 1 0,
             0 1 };
     
    p1 = pvPackmi(p1,x,"X",mask,1);
     
    print pvUnpack(p1,1);

::

    1.000 2.000
     3.000 4.000

::

    p1 = pvPutParVector(p1,5|6);
     
    print pvUnpack(p1,1);

::

    5.000 2.000
     3.000 6.000

.. seealso:: Functions :func:`pvPackm`, :func:`pvUnpack`
