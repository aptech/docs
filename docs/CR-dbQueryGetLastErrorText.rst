
dbQueryGetLastErrorText
==============================================

Purpose
----------------

Returns error information about the last error that occurred (if any) with the last executed query.

Format
----------------
.. function:: dbQueryGetLastErrorText()

    :returns: **err_txt** (*2x1 string array*) - database and driver text of last error.

Remarks
-------

Because a failed query will not have a valid handle (*id*), this function
retrieves stored error information about the last executed query.

.. seealso:: :func:`dbQueryGetLastErrorNum`
