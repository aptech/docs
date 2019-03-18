
dbIsValid
==============================================

Purpose
----------------

Reports whether a specified database connection has a valid driver.

Format
----------------
.. function:: dbIsValid(db_id)

    :param db_id: database connection index number.
    :type db_id: scalar

    :returns: ret (*scalar*), 1 if the database connection has a valid driver or 0 if not.

Examples
----------------

::

    // Use default connection
    db_id = dbAddDatabase("SQLITE"); 
    ret = dbIsValid(db_id);       // Returns 1 for 'true'
    db_id = dbAddDatabase("BAD_DRIVER_NAME");
    ret = dbIsValid(db_id);   // Returns 0 for 'false'

