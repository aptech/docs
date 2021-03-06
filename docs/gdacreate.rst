
gdaCreate
==============================================

Purpose
----------------

Creates a GAUSS Data Archive.

Format
----------------
.. function:: retcode = gdaCreate(filename, overwrite)

    :param filename: name of data file to create.
    :type filename: string

    :param overwrite: one of the following:

        .. csv-table::
            :widths: auto

            "0", "error out if file already exists."
            "1", "overwrite file if it already exists."

    :type overwrite: scalar

    :return retcode: return code, 0 if successful, otherwise one of the following error codes:

        .. csv-table::
            :widths: auto

            "1", "Null file name."
            "3", "File write error."
            "6", "File already exists."
            "7", "Cannot create file."

    :rtype retcode: scalar

Examples
----------------

::

  /*
  ** Create a GDA named `myfile`
  ** and overwrite existing `myfile`
  */
  ret = gdaCreate("myfile.gda", 1);

Remarks
-------

This command creates a GAUSS Data Archive containing only a header. To
add data to the GDA, call :func:`gdaWrite`.

It is recommended that you include a :file:`.gda` extension in :func:`filename`.
However, :func:`gdaCreate` will not force an extension.


.. seealso:: Functions :func:`gdaWrite`
