
screen
==============================================

Purpose
----------------

Controls output to the screen.

Format
----------------
.. function:: screen on 
			  screen off 
			  screen

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
mydata.dat into an ASCII file called 
mydata.asc. If mydata.asc
already exists, it will be overwritten.
Turning the window off will speed up execution. The end statement
above will automatically perform output off and screen on.

.. seealso:: Functions :func:`output`, :func:`end`, :func:`new`
