
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

    :rtype tables: Nx1 string array

Examples
----------------

::

    // Add MySQL to the list of database connections
    db_id = dbAddDatabase("MYSQL");
    dbSetDatabaseName(db_id, "mydb");
    dbOpen(db_id);

    // Get all user tables
    tables = dbGetTables(db_id);
    print tables;

    // Get all views
    views = dbGetTables(db_id, "Views");
    print views;

