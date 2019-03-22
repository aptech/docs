
dos
==============================================

Purpose
----------------

Provides access to the operating system from within GAUSS.

Format
----------------
.. function:: dos commd

    :param commd: the OS command to be executed.
    :type commd: literal or ^string

Remarks
-------

This allows all operating system commands to be used from within GAUSS.
It allows other programs to be run even though GAUSS is still resident
in memory.

If no operating system command (for instance, ``dir`` or ``copy``) or program
name is specified, then a shell of the operating system will be entered
which can be used just like the base level OS. The ``exit`` command must be
given from the shell to get back into GAUSS. If a command or program
name is included, the return to GAUSS is automatic after the OS command
has been executed.

All matrices are retained in memory when the OS is accessed in this way.
This command allows the use of word processing, communications, and
other programs from within GAUSS.

Do not execute programs that terminate and remain resident because they
will be left resident inside of GAUSS's workspace. Some examples are
programs that create RAM disks or print spoolers.

If the command is to be taken from a string variable, the ``^`` (caret) must
precede the string.

The shorthand "``>``" can be used in place of ":code:`dos`".


Examples
----------------

::

    cmdstr = "atog mycfile";
    dos ^cmdstr;

This will run the ATOG utility, using mycfile.cmd
as the ATOG command file. For more information, see `ATOG, Chapter 1`.

.. DANGER:: link up chapter

::

    > dir *.prg;

This will use the DOS ``dir`` command to print a
directory listing of all files with a .prg
extension on Windows. When the listing is finished, control
will be returned to GAUSS.

::

    > ls *.prg

This will perform the same operation on Linux.

::

    dos;

This will cause a second level OS shell to be
entered. The OS prompt will appear and OS
commands or other programs can be executed. To
return to GAUSS, type ``exit``.

.. seealso:: Functions :func:`exec`

