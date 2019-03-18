
printdos
==============================================

Purpose
----------------

Prints a string to the standard output.

Format
----------------
.. function:: printdos s

    :param s: string to be printed to the standard output.
    :type s: TODO

Examples
----------------

::

    printdos "\27[7m"; /* set for reverse video */
    printdos "\27[0m"; /* set for normal text */

.. seealso:: Functions :func:`print`, :func:`printfm`, :func:`screen`
