
filesa
==============================================

Purpose
----------------

Returns a string array of file names.

Format
----------------
.. function:: filesa(fspec)

    :param fspec: file specification to search for. Can include path and wildcards.
    :type fspec: string

    :returns: **fnames** (*Nx1 string array*) - all file names that match or null string if none are found.

Remarks
-------

*fnames* will contain file names only; any path information that was passed is
dropped.


Examples
----------------

::

    fnames = filesa("ch*");

In this example all files listed in the
current directory that begin with :code:`"ch"` will be
returned.

::

    proc exist(filename);
       retp(not filesa(filename) $== "");
    endp;

This procedure will return 1 if the file exists or 0 if not.

.. seealso:: Functions :func:`fileinfo`, :func:`shell`
