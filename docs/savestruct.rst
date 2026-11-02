
savestruct
==============================================

Purpose
----------------
Saves a matrix of structures to a file on the disk.

Format
----------------
.. function:: retcode = saveStruct(instance, file_name)

    :param instance: instances of a structure.
    :type instance: structure

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

The file on the disk will be given a :file:`.fsr` extension.

:func:`saveStruct` writes the GDAT v2 format (see :func:`saved`) under the
:file:`.fsr` name. Dataframe members keep their column names, types, date
formats and labels when the file is loaded with :func:`loadStruct` in another
session. A structure holding a value GDAT v2 does not support, such as a
string that is not valid UTF-8, is written in the older :file:`.fsr` format,
where dataframe members load as plain matrices.

GAUSS 26 and earlier cannot read files that :func:`saveStruct` writes in
GAUSS 27: their :func:`loadStruct` returns 1.

To save a structure to a ``.gdat`` file and load single members of it, use
:func:`saved` and :func:`loadd`.

.. seealso:: :func:`loadStruct`, :func:`saved`, :func:`loadd`
