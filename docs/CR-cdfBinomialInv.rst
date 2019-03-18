
cdfBinomialInv
==============================================

Purpose
----------------
Computes the binomial quantile or inverse cumulative distribution function.

Format
----------------
.. function:: cdfBinomialInv(p,trials,prob)

    :param p: Nx1 vector or scalar. 0 < p < 1.
    :type p: NxK matrix

    :param trials: ExE conformable with  p. trials > 0.
    :type trials: TODO

    :param prob: The probability of success on any given trial. ExE conformable with  p. 0 < prob < 1.
    :type prob: TODO

    :returns: s (*TODO*), The number of successes. NxK matrix, Nx1 vector or scalar.

Examples
----------------
What is a reasonable range of wins for a basketball team playing 82 games in a season, with a 60% chance of winning any game?
For our example we will define a reasonable range as falling between the top and bottom deciles.

::

    range = { .10, .9 };
    s = cdfBinomialInv(range, 82,.6);
    print 	"s = "	s;

After above code,

::

    s = 
    	43
    	55

This means that a team with a 60% chance of winning any one game would win between 43 and 55 games in 80% of seasons.

Remarks
+++++++

For invalid inputs, cdfBinomialInv will return a scalar error code
which, when its value is assessed by function scalerr, corresponds to
the invalid input. If the first input is out of range, scalerr will
return a 1; if the second is out of range, scalerr will return a 2; etc.

.. seealso:: Functions :func:`cdfBinomial`, :func:`pdfBinomial`, :func:`cdfNegBinomial`, :func:`cdfNegBinomialInv`

cdf binomial quantile inverse cumulative distribution function
