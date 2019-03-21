
fileinfo
==============================================

Purpose
----------------

Returns names and information for files that match a specification.

Format
----------------
.. function:: fileinfo(fspec)

    :param fspec: file specification. Can include path.
        Wildcards are allowed in  fspec.
    :type fspec: string

    :returns: fnames (*Nx1 string array of all file names that match*), null string if none are found.

    :returns: finfo (*Nx13 matrix*), information about matching files.
        Linux

    .. csv-table::
        :widths: auto

        "[N, 1]", "filesystem ID"
        "[N, 2]", "inode number"
        "[N, 3]", "mode bit mask"
        "[N, 4]", "number of links"
        "[N, 5]", "user ID"
        "[N, 6]", "group ID"
        "[N, 7]", "device ID (char/block special files only)"
        "[N, 8]", "size in bytes"
        "[N, 9]", "last access time"
        "[N,10]", "last data modification time"
        "[N,11]", "last file status change time"
        "[N,12]", "preferred I/O block size"
        "[N,13]", "number of 512-byte blocks allocated"
        "Windows"
        "[N, 1]", "drive number (A = 0, B = 1, etc.)"
        "[N, 2]", "n/a, 0"
        "[N, 3]", "mode bit mask"
        "[N, 4]", "number of links, always 1"
        "[N, 5]", "n/a, 0"
        "[N, 6]", "n/a, 0"
        "[N, 7]", "n/a, 0"
        "[N, 8]", "size in bytes"
        "[N, 9]", "last access time"
        "[N,10]", "last data modification time"
        "[N,11]", "creation time"
        "[N,12]", "n/a, 0"
        "[N,13]", "n/a, 0"
        "finfo will be a scalar zero if no matches are found."



Remarks
-------

fnames will contain file names only; any path information that was
passed is dropped.

The time stamp fields (finfo[N,9:11]) are expressed as the number of
seconds since midnight, Jan. 1, 1970, Coordinated Universal Time (UTC).

