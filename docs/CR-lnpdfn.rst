
lnpdfn
==============================================

Purpose
----------------

Computes standard Normal log-probabilities.

Format
----------------
.. function:: lnpdfn(x)

    :param x: , data.
    :type x: NxK matrix or N-dimensional array

    :returns: z (NxK matrix or N-dimensional array) log-probabilities.

Examples
----------------

::

    x = { -2, -1, 0, 1, 2 };
    z = lnpdfn(x);

::

    -2.9189385 
        -1.4189385 
    z = -0.9189385
        -1.4189385 
        -2.9189385

