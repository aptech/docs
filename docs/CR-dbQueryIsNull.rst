
dbQueryIsNull
==============================================

Purpose
----------------

Returns 1 if the query is active, positioned on a valid record and the
field is ``NULL``; otherwise returns 0.

Reports whether the current field pointed at by an active query positioned on
a valid record is ``NULL``.

Format
----------------
.. function:: ret = dbQueryIsNull(qid, field)

    :param qid: query number.
    :type qid: scalar

    :param field: index into result set.
    :type field: scalar

    :return ret: 1 if the field is ``NULL`` or 0 otherwise.

    :type ret: scalar

Remarks
-------

Note that for some drivers, :func:`dbQueryIsNull` will not return accurate
information until after an attempt is made to retrieve data.

.. seealso:: Functions :func:`dbQueryIsActive`, :func:`dbQueryIsValid`
