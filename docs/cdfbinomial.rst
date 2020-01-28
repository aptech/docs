
cdfBinomial
==============================================

Purpose
----------------

Computes the binomial cumulative distribution function.

Format
----------------
.. function:: p = cdfBinomial(successes, trials, prob)

    :param successes: Must be a positive number and must be less than *trials*
    :type successes: NxK matrix, Nx1 vector or scalar

    :param trials: ExE conformable with *successes*. *trials* must be greater than *successes*.
    :type trials: LxM matrix

    :param prob: ExE conformable with *successes*. The probability of *success* on any given *trial* with *successes*  :math:`0 < prob < 1`.
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
    successes = 270;

    // Number of trials
    trials = 704;

    // Probability of success
    prob = 0.317;

    // Call cdfBinomial
    p = cdfBinomial(successes, trials, prob);
    p = 0.9999199430052614

Therefore the odds of this player breaking Ichiro's record:

::

    1-p = 0.0000000000037863 or 0.0000000003786305%


Remarks
------------

.. math::

   \mathit{\mathrm{\mathtt{P\left( x\, \leq k \right)}} =}\mathit{\sum\limits_{i = 0}^{k}\begin{pmatrix}
   n \\
   i \\
   \end{pmatrix}\, p^{i}\left( 1 - p \right)^{n - i}}

For invalid inputs, :func:`cdfBinomial` will return a scalar error code which,
when its value is assessed by function :func:`scalerr`, corresponds to the
invalid input. If the first input is out of range, :func:`scalerr` will return a
1; if the second is out of range, :func:`scalerr` will return a 2; etc.

.. seealso:: Functions :func:`cdfBinomialInv`, :func:`cdfNegBinomial`, :func:`pdfBinomial`
