
dfft
==============================================

Purpose
----------------

Computes a discrete Fourier transform.

Format
----------------
.. function:: dfft(x)

    :param x: 
    :type x: Nx1 vector

    :returns: y (*TODO*), Nx1 vector.



Remarks
-------

The transform is divided by N.

This uses a second-order Goertzel algorithm. It is considerably slower
than fft, but it may have some advantages in some circumstances. For one
thing, N does not have to be an even power of 2.

