
dbQueryGetLastErrorText
==============================================

Purpose
----------------

Returns error information about the last error that occurred (if any) with the last executed query.

Format
----------------
.. function:: err_txt = dbQueryGetLastErrorText()

    :return err_txt: database and driver text of last error.

    :rtype err_txt: 2x1 string array

Remarks
-------

Because a failed query will not have a valid handle (*id*), this function
retrieves stored error information about the last executed query.

.. seealso:: :func:`dbQueryGetLastErrorNum`
