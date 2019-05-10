
rndHyperGeo
==============================================

Purpose
----------------

Computes the random numbers for the hypergeometric distribution

Format
----------------
.. function:: rndHyperGeo(r, c, m, k, n[, state])

    :param r: row dimension of the return matrix *x*
    :type r: scalar

    :param c: column dimension of the return matrix *x*
    :type c: scalar

    :param m: The size of the population from which draws will be made. ExE conformable with 
        the row and column dimensions of the return matrix, *r* and *c*

    :type m: matrix

    :param k: The number of items in the population which possess a specified trait. ExE conformable with 
        row and column dimensions of the return matrix, *r*, and *c*
    :type k: matrix

    :param n: The number of items drawn from the population. ExE conformable with the dimensions of the return matrix, *r* and *c*
    :type n: matrix

    :param state: Optional argument.

        **scalar case**
        
            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **opaque vector case**
        
            *state* = the state vector returned from a previous call to one of the rnd random number functions.

    :type state: scalar or opaque vector

    :returns: x (*NxK matrix, Nx1 vector or scalar*), The probability of drawing *x* items which possess a specified trait. 

    :returns: new_state (*Opaque vector*), the updated state

Examples
----------------

Basic Example
+++++++++++++

::

    // Population size
    m = 100;
    
    // Number of marked items
    k = 25;
    
    // Number of items drawn
    n = 40;
    
    // Compute 1 random number
    x = rndHyperGeo(1, 1, m, k, n);

Random matrix in which each column has different parameters.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Population size
    m = 100;
    
    // Number of marked items
    k = 25;
    
    // 1x2 row vector, number of items drawn
    n = { 40 50 };
    
    // Compute a 10 x 2 matrix of random number
    x = rndHyperGeo(10, 2, m, k, n);

Both columns of the variable *x* created in the code above use the same values for *m* and *k*. 
However, the first column of *x* will be calculated using the first element of *n*, 40. The second 
column of *x* will be calculated using the second element of *n*, 50.

Passing in a state vector
+++++++++++++++++++++++++

::

    // Starting seed value
    seed = 23424;
    
    // Population size
    m = 100;
    
    // Number of marked items
    k = 25;
    
    // Number of items drawn
    n = 40;
    
    // Compute 1000x1 vector of random numbers
    { x, state } = rndHyperGeo(1000, 1, m, k, n, seed);

.. seealso:: Functions :func:`cdfHyperGeo`, :func:`pdfHyperGeo`

