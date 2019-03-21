
loadstruct
==============================================

Purpose
----------------

Loads a structure into memory from a file on the disk.

Format
----------------
.. function:: loadstruct(file_name, structure_type)

    :param file_name: name of file containing structure.
    :type file_name: string

    :param structure_type: structure type.
    :type structure_type: string

    :returns: instance (*TODO*), instance of the structure.

    :returns: retcode (*scalar*), 0 if successful, otherwise 1.

Remarks
-------

instancecan be an array of structures.


Examples
----------------

::

    #include ds.sdf
    struct DS p3;
     
    { p3, retc } = loadstruct("p2", "ds");

