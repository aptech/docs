
rfftp
==============================================

Purpose
----------------

Computes a real 1- or 2-D FFT. Returns the results in a packed format.

Format
----------------
.. function:: y = rfftp(x)

    :param x: data
    :type x: NxK real matrix or K-length real vector

    :returns: y (*Lx(M/2+1) matrix or (M/2+1)-length vector*), where
        :math:`L` and :math:`M` are the smallest powers of 2 greater than or equal
        to :math:`N` and :math:`K`, respectively.

Remarks
-------

If a dimension of *x* is not a power of 2, it will be padded with zeros to
the next allowable size before the FFT is computed.

For 1-D FFT's, :func:`rfftp` returns the positive frequencies in ascending order
in the first :math:`M/2` elements, and the Nyquist frequency in the last
element. For 2-D FFT's, :func:`rfftp` returns the positive and negative
frequencies for the row dimension, and for the column dimension, it
returns the positive frequencies in ascending order in the first :math:`M/2`
columns, and the Nyquist frequencies in the last column. Usually the FFT
of a real function is calculated to find the power density spectrum or
to perform filtering on the waveform. In both these cases only the
positive frequencies are required. (See also :func:`rfft` and :func:`rfftn` for routines
that return the negative frequencies as well.)

:func:`rfftp` scales the computed FFT by :math:`1/(L*M)`.

:func:`rfftp` uses the Temperton FFT algorithm.

.. seealso:: Functions :func:`fft`, :func:`ffti`, :func:`fftm`, :func:`fftmi`, :func:`fftn`, :func:`rfft`, :func:`rffti`, :func:`rfftip`, :func:`rfftn`, :func:`rfftnp`

