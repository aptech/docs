
chrs
==============================================

Purpose
----------------

Converts a matrix of ASCII values into a string containing the appropriate characters.

Format
----------------
.. function:: chrs(x)

    :param x: NxK matrix.
    :type x: TODO

    :returns: y (*TODO*), string of length N*K containing the characters
        whose ASCII values are equal to the values in
        the elements of x.

Examples
----------------

::

    //42 is the ascii value for an asterisk '*'
    
    print chrs(42);

The code above returns:

::

    *

chrs can be used to create an interactive program in which the user is prompted
for keyboard input which the code uses to make decisions.

::

    //Print a string to prompt the user for input
    print "Choose a parameter: Enter [a,b,c]";
    
    //Wait for the user to enter a keystroke and assign the 
    //ASCII value of that key to 'param'
    param = keyw;
    
    //Convert the ASCII value to a string
    paramString = chrs(param);
    
    if paramString == "a";
       print "You have chosen:" "a";
       //execute code for this choice
    elseif paramString == "b";
       print "You have chosen:" "b";
       //execute code for this choice
    elseif paramString == "c";
       print "You have chosen:" "c";
       //execute code for this choice
    endif;

.. seealso:: Functions :func:`vals`, :func:`ftos`, :func:`stof`
