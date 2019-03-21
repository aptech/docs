
tempname
==============================================

Purpose
----------------

Creates a temporary file with a unique name.

Format
----------------
.. function:: tempname(path, pre, suf)

    :param path: path where the file will reside.
    :type path: string

    :param pre: a prefix to begin the file name with.
    :type pre: string

    :param suf: a suffix to end the file name with.
    :type suf: string

    :returns: tname (*string*), unique temporary file name of the form
        path/preXXXXnnnnnsuf,
        where XXXX are 4 letters, and nnnnn
        is the process id of the calling process.



Remarks
-------

Any or all of the inputs may be a null string or 0. If path is not
specified, the current working directory is used.

If unable to create a unique file name of the form requested, tempname
returns a null string.

WARNING: GAUSS does not remove temporary files created by tempname. It
is left to the user to remove them when they are no longer needed.

