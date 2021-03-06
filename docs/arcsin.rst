
arcsin
==============================================

Purpose
----------------
Computes the inverse sine.

Format
----------------
.. function:: y = arcsin(x)

    :param x: 
    :type x: NxK matrix or N-dimensional array

    :return y: the angle in radians whose sine is *x*.

    :rtype y: NxK matrix or N-dimensional array

Examples
----------------

::

    // Set 'x' to be the sequence -1, -0.5, 0, 0.5, 1
    x = seqa(-1, 0.5, 5);
    y = arcsin(x);

Assigns *y* to be equal to:

::

    -1.5707963
    -0.52359878
     0.00000000
     0.52359878
     1.5707963

Remarks
-------

If *x* is complex or has any elements whose absolute value is greater than
1, complex results are returned.

Source
------------

trig.src

