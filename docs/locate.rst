
locate
==============================================

Purpose
----------------

Positions the cursor in the window.

.. _locate:
.. index:: locate

Format
----------------

::

    locate m, n;

Examples
----------------

::

    // Get current row position of cursor
    r = csrlin;

    // Get current column positin of cursor
    c = csrcol;

    // Clear screen
    cls;

    // Place cursor at r, c
    locate r,c;

In this example the window is cleared without affecting
the cursor position.

Remarks
-------

`locate` locates the cursor in the current output window.

*m* and *n* denote the row and column, respectively, at which the cursor is
to be located.

The origin (1,1) is the upper left corner.

*m* and *n* may be any expressions that return scalars. Non-integers will be
truncated to an integer.


.. seealso:: Functions :func:`csrlin`, :func:`csrcol`

