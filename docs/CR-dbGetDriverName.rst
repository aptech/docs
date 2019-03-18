
dbGetDriverName
==============================================

Purpose
----------------

Returns the name of the connection's database driver.

Format
----------------
.. function:: dbGetDriverName(db_id)

    :param db_id: database connection index number.
    :type db_id: scalar

    :returns: driver_name (*string*), name of the database driver.

Examples
----------------

::

    db_id = dbAddDatabase("SQLITE");
    print "Driver = " dbGetDriverName(db_id);

::

    Driver = SQLITE

