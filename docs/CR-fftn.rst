
fftn
==============================================

Purpose
----------------

Computes a complex 1- or 2-D FFT.

Format
----------------
.. function:: fftn(x)

    :param x: 
    :type x: NxK matrix

    :returns: y (*LxM matrix*), where L and M are the smallest prime factor
        products greater than or equal to N and K, respectively.



Remarks
-------

fftn uses the Temperton prime factor FFT algorithm. This algorithm can
compute the FFT of any vector or matrix whose dimensions can be
expressed as the product of selected prime number factors. GAUSS
implements the Temperton algorithm for any power of 2, 3, and 5, and one
factor of 7. Thus, fftn can handle any matrix whose dimensions can be
expressed as

::

   2p x 3q x 5r x 7s

where p, q and r are nonnegative integers and s is equal to 0 or 1.

If a dimension of x does not meet this requirement, it will be padded
with zeros to the next allowable size before the FFT is computed.

fftn pads matrices to the next allowable dimensions; however, it
generally runs faster for matrices whose dimensions are highly composite
numbers, i.e., products of several factors (to various powers), rather
than powers of a single factor. For example, even though it is bigger, a
33600x1 vector can compute as much as 20% faster than a 32768x1 vector,
because 33600 is a highly composite number,
2\ :sup:`6`\ x3x5\ :sup:`2`\ x7, whereas 32768 is a simple power of 2,
2\ :sup:`15`. For this reason, you may want to hand-pad matrices to
optimum dimensions before passing them to fftn. The **Run-Time Library**
includes a routine, optn, for determining optimum dimensions.

The **Run-Time Library** also includes the nextn routine, for
determining allowable dimensions for a matrix. (You can use this to see
the dimensions to which fftn would pad a matrix.)

fftn scales the computed FFT by 1/(L*M).

.. seealso:: Functions :func:`fft`, :func:`ffti`, :func:`fftm`, :func:`fftmi`, :func:`rfft`, :func:`rffti`, :func:`rfftip`, :func:`rfftn`, :func:`rfftnp`, :func:`rfftp`
