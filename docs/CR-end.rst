
end
==============================================

Purpose
----------------

Terminates a program.

Format
----------------
.. function:: end

Remarks
-------

`end` causes GAUSS to revert to interactive mode, and closes all open
files. `end` also closes the auxiliary output file and turns the window
on. It is not necessary to put an `end` statement at the end of a program.

An `end` command can be placed above a label which begins a subroutine to
make sure that a program does not enter a subroutine without a `gosub`.

:func:`stop` also terminates a program but closes no files and leaves the window
setting as it is.


Examples
----------------

::

    output on;
    screen off;
    print x;
    end;

In this example, a matrix *x* is printed to the auxiliary output. The
output to the window is turned off to speed up the printing. The `end` statement
is used to terminate the program, so the output file will be closed
and the window turned back on.

.. seealso:: Functions :func:`new`, :func:`stop`, :func:`system`

