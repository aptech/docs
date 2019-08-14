
cons
==============================================

Purpose
----------------

Retrieves a character string from the keyboard.

Format
----------------
.. function:: x = cons()

    :returns: **x** (*string*) - the characters entered from the keyboard

Remarks
-------

*x* is assigned the value of a character string typed in at the keyboard.
The program will pause to accept keyboard input. The maximum length of
the string that can be entered is 254 characters. The program will
resume execution when the ``ENTER`` key is pressed.

Examples
----------------

::

    x = cons();

At the cursor enter:

::

    probability

Now *x* will be equal to:

::

    x = "probability";

.. seealso:: Functions :func:`con`
