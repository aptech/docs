
dffti
==============================================

Purpose
----------------

Computes inverse discrete Fourier transform.

Format
----------------
.. function:: y = dffti(x)

    :param x: values used to computer the inverse of the discrete Fourier transform.
    :type x: Nx1 vector

    :return y: the inverse discrete Fourier transform.

    :rtype y: Nx1 vector

Examples
----------------

::

    // Set k
    k = seqa(0, 1, 4);

    // Compute discrete frequencies
    f_k = 5 + 2 * cos(pi/2*k - 90*pi/180) + 3 * cos(pi*k);

After this ``f_k`` is equal to:

::

    8
    4
    8
    0

::

    // Discrete Fourier transform
    x = dfft(f_k);

    // Inverse Fourier transform
    y = dffti(x);

Now:

::

    x =   5
          0 -      1i
          3 +      0i
          0 +      1i

    y =   8 +      0i
          4 +      0i
          8 +      0i
          0 +      0i

Remarks
-------

The transform is divided by :math:`N`.

This uses a second-order Goertzel algorithm. It is considerably slower
than :func:`ffti`, but it may have some advantages in some circumstances. For
one thing, :math:`N` does not have to be an even power of 2.

Source
------

dffti.src

.. seealso:: :func:`fft`, :func:`dffti`, :func:`ffti`
