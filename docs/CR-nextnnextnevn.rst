
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

Remarks
-------

nextn and nextnevn determine allowable matrix dimensions for computing
FFT's. The Temperton FFT routines (see table below) can handle any
matrix whose dimensions can be expressed as:

::

   2px3qx5rx7s

where p, q and r are nonnegative integers and s is equal to 0 or 1.


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
