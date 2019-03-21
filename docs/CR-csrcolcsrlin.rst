
csrcol, csrlin
==============================================

Purpose
----------------

Returns the position of the cursor.

Format
----------------
.. function:: csrcol 
              csrlin

    :returns: y (*scalar*), row or column value.

Remarks
-------

*y* will contain the current column or row position of the cursor on the
screen. The upper left corner is (1,1).

:func:`csrcol` returns the column position of the cursor. :func:`csrlin` returns the row
position.

The :func:`locate` commmand allows the cursor to be positioned at a specific row
and column.

:func:`csrcol` returns the cursor column with respect to the current output
line, i.e., it will return the same value whether the text is wrapped or
not. :func:`csrlin` returns the cursor line with respect to the top line in the
window.

Examples
----------------

::

    r = csrlin;
    c = csrcol;
    
    //Clear the program input/output window
    cls;
    
    //Re-position the cursor to its location before the program 
    //input/output window was cleared
    locate r,c;

In this example the screen is cleared without
affecting the cursor position.

.. seealso:: Functions :func:`cls`, :func:`locate`

