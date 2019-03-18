
gdaSave
==============================================

Purpose
----------------

Writes variables in a workspace to a GDA.

Format
----------------
.. function:: gdaSave(filename,  varnames,  exclude,  overwrite,  report)

    :param filename: name of data file.
    :type filename: string

    :param varnames: names of variables in the  workspace to include or exclude.
    :type varnames: string or NxK string array

    :param exclude: include/exclude flag:
    :type exclude: scalar

    .. csv-table::
        :widths: auto

        "0", "include all variables contained in  varnames."
        "1", "exclude all variables contained in  varnames."

    :param overwrite: controls the overwriting of the file and variables in the file:
    :type overwrite: scalar

    .. csv-table::
        :widths: auto

        "0", "if file exists, return with an error code."
        "1", "if file exists, overwrite completely."
        "2", "if file exists, append to file, appending to variable names if necessary to avoid name conflicts."
        "3", "if file exists, update file. When a name confict occurs, update the existing variable in the file with the new variable."

    :param report: controls reporting:
    :type report: scalar

    .. csv-table::
        :widths: auto

        "0", "no reporting."
        "1", "report only name changes (note that name changes occur only when  overwrite is set to 2)."
        "3", "report everything."

    :returns: ret (*scalar*), return code, 0 if successful, otherwise one of the following error codes:

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

Examples
----------------

::

    run -r myfile.gau;
    ret = gdaSave("myfile.gda","x*",0,2,3);

This example runs a GAUSS program called myfile.gau and then
writes all initialized variables in the workspace beginning with 'x'
to the file myfile.gda. If myfile.gda already 
exists, this example appends to it, changing the names of the variables 
that it writes to the file if necessary to avoid name conficts. All writing
and variable name changing is reported.

.. seealso:: Functions :func:`gdaLoad`
