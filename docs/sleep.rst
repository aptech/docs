
sleep
==============================================

Purpose
----------------
Sleeps for a specified number of seconds.

Format
----------------
.. function:: unslept = sleep(secs)

    :param secs: number of seconds to sleep.
    :type secs: scalar

    :return unslept: number of seconds not slept.

    :rtype unslept: scalar

Remarks
-------

*secs* does not have to be an integer. If your system does not permit
sleeping for a fractional number of seconds, *secs* will be rounded to the
nearest integer, with a minimum value of 1.

If a program sleeps for the full number of *secs* specified, :func:`sleep` returns
0; otherwise, if the program is awakened early (e.g., by a signal),
:func:`sleep` returns the amount of time not slept.

A program may sleep for longer than *secs* seconds, due to system scheduling.

Examples
----------------

::

    // Sleep for 2 seconds
    unslept = sleep(2);
    print unslept;

If the program sleeps for the full 2 seconds, the output is:

::

    0.0000000

.. seealso:: Functions :func:`pause`, :func:`waitc`
