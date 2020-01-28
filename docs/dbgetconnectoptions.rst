
dbGetConnectOptions
==============================================

Purpose
----------------

Returns the connection options string used for a database connection.

Format
----------------
.. function:: options = dbGetConnectOptions(db_id)

    :param db_id: database connection index number.
    :type db_id: scalar

    :return options: Contains the connection options for the specified database connection.

    :rtype options: string

Remarks
-------

If you have not set any connection options with :func:`dbSetConnectOptions`,
then this function will return an empty string. For a full list of
options see :func:`dbSetConnectOptions`.

.. seealso:: :func:`dbSetConnectOptions`
