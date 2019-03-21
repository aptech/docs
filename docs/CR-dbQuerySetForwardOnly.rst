
dbQuerySetForwardOnly
==============================================

Purpose
----------------

Sets forward only mode to forward. If forward is true, only dbQuerySeekNext() and 
dbQuerySeek() with positive values, are allowed for navigating the results.

Format
----------------
.. function:: dbQuerySetForwardOnly(qid, forward)

    :param qid: query number.
    :type qid: scalar

    :param forward: 1 to set forward only or 0 to allow seeking in either direction.
    :type forward: scalar



Remarks
-------

Forward only mode can be (depending on the driver) more memory efficient
since results do not need to be cached. It will also improve performance
on some databases. For this to be true, you must call
dbQuerySetForwardOnly() before the query is prepared or executed.

Forward only mode is enabled by default.

Setting forward only to false is a suggestion to the database engine,
which has the final say on whether a result set is forward only or
scrollable.

dbQueryIsForwardOnly() will always return the correct status of the
result set.

