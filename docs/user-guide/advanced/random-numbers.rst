.. _random-numbers:

Random Number Generation
===============================================

GAUSS provides a powerful suite of random number generation (RNG)
functionality for simulation, Monte Carlo studies, and statistical
sampling. Key features include:

- Multiple modern pseudo-random generators (Mersenne Twister,
  MRG32k3a, and more)
- Quasi-random sequences (Sobol, Niederreiter) for numerical
  integration
- Over 20 distribution-specific sampling functions
- Thread-safe state-based generation for parallel computing
- Reproducible sequences via seeding

Before diving in, here are a few terms used throughout this page:

- **Seed** — an integer that initializes a generator. The same seed
  always produces the same sequence of random numbers.
- **State** — a data vector that captures a generator's type and
  current position in its sequence. Passing a state to a function
  continues the sequence where the previous call left off.
- **Stream** — an independent sequence within a multi-stream generator
  (e.g., MT2203 has 6024 streams).
- **Period** — the length of the full cycle before a generator repeats.

.. note::

    If you are coming from R, ``rndn`` is equivalent to ``rnorm`` and
    ``rndu`` is equivalent to ``runif``. The ``rndseed`` statement is
    analogous to ``set.seed()``. If you are coming from Python/NumPy,
    ``rndn`` corresponds to ``numpy.random.randn`` and ``rndu`` to
    ``numpy.random.rand``.


Basic Random Number Functions
--------------------------------------------

GAUSS provides two fundamental functions for generating random
numbers:

::

    // 3x2 matrix of standard normal random numbers
    x = rndn(3, 2);

    // 3x2 matrix of uniform random numbers on [0, 1)
    u = rndu(3, 2);

For random integers in a range, use :func:`rndi`:

::

    // 3x1 vector of random integers between 1 and 100
    ri = rndi(3, 1, 1|100);

These functions use a shared global state. For reproducible results,
set the seed before generating:

::

    rndseed 42;
    x = rndn(3, 2);

Running the above code will always produce the same output::

       0.55850061        2.0347955
       0.24048153      -0.97476365
      -0.85727785      -0.98405229

.. note::

    ``rndseed`` is a **language statement**, not a function — write
    ``rndseed 42;``, not ``rndseed(42);``. It sets the global seed
    for ``rndn``, ``rndu``, ``rndi``, and all distribution-specific
    functions that do not take an explicit state. Setting the seed
    again resets the sequence to the same starting point.


Sampling from Distributions
--------------------------------------------

GAUSS includes functions for sampling from many common distributions:

.. list-table::
    :widths: 30 70
    :header-rows: 1

    * - Function
      - Distribution

    * - :func:`rndn`
      - Standard normal (mean 0, variance 1)

    * - :func:`rndu`
      - Uniform on [0, 1)

    * - :func:`rndi`
      - Random integers in a range

    * - :func:`rndBernoulli`
      - Bernoulli (binary outcomes)

    * - :func:`rndBeta`
      - Beta

    * - :func:`rndBinomial`
      - Binomial

    * - :func:`rndCauchy`
      - Cauchy

    * - :func:`rndChiSquare`
      - Chi-square

    * - :func:`rndExp`
      - Exponential

    * - :func:`rndGamma`
      - Gamma

    * - :func:`rndGeo`
      - Geometric

    * - :func:`rndGumbel`
      - Gumbel (extreme value type I)

    * - :func:`rndHyperGeo`
      - Hypergeometric

    * - :func:`rndLaplace`
      - Laplace (double exponential)

    * - :func:`rndLogNorm`
      - Log-normal

    * - :func:`rndMVn`
      - Multivariate normal

    * - :func:`rndMVt`
      - Multivariate Student's t

    * - :func:`rndNegBinomial`
      - Negative binomial

    * - :func:`rndPoisson`
      - Poisson

    * - :func:`rndRayleigh`
      - Rayleigh

    * - :func:`rndWeibull`
      - Weibull

    * - :func:`rndWishart`
      - Wishart

    * - :func:`rndWishartInv`
      - Inverse Wishart

Example: Distribution sampling
++++++++++++++++++++++++++++++++++++

