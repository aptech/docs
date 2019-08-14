
pvPackm
==============================================

Purpose
----------------

Packs general matrix into a structure of type :class:`PV` with a mask and matrix name.

Format
----------------
.. function:: p1 = pvPackm(p1, x, nm, mask)

    :param p1: an instance of structure of type :class:`PV`
    :type p1: struct

    :param x: data
    :type x: MxN matrix or N-dimensional array

    :param nm: name of matrix/array or N-dimensional array.
    :type nm: string

    :param mask: *mask* matrix of zeros and ones.
    :type mask: MxN matrix

    :returns: p1 (*struct*) instance of :class:`PV` struct.

Remarks
-------

The *mask* argument allows storing a selected portion of a matrix into the
packed vector. The ones in *mask* indicate an element to be stored in the
packed matrix. When the matrix is unpacked (using :func:`pvUnpack`) the elements
corresponding to the zeros are restored. Elements corresponding to the
ones come from the packed vector which may have been changed.

If the mask is all zeros, the matrix or array is packed with the
specified elements in the second argument but no elements of the matrix
or array are entered into the parameter vector. When unpacked the matrix
or array in the second argument is returned without modification.


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
     
    p1 = pvPackm(p1, x, "X", mask);
     
    print pvUnpack(p1, 1);

::

     1.000 2.000
     3.000 4.000

::

    p1 = pvPutParVector(p1, 5|6);
     
    print pvUnpack(p1, "X");

::

     5.000 2.000
     3.000 6.000

Source
------

pv.src

