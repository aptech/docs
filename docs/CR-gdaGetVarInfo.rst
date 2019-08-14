
gdaGetVarInfo
==============================================

Purpose
----------------

Gets information about all of the variables in a GAUSS Data
Archive and returns it in an array of :class:`gdavartable`
structures.

Format
----------------
.. function:: vtab = gdaGetVarInfo(filename)

    :param filename: name of data file.
    :type filename: string

    :return vtab: Contains :class:`gdavartable`
        structures, where *N* is the number of variables in
        *filename*, containing the following members:

        .. csv-table::
            :widths: auto

            "*vtab[i].name*", "string, name of variable."
            "*vtab[i].type*", "scalar, type of variable."
            "*vtab[i].orders*", "Mx1 vector or scalar, orders of the variable."

    :type vtab: Nx1 array

Remarks
-------

The size of *vtab.orders* is dependent on the type of the variable as follows:

.. csv-table::
    :widths: auto

    "**Variable Type**", "**vtab.orders**"
    "array", "Mx1 vector, where M is the number of dimensions in the array, containing the sizes of each dimension, from the slowest-moving dimension to the fastest-moving dimension."
    "matrix", "2x1 vector containing the rows and columns of the matrix, respectively."
    "string", "scalar containing the length of string, excluding the null terminating byte."
    "string array", "2x1 vector containing the rows and columns of the string array, respectively."

*vtab.type* may contain any of the following:

+----+--------------+
| 6  | matrix       |
+----+--------------+
| 13 | string       |
+----+--------------+
| 15 | string array |
+----+--------------+
| 21 | array        |
+----+--------------+


Examples
----------------

::

    // Declare gdaVarTable structure
    struct gdaVarTable vtab;

    vtab = gdaGetVarInfo("myfile.gda");

Source
------

gdafns.src

.. seealso:: Functions :func:`gdaReportVarInfo`, :func:`gdaGetNames`, :func:`gdaGetTypes`, :func:`gdaGetOrders`
