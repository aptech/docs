
chrs
==============================================

Purpose
----------------

Converts a matrix of ASCII values into a string containing the appropriate characters.

Format
----------------
.. function:: y = chrs(x)

    :param x: matrix of ASCII values to be converted.
    :type x: NxK matrix

    :return s: This 1x1 string will contain NxK characters whose ASCII values are equal to the values in the elements of *x*.

    :type s: string

Remarks
-------


This function is useful for embedding control codes in strings and for
creating variable length strings when formatting printouts, reports,
etc.

Examples
----------------

Basic example
+++++++++++++

::

    // 42 is the ascii value for an asterisk '*'
    print chrs(42);

The code above returns:

::

    *

Multicharacter example
+++++++++++++++++++++

::

    // ASCII character codes:
    // 72 -> H, 105 -> i, 33 -> !
    acc = { 72 105 33 };

    // Convert the character codes in 'acc'
    // into a string of characters
    s = chrs(acc);

After the code above, *s* will equal:

::

    Hi!

Interactive example
++++++++++++++++++

:func:`chrs` can be used to create an interactive program in which the user is prompted
for keyboard input which the code uses to make decisions.

::

    // Print a string to prompt the user for input
    print "Choose a parameter: Enter [a,b,c]";

    /*
    ** Wait for the user to enter a keystroke and assign the
    ** ASCII value of that key to 'param'
    */
    param = keyw;

    // Convert the ASCII value to a string
    paramString = chrs(param);

    if paramString == "a";
       print "You have chosen:" "a";
       // execute code for this choice
    elseif paramString == "b";
       print "You have chosen:" "b";
       // execute code for this choice
    elseif paramString == "c";
       print "You have chosen:" "c";
       // execute code for this choice
    endif;

.. seealso:: Functions :func:`vals`, :func:`ftos`, :func:`stof`
