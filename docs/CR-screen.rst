
screen
==============================================

Purpose
----------------

Controls output to the screen.

.. _screen:
.. index:: screen

Format
----------------

::

    screen on;
    screen off; 
    screen;

Remarks
-------

-  When this is on, the results of all `print` statements will be directed
   to the window. When this is off, `print` statements will not be sent to
   the window. This is independent of the statement output on, which
   will cause the results of all `print` statements to be routed to the
   current auxiliary output file.
-  If you are sending a lot of output to the auxiliary output file on a
   disk drive, turning the window off will speed things up.
-  The `end` statement will automatically perform output off and screen
   on.
-  `screen` with no arguments will print "Screen is on" or "Screen is off"
   on the console.
-  Changing the `screen` setting is NOT threadsafe and therefore, should
   not be done inside of `threadbegin`, `threadstat` or `threadfor` blocks.


Examples
----------------

::

    output file = mydata.asc reset;
    screen off;
    
    format /m1/rz 1,8;
    open fp = mydata;
    do until eof(fp);
        print readr(fp,200);;
    endo;
    fp = close(fp);
    end;

The program above will write the contents of the GAUSS file
*mydata.dat* into an ASCII file called *mydata.asc*. If *mydata.asc*
already exists, it will be overwritten. Turning the window 
off will speed up execution. The `end` statement
above will automatically perform ``output off`` and ``screen on``.

.. seealso:: Functions `output`, `end`, `new`

