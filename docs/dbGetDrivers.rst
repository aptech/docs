
dbGetDrivers
==============================================

Purpose
----------------

Returns a list of available database drivers.

Format
----------------
.. function:: drivers = dbGetDrivers()

    :return drivers: list of available database drivers.

    :rtype drivers: Nx1 string array

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
