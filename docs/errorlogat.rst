
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
programs. 

To print an error message to the error window and error log file
*without* the file name and line number, use :func:`errorlog`.


Example
---------

::

    // Set X to be equal to +Infinity
    X = __INFP;

    // Check to see if X is an infinity, nan or missing value
    if isinfnanmiss(X);
        // Write error message
        errorlogat "X contains is a nan, missing value or infinity";
    endif;

The above example will print the message:

::

    X contains is a nan, missing value or infinity

to the error output window and error log file. It will also report the line number on which the :func:`errorlogat` statement was called.

.. seealso:: Functions :func:`errorlog`

