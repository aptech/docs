
for
==============================================

Purpose
----------------

Begins a `for` loop.

.. _for:
.. index:: for

Format
----------------

::

    for i (start, stop, step);
        ...
    endfor;

**Parameters:**

    :i: the name of the counter variable.
    :start: (*scalar*) - the initial value of the counter.
    :stop: (*scalar*) - the final value of the counter.
    :step: (*scalar*)  - the increment value.


Remarks
-------

The counter is strictly local to the loop. The expressions, *start*, *stop*
and *step* are evaluated only once when the loop initializes and are
stored local to the loop.

The commands `break` and `continue` are supported. The `continue` command
steps the counter and jumps to the top of the loop. The `break` command
terminates the current loop.

The loop terminates when the value of *i* exceeds *stop*. If `break` is used
to terminate the loop and you want the final value of the counter, you
need to assign it to a variable before the `break` statement (see the
third example, following).

.. NOTE:: The `for` loop is optimized for speed and much faster than a `do` loop. However, it is best to vectorize code to avoid loops if possible.

Examples
----------------

Example 1
+++++++++

::

    // A basic 'for' loop
    for i (1, 4, 1);
       print i;
    endfor;

::

    1.000
    2.000
    3.000
    4.000

Example 2
+++++++++

::

    // Pre-allocate matrix to fill in
    x = zeros(10,5);

    // Iterate over all rows in 'x'
    for i (1, rows(x), 1);

      // Iterate over all columns in the i'th row
      for j (1, cols(x), 1);
          x[i, j] = i*j;
      endfor;

    endfor;

After this loop, ``x`` is:

::

    x =  1.00    2.00    3.00
         2.00    4.00    6.00
         3.00    6.00    9.00
         4.00    8.00    12.0

Example 3
+++++++++

::

    // Create two random normal matrices
    x = rndn(3, 3);
    y = rndn(3, 3);

    // Iterate over all rows
    for i (1, rows(x), 1);

       // Iterate over all columns in the i'th row
       for j (1, cols(x), 1);

          // If the corresponding element in 'x'
          // is greater than the corresponding
          // element in 'y', go to the next element
          if x[i, j] >= y[i, j];
             continue;
          endif;

          // Swap the corresponding elements
          // of 'x' and 'y'
          temp = x[i, j];
          x[i, j] = y[i, j];
          y[i, j] = temp;

       endfor;
    endfor;

Example 4
+++++++++

::

    li = 0;
    x = { 1, 2, 3, 4, 5 };
    y = { 1, 2, 9, 4, 5 };

    /*
    ** Loop over all elements until
    ** 'x' and 'y' do not match.
    */
    for i (1, rows(x), 1);
       if x[i] != y[i];
          li = i;
          break;
       endif;
    endfor;

    // If 'li' does not equal zero,
    // print the row on which a
    // difference was found
    if li;
       print "Compare failed on row " li;
    endif;
