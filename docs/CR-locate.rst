
locate
==============================================

Purpose
----------------

Positions the cursor in the window.

Format
----------------
.. function:: locate m, n

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
