
optn, optnevn
==============================================

Purpose
----------------

Returns optimal matrix dimensions for computing FFT's.

Format
----------------
.. function:: n = optnevn(n0)

    :param n0: the length of a vector or the number of rows or columns in a matrix.
    :type n0: scalar

    :return n: the next optimal size for the given dimension
        for computing an FFT or RFFT. :math:`n > n0`.

    :rtype n: scalar

Examples
----------------

::

    n = optn(231);

The above code assigns *n* to be equal to 240.

Remarks
-------

The :func:`optn` and :func:`optnevn` procedures determine optimal matrix dimensions for computing
FFT's. The Temperton FFT routines (see table following) can handle any
matrix whose dimensions can be expressed as:

.. math::

   2p \times 3q \times 5r \times 7s

where *p*, *q* and *r* are nonnegative integers and *s* is equal to 0 or 1.

with one restriction: the vector length or matrix column size must be
even (*p* must be positive) when computing RFFT's.

The :func:`fftn`, etc., procedures pad matrices to the next allowable dimensions. However, they
generally run faster for matrices whose dimensions are highly composite
numbers, that is, products of several factors (to various powers),
rather than powers of a single factor. For example, even though it is
bigger, a 33600x1 vector can compute as much as 20% faster than a
32768x1 vector, because 33600 is a highly composite number, 2\ :sup:`6`
\* 3 \* 5\ :sup:`2` \* 7, whereas 32768 is a simple power of 2,
2\ :sup:`15`. The :func:`optn` and :func:`optnevn` procedures are provided so you can take advantage of
this fact by hand-sizing matrices to optimal dimensions before computing
the FFT.

Use the following table to determine what to call for a given function
and matrix:



================ ================ ============= ================
FFT              Vector           Matrix        Matrix
Function         Length           Rows          Columns
:func:`fftn`     :func:`optn`     :func:`optn`  :func:`optn`
:func:`rfftn`    :func:`optnevn`  :func:`optn`  :func:`optnevn`
:func:`rfftnp`   :func:`optnevn`  :func:`optn`  :func:`optnevn`
================ ================ ============= ================

.. seealso:: Functions :func:`fftn`, :func:`nextn`, :func:`nextnevn`, :func:`rfftn`, :func:`rfftnp`
