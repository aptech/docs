
rank
==============================================

Purpose
----------------
Computes the rank of a matrix, using the singular value decomposition.

Format
----------------
.. function:: rank(x)

    :param x: 
    :type x: NxP matrix

    :returns: k (*n estimate*) of the rank of x. This
        equals the number of singular values of x
        that exceed a prespecified tolerance in absolute value.



Source
------

svd.src



Global Input
------------

+---+-----------------------------------------------------+
| \ | scalar, the tolerance used in determining if any of |
| _ | the singular values are effectively 0. The default  |
| s | value is 10e\ :sup:`-13`. This can be changed       |
| v | before calling the procedure.                       |
| d |                                                     |
| t |                                                     |
| o |                                                     |
| l |                                                     |
+---+-----------------------------------------------------+

.. seealso:: Functions :func:`detl`, :func:`norm`
