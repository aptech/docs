
gdaLoad
==============================================

Purpose
----------------

Loads variables in a GDA into the workspace.

Format
----------------
.. function:: gdaLoad(filename,  create,  modify,  rename,  ftypes,  errh,  report)

    :param filename: name of data file.
    :type filename: string

    :param create: create flag:
    :type create: scalar

    .. csv-table::
        :widths: auto

        "0", "do not create any new variables in the workspace."
        "1", "create new variables in the workspace."

    :param modify: modify flag:
    :type modify: scalar

    .. csv-table::
        :widths: auto

        "0", "do not modify any variables in the workspace."
        "1", "if the name of a variable in the data file matches the name of a variable already in the workspace, modify that variable."

    :param rename: rename flag:
    :type rename: scalar

    .. csv-table::
        :widths: auto

        "0", "do not rename a variable retrieved from the data file when copying it into the workspace."
        "1", "rename variables retrieved from the data file when copying theminto the workspace if there are name conflicts with existing variables, which may not be modified."

    :param ftypes: type force flag:
    :type ftypes: scalar

    .. csv-table::
        :widths: auto

        "0", "do not force a type change on any variables in the workspacewhen modifying."
        "1", "force a type change on a variable in the workspace when modifyingit with the data in a variable of the same name in the data file. Note that if  ftypes is set to 1, gdaLoadwill follow regular type change rules. The types of sparse matrixand structure variables will NOT be changed."

    :param errh: controls the error handling of gdaLoad:
    :type errh: scalar

    .. csv-table::
        :widths: auto

        "0", "skip operations that cannot be performed, without setting an error return."
        "1", "return an error code if operations are skipped."
        "2", "terminate program if operations are skipped."

    :param report: controls reporting:
    :type report: scalar

    .. csv-table::
        :widths: auto

        "0", "no reporting."
        "1", "report only name changes and operations that could not be performed."
        "2", "report type changes, name changes, and operations that could not be performed."
        "3", "report everything."

    :returns: ret (*scalar*), return code, 0 if successful, otherwise one of the following error codes:

    .. csv-table::
        :widths: auto

        "4", "File read error."
        "5", "Invalid file type."
        "10", "File contains no variables."
        "14", "File too large to be read on current platform."
        "24", "Variables skipped."
        "26", "Cannot add structure definition."
        "27", "Structure definition does not match."

Examples
----------------

::

    ret = gdaLoad("myfile.gda",1,1,1,1,1,3);

This example loads the variables in myfile.gda into the
workspace, creating a new variable if a variable of the same name does not 
already exist, modifying an existing variable if a variable of the same
name does already exist and the modification does not result in an impossible 
type change, and renaming the variable if none of the above is possible.
The example returns an error code if any variables in myfile.gda
are skipped and reports all activity.

.. seealso:: Functions :func:`gdaSave`
