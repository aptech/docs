
warninglog
==============================================

Purpose
----------------

Prints a warning message to the error window and error log file. The only difference between this and :func:`errorlog` is that it will display a warning icon in the error output window.

Format
----------------
.. function:: warninglog str

    :param str: the warning message to print.
    :type str: string


Remarks
-------

This command enables you to do your own warning handling in your GAUSS
programs. To print a warning message to the error window and error log file
along with file name and line number information, use :func:`warninglogat`.

Example
--------

Check to see if *x* is less than zero, if so create an warning message and end the program.

::

   x = -4;

   if x < 0;
       warninglog "Warning X is less than 0";
       end;
   endif; 

.. seealso:: Functions :func:`warninglogat`, :func:`errorlog`, :func:`errorlogat`

