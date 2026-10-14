
rndGamma
==============================================

Purpose
----------------

Computes gamma pseudo-random numbers with a choice of underlying random number generator.

Format
----------------
.. function:: x = rndGamma(r, c, shape, scale)
              { x, newstate } = rndGamma(r, c, shape, scale, state)

    :param r: number of rows of resulting matrix.
    :type r: scalar

    :param c: number of columns of resulting matrix.
    :type c: scalar

    :param shape: Positive scalar shape parameter for the gamma distribution.
    :type shape: scalar

    :param scale: Positive scalar scale parameter for the gamma distribution.
    :type scale: scalar

    :param state: Optional argument.

        **scalar case**

            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **opaque vector case**

        *state* = the state vector returned from a previous call to one of the ``rnd`` random number functions.

    :type state: scalar or opaque vector

    :return x: gamma distributed random numbers.

    :rtype x: RxC matrix

    :return newstate: the updated state.

    :rtype newstate: Opaque vector

Examples
----------------

Example 1
+++++++++

::

    // Set seed for repeatable output
    rndseed 12345;

    num_rows = 5;
    num_cols = 1;
    shape = 3;
    scale = 2;

    x = rndGamma(num_rows, num_cols, shape, scale);

After the code above, *x* is:

::

       4.0057858
       5.4494189
       2.4490466
       4.3893173
       4.2732468

Example 2
+++++++++

The gamma distribution is sometimes described in terms of a shape parameter and an inverse
*scale* parameter, called the *rate* parameter. The *rate* parameter is the reciprocal of the *scale* parameter.
With this parameterization, the random numbers will have the following properties:

.. math::

    E(x) = \frac{shape}{rate}\\

    Var(x) = \frac{shape}{rate^2}

If you prefer to think about the gamma distribution in these terms, then pass in the
reciprocal of the *rate* parameter as the fourth argument to :func:`rndGamma`.

::

    // Set seed for repeatable output
    rndseed 12345;

    shape = 3;
    rate = 2;

    x = rndGamma(5, 1, shape, 1/rate);

After the code above, *x* is:

::

       1.0014464
       1.3623547
      0.61226164
       1.0973293
       1.0683117

The expected value is shape/rate = 3/2 = 1.5, and the sample values are centered around that.

Keyword arguments (GAUSS 27)
----------------------------

Use ``shape=`` and ``scale=`` to make the gamma parameterization explicit.
The population mean is ``shape*scale`` and the variance is ``shape*scale^2``.
For example, shape 3 and scale 2 give a population mean of 6.

The parameter names are ``r``, ``c``, ``shape``, ``scale`` and ``state``.
The first four are required. ``state`` is optional; omitting it uses the global
random stream. Named arguments can be reordered and must follow any positional
arguments. Existing positional calls keep their behavior.

.. code-block:: gauss

    // Shape-scale parameterization: population mean = 3*2 = 6.
    rndseed 12345;
    gamma_draws = rndGamma(1000, 1, shape=3, scale=2);

    // For rate=2, pass its reciprocal as scale: population mean = 3/2.
    rate_val = 2;
    gamma_rate_draws = rndGamma(1000, 1, shape=3, scale=1/rate_val);

    // A supplied seed/state returns both the draws and the updated state.
    { gamma_first, gamma_state } = rndGamma(5, 1, shape=3, scale=2, state=12345);
    { gamma_next, gamma_state } = rndGamma(5, 1, shape=3, scale=2, state=gamma_state);

``rate`` is not a keyword. Use ``scale=1/rate_val`` when your model specifies
a rate. Shape and scale must be positive scalars.
With ``state``, request both outputs and retain the returned state for later draws.


Remarks
-------

The properties of the pseudo-random numbers in *x* are:

.. math::

   E(x) = shape*scale\\

   Var(x) = shape*scale^2\\

   x > 0\\

   shape > 0\\

   scale > 0


Technical Notes
---------------

The default generator for :func:`rndGamma` is the SFMT Mersenne-Twister 19937.
You can specify a different underlying random number generator with the
function :func:`rndCreateState`.

.. seealso:: Functions :func:`rndCreateState`, :func:`rndStateSkip`
