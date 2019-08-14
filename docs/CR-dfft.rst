
dfft
==============================================

Purpose
----------------

Computes a discrete Fourier transform.

Format
----------------
.. function:: y = dfft(x)

    :param x: Values used to compute the discrete Fourier transform.
    :type x: Nx1 vector

    :return y: The discrete Fourier transform.

    :type y: Nx1 vector

Remarks
-------

The transform is divided by :math:`N`.

This uses a second-order Goertzel algorithm. It is considerably slower
than :func:`fft`, but it may have some advantages in some circumstances. For one
thing, :math:`N` does not have to be an even power of 2.

Examples
----------------

In this example we will a use a discrete sample of frequencies given by

.. math::

    f[k] = 5 + 2 * cos(\frac{\pi}{2}k - \frac{\pi}{2}) + 3cos(\pi k)

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

Now take the discrete Fourier transform of ``f_k``:

::

    // Discrete Fourier transform
    print dfft(f_k);

After the code the discrete Fourier transform is printed:

::

    5
    0 - 1i
    3 + 0i
    0 + 1i


Source
------

dfft.src

.. seealso:: :func:`dffti`, :func:`fft`, :func:`ffti`
