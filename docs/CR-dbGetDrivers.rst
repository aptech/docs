
dbGetDrivers
==============================================

Purpose
----------------

Returns a list of available database drivers.

Format
----------------
.. function:: dbGetDrivers()

    :returns: **drivers** (*Nx1 string array*) - list of available database drivers.

Examples
----------------

::

    print dbGetDrivers();

::

        DB2
        MYSQL
        OCI
        ODBC
        PSQL
        SQLITE
