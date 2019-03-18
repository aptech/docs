
optn, optnevn
==============================================

Purpose
----------------

Returns optimal matrix dimensions for computing FFT's.

Format
----------------
.. function:: optnevn(n0)

    :param n0: the length of a vector or the number of rows or columns in a matrix.
    :type n0: scalar

    :returns: n (*scalar*), the next optimal size for the given dimension
        for computing an FFT or RFFT. n > n0.

Examples
----------------

::

    n = optn(231);

The above code assigns n to be equal to 240.

.. seealso:: Functions :func:`fftn`, :func:`nextn`, :func:`nextnevn`, :func:`rfftn`, :func:`rfftnp`
