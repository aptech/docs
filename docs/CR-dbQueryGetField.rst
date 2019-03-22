
dbQueryGetField
==============================================

Purpose
----------------

Returns the value of a specified field in the current record. An overloaded version
that accepts a column name as input is available, but not as efficient.

Format
----------------
.. function:: dbQueryGetField(qid, idx_or_name)

    :param qid: query number.
    :type qid: scalar

    :param idx_or_name: index or name of the field whose value should be returned.
    :type idx_or_name: scalar or string

.. WARNING:: Using the *name* overload will result in decreased performance. Use with caution.


Remarks
-------

The fields are numbered from left to right using the text of the ``SELECT``
statement, e.g. in

::

   qid = dbExecQuery("SELECT forename, surname FROM people");

   do while dbQuerySeekNext(qid);
      forename = dbQueryGetField(qid, 1);
      // Using field index
      surname = dbQueryGetField(qid, 2);
      // Using field index
      forename = dbQueryGetField(qid, "forename");
      // Using field name
      surname = dbQueryGetField(qid, "surname");
      // Using field name
   endo;

Field 1 is *forename* and field 2 is *surname*. Using ``SELECT *`` is not
recommended because the order of the fields in the query is undefined.

.. seealso:: :func:`dbQueryFetchOneM`, :func:`dbQueryFetchOneSA`

