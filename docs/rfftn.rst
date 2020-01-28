
rfftn
==============================================

Purpose
----------------
Computes a real 1- or 2-D FFT.

Format
----------------
.. function:: y = rfftn(x)

    :param x: data
    :type x: NxK real matrix

    :return y: where :math:`L` and :math:`M` are the smallest prime
        factor products greater than or equal to :math:`N` and :math:`K`, respectively.

    :rtype y: LxM matrix

Remarks
-------

:func:`rfftn` uses the Temperton prime factor FFT algorithm. This algorithm can
compute the FFT of any vector or matrix whose dimensions can be
expressed as the product of selected prime number factors. GAUSS
implements the Temperton algorithm for any power of 2, 3, and 5, and one
factor of 7. Thus, rfftn can handle any matrix whose dimensions can be
expressed as:

.. math::

   2^p \times 3^q \times 5^r \times 7^s

For rows of the matrix :

.. math::

   p, q, r \geq 0

For columns of the matrix or length of a vector:

.. math::

   p > 0\\
   q, r \geq 0

For all dimensions:

.. math::

   s = 0 \text{ or } 1

If a dimension of *x* does not meet these requirements, it will be padded
with zeros to the next allowable size before the FFT is computed.

:func:`rfftn` pads matrices to the next allowable size; however, it generally
runs faster for matrices whose dimensions are highly composite numbers,
i.e., products of several factors (to various powers), rather than
powers of a single factor. For example, even though it is bigger, a
33600x1 vector can compute as much as 20 percent faster than a 32768x1
vector, because 33600 is a highly composite number,
:math:`2\ :sup:`6`\ x3x5\ :sup:`2`\ x7`, whereas 32768 is a simple power of 2,
:math:`2\ :sup:`15``. For this reason, you may want to hand-pad matrices to
optimum dimensions before passing them to :func:`rfftn`. The **Run-Time
Library** includes two routines, :func:`optn` and :func:`optnevn`, for determining
optimum dimensions. Use :func:`optn` to determine optimum rows for matrices, and
:func:`optnevn` to determine optimum columns for matrices and optimum lengths
for vectors.

The **Run-Time Library** also includes the :func:`nextn` and :func:`nextnevn` routines,
for determining allowable dimensions for matrices and vectors. (You can
use these to see the dimensions to which :func:`rfftn` would pad a matrix or
vector.)

:func:`rfftn` scales the computed FFT by :math:`\frac{1}{(L*M)}`.

.. seealso:: Functions :func:`fft`, :func:`ffti`, :func:`fftm`, :func:`fftmi`, :func:`fftn`, :func:`rfft`, :func:`rffti`, :func:`rfftip`, :func:`rfftnp`, :func:`rfftp`
