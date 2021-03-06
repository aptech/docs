
searchsourcepath
==============================================

Purpose
----------------

Searches the source path and (if specified) the src
subdirectory of the GAUSS installation directory for a
specified file.

Format
----------------
.. function:: fpath = searchsourcepath(fname, srcdir)

    :param fname: name of file to search for.
    :type fname: string

    :param srcdir: one of the following:
    :type srcdir: scalar

    .. csv-table::
        :widths: auto

        "0    do not search in the src subdirectory of the GAUSS 				installation directory."
        "1    search the src subdirectory first."
        "2    search the src subdirectory last."

    :return fpath: the path of *fname*, or
        null string if *fname* is not found.

    :rtype fpath: string

Remarks
-------

The source path is set by the :file:`src_path` configuration variable in your
GAUSS configuration file, :file:`gauss.cfg`.
