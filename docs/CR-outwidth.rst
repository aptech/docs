
outwidth
==============================================

Purpose
----------------

Specifies the width of the auxiliary output.

.. _outwidth:
.. index:: outwidth

Format
----------------

::

    outwidth n;

**Paramters:**

:n: (*scalar*) width of auxilary output.

Remarks
-------

*n* specifies the width of the auxiliary output in columns (characters).
After printing *n* characters on a line, GAUSS will output a line feed.

If a matrix is being printed, the line feed sequence will always be
inserted between separate elements of the matrix rather than being
inserted between digits of a single element.

*n* may be any scalar-valued expressions in the range of 2-256.
Nonintegers will be truncated to an integer. If 256 is used, no
additional lines will be inserted.

The default is setting is 256.


Examples
----------------

::

    outwidth 132;

This statement will change the auxiliary output width to 132 columns.

.. seealso:: Functions `output`, :func:`print`

