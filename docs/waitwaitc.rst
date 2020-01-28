
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

Source
------

wait.src, waitc.src

.. seealso:: Functions :func:`pause`

