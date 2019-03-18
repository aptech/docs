
dbGetTableHeaders
==============================================

Purpose
----------------

Returns a string array populated with the names of all the fields in a specified table (or view).

Format
----------------
.. function:: dbGetTableHeaders(db_id, table_name)

    :param db_id: database connection index number.
    :type db_id: scalar

    :param table_name: name of table or view.
    :type table_name: string

    :returns: field_names (*TODO*), string array containing the column names for the specified table or view.

