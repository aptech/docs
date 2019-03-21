
edit
==============================================

Purpose
----------------

Edits a disk file.

Format
----------------
.. function:: edit filename

    :param filename: the name of the file to be edited.
    :type filename: literal

Remarks
-------

The edit command does not follow the src_path to locate files. You must
specify the location in the filename. The default location is the
current directory.

To edit the last run file, use F7 or the Action List toolbar.


Examples
----------------

::

    edit test1.e;

.. seealso:: Functions :func:`run`
