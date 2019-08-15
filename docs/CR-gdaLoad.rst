
gdaLoad
==============================================

Purpose
----------------

Loads variables in a GDA into the workspace.

Format
----------------
.. function:: ret = gdaLoad(filename, create, modify, rename, ftypes, errh, report)

    :param filename: name of data file.
    :type filename: string

    :param create: create flag:

        .. csv-table::
            :widths: auto

            "0", "do not create any new variables in the workspace."
            "1", "create new variables in the workspace."

    :type create: scalar

    :param modify: modify flag:

        .. csv-table::
            :widths: auto

            "0", "do not modify any variables in the workspace."
            "1", "if the name of a variable in the data file matches the name of a variable already in the workspace, modify that variable."

    :type modify: scalar

    :param rename: rename flag:

        .. csv-table::
            :widths: auto

            "0", "do not rename a variable retrieved from the data file when copying it into the workspace."
            "1", "rename variables retrieved from the data file when copying them into the workspace if there are name conflicts with existing variables, which may not be modified."

    :type rename: scalar

    :param ftypes: type force flag:

        .. csv-table::
            :widths: auto

            "0", "do not force a type change on any variables in the workspace when modifying."
            "1", "force a type change on a variable in the workspace when modifying it with the data in a variable of the same name in the data file. Note that if  *ftypes* is set to 1, :func:`gdaLoad` will follow regular type change rules. The types of sparse matrix and structure variables will NOT be changed."

    :type ftypes: scalar

    :param errh: controls the error handling of :func:`gdaLoad`:

        .. csv-table::
            :widths: auto

            "0", "skip operations that cannot be performed, without setting an error return."
            "1", "return an error code if operations are skipped."
            "2", "terminate program if operations are skipped."

    :type errh: scalar

    :param report: controls reporting:

        .. csv-table::
            :widths: auto

            "0", "no reporting."
            "1", "report only name changes and operations that could not be performed."
            "2", "report type changes, name changes, and operations that could not be performed."
            "3", "report everything."

    :type report: scalar

    :return retcode: return code, 0 if successful, otherwise one of the following error codes:

        .. csv-table::
            :widths: auto

            "4", "File read error."
            "5", "Invalid file type."
            "10", "File contains no variables."
            "14", "File too large to be read on current platform."
            "24", "Variables skipped."
            "26", "Cannot add structure definition."
            "27", "Structure definition does not match."

    :rtype retcode: scalar

Remarks
-------

For each variable in *filename*, :func:`gdaLoad` will first compare the name of
the variable against the names of the variables already resident in the
GAUSS workspace to see if there is a match. If there is not a match, and
*create* is set to 1, it will create a new variable. Otherwise if *create*
is set to 0, it will skip that variable.

If the variable name does match that of a variable already resident in
the GAUSS workspace, and *modify* is set to 1, it will attempt to modify
that variable. If the types of the two variables are different, and
*ftype* is set to 1, it will force the type change if possible and modify
the existing variable.

If it cannot modify the variable or *modify* is set to 0, it will check to
see if *rename* is set to 1, and if so, attempt to rename the variable,
appending an *\_ num* to the variable name, beginning with :math:`num = 1` and
counting upward until it finds a name with which there are no conflicts.
If the variable cannot be modified and *rename* is set to 0, then the
variable will be skipped.

The *rename* argument also controls the handling of structure definitions.
If a structure variable is encountered in the GDA file, and no variable
of the same name exists in the workspace (or the variable is renamed),
:func:`gdaLoad` will attempt to find a structure definition in the workspace
that matches the one in the GDA. Note that in order for structure
definitions to match, the structure definition names must be the same as
well as the number, order, names, and types of their members.

If no matching structure definition is found, the definition in the file
will be loaded into the workspace. If there is already a non-matching
structure definition with the same name in the workspace and *rename* is
set to 1, then :func:`gdaLoad` will attempt to rename the structure definition,
using the same method as it does for variable names.

If a structure variable is encountered in the GDA file, a structure
variable of the same name already exists in the workspace, and *modify* is
set to 1, then :func:`gdaLoad` will modify the existing variable, providing that
the structure definitions of the two variables match.


Examples
----------------

::

    /*
    ** Create new variables if same name
    ** does not exist
    */
    create_new = 1;

    /*
    ** Modify variable if name matches
    ** existing variable
    */
    modify = 1;

    /*
    ** Rename variables retrieved from the
    ** data file when copying them into the
    ** workspace if there are name conflicts
    */
    rename = 1;

    /*
    ** Force a type change on a variable in
    ** the workspace when modifying it
    */
    ftypes = 1;

    /*
    ** Return an error code if operations
    ** are skipped
    */
    errh = 1;

    /*
    ** Report only name changes and operations
    ** that could not be performed
    */
    retcode = gdaLoad("myfile.gda", create_new, modify, rename, ftypes, errh, report)

This example loads the variables in :file:`myfile.gda` into the
workspace, creating a new variable if a variable of the same name does not
already exist, modifying an existing variable if a variable of the same
name does already exist and the modification does not result in an impossible
type change, and renaming the variable if none of the above is possible.
The example returns an error code if any variables in :file:`myfile.gda`
are skipped and reports all activity.

.. seealso:: Functions :func:`gdaSave`
