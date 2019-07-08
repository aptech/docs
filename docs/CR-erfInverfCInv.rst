
erfInv,erfCInv
==============================================

Purpose
----------------

Computes the inverse of the Gaussian error function (:func:`erfInv`) and its complement (:func:`erfcInv`).

Format
----------------
.. function:: erfInv(y);
              erfCInv(y)

    :param y:  Gaussian error function values. :math:`-1 < y < 1`
    :type y: scalar or NxK matrix

    :returns: **x** (*scalar or NxK matrix*) - The inverse of the Gaussian error function.

Examples
----------------

First find the Gaussian error function values for a vector of 10 sequential values starting at 0.1 and incrementing by 0.1:

::

    /*
    ** Set x equal to 10 sequential values
    ** starting at .1 with an increment of
    ** 0.1
    */
    x = seqa(.1, .1, 10);

    // Find Gaussian error function
    y = erf(x);

This results in:

::

        0.1000       0.1125
        0.2000       0.2227
        0.3000       0.3286
        0.4000       0.4284
    x = 0.5000   y = 0.5205
        0.6000       0.6039
        0.7000       0.6778
        0.8000       0.7421
        0.9000       0.7969
        1.0000       0.8427

Now find the inverse Gaussian error function of ``y`:

::

    print erfInv(y);

::

        0.1000
        0.2000
        0.3000
        0.4000
        0.5000
        0.6000
        0.7000
        0.8000
        0.9000
        1.0000

Also finding the complement of the inverse Gaussian error function:

::

    print erfCInv;

::

        1.122
        0.862
        0.691
        0.560
        0.454
        0.367
        0.294
        0.233
        0.182
        0.140

.. seealso:: Functions :func:`erf`, :func:`erfc`, :func:`cdfN`, :func:`cdfNC`, :func:`cdfNi`
