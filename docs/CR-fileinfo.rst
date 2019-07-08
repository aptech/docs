
fileinfo
==============================================

Purpose
----------------

Returns names and information for files that match a specification.

Format
----------------
.. function:: fileinfo(fspec)

    :param fspec: file specification. Can include path. Wildcards are allowed in *fspec*.
    :type fspec: string

    :returns: **fnames** (*Nx1 string array*) - all file names that match, null string if none are found.

    :returns: **finfo** (*Nx13 matrix*) - information about matching files.

        **Linux**

        .. csv-table::
            :widths: auto

            ":math:`[N, 1]`", "filesystem ID"
            ":math:`[N, 2]`", "inode number"
            ":math:`[N, 3]`", "mode bit mask"
            ":math:`[N, 4]`", "number of links"
            ":math:`[N, 5]`", "user ID"
            ":math:`[N, 6]`", "group ID"
            ":math:`[N, 7]`", "device ID (char/block special files only)"
            ":math:`[N, 8]`", "size in bytes"
            ":math:`[N, 9]`", "last access time"
            ":math:`[N,10]`", "last data modification time"
            ":math:`[N,11]`", "last file status change time"
            ":math:`[N,12]`", "preferred I/O block size"
            ":math:`[N,13]`", "number of 512-byte blocks allocated"

        **Windows**

        .. csv-table::
            :widths: auto

            ":math:`[N, 1]`", "drive number (A = 0, B = 1, etc.)"
            ":math:`[N, 2]`", "n/a, 0"
            ":math:`[N, 3]`", "mode bit mask"
            ":math:`[N, 4]`", "number of links, always 1"
            ":math:`[N, 5]`", "n/a, 0"
            ":math:`[N, 6]`", "n/a, 0"
            ":math:`[N, 7]`", "n/a, 0"
            ":math:`[N, 8]`", "size in bytes"
            ":math:`[N, 9]`", "last access time"
            ":math:`[N,10]`", "last data modification time"
            ":math:`[N,11]`", "creation time"
            ":math:`[N,12]`", "n/a, 0"
            ":math:`[N,13]`", "n/a, 0"

        *finfo* will be a scalar zero if no matches are found.

Remarks
-------

*fnames* will contain file names only; any path information that was
passed is dropped.

The time stamp fields (:math:`finfo[N, 9:11]`) are expressed as the number of
seconds since midnight, Jan. 1, 1970, Coordinated Universal Time (UTC).

.. seealso:: Functions :func:`filesa`
