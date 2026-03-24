
keyav
==============================================

Purpose
----------------

Check if keystroke is available.

Format
----------------
.. function:: x = keyav()

    :return x: value of key or 0 if no key is available.

    :rtype x: scalar

Example
-------

::

    // Check if a key has been pressed
    // (interactive mode only)
    k = keyav();
    if k;
        print "Key pressed:" k;
    else;
        print "No key available.";
    endif;

.. seealso:: Functions :func:`keyw`, :func:`key`
