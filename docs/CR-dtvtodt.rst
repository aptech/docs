
dtvtodt
==============================================

Purpose
----------------
Converts DT vector format to DT scalar format.

Format
----------------
.. function:: dtvtodt(dtv)

    :param dtv: DTV vector format.
    :type dtv: Nx8 matrix

    :returns: dt (*Nx1 vector*), DT scalar format.

Examples
----------------

::

    let dtv = { 2012 9 16 11 7 22 1 84 };
    dt = dtvtodt(dtv);

The code above assigns dt as follows:

::

    20120916110722

Source
++++++

time.src

.. seealso:: Functions :func:`dtvnormal`, :func:`timeutc`, :func:`utctodtv`, :func:`dttodtv`, :func:`dttoutc`, :func:`strtodt`, :func:`dttostr`
