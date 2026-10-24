
cdfBinomial
==============================================

Purpose
----------------

Computes the binomial cumulative distribution function.

Format
----------------
.. function:: p = cdfBinomial(x, trials, prob)

    :param x: The number of successes. An *x* within 1e-9 (relative) of a whole number is treated as that whole number. Any other fractional *x* is rounded down. An *x* below 0 returns 0 and an *x* above *trials* returns 1.
    :type x: NxK matrix, Nx1 vector or scalar

    :param trials: ExE conformable with *x*. The number of trials, :math:`trials > 0`.
    :type trials: LxM matrix

    :param prob: ExE conformable with *x*. The probability of *success* on any given *trial*. :math:`0 \leq prob \leq 1`.
    :type prob: PxQ matrix

    :return p: Each element in *p* is the binomial cdf value evaluated at the corresponding element in *x*.

    :rtype p: NxK matrix, Nx1 vector or scalar

Examples
----------------
What are the chances that a baseball player with a long-term batting average of .317 could break Ichiro Suzuki's record of 270 hits in a season if he had as many at bats as Ichiro had that year, 704?

::

    /*
    ** We will find the cumulative probability
    ** of our player getting 270 or
    ** fewer hits in the season
    */

    // Number of successes
    x = 270;

    // Number of trials
    trials = 704;

    // Probability of success
    prob = 0.317;

    // Call cdfBinomial
    p = cdfBinomial(x, trials, prob);

After the code above:

::

    p = 0.9999199430052614

Therefore the odds of this player breaking Ichiro's record:

::

    1-p = 0.0000800569947386 or 0.00800569947386%


Remarks
------------

.. math::

   \mathit{\mathrm{\mathtt{P\left( x\, \leq k \right)}} =}\mathit{\sum\limits_{i = 0}^{k}\begin{pmatrix}
   n \\
   i \\
   \end{pmatrix}\, p^{i}\left( 1 - p \right)^{n - i}}

where *k* is *x*, *n* is *trials* and *p* is *prob*.

If *trials* is not greater than 0 or *prob* is outside [0, 1],
:func:`cdfBinomial` returns a scalar error code and :func:`scalerr` returns the
position of that argument: 2 for *trials*, 3 for *prob*. An *x* below 0 or above
*trials* is not an error: it returns 0 or 1. A missing value in any argument
returns a missing value.

.. seealso:: Functions :func:`cdfBinomialInv`, :func:`cdfNegBinomial`, :func:`pdfBinomial`
