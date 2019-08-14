
dbGetDriverName
==============================================

Purpose
----------------

Returns the name of the connection's database driver.

Format
----------------
.. function:: driver_name = dbGetDriverName(db_id)

    :param db_id: database connection index number.
    :type db_id: scalar

    :return driver_name: name of the database driver.

    :type driver_name: string

Examples
----------------

::

    db_id = dbAddDatabase("SQLITE");
    print "Driver = " dbGetDriverName(db_id);

::

    Driver = SQLITE
