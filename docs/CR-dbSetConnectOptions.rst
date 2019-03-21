
dbSetConnectOptions
==============================================

Purpose
----------------

Sets database-specific options.

Format
----------------
.. function:: dbSetConnectOptions(db_id, db_options)

    :param db_id: database connection index number.
    :type db_id: scalar

    :param db_options: a semi-colon separated list of option names or option=value pairs. Available options will depend upon the database being used.
    :type db_options: string

Remarks
-------

This must be done before the connection is opened or it has no effect
(or you can dbClose() the connection, call this function and dbOpen()
the connection again). The format of the options string is a semicolon
separated list of option names or option=value pairs. The options depend
on the database client used:
ODBC
SQL_ATTR_ACCESS_MODE
SQL_ATTR_LOGIN_TIMEOUT
SQL_ATTR_CONNECTION_TIMEOUT
SQL_ATTR_CURRENT_CATALOG
SQL_ATTR_METADATA_ID
SQL_ATTR_PACKET_SIZE
SQL_ATTR_TRACEFILE
SQL_ATTR_TRACE
SQL_ATTR_CONNECTION_POOLING
SQL_ATTR_ODBC_VERSION
MySQL
CLIENT_COMPRESS
CLIENT_FOUND_ROWS
CLIENT_IGNORE_SPACE
CLIENT_SSL
CLIENT_ODBC
CLIENT_NO_SCHEMA
CLIENT_INTERACTIVE
UNIX_SOCKET
MYSQL_OPT_RECONNECT
PostgreSQL
connect_timeout
options
tty
requiressl
service
DB2
SQL_ATTR_ACCESS_MODE
SQL_ATTR_LOGIN_TIMEOUT
OCI
OCI_ATTR_PREFETCH_ROWS
OCI_ATTR_PREFETCH_MEMORY
TDS
none
SQLite
QSQLITE_BUSY_TIMEOUT
QSQLITE_OPEN_READONLY
QSQLITE_ENABLE_SHARED_CACHE
Interbase
ISC_DPB_LC_CTYPE
ISC_DPB_SQL_ROLE_NAME


Examples
----------------

::

    // MySQL connection
    // use an SSL connection to the server
    dbSetConnectOptions(db_id, "CLIENT_SSL=1;
        CLIENT_IGNORE_SPACE=1"); 
    
    if not dbOpen();
        // clears the connect option string
        dbSetConnectOptions(db_id, ""); 
        ...
    endif;

::

    // PostgreSQL connection
    // enable PostgreSQL SSL connections
    dbSetConnectOptions(db_id, "requiressl=1");
    if not dbOpen();
        // clear options
        dbSetConnectOptions(db_id, "");
        ...
    endif;

::

    // ODBC connection
    dbSetConnectOptions(db_id, "SQL_ATTR_ACCESS_MODE=
        SQL_MODE_READ_ONLY;
        SQL_ATTR_TRACE=
        SQL_OPT_TRACE_ON"); 
    // set ODBC options
    if not  dbOpen();
        // don't try to set this option
        dbSetConnectOptions(db_id, ""); 
        ...
    endif;

