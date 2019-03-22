
rfftn
==============================================

Purpose
----------------
Computes a real 1- or 2-D FFT.

Format
----------------
.. function:: rfftn(x)

    :param x: 
    :type x: NxK real matrix

    :returns: y (*LxM matrix*), where L and M are the smallest prime
        factor products greater than or equal to N and K, respectively.



Remarks
-------

rfftn uses the Temperton prime factor FFT algorithm. This algorithm can
compute the FFT of any vector or matrix whose dimensions can be
expressed as the product of selected prime number factors. GAUSS
implements the Temperton algorithm for any power of 2, 3, and 5, and one
factor of 7. Thus, rfftn can handle any matrix whose dimensions can be
expressed as:

::

   2p x 3q x 5r x 7s

   p, q, r ≥ 0     -- for rows of matrix

   p > 0. q, r ≥ 0 -- for columns of matrix

   p > 0. q, r ≥ 0 -- for length of a vector

   s = 0 or 1      -- for all dimensions

If a dimension of x does not meet these requirements, it will be padded
with zeros to the next allowable size before the FFT is computed.

rfftn pads matrices to the next allowable size; however, it generally
runs faster for matrices whose dimensions are highly composite numbers,
i.e., products of several factors (to various powers), rather than
powers of a single factor. For example, even though it is bigger, a
33600x1 vector can compute as much as 20 percent faster than a 32768x1
vector, because 33600 is a highly composite number,
2\ :sup:`6`\ x3x5\ :sup:`2`\ x7, whereas 32768 is a simple power of 2,
2\ :sup:`15`. For this reason, you may want to hand-pad matrices to
optimum dimensions before passing them to rfftn. The **Run-Time
Library** includes two routines, optn and optnevn, for determining
optimum dimensions. Use optn to determine optimum rows for matrices, and
optnevn to determine optimum columns for matrices and optimum lengths
for vectors.

The **Run-Time Library** also includes the nextn and nextnevn routines,
for determining allowable dimensions for matrices and vectors. (You can
use these to see the dimensions to which rfftn would pad a matrix or
vector.)

rfftn scales the computed FFT by 1/(L*M).

.. seealso:: Functions :func:`fft`, :func:`ffti`, :func:`fftm`, :func:`fftmi`, :func:`fftn`, :func:`rfft`, :func:`rffti`, :func:`rfftip`, :func:`rfftnp`, :func:`rfftp`
