
fftn
==============================================

Purpose
----------------

Computes a complex 1- or 2-D FFT.

Format
----------------
.. function:: y = fftn(x)

    :param x: The data used to compute the FFT.
    :type x: NxK matrix

    :return y: where *L* and *M* are the smallest prime factor
        products greater than or equal to *N* and *K*, respectively.

    :type y: LxM matrix

Remarks
-------

:func:`fftn` uses the Temperton prime factor FFT algorithm. This algorithm can
compute the FFT of any vector or matrix whose dimensions can be
expressed as the product of selected prime number factors. GAUSS
implements the Temperton algorithm for any power of 2, 3, and 5, and one
factor of 7. Thus, :func:`fftn` can handle any matrix whose dimensions can be
expressed as

.. math :: 2^p \times 3^q \times 5^r \times 7^s

where *p*, *q* and *r* are nonnegative integers and *s* is equal to 0 or 1.

If a dimension of *x* does not meet this requirement, the :func:`fftn` pads matrices to the next allowable dimensions. However, it
generally runs faster for matrices whose dimensions are highly composite numbers. Highly composite numbers are products of several factors (to various powers), rather than powers of a single factor.

For example, even though it is bigger, a
33600x1 vector can compute as much as 20% faster than a 32768x1 vector,
because 33600 is a highly composite number,
:math:`2^6 \times 3 \times 5^2 \times 7`, whereas 32768 is a simple power of 2,
:math:`2^15`.

For this reason, you may want to hand-pad matrices to
optimum dimensions before passing them to :func:`fftn`. The `Run-Time Library`
includes a routine, :func:`optn`, for determining optimum dimensions.

The `Run-Time Library` also includes the :func:`nextn` routine, for
determining allowable dimensions for a matrix. (You can use this to see
the dimensions to which :func:`fftn` would pad a matrix.)

:func:`fftn` scales the computed FFT by :math:`1/(L*M)`.

.. seealso:: Functions :func:`fft`, :func:`ffti`, :func:`fftm`, :func:`fftmi`, :func:`rfft`, :func:`rffti`, :func:`rfftip`, :func:`rfftn`, :func:`rfftnp`, :func:`rfftp`
