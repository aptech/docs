
locate
==============================================

Purpose
----------------

Positions the cursor in the window.

Format
----------------
.. function:: locate m, n

Remarks
-------

locate locates the cursor in the current output window.

m and n denote the row and column, respectively, at which the cursor is
to be located.

The origin (1,1) is the upper left corner.

mandn may be any expressions that return scalars. Nonintegers will be
truncated to an integer.


Examples
----------------

::

    r = csrlin;
    c = csrcol;
    cls;
    locate r,c;

In this example the window is cleared without affecting
the cursor position.

.. seealso:: Functions :func:`csrlin`, :func:`csrcol`
