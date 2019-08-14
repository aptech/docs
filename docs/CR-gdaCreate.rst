
gdaCreate
==============================================

Purpose
----------------

Creates a GAUSS Data Archive.

Format
----------------
.. function:: ret = gdaCreate(filename, overwrite)

    :param filename: name of data file to create.
    :type filename: string

    :param overwrite: one of the following:

        .. csv-table::
            :widths: auto

            "0", "error out if file already exists."
            "1", "overwrite file if it already exists."

    :type overwrite: scalar

    :returns: **retcode** (*scalar*) - return code, 0 if successful, otherwise one of the following error codes:

        .. csv-table::
            :widths: auto

            "1", "Null file name."
            "3", "File write error."
            "6", "File already exists."
            "7", "Cannot create file."

Remarks
-------

This command creates a GAUSS Data Archive containing only a header. To
add data to the GDA, call :func:`gdaWrite`.

It is recommended that you include a ``.gda`` extension in :func:`filename`.
However, :func:`gdaCreate` will not force an extension.


Examples
----------------

::

  /*
  ** Create a GDA named `myfile`
  ** and overwrite existing `myfile`
  */
  ret = gdaCreate("myfile.gda", 1);

.. seealso:: Functions :func:`gdaWrite`
