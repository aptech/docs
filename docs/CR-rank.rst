
rank
==============================================

Purpose
----------------
Computes the rank of a matrix, using the singular value decomposition.

Format
----------------
.. function:: k = rank(x)

    :param x: data
    :type x: NxP matrix

    :returns: k, an estimate of the rank of *x*. This
        equals the number of singular values of *x*
        that exceed a prespecified tolerance in absolute value.

Global Input
------------

:_svdtol: scalar, the tolerance used in determining if any of the singular values 
    are effectively 0. The default value is 10e\ :sup:`-13`. This can be changed 
    before calling the procedure.

Source
------

svd.src

.. seealso:: Functions :func:`detl`, :func:`norm`
