
gdaPack
==============================================

Purpose
----------------

Packs the data in a GAUSS Data Archive, removing all empty bytes and truncating the file.

Format
----------------
.. function:: retcode = gdaPack(filename)

    :param filename: name of data file.
    :type filename: string

    :return retcode: return code, 0 if successful, otherwise one of the following error codes:

        .. csv-table::
            :widths: auto

            "1", "Null file name."
            "2", "File open error."
            "3", "File write error."
            "4", "File read error."
            "5", "Invalid data file type."
            "10", "File contains no variables."
            "12", "File truncate error."
            "14", "File too large to be read on current platform."

    :rtype retcode: scalar

Examples
----------------

::

    retcode = gdaPack("myfile.gda");

Remarks
-------

You may want to call :func:`gdaPack` after several calls to :func:`gdaUpdate` to remove
all of the empty bytes from a GDA.


.. seealso:: Functions :func:`gdaUpdate`, :func:`gdaWrite`
