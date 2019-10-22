
vals
==============================================

Purpose
----------------

Converts a string into a matrix of its ASCII values.

Format
----------------
.. function:: y = vals(s)

    :param s: string of length :math:`N` where :math:`N > 0`
    :type s: string

    :return y: containing the ASCII values of the characters in the string *s*.

    :rtype y: Nx1 matrix

Examples
----------------

::

    // Initialize 'k' so it will be 0 for the first iteration of
    // the 'do while' loop
    k = 0;
    
    // Prompt the user for input
    print"Continue Program? [Y/N]";
    
    // Continually check for keyboard input and exit the loop on
    // keyboard input
    do while (k == 0);
       k = key;
    endo;
    
    // Follow a different code branch depending upon which key
    // the user entered
    if k == vals("Y") or k == vals("y");
       print "You chose to continue";
    else;
       print "Exiting program now";
    endif;

In this example the :func:`key` function is used to read 
keyboard input. When :func:`key` returns a nonzero value,
meaning a key has been pressed, the ASCII value it
returns is tested to see if it is an uppercase or lowercase 'Y'.
If it is, the program will follow the first branch and print:

::

    You chose to continue

otherwise, it will follow the second branch and print:

::

    Exiting program now

Remarks
-------

If the string is null, the function will fail and an error message will be given.


.. seealso:: Functions :func:`chrs`, :func:`ftos`, :func:`stof`

