
break
==============================================

Purpose
----------------
 Breaks out of a do or for loop.

Format
----------------
.. function:: break

Examples
----------------

::

    x = rndn(4,4);
    
    //Loop through each row of 'x' using 'r' as the loop 
    //counter
    for r(1, rows(x), 1);
       //For each row, loop through its elements 
       for c(1, cols(x), 1);
          if c == r;     /* Set the diagonal to 1 */
             x[r,c] = 1;
          elseif c > r;  /* leave upper triangle as it is */  
             break;      /* terminate inner loop */ 
          else;
             x[r,c] = 0; /* set lower triangle elements to 0 */ 
          endif;
       endfor;           /* break jumps to the statement after
                            this endfor */
    endfor;

After running the code above, x should be a lower triangular matrix similar to below. Due to
the use of random data, your matrix will have different non-zero elements above the diagonal.

::

    1.000  1.288 -0.060  1.801
    0.000  1.000  1.609  1.474
    0.000  0.000  1.000 -0.768
    0.000  0.000  0.000  1.000

Remarks
+++++++

This command works just like in C.

.. seealso:: Functions :func:`continue`, :func:`do`, :func:`for`
