
utrisol
==============================================

Purpose
----------------

Computes the solution of Ux = b where  U is an upper
triangular matrix.

Format
----------------
.. function:: utrisol(b, U)

    :param b: 
    :type b: PxK matrix

    :param U: 
    :type U: PxP upper triangular matrix

    :returns: x (*PxK matrix*), solution of Ux = b.



Remarks
-------

utrisol applies a back solve to Ux = b to solve for x. If b has more
than one column, each column is solved for separately, i.e., utrisol
applies a back solve to U \* x[.,i]= b[.,i].

