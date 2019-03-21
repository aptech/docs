
cond
==============================================

Purpose
----------------

Computes the condition number of a matrix using the singular value decomposition.

Format
----------------
.. function:: cond(x)

    :param x: 
    :type x: NxK matrix

    :returns: c (*scalar*), an estimate of the condition number of *x*.
        This equals the ratio of the largest singular
        value to the smallest. If the smallest singular
        value is zero or not all of the singular values
        can be computed, the return value is 10300.

Examples
----------------

::

    x = { 4 2 6,
          8 5 7,
          3 8 9 };
     
    y = cond(x);

will assign *y* to equal:

::

    y = 9.8436943

Source
------------

svd.src

