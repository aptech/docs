
todaydt
==============================================

Purpose
----------------

Returns system date in DT scalar format. The time returned is 
always midnight (00:00:00), the beginning of the returned day.

Format
----------------
.. function:: todaydt

    :returns: dt (*scalar*), system date in DT scalar format.



Remarks
-------

The DT scalar format is a double precision representation of the date
and time. In the DT scalar format, the number:

::

   20120906130525

represents 13:05:25 or 1:05:25 PM on September 6, 2012.

