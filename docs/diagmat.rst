
diagmat
==============================================

Purpose
----------------
Creates a diagonal matrix from a vector.

Format
----------------
.. function:: D = diagmat(v)

    :param v: the diagonal elements.
    :type v: Nx1 or 1xN vector

    :return D: with *v* on the diagonal and zeros elsewhere.

    :rtype D: NxN matrix

Examples
----------------

Basic usage
++++++++++++++++++++++++++++++++++++++++++++

::

    v = { 1, 2, 3 };

    D = diagmat(v);

After the above code, ``D`` will equal:

::

    1 0 0
    0 2 0
    0 0 3

Round-trip with diag
++++++++++++++++++++++++++++++++++++++++++++

::

    v = { 5, 10, 15 };

    // Create diagonal matrix, then extract diagonal
    D = diagmat(v);
    v2 = diag(D);

After the above code, ``v2`` will equal ``v``.

Remarks
-------

.. versionadded:: 26.0.1

:func:`diagmat` creates a new diagonal matrix. To extract the diagonal of an existing matrix, use :func:`diag`. To replace the diagonal of an existing matrix, use :func:`diagrv`.

.. seealso:: Functions :func:`diag`, :func:`diagrv`, :func:`eye`
