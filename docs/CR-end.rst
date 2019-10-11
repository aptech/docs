
end
==============================================

Purpose
----------------

Terminates a program.

.. _end:
.. index:: end:

Format
----------------

::

    end

Examples
----------------

::

    // Turn on auxiliary output
    output on;

    // Turn off screen
    screen off;

    // Print x
    print x;

    // End program
    end;

In this example, a matrix *x* is printed to the auxiliary output. The
output to the window is turned off to speed up the printing. The `end` statement
is used to terminate the program, so the output file will be closed
and the window turned back on.

Remarks
-------

The `end` statement causes GAUSS to revert to interactive mode, and closes all open
files. The `end` statement also closes the auxiliary output file and sets `screen` command to on.
It is not necessary to put an `end` statement at the end of a program.

An `end` statement can be placed above a label which begins a subroutine to
make sure that a program does not enter a subroutine without a `gosub`.

The `stop` statement also terminates a program but closes no files and leaves the `screen`
setting as it is.


.. seealso:: Functions `new`, `stop`, `system`
