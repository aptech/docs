
fft
==============================================

Purpose
----------------

Computes a 1- or 2-D Fast Fourier transform.

Format
----------------
.. function:: y = fft(x)

    :param x: The values used to compute the Fast Fourier transform.
    :type x: NxK matrix

    :return y: where *L* and *M* are the smallest powers of 2 greater than or equal to *N* and *K*, respectively.

    :rtype y: LxM matrix

Examples
----------------
This is example uses the FFT to find the frequency component of a signal buried in a noise. The first section sets up the parameters for the signal of sampling frequency 1 kHz and a signal duration of 1.5 secs

::

      // Sampling frequency
      Fs = 1000;

      // Sampling period
      big_T = 1/Fs;

      // Length of signal
      L = 1500;

      // Time vector
      t = seqa(0, big_T, L);

Now form the signal given by

.. math:: 0.7*sin(2\pi50t) + sin(2\pi120t)

::

      // Compute signal
      s = 0.7*sin(2*pi*50*t) + sin(2*pi*120*t);

Corrupt the signal with zero-mean white noise:

::

    // Add white noise
    x = s + 2*rndn(L,1);

Finally, compute the Fourier transform:

::

  // Compute Fourier transform
  y = fft(x);


Remarks
-------

This computes the FFT of *x*, scaled by :math:`1/N`.

This uses a Temperton Fast Fourier algorithm.

If *N* or *K* is not a power of 2, *x* will be padded out with zeros before computing the transform.

.. seealso:: Functions :func:`ffti`, :func:`rfft`, :func:`rffti`
