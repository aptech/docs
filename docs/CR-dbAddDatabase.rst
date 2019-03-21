
dbAddDatabase
==============================================

Purpose
----------------

Adds a database to the list of database connections using the driver type or a connection URL.

Format
----------------
.. function:: dbAddDatabase(connection_url)

    :param driver_type: supported options include:
        DB2,
        IBASE,
        MYSQL,
        OCI,
        ODBC,
        PSQL,
        SQLITE,
        SQLITE2,
        TDS.
    :type driver_type: string

    :param connection_url: with the following format:
        driver://username:password@hostname:port/database_name
    :type connection_url: string

    :returns: db_id (*scalar*), index into a table of all opened database connections, or 0 on failure.

Examples
----------------

::

    db_id = dbAddDatabase("MYSQL");

::

    url = "mysql://webuser:pswd@localhost:3306/dev";
    db_id = dbAddDatabase(url);

Remarks
+++++++

Before using the connection, it must be initialized. e.g., call some or
all of dbSetDatabaseName(),
dbSetUserName(),dbSetPassword(),dbSetHostName(), dbSetPort(), and
dbSetConnectOptions(), and, finally, dbOpen().

The exception to this is using a connection URL, since this performs the
above mentioned steps. Omitting portions of the connection URL is
allowed, but the syntax must remain the same. For example:

::

   id = dbAddDatabase("oci://root:@localhost:/testing");

is a valid connection URL, but will not set the password or port number
fields.

