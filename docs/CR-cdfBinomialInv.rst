
cdfBinomialInv
==============================================

Purpose
----------------
Computes the binomial quantile or inverse cumulative distribution function.

Format
----------------
.. function:: s = cdfBinomialInv(p, trials, prob)

    :param p: Probabilities at which to compute the inverse of the Binomial cumulative distribution function. :math:`0 \lt p \lt 1`.
    :type p: NxK matrix, Nx1 vector or scalar

    :param trials: ExE conformable with *p*. :math:`trials > 0`.
    :type trials: LxM matrix

    :param prob: The probability of *success* on any given trial. ExE conformable with *p*. :math:`0 < prob < 1`.
    :type prob: PxQ matrix

    :return s: The number of successes.

    :rtype s: NxK matrix, Nx1 vector or scalar

Remarks
-----------

For invalid inputs, :func:`cdfBinomialInv` will return a scalar error code
which, when its value is assessed by function :func:`scalerr`, corresponds to
the invalid input. If the first input is out of range, :func:`scalerr` will
return a 1; if the second is out of range, :func:`scalerr` will return a 2; etc.


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
    prob = 0.6

    // Call cdfBinomialInv
    s = cdfBinomialInv(range, trials, prob);
    print 	"s = "	s;

After above code,

::

    s =
    	43
    	55

This means that a team with a 60% chance of winning any one game would win between 43 and 55 games in 80% of seasons.

.. seealso:: Functions :func:`cdfBinomial`, :func:`pdfBinomial`, :func:`cdfNegBinomial`, :func:`cdfNegBinomialInv`
