
erfInv,erfCInv
==============================================

Purpose
----------------

Computes the inverse of the Gaussian error function (erfInv) and its complement (erfcInv).

Format
----------------
.. function:: erfCInv(y)

    :param y:  -1 < y < 1.
    :type y: scalar or NxK matrix

    :returns: x (*scalar or NxK matrix*) .

Examples
----------------

::

    x = seqa(.1,.1,10);
    y = erf(x);

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

.. seealso:: Functions :func:`erf`, :func:`erfc`, :func:`cdfN`, :func:`cdfNC`, :func:`cdfNi`

inverse complement Gaussian error function
