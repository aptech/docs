
dbQueryGetLastErrorNum
==============================================

Purpose
----------------

Returns error information about the last error that occurred (if any) with the last executed query.

Format
----------------
.. function:: err_num = dbQueryGetLastErrorNum()

    :return err_num: number of last error.

    :rtype err_num: scalar

Remarks
-------

Because a failed query will not have a valid handle (*id*), this function
retrieves stored error information about the last executed query.

.. seealso:: :func:`dbQueryGetLastErrorText`
