
DOSWinCloseall
==============================================

Purpose
----------------

Closes the DOS compatibility window. NOTE: The DOS compatibility window is no longer supported. This documenation is provided as a reference for understanding legacy code.

Format
----------------
.. function:: DOSWinCloseall

Remarks
-------

Calling DOSWinCloseall closes the DOS window immediately, without asking
for confirmation. If a program is running, its I/O reverts to the
Command window.


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

