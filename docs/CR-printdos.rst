
printdos
==============================================

Purpose
----------------

Prints a string to the standard output.

.. _printdos:
.. index:: printdos

Format
----------------

::

    printdos s;

**Parameters**

:s: (*string*) to be printed to the standard output

Remarks
-------

This function is useful for printing messages to the screen when ``screen
off`` is in effect. The output of this function will not go to the
auxiliary output.

This function was used in the past to send escape sequences to the
ansi.sys device driver on DOS. It still works on some terminals.


Examples
----------------

::

    printdos "\27[7m"; /* set for reverse video */
    printdos "\27[0m"; /* set for normal text */

.. seealso:: Functions :func:`print`, :func:`printfm`, `screen`

