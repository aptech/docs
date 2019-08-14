
fileinfo
==============================================

Purpose
----------------

Returns names and information for files that match a specification.

Format
----------------
.. function:: { fnames, finfo } = fileinfo(fspec)

    :param fspec: file specification. Can include path and wildcards.
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

Examples
----------------

::

    { fnames, finfo} = fileinfo("fourier_*");

    // Print results
    print "File names"; fnames;
    print "File information"; finfo;

This prints results about all files starting with ``fourier_`` in the current working directory:

::

    File names

      fourier_adf.e
    fourier_adf_rev.e
    fourier_adf_turkish.e

    File information

    2.0000   0.0000 33206.0000   1.0000   0.0000   0.0000   0.0000 1270.0000 1559719168.0000 1559719168.0000 1559718437.0000   0.0000   0.0000
    2.0000   0.0000 33206.0000   1.0000   0.0000   0.0000   0.0000 1270.0000 1559719236.0000 1559719236.0000 1559719236.0000   0.0000   0.0000
    2.0000   0.0000 33206.0000   1.0000   0.0000   0.0000   0.0000 1277.0000 1562820073.0000 1562820073.0000 1562820032.0000   0.0000   0.0000

Remarks
-------

*fnames* will contain file names only; any path information that was
passed is dropped.

The time stamp fields (``finfo[N, 9:11]``) are expressed as the number of
seconds since midnight, Jan. 1, 1970, Coordinated Universal Time (UTC).

.. seealso:: Functions :func:`filesa`
