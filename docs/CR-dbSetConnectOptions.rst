
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

