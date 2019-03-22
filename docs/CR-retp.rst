
retp
==============================================

Purpose
----------------
Returns from a procedure or keyword.

Format
----------------
.. function:: retpretp(x, y,...)



Remarks
-------

For more details, see **Procedures and Keywords**, Chapter 1.

In a retp statement 0-1023 items may be returned. The items may be
expressions. Items are separated by commas.

It is legal to return with no arguments, as long as the procedure is
defined to return 0 arguments.

.. seealso:: Functions :func:`proc`, :func:`keyword`, :func:`endp`
