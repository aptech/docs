
rndHyperGeo
==============================================

Purpose
----------------

Computes the random numbers for the hypergeometric distribution

Format
----------------
.. function:: x = rndHyperGeo(r, c, pop_size, n_marked, n_drawn)
              { x, newstate } = rndHyperGeo(r, c, pop_size, n_marked, n_drawn, state)

    :param r: row dimension of the return matrix *x*
    :type r: scalar

    :param c: column dimension of the return matrix *x*
    :type c: scalar

    :param pop_size: The size of the population from which draws will be made. ExE conformable with 
        the row and column dimensions of the return matrix, *r* and *c*

    :type pop_size: matrix

    :param n_marked: The number of items in the population which possess a specified trait. ExE conformable with 
        row and column dimensions of the return matrix, *r*, and *c*
    :type n_marked: matrix

    :param n_drawn: The number of items drawn from the population. ExE conformable with the dimensions of the return matrix, *r* and *c*
    :type n_drawn: matrix

    :param state: Optional argument.

        **scalar case**
        
            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **opaque vector case**
        
        *state* = the state vector returned from a previous call to one of the ``rnd`` random number functions.

    :type state: scalar or opaque vector

    :return x: The probability of drawing *x* items which possess a specified trait.

    :rtype x: NxK matrix, Nx1 vector or scalar

    :return new_state: the updated state

    :rtype new_state: Opaque vector

Examples
----------------

Basic Example
+++++++++++++

::

    // Set seed for repeatable output
    rndseed 12345;

    // Population size
    pop_size = 100;

    // Number of marked items
    n_marked = 25;

    // Number of items drawn
    n_drawn = 40;

    // Compute 1 random number
    x = rndHyperGeo(1, 1, pop_size, n_marked, n_drawn);
    print x;

::

       13.000000

The expected value is n_drawn*n_marked/pop_size = 40*25/100 = 10. A single draw of 13 is a reasonable outcome.

Random matrix in which each column has different parameters.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Population size
    pop_size = 100;
    
    // Number of marked items
    n_marked = 25;
    
    // 1x2 row vector, number of items drawn
    n_drawn = { 40 50 };
    
    // Compute a 10 x 2 matrix of random number
    x = rndHyperGeo(10, 2, pop_size, n_marked, n_drawn);

Both columns of the variable *x* created in the code above use the same values for *pop_size* and *n_marked*. 
However, the first column of *x* will be calculated using the first element of *n_drawn*, 40. The second 
column of *x* will be calculated using the second element of *n_drawn*, 50.

Passing in a state vector
+++++++++++++++++++++++++

::

    // Starting seed value
    seed = 23424;
    
    // Population size
    pop_size = 100;
    
    // Number of marked items
    n_marked = 25;
    
    // Number of items drawn
    n_drawn = 40;
    
    // Compute 1000x1 vector of random numbers
    { x, state } = rndHyperGeo(1000, 1, pop_size, n_marked, n_drawn, seed);

.. seealso:: Functions :func:`cdfHyperGeo`, :func:`pdfHyperGeo`

