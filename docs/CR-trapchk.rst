
trapchk
==============================================

Purpose
----------------
Tests the value of the trap flag.

Format
----------------
.. function:: trapchk(m)

    :param m: mask value
    :type m: scalar

    :returns: y (*scalar which is*) the result of the bitwise
        logical AND of the `trap` flag and the *mask* value.

Remarks
-------

To check the various bits in the `trap` flag, add the decimal values for
the bits you wish to check according to the chart below and pass the sum
in as the argument to the :func:`trapchk` function:

+-----+---------------+
| bit | decimal value |
+-----+---------------+
| 0   | 1             |
+-----+---------------+
| 1   | 2             |
+-----+---------------+
| 2   | 4             |
+-----+---------------+
| 3   | 8             |
+-----+---------------+
| 4   | 16            |
+-----+---------------+
| 5   | 32            |
+-----+---------------+
| 6   | 64            |
+-----+---------------+
| 7   | 128           |
+-----+---------------+
| 8   | 256           |
+-----+---------------+
| 9   | 512           |
+-----+---------------+
| 10  | 1024          |
+-----+---------------+
| 11  | 2048          |
+-----+---------------+
| 12  | 4096          |
+-----+---------------+
| 13  | 8192          |
+-----+---------------+
| 14  | 16384         |
+-----+---------------+
| 15  | 32768         |
+-----+---------------+

If you want to test if either bit 0 or bit 8 is set, then pass an
argument of 1+256 or 257 to :func:`trapchk`. The following table demonstrates
values that will be returned for:

::

   y = trapchk(257);

+-----------------------------+-----+-----+-----------------------------+
|                             | 0   | 1   | value of bit 0 in trap flag |
+-----------------------------+-----+-----+-----------------------------+
| 0                           | 0   | 1   |                             |
+-----------------------------+-----+-----+-----------------------------+
| 1                           | 256 | 257 |                             |
+-----------------------------+-----+-----+-----------------------------+
| value of bit 8 in trap flag |     |     |                             |
+-----------------------------+-----+-----+-----------------------------+

GAUSS functions that test the trap flag currently test only bits 0 and 1.

.. seealso:: Functions :func:`scalerr`, `trap`, :func:`error`

