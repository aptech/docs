
dtvtoutc
==============================================

Purpose
----------------

Converts DTV vector format to UTC scalar format.

Format
----------------
.. function:: dtvtoutc(dtv)

    :param dtv: DTV vector format.
    :type dtv: Nx8 matrix

    :returns: utc (*Nx1 vector*), UTC scalar format.

Examples
----------------

::

    dtv = utctodtv(timeutc);
    utc = dtvtoutc(dtv);

::

    dtv = 2012    7   17   10   13   48    2  198 
    utc = 1342545228

.. seealso:: Functions :func:`dtvnormal`, :func:`timeutc`, :func:`utctodt`, :func:`dttodtv`, :func:`dttoutc`, :func:`dtvtodt`, :func:`dtvtoutc`, :func:`strtodt`, :func:`dttostr`