::

    rndseed 42;

    // 1000 Gamma(shape=2, scale=1) draws
    g = rndGamma(1000, 1, 2, 1);

    // 1000 Poisson(lambda=5) draws
    p = rndPoisson(1000, 1, 5);

    // Multivariate normal with correlation
    // { 0, 0 } is a 2x1 column vector; { 1 0.5, 0.5 1 } is a 2x2 matrix
    // (commas separate rows, spaces separate columns)
    mu = { 0, 0 };
    sigma = { 1 0.5, 0.5 1 };
    mv = rndMVn(500, mu, sigma);


Available Generators
--------------------------------------------

GAUSS includes several pseudo-random and quasi-random number
generators. You select a generator by creating a **state** with
:func:`rndCreateState`:

.. list-table::
    :widths: 18 10 12 12 48
    :header-rows: 1

    * - Generator
      - Streams
      - Period
      - BigCrush
      - Notes

    * - SFMT19937
      - 1
      - 2\ :sup:`19937`
      - —
      - Default for ``rndn``/``rndu``. Fastest available

    * - MRG32k3a
      - 1
      - 2\ :sup:`191`
      - 0 failures
      - Supports block-skipping via :func:`rndStateSkip`

    * - MT19937
      - 1
      - 2\ :sup:`19937`
      - 2 failures
      - Classic Mersenne Twister

    * - MT2203
      - 6024
      - 2\ :sup:`2203`
      - 4 failures
      - Multiple independent streams for parallel work

    * - Wichmann-Hill
      - 273
      - 2\ :sup:`42.7`
      - 22 failures
      - Multiple independent streams. Supports block-skipping

    * - Sobol
      - —
      - —
      - —
      - Quasi-random (low discrepancy). Dimensions 1–40.
        The seed argument to :func:`rndCreateState` sets
        the dimension, not a random seed

    * - Niederreiter
      - —
      - —
      - —
      - Quasi-random (low discrepancy). Dimensions 1–318.
        The seed argument sets the dimension

The **BigCrush** column shows the number of failures on the TestU01
BigCrush test suite (160 tests). All generators pass DIEHARD.
SFMT19937 was not tested because its output is not compatible with
the scalar-at-a-time interface required by TestU01.

Choosing a generator
++++++++++++++++++++++++++++++++++++

For most work, the default generator (SFMT19937 for ``rndn``/``rndu``)
is an excellent choice. Consider switching when:

- **You need parallel streams** — use MT2203 (6024 streams) or
  Wichmann-Hill (273 streams)
- **You need block-skipping** — use MRG32k3a or Wichmann-Hill
  (the generators that support :func:`rndStateSkip`)
- **You need top statistical quality** — use MRG32k3a (zero BigCrush
  failures)
- **You need quasi-random sequences** — use Sobol or Niederreiter for
  numerical integration (these are deterministic, not pseudo-random)

.. tip::

    For simulation studies that do not require parallel generation,
    the simplest approach is ``rndseed`` plus ``rndn``/``rndu``. You
    only need explicit state management when working with threads or
    when you need multiple independent sequences.


State-Based Generation
--------------------------------------------

For full control over the random number sequence, GAUSS supports
**state-based** generation. A state encapsulates the generator type,
stream index, and current position in the sequence.

Creating a state
++++++++++++++++++++++++++++++++++++

Use :func:`rndCreateState` to create a state for any generator:

::

    // MRG32k3a with seed 192938
    state = rndCreateState("mrg32k3a", 192938);

    // Generate 3 standard normal values using this state.
    // The { x, state } syntax is a multi-return assignment:
    //   x     gets the random numbers
    //   state gets the updated generator state
    { x, state } = rndn(3, 1, state);
    print x;

This prints::

       0.20471263
       0.14053340
       -1.4368991

Always pass the **updated** state to the next call to continue the
sequence where it left off — do not reuse the original seed or state.

Selecting a stream
++++++++++++++++++++++++++++++++++++

For generators with multiple streams (MT2203, Wichmann-Hill), append a
hyphen and stream number to the generator name:

::

    seed = 192938;

    // Wichmann-Hill stream 3
    whState3 = rndCreateState("wh-3", seed);

    // MT2203 stream 21
    mtState21 = rndCreateState("mt2203-21", seed);

Each stream is an independent pseudo-random sequence with the same
statistical properties. Two different streams seeded identically will
produce completely different sequences.

.. note::

    The KISS-Monster generator and its dedicated functions
    (``rndKMn``, ``rndKMu``, ``rndKMi``) are **deprecated**. Use
    :func:`rndCreateState` with any supported generator instead.


Thread Safety
--------------------------------------------

