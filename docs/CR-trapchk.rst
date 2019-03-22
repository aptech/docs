
trapchk
==============================================

Purpose
----------------
Tests the value of the trap flag.

Format
----------------
.. function:: trapchk(m)

    :param m: 
    :type m: scalar mask value

    :returns: y (*scalar which is*) the result of the bitwise
        logical AND of the trap flag
        and the mask value.



Remarks
-------

To check the various bits in the trap flag, add the decimal values for
the bits you wish to check according to the chart below and pass the sum
in as the argument to the trapchk function:

.. raw:: html

   <div align="center">

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

