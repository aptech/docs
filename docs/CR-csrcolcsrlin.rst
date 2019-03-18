
csrcol,csrlin
==============================================

Purpose
----------------

Returns the position of the cursor.

Format
----------------
.. function:: csrcol 
			  csrlin

    :returns: y (*scalar*), row or column value.

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
