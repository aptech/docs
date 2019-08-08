
keyword
==============================================

Purpose
----------------

Begins the definition of a `keyword` procedure. Keywords are user-defined functions with local or global variables.

.. _keyword:
.. index:: keyword

Format
----------------

::

    keyword name(str);
        ...;
    endp;

**Parameters:**

:name: (*scalar*) name of the keyword. This name will be a global symbol.
:str: (*string*) a name to be used inside the keyword to refer to the argument that is passed to the keyword when the keyword is called.
    This will always be local to the keyword, and cannot be accessed from outside the keyword or from other keywords or procedures.


Remarks
-------

A keyword definition begins with the `keyword` statement and ends with the
`endp` statement. See **Procedures and Keywords**, Chapter 1.

Keywords always have 1 string argument and 0 returns. GAUSS will take
everything past name, excluding leading spaces, and pass it as a string
argument to the keyword. Inside the keyword, the argument is a local
string. The user is responsible to manipulate or parse the string.

An example of a keyword definition is:

::

   keyword add(str);
      local tok, sum;

      sum = 0;

      do until str $== "";

         { tok, str } = token(str);
         sum = sum + stof(tok);

      endo;

      print "Sum is: " sum;
   endp;

To use this keyword, type:

::

   add 1 2 3 4 5;

This keyword will respond by printing:

::

   Sum is: 15

.. seealso:: Functions `proc`, `local`, `endp`
