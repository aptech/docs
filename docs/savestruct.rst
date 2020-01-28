
savestruct
==============================================

Purpose
----------------
Saves a matrix of structures to a file on the disk.

Format
----------------
.. function:: retcode = saveStruct(instance, file_name)

    :param instance: instances of a structure.
    :type instance: MxN matrix

    :param file_name: name of file on disk to contain matrix of structures.
    :type file_name: string

    :return retcode: 0 if successful, otherwise it will be non-zero.

    :rtype retcode: scalar

Examples
----------------

::

    // Create DS structure
    struct DS p0;
    p0 = reshape(dsCreate(), 2, 3);

    // Save the p0 DS structure as p2
    retc = saveStruct(p0, "p2");

Remarks
-------

The file on the disk will be given a :file:`.fsr` extension
