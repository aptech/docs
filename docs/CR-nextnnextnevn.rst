
nextn, nextnevn
==============================================

Purpose
----------------

Returns allowable matrix dimensions for computing FFT's.

Format
----------------
.. function:: n = nextn(n0)
              n = nextnevn(n0)

    :param n0: the length of a vector or the number of rows or columns in a matrix.
    :type n0: scalar

    :return n: the next allowable size for the given dimension
        for computing an FFT or RFFT. :math:`n > n0`.

    :rtype n: scalar

Examples
----------------

::

    n = nextn(456);

The code above will assign *n* to be equal to 480.

Remarks
-------

The Temperton FFT routines (see table below) can handle any matrix whose dimensions can be expressed as:

.. math::

   2p \times 3q \times 5r \times 7s

where *p*, *q* and *r* are nonnegative integers and *s* is equal to 0 or 1.

The one restriction is that the vector length or matrix column size must be even (*p* must be positive) when computing RFFT's.

The :func:`fftn`, etc., functions will automatically pad matrices (with zeros) to the next allowable dimensions. The functions :func:`nextn` and :func:`nextnevn` are provided in case you want to check or fix matrix sizes yourself.

Use the following table to determine what to call for a given function and matrix:

.. csv-table::
    :widths: auto
    :header-rows: 2

    "FFT", "Vector", "Matrix", "Matrix"
    "Function", "Length", "Rows", "Columns"
    ":func:`fftn`", ":func:`nextn`", ":func:`nextn`", ":func:`nextn`"
    ":func:`rfftn`", ":func:`nextnevn`", ":func:`nextn`", ":func:`nextnevn`"
    ":func:`rfftnp`", ":func:`nextnevn`", ":func:`nextn`", ":func:`nextnevn`"

Source
------

optim.src

.. seealso:: Functions :func:`fftn`, :func:`optn`, :func:`optnevn`, :func:`rfftn`, :func:`rfftnp`
