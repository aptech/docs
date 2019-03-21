
savestruct
==============================================

Purpose
----------------
Saves a matrix of structures to a file on the disk.

Format
----------------
.. function:: saveStruct(instance, file_name)

    :param instance: instances of a structure.
    :type instance: MxN matrix

    :param file_name: name of file on disk to contain matrix of structures.
    :type file_name: string

    :returns: retcode (*scalar*), 0 if successful, otherwise it will be non-zero.

Examples
----------------

::

    struct DS p0;
    p0 = reshape(dsCreate(), 2, 3);
    retc = saveStruct(p2, "p2");

