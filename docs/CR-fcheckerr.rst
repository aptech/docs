
fcheckerr
==============================================

Purpose
----------------

Gets the error status of a file.

Format
----------------
.. function:: fcheckerr(fh)

    :param fh: file handle of a file opened with :func:`fopen`.
    :type fh: scalar

    :returns: **err** (*scalar*) - error status equal to 1 if there has been a read or write error on a file,
              0 otherwise.

Remarks
-------

If you pass :func:`fcheckerr` the handle of a file opened with :func:`open` (i.e., a
dataset or matrix file), your program will terminate with a fatal error.

Examples
----------

::

    // Create a file name with full path
    fname = getGAUSSHome() $+ "startup";
    
    // Open a file handle for
    // reading only from the file
    fh = fopen(fname, "r");
    
    // Try to write to the file using a read-only file handle
    ret = fputs(fh, "alpha,beta,gamma");
    
    // Check to see if there was a file i/o error
    if fcheckerr(fh);
        print "File write failed";
    endif;
    
    call close(fh);

After the above code, the program will print:

::

    File write failed
