
dbSetDatabaseName
==============================================

Purpose
----------------
Sets the connection's database name. To have effect, the database name must be set before the connection is opened. Alternatively, you can :func:`dbClose` the connection, set the database name, and call :func:`dbOpen` again.

Format
----------------
.. function:: dbSetDatabaseName(db_id, database_name)

    :param db_id: database connection index number.
    :type db_id: scalar

    :param database_name: the name to apply to the specified database connection.
    :type database_name: string

Remarks
-------

For the OCI (Oracle) driver, the database name is the TNS Service Name.

For the ODBC driver, the name can either be a DSN, a DSN filename (in
which case the file must have a ``.dsn`` extension), or a connection string.

For example, Microsoft Access users can use the following connection
string to open an ``.mdb`` file directly, instead of having to create a DSN
entry in the ODBC manager:

::

   // Add ODBC to list of database connections
   db_id = dbAddDatabase("ODBC");

   // Set database name
   dbSetDatabaseName(db_id, "DRIVER=
      {Microsoft Access Driver (*.mdb)};
      FIL={MS Access};
      DBQ=myaccessfile.mdb");

   // Open database
   dbOpen(db_id);


.. seealso:: :func:`dbGetDatabaseName`
