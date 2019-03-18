
dttoutc
==============================================

Purpose
----------------
Converts DT scalar format to UTC scalar format.

Format
----------------
.. function:: dttoutc(dt)

    :param dt: DT scalar format.
    :type dt: Nx1 vector

    :returns: utc (*Nx1 vector*), UTC scalar format.

Examples
----------------

::

    dt = 20010326085118;
    tc = dttoutc(dt);
     
    print "tc = " tc;

The above code produces the following output:

::

    tc = 985633642;

Source
++++++

time.src

.. seealso:: Functions :func:`dtvnormal`, :func:`timeutc`, :func:`utctodtv`, :func:`dttodtv`, :func:`dtvtodt`, :func:`dtvtoutc`, :func:`dtvtodt`, :func:`strtodt`, :func:`dttostr`
