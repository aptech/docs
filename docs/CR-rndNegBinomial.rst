
rndNegBinomial
==============================================

Purpose
----------------

Computes negative binomial pseudo-random numbers with a choice of underlying random number generator.

Format
----------------
.. function:: rndNegBinomial(r, c, ns, prob, state) 
			  rndNegBinomial(r, c, ns, prob)

    :param r: number of rows of resulting matrix.
    :type r: Scalar

    :param c: number of columns of resulting matrix.
    :type c: Scalar

    :param ns: or
        rx1 vector, or 1xc vector,
        or scalar, ''event'' argument for negative binomial distribution.
    :type ns: r x c matrix

    :param prob: or
        rx1 vector, or 1xc vector,
        or scalar, ''probability'' argument for negative binomial distribution.
    :type prob: r x c matrix

    :param state: 
        Scalar case:state = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.
        
        Opaque vector case:state = the state vector returned from a previous
        call to one of the state returning random number functions.
    :type state: Optional argument - scalar or opaque vector

    :returns: x (*r x c matrix*), negative
        binomial distributed random numbers.

    :returns: newstate (*Opaque vector*), the updated state.

Remarks
-------

The properties of the pseudo-random numbers in x are:

::

   E(x) = num_s*(1 - prob)/prob
   Var(x) = num_s*(1 - prob)/prob2
   num_s > 0
   0 < prob < 1

rndNegBinomial has a different parameterization than the deprecated
rndnb. To convert a call to rndnb to an equivalent call to
rndNegBinomial, pass in 1 - prob in place of prob. For example, the
following two calls are equivalent.

::

   x_1 = rndnb(1e6, 1, 15, 0.3);
   x_2 = rndNegBinomial(1e6, 1, 15, 0.7);

r and c will be truncated to integers if necessary.


Examples
----------------

Simulate the number of failures before 30 successes where each trial has a 70% probability of success.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    num_obs = 100;
    
    num_s = 30;
    prob = 0.70;
    
    num_f = rndNegBinomial(num_obs, 1, num_s, prob);

An alternative parameterization specifies the negative binomial distribution in terms of a dispersion parameter (dp) and a mean parameter (mu). If you would prefer to think of it in those terms, you may do so by passing in the dispersion parameter dp, in place of num_s and passing  in dp/(dp + mu) in place of prob.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // dispersion parameter
    dp = 12;
    
    // mean parameter
    mu = 3;
    
    x = rndNegBinomial(100, 1, dp, dp./(dp + mu));

Technical Notes
+++++++++++++++

The default generator for rndNegBinomial is the SFMT Mersenne-Twister
19937. You can specifiy a different underlying random number generator
with the function rndCreateState.

.. seealso:: Functions :func:`rndCreateState`, :func:`rndStateSkip`

negative binomial pseudo-random number generator
