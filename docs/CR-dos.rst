
dos
==============================================

Purpose
----------------

Provides access to the operating system from within GAUSS.

Format
----------------
.. function:: dos commd

    :param commd: literal or ^string, the OS command to be executed.
    :type commd: TODO

Examples
----------------

::

    cmdstr = "atog mycfile";
    dos ^cmdstr;

This will run the ATOG utility, using mycfile.cmd
as the ATOG command file. For more information, see  ATOG, Chapter  1.

::

    > dir *.prg;

This will use the DOS dir command to print a
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
return to GAUSS, type exit.

.. seealso:: Functions :func:`exec`
