
loadstruct
==============================================

Purpose
----------------

Loads a structure into memory from a file on the disk.

Format
----------------
.. function:: { instance, retcode } = loadstruct(file_name, structure_type)

    :param file_name: name of file containing structure.
    :type file_name: string

    :param structure_type: structure type.
    :type structure_type: string

    :returns: instance (*struct*) instance of the struct.

    :returns: retcode (*scalar*), 0 if successful, otherwise 1.

Remarks
-------

*instance* can be an array of structures.


Examples
----------------

::

    #include ds.sdf
    struct DS p3;
     
    { p3, retc } = loadstruct("p2", "ds");

