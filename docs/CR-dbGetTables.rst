
dbGetTables
==============================================

Purpose
----------------

Returns the database's tables, system tables and views.

Format
----------------
.. function:: dbGetTables(db_id, type) 
			  dbGetTables(db_id)

    :param db_id: database connection index number.
    :type db_id: scalar

    :param type: string:
    :type type: TODO

    .. csv-table::
        :widths: auto

        ""Tables"", "All tables visible to the user. This is the default value."
        ""System Tables"", "Internal tables used by the database."
        ""Views"", "All views visible to the user."
        ""All"", "All of the above."

    :returns: tables (*TODO*), Nx1 string array containing the information specified by the 'type' parameter.

