
keyw
==============================================

Purpose
----------------

Waits for and gets a key.

Format
----------------
.. function:: keyw

    :returns: k (*scalar*), ASCII value of the key pressed.



Remarks
-------

If you are working in terminal mode, GAUSS will not see any input until
you press the ENTER key. keyw gets the next key from the keyboard
buffer. If the keyboard buffer is empty, keyw waits for a keystroke. For
normal keys, keyw returns the ASCII value of the key.

