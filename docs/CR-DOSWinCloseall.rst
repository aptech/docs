
DOSWinCloseall
==============================================

Purpose
----------------

Closes the DOS compatibility window. NOTE: The DOS compatibility window is no longer supported. This documenation is provided as a reference for understanding legacy code.

Format
----------------
.. function:: DOSWinCloseall

Examples
----------------

::

    let attr = 50 50 7 0 7;
    if not DOSWinOpen("Legacy Window", attr);
       errorlog "Failed to open DOS window, aborting";
       stop;
    endif;
     .
     .
     .
    DOSWinCloseall;

