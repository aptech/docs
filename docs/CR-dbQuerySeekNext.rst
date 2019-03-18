
dbQuerySeekNext
==============================================

Purpose
----------------

Retrieves the next record in the result, if available, and positions the query 
on the retrieved record. 

Format
----------------
.. function:: dbQuerySeekNext(qid)

    :param qid: query number.
    :type qid: scalar

    :returns: ret (*scalar*), if the record could not be retrieved, the result is positioned after the last record and 0 is returned. If the record is successfully retrieved, 1 is returned.

Examples
----------------

::

    qid = dbCreateQuery(db_id, "SELECT * 
        FROM PEOPLE");
    
    do while dbQuerySeekNext(qid);
        row = dbQueryFetchOneSA(qid);
        // Or dbQueryFetchOneM(qid) if data 
        // is numeric  
    endo;

.. seealso:: Functions :func:`dbQuerySeekFirst`, :func:`dbQuerySeekLast`, :func:`dbQuerySeekPrevious`, :func:`dbQuerySeek`, :func:`dbQueryGetPosition`
