
searchsourcepath
==============================================

Purpose
----------------

Searches the source path and (if specified) the src 
subdirectory of the GAUSS installation directory for a 
specified file. 

Format
----------------
.. function:: searchsourcepath(fname, srcdir)

    :param fname: name of file to search for.
    :type fname: string

    :param srcdir: one of the following:
    :type srcdir: scalar

    .. csv-table::
        :widths: auto

        "0    do not search in the src subdirectory of the GAUSS 				installation directory."
        "1    search the src subdirectory first."
        "2    search the src subdirectory last."

    :returns: fpath (*string*), the path of  fname, or
        null string if  fname is not found.



Remarks
-------

The source path is set by the src_path configuration variable in your
GAUSSconfiguration file, gauss.cfg.

