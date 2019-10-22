
edit
==============================================

Purpose
----------------

Opens a file in the GAUSS programming editor.

Format
----------------
.. function:: edit filename

    :param filename: the name of the file to be opened.
    :type filename: literal

Examples
----------------

::

    edit test1.e;

Remarks
-------

The :func:`edit` command does not follow the `src_path` to locate files. You must
specify the location in the filename. The default location is the current directory.

To edit the last run file, use ``F7`` or the Action List toolbar.


.. seealso:: Functions `run`

