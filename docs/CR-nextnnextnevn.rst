
nextn, nextnevn
==============================================

Purpose
----------------

Returns allowable matrix dimensions for computing FFT's.

Format
----------------
.. function:: nextn(n0) 
			  nextnevn(n0)

    :param n0: the length of a vector or the number of rows or columns in a matrix.
    :type n0: scalar

    :returns: n (*scalar*), the next allowable size for the given dimension
        for computing an FFT or RFFT. n > n0.

Examples
----------------

::

    n = nextn(456);

The code above will assign n to be equal to 480.

Source
++++++

optim.src

.. seealso:: Functions :func:`fftn`, :func:`optn`, :func:`optnevn`, :func:`rfftn`, :func:`rfftnp`

compute FFT
