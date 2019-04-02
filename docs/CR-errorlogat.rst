
errorlogat
==============================================

Purpose
----------------

Prints an error message to the window and error log file, along with the file name
and line number at which the error occurred.

Format
----------------
.. function:: errorlogat str

    :param str: the error message to print.
    :type str: string



Remarks
-------

This command enables you to do your own error handling in your GAUSS
programs. To print an error message to the window and error log file
without file name and line number information, use :func:`errorlog`.

.. seealso:: Functions :func:`errorlog`

