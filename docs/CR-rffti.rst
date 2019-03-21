
rffti
==============================================

Purpose
----------------

Computes inverse real 1- or 2-D Fast Fourier transform.

Format
----------------
.. function:: rffti(x)

    :param x: 
    :type x: NxK matrix

    :returns: y (*LxM real matrix*), where L and M are the smallest
        prime factor products greater than or equal to N and K.



Remarks
-------

It is up to the user to guarantee that the input will return a real
result. If in doubt, use ffti.

