
doswin
==============================================

Purpose
----------------

Opens the DOS compatibility window with default settings. 

.. WARNING:: This function is no longer supported. This documentation is provided as a reference for understanding legacy code. In many cases, you may simply comment out calls to :func:`doswin` and the program will run successfully in the program input/output window.

Format
----------------
.. function:: doswin

Remarks
-------

Calling :func:`doswin` is equivalent to:

::

   call DOSWinOpen("", error(0));

Source
------

gauss.src

