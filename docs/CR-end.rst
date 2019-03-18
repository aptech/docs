
end
==============================================

Purpose
----------------

Terminates a program.

Format
----------------
.. function:: end

Examples
----------------

::

    output on;
    screen off;
    print x;
    end;

In this example, a matrix x is printed to the auxiliary output. The
output to the window is turned off to speed up the printing. The end statement
is used to terminate the program, so the output file will be closed
and the window turned back on.

.. seealso:: Functions :func:`new`, :func:`stop`, :func:`system`
