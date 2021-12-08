
warninglogat
==============================================

Purpose
----------------

Prints a warning message to the window and warning log file, along with the file name
and line number at which the warning occurred. The only difference between this and :func:`errorlogat` 
is that it will display a warning icon in the error output window.

Format
----------------
.. function:: warninglogat str

    :param str: the warning message to print.
    :type str: string



Remarks
-------

This command enables you to do your own warning handling in your GAUSS
programs. 

To print a warning message to the warning window and warning log file
*without* the file name and line number, use :func:`warninglog`.


Example
---------

::

    // Set X to be equal to +Infinity
    X = __INFP;

    // Check to see if X is an infinity, nan or missing value
    if isinfnanmiss(X);
        // Write warning message
        warninglogat "X contains a nan, missing value or infinity";
    endif;

The above example will print the message:

::

    X contains a nan, missing value or infinity

to the warning output window and warning log file. It will also report the line number on which the :func:`warninglogat` statement was called.

.. seealso:: Functions :func:`warninglog`, :func:`errorlog`, :func:`errorlogat`

