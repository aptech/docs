
null
==============================================

Purpose
----------------

Computes an orthonormal basis for the (right) null space of a matrix.

Format
----------------
.. function:: null(x)

    :param x: 
    :type x: NxM matrix

    :returns: b (*MxK matrix*), where K is the nullity of x, such that:
        
        x * b = 0 //NxK matrix of 0'sand
        b'b = I  //MxM identity matrixThe error returns are returned in  b:

    .. csv-table::
        :widths: auto

        "error code", "reason"
        "1", "there is no null space"
        "2", "b is too large to return in a single matrix"
        "Use scalerr to test for error returns."

Remarks
-------

The orthogonal complement of the column space of x' is computed using
the QR decomposition. This provides an orthonormal basis for the null
space of x.


Examples
----------------

::

    let x[2,4] = 2 1 3 -1
                 3 5 1  2;
     
    b = null(x);
    z = x*b;
    i = b'b;

After the code above:

::

    -0.804  0.142 
    b =  0.331 -0.473  z = 0  0  i = 1  0
         0.473  0.331      0  0      0  1
         0.142  0.804

Source
++++++

null.src

Globals
+++++++

\_qrdc, \_qrsl

orthonormal basis for right null space
