
where
==============================================

Purpose
----------------

Returns elements of either ``a`` or ``b`` depending on ``condition``

Format
----------------
.. function:: c = where(condition, a, b)

    :param condition: Binary matrix where a 1 indicates an element should be selected from ``a`` and a 0 indicates an element should be selected from ``b``.
    :type condition: NxK matrix

    :param a: The elements to return where ``condition`` equals 1.
    :type a: Scalar, Nx1 vector, 1xK matrix or NxK matrix

    :param b: The elements to return where ``condition`` equals 0.
    :type b: Scalar, Nx1 vector, 1xK matrix or NxK matrix

    :return c: The combined data.
    :rtype c: NxK matrix

Examples
----------------

Basic usage
++++++++++++++++

::

    condition = { 1 0 0,
                  0 1 0 };

    a = { 1 2 3,
          4 5 6 };
    b = { 10 20 30,
          40 50 60 };

    c = where(condition, a, b);

The code above assigns *c* to be equal to:

::

       1       20       30 
      40        5       60


Vectors and scalars will be expanded to fit the dimensions of the larger inputs.

::

    condition = { 1 0 0,
                  0 1 0 };

    a = { 1 2 3 };
    b = { 10,
          40 };

    c = where(condition, a, b);

As we see in the result below, the row vector ``a`` has been broadcast as if it was a 2x3 matrix with the same elements in each row, while the column vector ``b`` has been broadcast as if it was a 2x3 matrix with the same elements in each column.

::

       1       10       10 
      40        2       40

Remarks
-------

* To return the elements with the greatest (or least) magnitude among two matrices, use :func:`maxv` (or :func:`minv`).
* To replace elements according to a binary matrix or vector, use :func:`missex`.

.. seealso:: Functions :func:`indexcat`, :func:`minv`, :func:`maxv', :func:`missex`, :func:`reclassify`, :func:`reclassifycuts`
