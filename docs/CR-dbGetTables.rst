
dbGetTables
==============================================

Purpose
----------------

Returns the database's tables, system tables and views.

Format
----------------
.. function:: tables = dbGetTables(db_id[, type])

    :param db_id: database connection index number.
    :type db_id: scalar

    :param type:

        .. csv-table::
            :widths: auto

            ":code:`Tables`", "All tables visible to the user. This is the default value."
            ":code:`System Tables`", "Internal tables used by the database."
            ":code:`Views`", "All views visible to the user."
            ":code:`All`", "All of the above."

    :type type: string:

    :return tables: Contains the information specified by the *type* parameter.

    :type tables: Nx1 string array

