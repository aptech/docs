
timedt
==============================================

Purpose
----------------

Returns system date and time in DT scalar format.

Format
----------------
.. function:: dt = timedt()

    :returns: dt (*scalar*), system date and time in DT scalar format.

Remarks
-------

The DT scalar format is a double precision representation of the date
and time. In the DT scalar format, the number:

::

   20100306071511

represents:

::

   07:15:11 or 7:15:11 AM on March 6, 2010.

Source
------

time.src

.. seealso:: Functions :func:`todaydt`, :func:`timeutc`, :func:`dtdate`

