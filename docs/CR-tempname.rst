
tempname
==============================================

Purpose
----------------

Creates a temporary file with a unique name.

Format
----------------
.. function:: tempname(path,  pre,  suf)

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

