
shell
==============================================

Purpose
----------------
Executes an operating system command.

.. _shell:
.. index:: shell

Format
----------------

::

    shell stmt;

**Parameters**

:stmt: (*literal or ^string*) the command to be executed.


Examples
----------------

::

    comstr = "ls ./src";
    shell ^comstr;

This lists the contents of the *./src* subdirectory, then returns to GAUSS.

::

    shell cmp n1.fmt n1.fmt.old;

This compares the matrix file :file:`n1.fmt` to an older version of
itself, :file:`n1.fmt.old`, to see if it has changed.

When ``cmp`` finishes, control is returned to GAUSS.

::

    shell;

This executes an interactive shell. The OS prompt will appear and OS commands
or other programs can be executed. To return to GAUSS, type ``exit``.

Remarks
-------

`shell` lets you run `shell` commands and programs from inside GAUSS. If a
command is specified, it is executed; when it finishes, you
automatically return to GAUSS. If no command is specified, the shell is
executed and control passes to it, so you can issue commands
interactively. You have to type ``exit`` to get back to GAUSS in that case.

If you specify a command in a string variable, precede it with the ``^``
(caret) as shown in the examples below.

.. seealso:: Functions :func:`exec`
