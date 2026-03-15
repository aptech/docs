
stop
==============================================

Purpose
----------------

Stops a program and returns to the command prompt. Does not close files.

.. _stop:
.. index:: stop

Format
----------------

::

    stop;

Remarks
-------

This command has the same effect as `end`, except it does not close files
or the auxiliary output.

It is not necessary to put a `stop` or an `end` statement at the end of a
program. If neither is found, an implicit `stop` is executed.

Examples
--------

::

    // Stop program execution without closing files
    x = rndn(3, 3);
    print x;
    stop;
    // Code below this point will not execute
    print "This will not print";

.. seealso:: Functions `end`, `new`, `system`

