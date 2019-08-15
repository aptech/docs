
varget
==============================================

Purpose
----------------
Accesses a global variable whose name is given as a string argument.

Format
----------------
.. function:: y = varget(s)

    :param s: the name of the global symbol you wish to access
    :type s: string

    :return y: contents of the variable whose name is in *s*.

    :rtype y: any

Remarks
-------

This function searches the global symbol table for the symbol whose name
is in *s* and returns the contents of the variable if it exists. If the
symbol does not exist, the function will terminate with an Undefined
symbol error message. If you want to check to see if a variable exists
before using this function, use :func:`typecv`.


Examples
----------------

::

    alpha = 1;
    beta = 2;
    letter = "alpha";
    
    // Check to see if a variable named alpha exists
    if typecv(letter) == miss(0,0);
       print letter " does NOT exist";
    else;
       // Assign the value of the variable named alpha to 'tmp'
       tmp = varget(letter);
       print "the value of " letter " is: " tmp;
    endif;

The code above produces the following output:

::

    the value of alpha is: 1

