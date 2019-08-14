
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

.. NOTE:: The `for` loop is optimized for speed and much faster than a `do` loop.

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

    x = zeros(10,5);
    for i (1, rows(x), 1);
      for j (1, cols(x), 1);
    	x[i, j] = i*j;
      endfor;
    endfor;

After this loop, ``x`` is:

::

    x =  1.0000000        2.0000000        3.0000000        4.0000000        5.0000000
         2.0000000        4.0000000        6.0000000        8.0000000        10.000000
         3.0000000        6.0000000        9.0000000        12.000000        15.000000
         4.0000000        8.0000000        12.000000        16.000000        20.000000
         5.0000000        10.000000        15.000000        20.000000        25.000000
         6.0000000        12.000000        18.000000        24.000000        30.000000
         7.0000000        14.000000        21.000000        28.000000        35.000000
         8.0000000        16.000000        24.000000        32.000000        40.000000
         9.0000000        18.000000        27.000000        36.000000        45.000000
         10.000000        20.000000        30.000000        40.000000        50.000000

Example 3
+++++++++

::

    x = rndn(3, 3);
    y = rndn(3, 3);

    for i (1, rows(x), 1);
       for j (1, cols(x), 1);

          if x[i, j] >= y[i, j];
             continue;
          endif;

          temp = x[i, j];
          x[i, j] = y[i, j];
          y[i, j] = temp;

       endfor;
    endfor;

Example 4
+++++++++

::

    li = 0;
    x = rndn(100, 1);
    y = rndn(100, 1);

    for i (1, rows(x), 1);
       if x[i] != y[i];
          li = i;
          break;
       endif;
    endfor;

    if li;
       print "Compare failed on row " li;
    endif;
