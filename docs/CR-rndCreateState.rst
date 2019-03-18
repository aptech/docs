
rndCreateState
==============================================

Purpose
----------------

			Creates a new random number stream for a specified 

			generator type from a seed value.
		

Format
----------------
.. function:: rndCreateState(brng, seed)

    :param brng: generator name. Options
        
        include:
    :type brng: String

    .. csv-table::
        :widths: auto

        ""mrg32k3a"", "L'Ecuyer's MRG32K3A"
        ""mt19937"", "Mersenne-Twister 19937"
        ""sfmt19937"", "optimized Mersenne-Twister 19937"
        ""mt2203-01"", "Mersenne-Twister 2203"
        ""niederreiter"", "Niederreiter quasi-random numbers"
        ""sobol"", "Sobol quasi-random numbers"
        ""wh-01"", "Wichmann-Hill"

    :param seed: starting seed value. if -1, 					GAUSS computes the starting seed based on the system clock.
        NOTE: For the quasi-random number generators, "sobol"
        and "niederreiter", this second input is the dimension rather than a starting seed. For "sobol", 1 ≤ dimension ≤ 40. For niederreiter, 1 ≤ dimension ≤ 318. See examples below.
    :type seed: Scalar

    :returns: state (*Opaque vector*), the newly created state.

Examples
----------------

Basic usage
+++++++++++

::

    //Starting seed value
    	seed = 123456;
    
    	//Create state for generator 'mrg32k3a'
    	state = rndCreateState("mrg32k3a", seed);
    
    	//Create a 5x1 vector of random normal numbers with
    	//the state created above
    	{ r, newstate } = rndn(5, 1, state);

After the code above, r will equal:

::

    0.51489262
    	0.14053340
    	r = 1.2128406
    	0.17112172
    	-0.18788202

creating a state from a numbered stream
+++++++++++++++++++++++++++++++++++++++

Most random number generators have one single stream in which you can think of the starting 

				state as a bookmark. The "mt2203" and "wh" 

				(or Wichmann-HIll) each have multiple separate streams. The example below shows how to uses these 

			random number streams.

::

    seed = 123456;
    
    	//Create a state from the 1028th substream of the
    	//Mersenne-Twister 2203 RNG
    	state_mt = rndCreateState("mt2203-1028", seed);
    
    	//Create a state from the 112th substream of the
    	//Wichmann-Hill RNG
    	state_wh = rndCreateState("wh-112", seed);
    
    	//Generate numbers using the states
    	{ r1, state_mt } = rndu(4, 1, state_mt);
    	{ r2, state_wh } = rndu(4, 1, state_wh);

After the code above, r1 and r2 should 

			equal:

::

    r1 =  0.14291687    r2 =  0.0073824407 
    	0.99670199           0.93756896 
    	0.59512065           0.071140446 
    	1.5776604e-06        0.021328991

initializing the Sobol quasi-random number generator
++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    //Initialize random seed with a dimension of 2
    	state = rndCreateState("sobol", 2);
    
    	//Create some random numbers using this state
    	{ r, state } = rndu(10, 2, state);

After the code above, r, should be equal to:

::

    r = 0.5000    0.5000 
    	0.7500    0.2500 
    	0.2500    0.7500 
    	0.3750    0.3750 
    	0.8750    0.8750 
    	0.6250    0.1250 
    	0.1250    0.6250 
    	0.1875    0.3125 
    	0.6875    0.8125 
    	0.9375    0.0625

Remarks
+++++++

The states returned from this function may NOT be used with rndMTu or
any of the rndKM or rndLC functions.

.. seealso:: Functions :func:`rndStateSkip`, :func:`rndn`, :func:`rndu`, :func:`rndBeta`

random number stream specified generator type seed value
