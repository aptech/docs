
rfftip
==============================================

Purpose
----------------

Computes an inverse real 1- or 2-D FFT. Takes a packed format FFT as input.

Format
----------------
.. function:: rfftip(x)

    :param x: 
    :type x: NxK matrix or K-length vector

    :returns: y (*LxM real matrix or M-length vector*) .



Remarks
-------

rfftip assumes that its input is of the same form as that output by
rfftp and rfftnp.

rfftip uses the Temperton prime factor FFT algorithm. This algorithm can
compute the inverse FFT of any vector or matrix whose dimensions can be
expressed as the product of selected prime number factors. GAUSS
implements the Temperton algorithm for any integer power of 2, 3, and 5,
and one factor of 7. Thus, rfftip can handle any matrix whose dimensions
can be expressed as:

::

   2p x 3q x 5r x 7s

   p, q, r ≥ 0
   s = 0 or 1

If a dimension of x does not meet this requirement, it will be padded
with zeros to the next allowable size before the inverse FFT is
computed. Note that rfftip assumes the length (for vectors) or column
dimension (for matrices) of x is K-1 rather than K, since the last
element or column does not hold FFT information, but the Nyquist
frequencies.

The sizes of x and y are related as follows: L will be the smallest
prime factor product greater than or equal to N, and M will be twice the
smallest prime factor product greater than or equal to K-1. This takes
into account the fact that x contains both positive and negative
frequencies in the row dimension (matrices only), but only positive
frequencies, and those only in the first K-1 elements or columns, in the
length or column dimension.

It is up to the user to guarantee that the input will return a real
result. If in doubt, use ffti. Note, however, that ffti expects a full
FFT, including negative frequency information, for input.

Do not pass rfftip the output from rfft or rfftn-it will return
incorrect results. Use rffti with those routines.

.. seealso:: Functions :func:`fft`, :func:`ffti`, :func:`fftm`, :func:`fftmi`, :func:`fftn`, :func:`rfft`, :func:`rffti`, :func:`rfftn`, :func:`rfftnp`, :func:`rfftp`
