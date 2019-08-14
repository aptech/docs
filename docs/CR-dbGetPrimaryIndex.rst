
dbGetPrimaryIndex
==============================================

Purpose
----------------

Returns the primary index for the specified table.

Format
----------------
.. function:: primary_index = dbGetPrimaryIndex(db_id, table_name)

    :param db_id: database connection index number.
    :type db_id: scalar

    :param table_name: name of the table to reference.
    :type table_name: string

    :return primary_index: the :math:`[1,1]` element is the cursor name and the :math:`[2,1]` element is the index name

    :type primary_index: 2x1 string array

