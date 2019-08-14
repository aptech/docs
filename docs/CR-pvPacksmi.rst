
pvPacksmi
==============================================

Purpose
----------------

Packs symmetric matrix into a :class:`PV` instance with a mask, matrix name, and index.

Format
----------------
.. function:: p1 = pvPacksmi(p1, x, nm, mask, i)

    :param p1: an instance of structure of type :class:`PV`
    :type p1: struct 

    :param x: data
    :type x: MxM symmetric matrix

    :param nm: matrix name.
    :type nm: string

    :param mask: symmetric mask matrix of zeros and ones.
    :type mask: MxM matrix

    :param i: index of matrix in lookup table.
    :type i: scalar

    :returns: p1 (*struct*) instance of :class:`PV` struct.

Remarks
-------

:func:`pvPacksmi` does not support the packing of arrays.

The *mask* allows storing a selected portion of a matrix into the
parameter vector. The ones in the *mask* matrix indicate an element to be
stored in the parameter vector. When the matrix is unpacked (using
:func:`pvUnpackm`) the elements corresponding to the zeros are restored.
Elements corresponding to the ones come from the parameter vector.

Only the lower left portion of the mask matrix is used, and only the
lower left portion of the *x* matrix is stored in the packed vector.

If the mask is all zeros, the matrix is packed with the specified
elements in the second argument but no elements of the matrix are
entered into the parameter vector. When unpacked the matrix in the
second argment is returned without modification.


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

