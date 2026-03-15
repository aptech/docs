
dbSetNumericalPrecPolicy
==============================================

Purpose
----------------

Sets the current precision policy for all queries used with a specified database connection.

Format
----------------
.. function:: dbSetNumericalPrecPolicy(db_id, prec_policy)

    :param db_id: database connection index number.
    :type db_id: scalar

    :param prec_policy: 

        .. csv-table::
            :widths: auto
    
            "0", "Strings will be used to preserve precision."
            "1", "Force 32-bit integer values."
            "2", "Force 64-bit integer values."
            "4", "Force double values. This is the default policy."

    :type prec_policy: scalar

Examples
----------------

::

    // Add MySQL to the list of database connections
    db_id = dbAddDatabase("MYSQL");
    dbSetDatabaseName(db_id, "mydb");
    dbOpen(db_id);

    // Set precision policy to use strings for high precision
    dbSetNumericalPrecPolicy(db_id, 0);

    // Verify the policy was set
    prec = dbGetNumericalPrecPolicy(db_id);
    print (prec);

