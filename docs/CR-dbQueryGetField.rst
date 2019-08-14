
dbQueryGetField
==============================================

Purpose
----------------

Returns the value of a specified field in the current record. An overloaded version
that accepts a column name as input is available, but not as efficient.

Format
----------------
.. function:: field_value = dbQueryGetField(qid, idx_or_name)

    :param qid: query number.
    :type qid: scalar

    :param idx_or_name: index or name of the field whose value should be returned.
    :type idx_or_name: scalar or string

.. WARNING:: Specifying a string name may result in much slower performance than a numeric index. Use with caution.


Remarks
-------

The fields are numbered from left to right using the text of the ``SELECT``
statement, e.g. in

::

   // Execute query
   qid = dbExecQuery(db_id, "SELECT forename, surname FROM people");

   do while dbQuerySeekNext(qid);
      // Using field index
      forename = dbQueryGetField(qid, 1);

      // Using field index
      surname = dbQueryGetField(qid, 2);

      // Using field name
      forename = dbQueryGetField(qid, "forename");

      // Using field name
      surname = dbQueryGetField(qid, "surname");
   endo;

Field 1 is *forename* and field 2 is *surname*. Using ``SELECT *`` is not
recommended because the order of the fields in the query is undefined.

.. seealso:: :func:`dbQueryFetchOneM`, :func:`dbQueryFetchOneSA`
