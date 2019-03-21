
rndGamma
==============================================

Purpose
----------------

Computes gamma pseudo-random numbers with a choice of underlying random number generator.

Format
----------------
.. function:: rndGamma(r, c, shape, scale, state) 
			  rndGamma(r, c, shape, scale)

    :param r: number of rows of resulting matrix.
    :type r: Scalar

    :param c: number of columns of resulting matrix.
    :type c: Scalar

    :param shape: or r x 1 vector, or 1 x c vector, or scalar, shape argument for gamma distribution.
    :type shape: r x c matrix

    :param scale: or r x 1 vector, or 1 x c vector, or scalar, scale argument for gamma distribution.
    :type scale: r x c matrix

    :param state: 
        
        Scalar case:state = starting seed value only. If -1, GAUSS
        computes the starting seed based on the system clock.
        Opaque vector case:state = the state vector returned from a previous
        call to one of the rnd random number functions.
    :type state: Optional argument - scalar or opaque vector

    :returns: x (*r x c matrix*), gamma distributed random numbers.

    :returns: newstate (*Opaque vector*), the updated state.

Remarks
-------

The properties of the pseudo-random numbers in x are:

::

   E(x) = shape*scale
   Var(x) = shape*scale2
   x > 0
   shape > 0
   scale > 0


Examples
----------------

num_rows = 5;
num_cols = 1;
shape = 3;
scale = 2;

x = rndGamma(num_rows, num_cols, shape, scale);
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The gamma distribution is sometimes described in terms of a shape parameter and an inverse scale parameter, called the rate parameter. The rate parameter is the reciprocal of the scale parameter. With this parameterization, the random numbers will have the following properties:
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    E(x) = shape/rate
    Var(x) = shape/(rate2)

If you prefer to think about the gamma distribution in these terms, then pass in the reciprocal of the rate parameter as the fourth argument to rndGamma.

::

    shape = 3;
    rate = 2;
    
    x = rndGamma(5, 1, shape, 1/rate);

Technical Notes
+++++++++++++++

The default generator for rndGamma is the SFMT Mersenne-Twister 19937.
You can specifiy a different underlying random number generator with the
function rndCreateState.

.. seealso:: Functions :func:`rndCreateState`, :func:`rndStateSkip`

gamma pseudo-random numbers random generator
