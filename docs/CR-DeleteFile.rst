
deleteFile
==============================================

Purpose
----------------

Deletes files.

Format
----------------
.. function:: ret = deleteFile(name)

    :param name: name of file or files to delete.
    :type name: string or NxK string array

    :return ret: scalar if *name* is a string. If *name* is an NxK
        string array, *ret* will be an NxK matrix reflecting the success or
        failure of each separate file deletion. *ret* will be zero if file deletion is successful.

    :type ret: scalar or NxK matrix

Remarks
-------

:func:`deleteFile` calls the C library ``unlink`` function for each file. If ``unlink``
fails it sets the C library ``errno`` value. :func:`deleteFile` returns the value of
``errno`` if ``unlink`` fails, otherwise it returns zero. If you want detailed
information about the reason for failure, consult the C library ``unlink``
documentation for your platform for details.

Examples
----------------

::

    // Create random x matrix
    x = rndn(500,1);

    // Save as GAUSS dataset
    saved(x, "x.dat", "X1");

    // Delete file
    deleteFile("x.dat");

This returns

::

    0.00000000

Now we will try again to delete the ``x.dat`` file :

::

    // Delete file
    deleteFile("x.dat");

This returns

::

    2.0000000

The ``errno`` value of 2 indicates that the file ``x.dat`` no longer exists when we try to delete the file the second time.

