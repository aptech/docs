
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

    :return query_string: text of the current query, or empty string if there is no current query.

    :type query_string: string

