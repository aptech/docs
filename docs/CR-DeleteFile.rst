
deleteFile
==============================================

Purpose
----------------

Deletes files.

Format
----------------
.. function:: deleteFile(name)

    :param name: name of file or files to delete.
    :type name: string or NxK string array

    :returns: ret (*scalar or NxK matrix*), 0 if successful.



Remarks
-------

The return value, ret, is scalar if name is a string. If name is an NxK
string array, ret will be an NxK matrix reflecting the success or
failure of each separate file deletion.

deleteFile calls the C library unlink function for each file. If unlink
fails it sets the C library errno value. deleteFile returns the value of
errno if unlink fails, otherwise it returns zero. If you want detailed
information about the reason for failure, consult the C library unlink
documentation for your platform for details.

