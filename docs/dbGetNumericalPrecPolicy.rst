
dbGetNumericalPrecPolicy
==============================================

Purpose
----------------

Returns the default numerical precision policy for a specified database connection.

Format
----------------
.. function:: prec_policy = dbGetNumericalPrecPolicy(db_id)

    :param db_id: database connection index number.
    :type db_id: scalar

    :return prec_policy: 

        .. csv-table::
            :widths: auto

            "DB_HIGH_PRECISION", "strings will be used to preserve precision"
            "DB_LOW_PRECISION_INT32", "Force 32-bit integer values"
            "DB_LOW_PRECISION_INT64", "Force 64-bit integer values"
            "DB_LOW_PRECISION_DOUBLE", "Force double values. This is the default policy."

    :rtype prec_policy: scalar

