
dbIsDriverAvailable
==============================================

Purpose
----------------

Returns 1 if a specified database driver is available.

Format
----------------
.. function:: ret = dbIsDriverAvailable(name)

    :param name: name of driver to check
    :type name: string

    :return ret: 1 if the specified driver is available, or 0 if not.

    :rtype ret: scalar

Examples
----------------

::

    // Check if the MySQL driver is available
    ret = dbIsDriverAvailable("MYSQL");

    if ret;
        print "MySQL driver is available";
    else;
        print "MySQL driver is not available";
    endif;

