
break
==============================================

Purpose
----------------
Breaks out of a `do` or `for` loop.

.. _break:
.. index:: break

Format
----------------

::

    break;

Examples
----------------

::

    x = rndn(4, 4);

    /*
    ** Loop through each row of 'x' using 'r' as the loop
    ** counter
    */
    for r(1, rows(x), 1);
       // For each row, loop through its elements
       for c(1, cols(x), 1);
          // Set the diagonal to 1
          if c == r;     

             x[r, c] = 1;

          // Leave upper triangle as it is
          elseif c > r;

             // Terminate inner loop
             break;
          else;
             // Set lower triangle elements to 0
             x[r, c] = 0;
          endif;
       endfor;           /* break jumps to the statement after
                            this endfor */
    endfor;

After running the code above, *x* should be a lower triangular matrix similar to below. Due to
the use of random data, your matrix will have different non-zero elements above the diagonal.

::

    1.000  1.288 -0.060  1.801
    0.000  1.000  1.609  1.474
    0.000  0.000  1.000 -0.768
    0.000  0.000  0.000  1.000

Remarks
-------

This command works just like in **C**.

.. seealso:: Functions `continue`, `do while`, `do until`, `for`
