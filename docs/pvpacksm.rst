
pvPacksm
==============================================

Purpose
----------------

Packs symmetric matrix into a structure of type :class:`PV` with a mask.

Format
----------------
.. function:: p1 = pvPacksm(p1, x, nm, mask)

    :param p1: an instance of structure of type :class:`PV`
    :type p1: struct

    :param x: data
    :type x: MxM symmetric matrix

    :param nm: matrix name.
    :type nm: string

    :param mask: mask matrix of zeros and ones.
    :type mask: MxM matrix

    :return p1: instance of :class:`PV` struct.

    :rtype p1: struct

Examples
----------------

::

    // Declare 'p1' to be a 'PV' struct
    struct PV p1;

    // Apply 'PV' struct defaults
    p1 = pvCreate();

    // Declare symmetric matrix
    x = { 1 2 4,
          2 3 5,
          4 5 6};

    // Create mask declaring the diagonal and
    // the (1,3) element to be parameters to estimate
    mask = { 1 0 1,
             0 1 0,
             1 0 1 };

    p1 = pvPacksm(p1, x, "A", mask);

    print pvUnpack(p1, "A");

:func:`pvUnpack`, will return the entire symmetrix matrix from *p1*.

::

      1.000 2.000 4.000
      2.000 3.000 5.000
      4.000 5.000 6.000

:func:`pvGetParVector`, returns the free, non-redundant parameters from *p1* as a vector.

::

    p2 = pvGetParVector(p1);

    print p2;

::

      1.000
      3.000
      4.000
      6.000

:func:`pvPutParVector` will overwrite the free parameters with the new data passed in.

::

    p3 = { 10, 11, 12, 13 };
    p1 = pvPutParVector(p1, p3);

    print pvUnpack(p1, "A");

::

      10.000  2.000 12.000
       2.000 11.000  5.000
      12.000  5.000 13.000

Remarks
-------

:func:`pvPacksm` does not support the packing of arrays.

The *mask* allows storing a selected portion of a matrix into the packed
vector. The ones in *mask* indicate an element to be stored in the packed
matrix. When the matrix is unpacked (using :func:`pvUnpack`) the elements
corresponding to the zeros are restored. Elements corresponding to the
ones come from the packed vector which may have been changed.

Only the lower left portion of the *mask* matrix is used, and only the
lower left portion of the *x* matrix is stored in the packed vector.

If the mask is all zeros, the matrix is packed with the specified
elements in the second argument but no elements of the matrix are
entered into the parameter vector. When unpacked the matrix in the
second argment is returned without modification.


Source
------

pv.src
