
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

