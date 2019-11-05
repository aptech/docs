
token
==============================================

Purpose
----------------
Extracts the leading token from a string.

Format
----------------
.. function:: { token, str_left } = token(str)

    :param str: the string to parse.
    :type str: string

    :return token: the first token in *str*.

    :rtype token: string

    :return str_left: *str* minus *token*.

    :rtype str_left: string

Examples
----------------
Here is a keyword that uses :func:`token` to parse its string parameter:

::

    // Create a keyword called 'add' that takes the input
    //'s' and executes all of the code from the 'keyword
    // add(s)' line until the 'endp' statement each time
    // it is called
    keyword add(s);
       local tok, sum;
       sum = 0;

       // Continue loop until 's' equals an empty string
       do until s $== "";

          // Remove the first token from 's' and return
          // it in 'tok'
          { tok, s } = token(s);

          // Convert the string in 'tok' to a floating
          // point number and add it to 'sum'
          sum = sum + stof(tok);
       endo;

       // Set the formatting for print statements to
       // create 1 space between numbers and
       // to print 2 digits after the decimal point
       format /rd 1,2;
       print "Sum is: " sum;
    endp;

If you type:

::

    // Since it is a 'keyword' and not a 'proc', 'add'
    // will take everything between 'add' and the
    // semi-colon as a string input and refer to it
    // internally as the 's' variable
    add 1 2 3 4 5;

*add* will respond:

::

    Sum is: 15.00

Remarks
-------

*str* can be delimited with commas or spaces.

The advantage of :func:`token` over :func:`parse` is that :func:`parse` is limited to tokens of
8 characters or less; :func:`token` can extract tokens of any length.


Source
------

token.src

.. seealso:: Functions :func:`parse`
