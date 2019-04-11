
dbNumericalPrecPolicy
==============================================

Purpose
----------------

Returns the default numerical precision policy for a specified database connection.

Format
----------------
.. function:: dbNumericalPrecPolicy(db_id)

    :param db_id: database connection index number.
    :type db_id: scalar

    :returns: prec_policy (*scalar*)

        .. csv-table::
            :widths: auto
    
            "0", "strings will be used to preserve precision"
            "1", "Force 32-bit integer values"
            "2", "Force 64-bit integer values"
            "4", "Force double values. This is the default policy."

