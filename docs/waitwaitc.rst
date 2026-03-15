
wait, waitc
==============================================

Purpose
----------------
Waits until any key is pressed.

.. _wait:
.. _waitc:
.. index:: wait, waitc

Format
----------------

::

    wait;
    waitc;

Remarks
-------

If you are working in terminal mode, these commands do not "see" any
keystrokes until :kbd:`ENTER` is pressed. `waitc` clears any pending keystrokes
before waiting until another key is pressed.

Examples
--------

::

    // Pause until a key is pressed
    print "Press any key to continue...";
    wait;

::

    // Clear pending keystrokes, then wait for a new one
    print "Press a key to start...";
    waitc;

Source
------

wait.src, waitc.src

.. seealso:: Functions :func:`sleep`, :func:`pause`, :func:`keyav`