When using threads (``threadBegin`` / ``threadEnd``), the global-state
functions (``rndn``, ``rndu``, ``rndGamma``, etc.) share a single state
and must **not** be called concurrently:

::

    // WRONG — concurrent writes to global state
    threadBegin;
       x = rndn(500, 1);
    threadEnd;
    threadBegin;
       x2 = rndn(500, 1);
    threadEnd;
    threadJoin;

There are two safe alternatives:

**Option 1: Generate before threads**

::

    x = rndn(500, 1);
    x2 = rndn(500, 1);
    threadBegin;
       y = myFunction(x);
    threadEnd;
    threadBegin;
       y2 = myFunction(x2);
    threadEnd;
    threadJoin;

**Option 2: Use explicit states**

Each thread gets its own state, so there is no shared global state to
corrupt. This example uses MRG32k3a, but any generator works:

::

    state1 = rndCreateState("mrg32k3a", 723193);
    state2 = rndCreateState("mrg32k3a", 94493);
    threadBegin;
       { x1, state1 } = rndn(500, 1, state1);
       y1 = myFunction(x1);
    threadEnd;
    threadBegin;
       { x2, state2 } = rndn(500, 1, state2);
       y2 = myFunction(x2);
    threadEnd;
    threadJoin;


Parallel Generation with Block-Skipping
--------------------------------------------

When you need a single contiguous pseudo-random sequence split across
multiple threads, use **block-skipping**. The :func:`rndStateSkip`
function advances a state by a specified number of values without
generating them:

::

    // Create initial state
    seed = 2342343;
    state1 = rndCreateState("mrg32k3a", seed);

    // Create 3 additional states, each starting 1e8 values forward
    state2 = rndStateSkip(1e8, state1);
    state3 = rndStateSkip(1e8, state2);
    state4 = rndStateSkip(1e8, state3);

    // Process each block in a separate thread
    threadBegin;
       { x1, state1 } = rndGamma(1e8, 1, 2, 2, state1);
       y1 = myfunc(x1);
    threadEnd;
    threadBegin;
       { x2, state2 } = rndGamma(1e8, 1, 2, 2, state2);
       y2 = myfunc(x2);
    threadEnd;
    threadBegin;
       { x3, state3 } = rndGamma(1e8, 1, 2, 2, state3);
       y3 = myfunc(x3);
    threadEnd;
    threadBegin;
       { x4, state4 } = rndGamma(1e8, 1, 2, 2, state4);
       y4 = myfunc(x4);
    threadEnd;
    threadJoin;

The four threads together produce the same sequence as a single call
generating 4 x 10\ :sup:`8` values — just processed in parallel.

.. note::

    Block-skipping via :func:`rndStateSkip` is available with the
    **MRG32k3a** and **Wichmann-Hill** generators. For other
    generators, use multiple independent streams (MT2203) or
    separate seeds instead.


Performance Tips
--------------------------------------------

- **Generate in bulk.** Creating one million numbers in a single call
  is much faster than 100,000 calls of 10 numbers each. Avoid
  generating random numbers one at a time inside loops.

- **Use SFMT19937 for speed.** The optimized Mersenne Twister is the
  fastest generator available. The default generator for
  ``rndn``/``rndu`` is already very fast.

- **Use multiple threads.** For large-scale simulations, distribute
  work across threads using state-based generation (see above).

- **Watch memory.** Generating a very large matrix in one call can
  exhaust available RAM. Balance batch size against available memory.


Quick Reference
--------------------------------------------

.. list-table::
    :widths: 45 55
    :header-rows: 1

    * - Task
      - How

    * - Set seed for reproducibility
      - ``rndseed 42;``

    * - Standard normal matrix
      - ``x = rndn(n, k);``

    * - Uniform matrix
      - ``u = rndu(n, k);``

    * - Random integers in [a, b]
      - ``ri = rndi(n, k, a|b);``

    * - Gamma draws
      - ``g = rndGamma(n, 1, shape, scale);``

    * - Multivariate normal
      - ``mv = rndMVn(n, mu, sigma);``

    * - Create generator state
      - ``state = rndCreateState("mrg32k3a", seed);``

    * - Generate with state
      - ``{ x, state } = rndn(n, k, state);``

    * - Select a stream
      - ``state = rndCreateState("mt2203-9", seed);``

    * - Skip ahead in sequence
      - ``state2 = rndStateSkip(1e6, state1);``


.. seealso:: :doc:`/user-guide/advanced/structures`
