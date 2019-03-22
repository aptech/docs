
do while, do until
==============================================

Purpose
----------------

Executes a series of statements in a loop as long as a given expression is true (or false).

Format
----------------
.. function:: do while expression ... endo
              do until expression ... endo
endo

Remarks
-------

expression is any expression that returns a scalar. It is ``TRUE`` if it is
nonzero and ``FALSE`` if it is zero.

In a :code:`do while` loop, execution of the loop will continue as long as the
expression is ``TRUE``.

In a :code:`do until` loop, execution of the loop will continue as long as the
expression is ``FALSE``.

The condition is checked at the top of the loop. If execution can
continue, the statements of the loop are executed until the :code:`endo` is
encountered. Then GAUSS returns to the top of the loop and checks the
condition again.

The :code:`do` loop does not automatically increment a counter. See the first
example below.

:code:`do` loops may be nested.

.. NOTE:: It is often possible to avoid using loops in GAUSS by using the
    appropriate matrix operator or function. It is almost always preferable
    to avoid loops when possible, since the corresponding matrix operations
    can be much faster.

Examples
----------------

::

    format /rdn 1,0;
    space = " ";
    comma = ",";
    i = 1;
    do while i <= 4;
       j = 1;
       do while j <= 3;
          print space i comma j;;
          j = j+1;
       endo;
       i = i+1;
       print;
    endo;

The code above prints the following output:

::

    1,1 1,2 1,3
    2,1 2,2 2,3
    3,1 3,2 3,3
    4,1 4,2 4,3

In the example above, two nested loops are executed and the loop
counter values are printed out. Note that the inner loop counter
must be reset inside of the outer loop before entering the inner
loop. An empty print statement is used to print a carriage
return/line feed sequence after the inner loop finishes.
The following are examples of simple loops that execute a
predetermined number of times. These loops will both have the result
shown.
First loop:

::

    format /rd 1,0;
    i = 1;
    do while i <= 10;
        print i;;
        i = i+1;
    endo;

::

    1 2 3 4 5 6 7 8 9 10

Second loop:

::

    format /rd 1,0;
       i = 1;
       do until i > 10;
           print i;;
           i = i+1;
      endo;

::

    1 2 3 4 5 6 7 8 9 10

.. seealso:: Functions :func:`continue`, :func:`break`

