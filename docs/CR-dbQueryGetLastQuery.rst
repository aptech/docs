
dbQueryGetLastQuery
==============================================

Purpose
----------------

Returns the text of the current query being used.

Format
----------------
.. function:: query_string = dbQueryGetLastQuery(qid)

    :param qid: query number.
    :type qid: scalar

    :returns: **query_string** (*string*) - text of the current query, or empty string if there is no current query.
