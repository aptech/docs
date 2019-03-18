
pvPackm
==============================================

Purpose
----------------

Packs general matrix into a structure of type PV with a mask and matrix name.

Format
----------------
.. function:: pvPackm(p1, x,  nm,  mask)

    :param p1: an instance of structure of type PV.
    :type p1: TODO

    :param x: MxN matrix or N-dimensional array.
    :type x: TODO

    :param nm: name of matrix/array or N-dimensional array.
    :type nm: string

    :param mask: mask matrix of zeros and ones.
    :type mask: MxN matrix

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
     
    p1 = pvPackm(p1,x,"X",mask);
     
    print pvUnpack(p1,1);

::

    1.000 2.000
     3.000 4.000

::

    p1 = pvPutParVector(p1,5|6);
     
    print pvUnpack(p1,"X");

::

    5.000 2.000
     3.000 6.000

Source
++++++

pv.src

.. raw:: html

   </div>
