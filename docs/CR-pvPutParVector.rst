
pvPutParVector
==============================================

Purpose
----------------

Inserts parameter vector into structure of type :class:`PV`.

Format
----------------
.. function:: pvPutParVector(p1, p)

    :param p1: an instance of structure of type :class:`PV`
    :type p1: struct

    :param p: parameter vector.
    :type p: Kx1 vector

    :returns: p1 (*struct*) instance of :class:`PV` struct.

Remarks
-------

Matrices or portions of matrices (stored using a *mask*) are stored in the
structure of type :class:`PV` as a vector in the *p* member.

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
     
    // Packed as square matrix
    p1 = pvPackm(p1,x,"A",mask);
     
    print pvUnpack(p1,"A");

::

    1.000 2.000 4.000
      2.000 3.000 5.000
      4.000 5.000 6.000

::

    p3 = { 10, 11, 12, 13, 14 };
    p1 = pvPutParVector(p1,p3);
     
    print pvUnpack(p1,"A");

::

      10.000  2.000 11.000
       2.000 12.000  5.000
      13.000  5.000 14.000

Source
------

pv.src

