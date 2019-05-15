
system
==============================================

Purpose
----------------
Quits GAUSS and returns to the operating system.

.. _system:
.. index:: system

Format
----------------

::

    system;
    system c;

**Parameters**

:c: (*scalar*) an optional exit code that can be recovered by the program that 
    invoked GAUSS. The default is 0. Valid arguments are 0-255.

Remarks
-------

The `system` command always returns an exit code to the operating system
or invoking program. If you don't supply one, it returns 0. This is
usually interpreted as indicating success.

.. seealso:: Functions :func:`exec`

