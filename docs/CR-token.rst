
token
==============================================

Purpose
----------------
Extracts the leading token from a string.

Format
----------------
.. function:: token(str)

    :param str: the string to parse.
    :type str: string

    :returns: token (*string*), the first token in  str.

    :returns: str_left (*string*), str minus  token.

Examples
----------------
Here is a keyword that uses token to parse its string parameter:

::

    //Create a keyword called 'add' that takes the input 
    //'s' and executes all of the code from the 'keyword 
    //add(s)' line until the 'endp' statement each time
    //it is called
    keyword add(s);
       local tok,sum;
       sum = 0;
    
       //Continue loop until 's' equals an empty string
       do until s $== "";
    
          //Remove the first token from 's' and return
          //it in 'tok'
          { tok, s } = token(s);
    
          //Convert the string in 'tok' to a floating
          //point number and add it to 'sum'
          sum = sum + stof(tok);
       endo;
    
       //Set the formatting for print statements to 
       //create 1 space between numbers and
       //to print 2 digits after the decimal point
       format /rd 1,2;
       print "Sum is: " sum;
    endp;

If you type:

::

    //Since it is a 'keyword' and not a 'proc', 'add'
    //will take everything between 'add' and the 
    //semi-colon as a string input and refer to it 
    //internally as the 's' variable
    add 1 2 3 4 5 6;

add will respond:

::

    Sum is: 15.00

Source
++++++

token.src

.. seealso:: Functions :func:`parse`
