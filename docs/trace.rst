
trace
==============================================

Purpose
----------------
Allows the user to trace program execution for debugging purposes.

.. _trace:
.. index:: trace

Format
----------------

::

    trace new;
    trace new, mask;

**Parameters**

    :new: (*scalar*) new value for trace flag.
    :mask: (*scalar*) optional mask to allow leaving some bits of the trace flag unchanged.

Examples
----------------

::

    trace 1+8;    // trace fn/proc calls/returns to standard 
                  // output 
    trace 2+8;    // trace line numbers to standard output 
    trace 1+2+8;  // trace line numbers and fn/proc calls/
                  // returns to standard output
    trace 1+16;   // trace fn/proc calls/returns to printer 
    trace 2+16;   // trace line numbers to printer
    trace 1+2+16; // trace line numbers and fn/proc calls/ 
                  // returns to printer

Remarks
-------

The `trace` command has no effect unless you are running your program
under GAUSS's source level debugger. Setting the `trace` flag will not
generate any debugging output during normal execution of a program.

The argument is converted to a binary integer with the following
meanings:

+-------------+---------+----------------------------+
| bit         | decimal | meaning                    |
+-------------+---------+----------------------------+
| ones        | 1       | trace calls/returns        |
+-------------+---------+----------------------------+
| twos        | 2       | trace line numbers         |
+-------------+---------+----------------------------+
| fours       | 4       | unused                     |
+-------------+---------+----------------------------+
| eights      | 8       | output to window           |
+-------------+---------+----------------------------+
| sixteens    | 16      | output to print            |
+-------------+---------+----------------------------+
| thirty-twos | 32      | output to auxiliary output |
+-------------+---------+----------------------------+
| sixty-fours | 64      | output to error log        |
+-------------+---------+----------------------------+

You must set one or more of the output bits to get any output from
`trace`. If you set `trace` to 2, you'll be doing a line number trace of
your program, but the output will not be displayed anywhere.

The `trace` output as a program executes will be as follows:

+---------+------------------------------------+
| (+GRAD) | calling function or procedure GRAD |
+---------+------------------------------------+
| (-GRAD) | returning from GRAD                |
+---------+------------------------------------+
| [47]    | executing line 47                  |
+---------+------------------------------------+

Note that the line number trace will only produce output if the program
was compiled with line number records.

To set a single bit use two arguments:

+------------------+----------------------------+
| ``trace 16,16;`` | turn on output to printer  |
+------------------+----------------------------+
| ``trace 0,16;``  | turn off output to printer |
+------------------+----------------------------+

.. seealso:: Functions :func:`lineson`

