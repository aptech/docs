
gdaSave
==============================================

Purpose
----------------

Writes variables in a workspace to a GDA.

Format
----------------
.. function:: ret = gdaSave(filename, varnames, exclude, overwrite, report)

    :param filename: name of data file.
    :type filename: string

    :param varnames: names of variables in the workspace to include or exclude.
    :type varnames: string or NxK string array

    :param exclude: include/exclude flag:

        .. csv-table::
            :widths: auto

            "0", "include all variables contained in *varnames*."
            "1", "exclude all variables contained in *varnames*."

    :type exclude: scalar

    :param overwrite: controls the overwriting of the file and variables in the file:

        .. csv-table::
            :widths: auto

            "0", "if file exists, return with an error code."
            "1", "if file exists, overwrite completely."
            "2", "if file exists, append to file, appending to variable names if necessary to avoid name conflicts."
            "3", "if file exists, update file. When a name conflict occurs, update the existing variable in the file with the new variable."

    :type overwrite: scalar

    :param report: controls reporting:

        .. csv-table::
            :widths: auto

            "0", "no reporting."
            "1", "report only name changes (note that name changes occur only when *overwrite* is set to 2)."
            "3", "report everything."

    :type report: scalar

    :return retcode: return code, 0 if successful, otherwise one of the following error codes:

        .. csv-table::
            :widths: auto

            "1", "Null file name."
            "3", "File write error."
            "4", "File read error."
            "5", "Invalid file type."
            "6", "File exists and  overwrite set to 0."
            "7", "Cannot create file."
            "14", "File too large to be read on current platform."
            "16", "Cannot write to GDA - version outdated."
            "17", "Type mismatch."

    :type retcode: scalar

Remarks
-------

Only initialized variables are written to the GDA with :func:`gdaSave`.

If *varnames* is a null string and *exclude* is set to 0, it will be
interpreted as indicating all of the variables in the workspace.

You may add an asterisk, ``*``, to the end of a variable name in *varnames*
to indicate that all variables beginning with the specified text are to
be selected. For example, setting *varnames* to the string :code:`"_*"` and
setting *exclude* to 1 indicates that all variables EXCEPT those starting
with an underscore should be written to the GDA.

The names of the variables in the workspace are the names that are given
to the variables when they are written to the GDA, with the exception of
names that are changed to avoid conflicts.

If you set *overwrite* to 2, and variable name conflicts are encountered,
:func:`gdaSave` will append an underscore and a number to the name of the
variable it is adding. It will first try changing the name to *name_1*. If
there is a conflict with that name, it will change it to *name_2*, and so
on until it finds a name that does not conflict with any of the
variables already in the GDA.


Examples
----------------

::

    run -r myfile.gau;
    ret = gdaSave("myfile.gda","x*", 0, 2, 3);

This example runs a GAUSS program called ``myfile.gau`` and then
writes all initialized variables in the workspace beginning with 'x'
to the file ``myfile.gda``. If ``myfile.gda`` already
exists, this example appends to it, changing the names of the variables
that it writes to the file if necessary to avoid name conflicts. All writing
and variable name changing is reported.

.. seealso:: Functions :func:`gdaLoad`
