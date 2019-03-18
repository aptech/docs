
dbQueryIsForwardOnly
==============================================

Purpose
----------------

Reports whether you can only scroll forward through a result set. 

Format
----------------
.. function:: dbQueryIsForwardOnly(qid)

    :param qid: query number.
    :type qid: scalar

    :returns: ret (*scalar*), 1 if the result set can only be scrolled through forward, otherwise a 0.

