
dbQueryFetchAllSA
==============================================

Purpose
----------------

Returns the result set for the current query as a string array.

Format
----------------
.. function:: dbQueryFetchAllSA(qid[, columns])

    :param qid: query number.
    :type qid: scalar

    :param columns: Optional input. Gives specific columns to pull out from result matrix.
        Must be a subset of fields from ``SELECT`` statement.
    :type columns: string or string array

    :returns: **result** (*string array*) - containing the result set for the current query. If the result set is empty, a scalar error code is returned.

Remarks
-------

For numerical only results, use :func:`dbQueryFetchAllM` to return a matrix.

This function retrieves all rows at once. You can process rows in an
iterative manner by using the :func:`dbQueryFetchNextM` and
:func:`dbQueryFetchNextSA` functions.

Examples
----------------

::

    // Prepare a query
    qid = dbExecQuery(db_id, "SELECT * FROM
         PEOPLE WHERE COUNTRY = ?", "USA");

    /*
    ** Specify 'FIRST_NAME' and 'LAST_NAME'
    ** as columns of interest
    */
    names = dbQueryFetchAllSA(qid,
         "FIRST_NAME"$|"LAST_NAME");

    /*
    ** Print result if 'names'
    ** is not a scalar error code
    */
    if not scalmiss(names);
        print "People in the USA = " names;
    endif;

.. seealso:: Functions :func:`dbQueryFetchAllM`, :func:`dbQueryFetchNextSA`, :func:`dbQueryFetchNextM`
