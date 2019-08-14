
seekr
==============================================

Purpose
----------------
Moves the pointer in a *.dat* or *.fmt* file to a particular row.

Format
----------------
.. function:: y = seekr(fh, r)

    :param fh: file handle of an open file.
    :type fh: scalar

    :param r: the row number to which the pointer is to be moved.
    :type r: scalar

    :returns: y (*scalar*), the row number to which the pointer has been moved.

Remarks
-------

If *r* = -1, the current row number will be returned.

If *r* = 0, the pointer will be moved to the end of the file, just past the end of the last row.

:func:`rowsf` returns the number of rows in a file.

::

   seekr(fh,0) == rowsf(fh) + 1;

.. DANGER:: Do NOT try to seek beyond the end of a file.

.. seealso:: Functions `open`, :func:`readr`, :func:`rowsf`

