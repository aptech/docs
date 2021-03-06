
dbGetTableHeaders
==============================================

Purpose
----------------

Returns a string array populated with the names of all the fields in a specified table (or view).

Format
----------------
.. function:: field_names = dbGetTableHeaders(db_id, table_name)

    :param db_id: database connection index number.
    :type db_id: scalar

    :param table_name: name of table or view.
    :type table_name: string

    :return field_names: containing the column names for the specified table or view.

    :rtype field_names: string array

Remarks
-------

The order in which the fields appear in the record is undefined.
