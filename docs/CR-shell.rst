
shell
==============================================

Purpose
----------------
Executes an operating system command.

Format
----------------
.. function:: shell stmt

    :param stmt: , the command to be
        executed.
    :type stmt: literal or ^string

Examples
----------------

::

    comstr = "ls ./src";
    shell ^comstr;

This lists the contents of the ./src subdirectory, 
then returns to GAUSS.

::

    shell cmp n1.fmt n1.fmt.old;

This compares the matrix file n1.fmt to an older version of
itself, n1.fmt.old, to see if it has changed.
When cmp finishes, control is returned to GAUSS.

::

    shell;

This executes an interactive shell.
 The OS prompt will appear and OS
 commands or other programs can be executed. To
 return to GAUSS, type exit.

.. seealso:: Functions :func:`exec`
