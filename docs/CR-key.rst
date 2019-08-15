
key
==============================================

Purpose
----------------

Returns the ASCII value of the next key available in the keyboard buffer.

Format
----------------
.. function:: y = key()

    :return y: ASCII value of next available key in keyboard buffer.

    :rtype y: scalar

Remarks
-------

If you are working in terminal mode, :func:`key` does not "see" any keystrokes
until :kbd:`ENTER` is pressed. The value returned will be zero if no key is
available in the buffer or it will equal the ASCII value of the key if
one is available. The key is taken from the buffer at this time and the
next call to key will return the next key.

Here are the values returned if the key pressed is not a standard ASCII character in the range of 1-255:

=========== ================================
Value       Key Sequence
=========== ================================
1015        :kbd:`Shift+Tab`
1016-1025   :kbd:`Alt+Q, W, E, R, T, Y, U, I, O, P`
1030-1038   :kbd:`Alt+A, S, D, F, G, H, J, K, L`
1044-1050   :kbd:`Alt+Z, X, C, V, B, N, M`
1059-1068   :kbd:`F1-F10`
1071        :kbd:`HOME`
1072        :kbd:`CURSOR UP`
1073        :kbd:`PAGE UP`
1075        :kbd:`CURSOR LEFT`
1077        :kbd:`CURSOR RIGHT`
1079        :kbd:`END`
1080        :kbd:`CURSOR DOWN`
1081        :kbd:`PAGE DOWN`
1082        :kbd:`INSERT`
1083        :kbd:`DELETE`
1084-1093   :kbd:`Shift+F1-F10`
1094-1103   :kbd:`Ctrl+F1-F10`
1104-1113   :kbd:`Alt+F1-F10`
1114        :kbd:`Ctrl+PRINT SCREEN`
1115        :kbd:`Ctrl+CURSOR LEFT`
1116        :kbd:`Ctrl+CURSOR RIGHT`
1117        :kbd:`Ctrl+END`
1118        :kbd:`Ctrl+PAGE DOWN`
1119        :kbd:`Ctrl+HOME`
1120-1131   :kbd:`Alt+1, 2, 3, 4, 5, 6, 7, 8, 9, 0, -, =`
1132        :kbd:`Ctrl+PAGE UP`
=========== ================================


Examples
----------------

::

    format /rds 1,0;
    kk = 0;

    // Loop until q key
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
input. This loop will continue until the ``q`` key
(ASCII 113) is pressed.

.. seealso:: Functions :func:`keyw`, :func:`vals`, :func:`chrs`, :func:`upper`, :func:`lower`, :func:`con`, :func:`cons`
