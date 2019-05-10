
rndRayleigh
==============================================

Purpose
----------------

Computes rayleigh pseudo-random numbers with the choice of underlying random number generator.

Format
----------------
.. function:: rndRayleigh(r, c, sigma[, state])

    :param r: number of rows of resulting matrix.
    :type r: scalar

    :param c: number of columns of resulting matrix.
    :type c: scalar

    :param sigma: scale parameter, or matrix ExE conformable with '*r*' and '*c*'.
    :type sigma: scalar

    :param state: Optional argument.

        **scalar case**
        
            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **opaque vector case**
        
            *state* = the state vector returned from a previous call to one of the rnd random number functions.

    :type state: scalar or opaque vector

    :returns: x (*RxC matrix*), rayleigh distributed random numbers.

    :returns: newstate (*Opaque vector*), the updated state.

Examples
----------------

Basic example
+++++++++++++

::

    // Set rndseed for repeatable random numbers
    rndseed 4323;
    
    // Create a 3x1 column vector of Rayleigh distributed
    // random deviates with sigma equal to 2
    x = rndRayleigh(3, 1, 2);

After the above code, '*x*' should be equal to:

::

    0.28950290
    1.9994478
    5.089132

Columns with different sigma values
+++++++++++++++++++++++++++++++++++

::

    // Set rndseed for repeatable random numbers
    rndseed 4323;
    
    // Create a 3x2 column vector of Rayleigh distributed
    // random deviates with sigma equal to 1 for the
    // first column and equal to 3 for the second column
    sigma = { 1 3 };
    x = rndRayleigh(3, 2, sigma);

After the above code, '*x*' should be equal to:

::

    0.1447515        2.9991717
    2.5445664        2.4191846   
    1.1406313        5.0636878

Using a state vector
++++++++++++++++++++

::

    // Create a 3x1 column vector of Rayleigh distributed
    // random deviates with sigma equal to 2
    seed = 4323;
    { x1, state } = rndRayleigh(3, 1, 2, seed);
    
    // Create 3 additional random deviates, using
    // the state vector returned by the previous call
    { x2, state } = rndRayleigh(3, 1, 2, state);

After the above code, '*x1*' and '*x2*' should be equal to:

::

          0.28950290         1.6127897
    x1 =  1.9994478    x2 =  2.2812626
          5.0891327          3.3757919

Remarks
-------

The properties of the pseudo-random numbers in x are:

.. math::

    E(X) = \\sigma\sqrt{\pi/2}\\\
    
    Var(X) = \\sigma^2{(4 - \\pi)}/2`

*r* and *c* will be truncated to integers if necessary.

Technical Notes
---------------

The default generator for :func:`rndRayleigh` is the SFMT Mersenne-Twister
19937. You can specifiy a different underlying random number generator
with the function :func:`rndCreateState`.

.. seealso:: Functions :func:`rndCreateState`, :func:`rndStateSkip`, :func:`cdfRayleigh`, :func:`pdfRayleigh`

