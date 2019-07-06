
ed
==============================================

Purpose
----------------

Accesses an alternate editor.

Format
----------------
.. function:: ed filename

    :param filename: the name of the file to be edited.
    :type filename: literal



Remarks
-------

The default name of the editor is set in ``gauss.cfg``. To change the name
of the editor used from within a GAUSS session enter:

::

   ed = editor_name flags;

or

::

   ed = "editor_name flags";

The flags are any command line flags you may want between the name of
the editor and the filename when your editor is invoked. The quoted
version will prevent the flags, if any, from being forced to uppercase.

This command can be placed in the startup file, so it will be set for
you automatically when you start GAUSS.

See the edit command to open a file in the GAUSS editor from the command
line.
