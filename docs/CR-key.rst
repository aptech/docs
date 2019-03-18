
key
==============================================

Purpose
----------------

Returns the ASCII value of the next key available in the keyboard buffer.

Format
----------------
.. function:: key

    :returns: y (*scalar*), ASCII value of next available key in keyboard buffer.

Examples
----------------

::

    format /rds 1,0;
    kk = 0;
    do until kk == 113;
       kk = key;
       if kk == 0;
          continue;
       elseif kk == vals(" ");
          print "space \\" kk;
       elseif kk >= vals("0") and kk <= vals("9");
          print "digit \\" kk chrs(kk);
       else;
          print "\\" kk;
       endif;
    endo;

This is an example of a loop that processes keyboard
input. This loop will continue until the  q key
(ASCII 113) is pressed.

.. seealso:: Functions :func:`vals`, :func:`chrs`, :func:`upper`, :func:`lower`, :func:`con`, :func:`cons`
