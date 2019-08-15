
new
==============================================

Purpose
----------------

Erases everything in memory including the symbol table; closes all open files as well as the auxiliary output and turns
the window on if it was off; also allows the size of the new symbol table and the main program space to be specified.

.. _new:
.. index:: new

Format
----------------

::

    new;
    new nos;

**Parameters:**

:nos: optional input which indicates the maximum number of global symbols allowed.

Remarks
-------

Procedures, user-defined functions, and global matrices, strings, and
string arrays are all global symbols.

If you would like your user-defined procedures to not be cleared after a
new statement, you can either add them to a GAUSS Library or create a
file in your `GAUSSHOME` directory with the same name as your procedure
and a .g file extension. This file :file:`.g` file should only contain your
procedure.

This command can be used with arguments as the first statement in a
program to clear the symbol table and to allocate only as much space for
program code as your program actually needs. When used in this manner,
the auxiliary output will not be closed. This will allow you to open the
auxiliary output from the command level and run a program without having
to remove the new at the beginning of the program. If this command is
not the first statement in your program, it will cause the program to
terminate.


Examples
----------------

::

    new; /* clear global symbols. */

::

    new 300; /* clear global symbols,set maximum
             ** number of global symbols to 300,
             ** and leave program space unchanged.
             */

.. seealso:: Functions :func:`clear`, `delete`, `output`

