
dbClose
==============================================

Purpose
----------------

Closes a database connection and destroys any remaining queries.

Format
----------------
.. function:: dbClose(db_id)

    :param db_id: database connection index number.
    :type db_id: scalar



Remarks
-------

dbClose() does not remove the database connection from the list of
available database connections. The connection can be opened again
without repeating the database initialization and setup steps.

