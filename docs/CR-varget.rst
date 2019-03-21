
varget
==============================================

Purpose
----------------
Accesses a global variable whose name is given as a string argument.

Format
----------------
.. function:: varget(s)

    :param s: 
    :type s: string containing the name of the global symbol
        you wish to access

    :returns: y (*TODO*), contents of the variable whose name is
        in  s.

Examples
----------------

::

    alpha = 1;
    beta = 2;
    letter = "alpha";
    
    //Check to see if a variable named alpha exists
    if typecv(letter) == miss(0,0);
       print letter " does NOT exist";
    else;
       //Assign the value of the variable named alpha to 'tmp'
       tmp = varget(letter);
       print "the value of " letter " is: " tmp;
    endif;

The code above produces the following output:

::

    the value of alpha is: 1

