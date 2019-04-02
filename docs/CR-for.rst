
for
==============================================

Purpose
----------------

Begins a for loop.

.. DANGER:: Fix formatting for format

Format
----------------
.. function:: for i (start, stop, step)
              endfor

    :param i: the name of the counter variable.
    :type i: literal

    :param start: the initial value of the counter.
    :type start: scalar expression

    :param stop: the final value of the counter.
    :type stop: scalar expression

    :param step: the increment value.
    :type step: scalar expression

Remarks
-------

The counter is strictly local to the loop. The expressions, *start*, *stop*
and *step* are evaluated only once when the loop initializes and are
stored local to the loop.

The commands :func:`break` and :func:`continue` are supported. The :func:`continue` command
steps the counter and jumps to the top of the loop. The :func:`break` command
terminates the current loop.

The loop terminates when the value of *i* exceeds *stop*. If :func:`break` is used
to terminate the loop and you want the final value of the counter, you
need to assign it to a variable before the :func:`break` statement (see the
third example, following).

.. NOTE:: The :func:`for` loop is optimized for speed and much faster than a :func:`do` loop.

Examples
----------------

Example 1
+++++++++

::

    //A basic 'for' loop
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
    	x[i,j] = i*j;
      endfor;
    endfor;

Example 3
+++++++++

::

    x = rndn(3,3);
    y = rndn(3,3);
    
    for i (1, rows(x), 1);
       for j (1, cols(x), 1);
          if x[i,j] >= y[i,j];
             continue;
          endif;
          temp = x[i,j];
          x[i,j] = y[i,j];
          y[i,j] = temp;
       endfor;
    endfor;

Example 4
+++++++++

::

    li = 0;
    x = rndn(100,1);
    y = rndn(100,1);
    
    for i (1, rows(x), 1);
       if x[i] != y[i];
          li = i;
          break;
       endif;
    endfor;
    
    if li;
       print "Compare failed on row " li;
    endif;

