
dbIsValid
==============================================

Purpose
----------------

Reports whether a specified database connection has a valid driver.

Format
----------------
.. function:: ret = dbIsValid(db_id)

    :param db_id: database connection index number.
    :type db_id: scalar

    :return ret: 1 if the database connection has a valid driver or 0 if not.

    :type ret: scalar

Examples
----------------

::

    // Use default connection
    db_id = dbAddDatabase("SQLITE");
    ret = dbIsValid(db_id);       // Returns 1 for 'true'
    
    db_id = dbAddDatabase("BAD_DRIVER_NAME");
    ret = dbIsValid(db_id);   // Returns 0 for 'false'
