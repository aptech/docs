
findIdx
==============================================

Purpose
----------------
Returns the indices of elements where a condition is true.

Format
----------------
.. function:: idx = findIdx(cond)

    :param cond: boolean vector of 0s and 1s, typically the result of an element-wise comparison such as ``x .> 0``. Both column vectors and row vectors are accepted.
    :type cond: Nx1 or 1xN vector

    :return idx: the row indices where *cond* is nonzero. If no elements are nonzero, a scalar missing value is returned.

    :rtype idx: Mx1 vector

Examples
----------------

Find indices of positive elements
++++++++++++++++++++++++++++++++++++++++++++

::

    x = { 3, -1, 5, -2, 7 };

    idx = findIdx(x .> 0);

After the above code, ``idx`` will equal:

::

    1
    3
    5

Use indices to extract matching elements
++++++++++++++++++++++++++++++++++++++++++++

::

    x = { 3, -1, 5, -2, 7 };

    // Get indices where x is negative
    idx = findIdx(x .< 0);

    // Extract those elements
    neg_vals = x[idx];

After the above code, ``neg_vals`` will equal:

::

    -1
    -2

Remarks
-------

.. versionadded:: 26.0.1

:func:`findIdx` is equivalent to::

    idx = selif(seqa(1, 1, rows(cond)), cond);

If you only need the matching *values* (not their indices), use :func:`selif` directly::

    pos_vals = selif(x, x .> 0);

.. seealso:: Functions :func:`selif`, :func:`delif`, :func:`indexcat`, :func:`ismiss`
