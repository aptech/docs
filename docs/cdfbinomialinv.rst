
cdfBinomialInv
==============================================

Purpose
----------------
Computes the binomial quantile or inverse cumulative distribution function.

Format
----------------
.. function:: s = cdfBinomialInv(p, trials, prob)

    :param p: Probabilities at which to compute the inverse of the Binomial cumulative distribution function. :math:`0 \leq p \leq 1`.
    :type p: NxK matrix, Nx1 vector or scalar

    :param trials: ExE conformable with *p*. :math:`trials > 0`.
    :type trials: LxM matrix

    :param prob: The probability of *success* on any given trial. ExE conformable with *p*. :math:`0 \leq prob \leq 1`.
    :type prob: PxQ matrix

    :return s: The number of successes.

    :rtype s: NxK matrix, Nx1 vector or scalar

Examples
----------------
What is a reasonable range of wins for a basketball team playing 82 games in a season, with a 60% chance of winning any game?
For our example we will define a reasonable range as falling between the top and bottom deciles.

::

    // Probability range
    range = { .10, .9 };

    // Number of trials
    trials = 82;

    // Probabiliy of success
    prob = 0.6;

    // Call cdfBinomialInv
    s = cdfBinomialInv(range, trials, prob);
    print 	"s = "	s;

After above code,

::

    s =
    	43
    	55

This means that a team with a 60% chance of winning any one game would win between 43 and 55 games in 80% of seasons.

Remarks
-----------

*s* is the smallest number of successes whose cumulative probability is at
least *p*.

If *p* is outside [0, 1], *trials* is not greater than 0, or *prob* is outside
[0, 1], :func:`cdfBinomialInv` returns a scalar error code and :func:`scalerr`
returns the position of that argument: 1 for *p*, 2 for *trials*, 3 for *prob*.
A missing value in any argument returns a missing value.


.. seealso:: Functions :func:`cdfBinomial`, :func:`pdfBinomial`, :func:`cdfNegBinomial`, :func:`cdfNegBinomialInv`
