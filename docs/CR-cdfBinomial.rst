
cdfBinomial
==============================================

Purpose
----------------

Computes the binomial cumulative distribution function.

Format
----------------
.. function:: cdfBinomial(successes, trials, prob)

    :param successes: must be a positive number and < *trials*
    :type successes: NxK matrix, Nx1 vector or scalar

    :param trials: must be > *successes*.
    :type trials: ExE conformable

    :param prob:  The probability of *success* on any given *trial* with *successes* :math:`0 < prob < 1`.
    :type prob: ExE conformable 

    :returns: p (*NxK matrix, Nx1 vector or scalar*)

Remarks
------------

.. math::

   \mathit{\mathrm{\mathtt{P\left( x\, \leq k \right)}} =}\mathit{\sum\limits_{i = 0}^{k}\begin{pmatrix}
   n \\
   i \\
   \end{pmatrix}\, p^{i}\left( 1 - p \right)^{n - i}}

.. DANGER::
   Inspect equation

For invalid inputs, :func:`cdfBinomial` will return a scalar error code which,
when its value is assessed by function :func:`scalerr`, corresponds to the
invalid input. If the first input is out of range, :func:`scalerr` will return a
1; if the second is out of range, :func:`scalerr` will return a 2; etc.

Examples
----------------
What are the chances that a baseball player with a long-term batting average of .317 could break Ichiro Suzuki's record of 270 hits in a season if he had as many at bats as Ichiro had that year, 704?

::

    // The cumulative probability of our player 
    // getting 270 or fewer hits in the season  
    p = cdfBinomial(270,704,.317); 
    p = 0.9999199430052614

Therefore the odds of this player breaking Ichiro's record:

::

    1-p = 0.0000000000037863 or 0.0000000003786305%


.. seealso:: Functions :func:`cdfBinomialInv`, :func:`cdfNegBinomial`, :func:`pdfBinomial`

