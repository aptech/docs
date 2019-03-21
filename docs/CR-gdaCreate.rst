
gdaCreate
==============================================

Purpose
----------------

Creates a GAUSS Data Archive.

Format
----------------
.. function:: gdaCreate(filename, overwrite)

    :param filename: name of data file to create.
    :type filename: string

    :param overwrite: one of the following:
    :type overwrite: scalar

    .. csv-table::
        :widths: auto

        "0", "error out if file already exists."
        "1", "overwrite file if it already exists."

    :returns: ret (*scalar*), return code, 0 if successful, otherwise one of the following error codes:

    .. csv-table::
        :widths: auto

        "1", "Null file name."
        "3", "File write error."
        "6", "File already exists."
        "7", "Cannot create file."

Remarks
-------

This command creates a GAUSS Data Archive containing only a header. To
add data to the GDA, call gdaWrite.

It is recommended that you include a .gda extension in filename.
However, gdaCreate will not force an extension.


Examples
----------------

::

    ret = gdaCreate("myfile.gda",1);

.. seealso:: Functions :func:`gdaWrite`
