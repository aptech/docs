
errorlog
==============================================

Purpose
----------------

Prints an error message to the error window and error log file.

Format
----------------
.. function:: errorlog str

    :param str: the error message to print.
    :type str: string



Remarks
-------

This command enables you to do your own error handling in your GAUSS
programs. To print an error message to the error window and error log file
along with file name and line number information, use :func:`errorlogat`.

Example
--------

Check to see if *x* is less than zero, if so create an error message and end the program.

::

   x = -4;

   if x < 0;
       errorlog "Error X is less than 0";
       end;
   endif; 

.. seealso:: Functions :func:`errorlogat`

