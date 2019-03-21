
continue
==============================================

Purpose
----------------

Jumps to the top of a :func:`do` or :func:`for` loop.

Format
----------------
.. function:: continue

Remarks
------------

This command works just as in **C**.

Examples
----------------

::

    rndseed   8989;
    x = rndn(4,4);
    //Loop through each row of 'x' using 'r' as the loop
    //counter
    for r(1, rows(x), 1);
       //Loop through each element in our current row
       for c(1, cols(x), 1); /* continue jumps here */
             //If we are on the diagonal skip the rest of the 
             //inner loop
             if c == r;
                continue;
             endif;
          //Set the non-diagonal elements to 0
          x[r,c] = 0;
       endfor;
    endfor;

Before the loops, x looks like:

::

    0.010555555     -0.045969063       0.12701699        1.6454828 
    1.2380373       0.53988699        1.1556776      -0.53575797 
    0.14056238       0.11221419       0.91500922       -2.2910169 
    1.4278412      -0.96476892       0.22852569       -1.6014053

After the loops above, x looks like:

::

    0.010555555       0.00000000       0.00000000       0.00000000 
    0.00000000       0.53988699       0.00000000       0.00000000 
    0.00000000       0.00000000       0.91500922       0.00000000 
    0.00000000       0.00000000       0.00000000       -1.6014053

