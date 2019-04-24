
nextn, nextnevn
==============================================

Purpose
----------------

Returns allowable matrix dimensions for computing FFT's.

Format
----------------
.. function:: nextn(n0) 
              nextnevn(n0)

    :param n0: the length of a vector or the number of rows or columns in a matrix.
    :type n0: scalar

    :returns: n (*scalar*), the next allowable size for the given dimension
        for computing an FFT or RFFT. :math:`n > n0`.

Remarks
-------

:func:`nextn` and :func:`nextnevn` determine allowable matrix dimensions for computing
FFT's. The Temperton FFT routines (see table below) can handle any matrix whose dimensions can be expressed as:

.. math::

   2px3qx5rx7s

.. DANGER:: fix equations

where *p*, *q* and *r* are nonnegative integers and *s* is equal to 0 or 1.

with one restriction: the vector length or matrix column size must be even (*p* must be positive) when computing RFFT's.

:func:`fftn`, etc., automatically pad matrices (with zeros) to the next allowable dimensions; :func:`nextn` and :func:`nextnevn` 
are provided in case you want to check or fix matrix sizes yourself.

Use the following table to determine what to call for a given function and matrix:

.. csv-table::
    :widths: auto
    :header-rows: 2

    "FFT", "Vector", "Matrix", "Matrix"
    "Function", "Length", "Rows", "Columns"
    ":func:`fftn`", ":func:`nextn`", ":func:`nextn`", ":func:`nextn`"
    ":func:`rfftn`", ":func:`nextnevn`", ":func:`nextn`", ":func:`nextnevn`"
    ":func:`rfftnp`", ":func:`nextnevn`", ":func:`nextn`", ":func:`nextnevn`"

Examples
----------------

::

    n = nextn(456);

The code above will assign *n* to be equal to 480.

Source
------

optim.src

.. seealso:: Functions :func:`fftn`, :func:`optn`, :func:`optnevn`, :func:`rfftn`, :func:`rfftnp`

