
dbQueryGetField
==============================================

Purpose
----------------

Returns the value of a specified field in the current record. An overloaded version
that accepts a column name as input is available, but not as efficient.

Format
----------------
.. function:: dbQueryGetField(qid, name)

    :param qid: query number.
    :type qid: scalar

    :param idx: index of the field whose value should be returned.
    :type idx: scalar

