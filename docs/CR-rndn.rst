
rndn
==============================================

Purpose
----------------

Computes normally distributed pseudo-random numbers with a choice of underlying random number generator.

Format
----------------
.. function:: rndn(r, c)

    :param r: row dimension.
    :type r: Scalar

    :param c: column dimension.
    :type c: Scalar

    :param state: 
        Scalar case:state = starting seed value. If -1, GAUSS
        computes the starting seed based on the system clock.
        
        Opaque vector case:state = the state vector returned from a previous
        call to one of the rndn random number generators.
    :type state: Optional argument - scalar or opaque vector

    :returns: y (*TODO*), r x c matrix of standard
        normal random numbers.

    :returns: newstate (*Opaque vector*), the updated state.

Examples
----------------

//Create a 100 by 1 vector of standard normal numbers
my_var = rndn(100, 1);
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This example simulates the linear model: y = α + β1*X + ε
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    num_obs = 100;
    alpha = 2.5;
    beta_1 = 0.8;
    
    //Simulate error term
    err = rndn(num_obs, 1);
    
    //Simulate 'x' variable
    x = rndn(num_obs, 1);
    
    //Simulate data generating process
    y = alpha + beta_1*x + err;

This example generates two thousand vectors of standard normal 
random numbers, each with one million elements. The state of the 
random number generator after each iteration is used as an input to
the next generation of random numbers.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    state = 13;
    n = 2000;
    k = 1000000;
    
    //Create vector to hold 'n' submeans
    submean = zeros(n, 1);
     
    for i(1, n, 1);
       //Create a kx1 vector of random normal numbers,
       //using the optional 'state' input
       { y,state } = rndn(k,1,state);
    
       submean[i] = meanc(y);
    endfor;
     
    mean = meanc(submean);
    print mean;

Technical Notes
+++++++++++++++

-  The default generator for rndn is the SFMT Mersenne-Twister 19937.
   You can specify a different underlying random number generator with
   the function rndCreateState.
-  The rndseed keyword will create a new state vector (starting point)
   for rndn. This means you can use rndseed to control rndn. However,
   rndn will not update the rndseed as its internal state changes.
-  For testing and comparison purposes, the function \_rndng10 will
   reproduce the results of the function rndn in GAUSS 10 and earlier.
   In GAUSS 11 an improvement to the normality transformation algorithm
   was added to rndn. This can be reproduced with the function \_rndn.
   Do not use either of the functions for any purpose other than
   comparison with previous versions. The current rndn algorithm is a
   much higher quality random number generator.

.. seealso:: Functions :func:`rndCreateState`, :func:`rndStateSkip`

normal distribution random number matrix
