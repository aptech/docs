
cdfNegBinomial
==============================================

Purpose
----------------
Computes the cumulative distribution function for the negative binomial distribution.

Format
----------------
.. function:: cdfNegBinomial(f, s, prob)

    :param f: :math:`0 < f`.
    :type f: NxK matrix or Nx1 vector or scalar

    :param s: ExE conformable with *f*. :math:`0 < s`.
    :type s: matrix

    :param prob: The probability of success on any given trial. ExE conformable with *f*. :math:`0 < prob < 1`.
    :type prob: matrix

    :returns: p (*NxK matrix or Nx1 vector or scalar*). The probability of observing *f* failures before observing *s*.

Remarks
-------

For invalid inputs, :func:`cdfNegBinomial` will return a scalar error code
which, when its value is assessed by function :func:`scalerr`, corresponds to
the invalid input. If the first input is out of range, scalerr will
return a 1; if the second is out of range, :func:`scalerr` will return a 2; etc.

Example
-------

Pat is required to sell candy bars to raise money for the 6th grade
field trip. There are thirty houses in the neighborhood, and Pat is not
supposed to return home until five candy bars have been sold. So the
child goes door to door, selling candy bars. At each house, there is a
0.4 probability of selling one candy bar and a 0.6 probability of
selling nothing.

What's the probability that Pat finishes on or before reaching the
eighth house?

::

   // f is number of failure times, f = 0, 1, 2, 3  
   f = seqa(0,1,4);
                   
   // p is the probability of selling the last candy bar                                  
   // the probability of selling each candy bar is 0.4, success number = 5  
   p = cdfNegBinomial(f, 5, 0.4); 

   // since the success number is 5, so the total number is f + 5 
   f = f + 5;
                   
   print  "After nth try, the probability =";         
   print f~p;         

After running above code, the probability that Pat finishes on or before
reaching the eighth house is 0.1736704 or 17.36704%.

::

   After nth try, the probability =

   5.0000000      0.010240000 
   6.0000000      0.040960000 
   7.0000000      0.096256000 
   8.0000000       0.17367040 

.. seealso:: :func:`cdfBinomial`, :func:`cdfBinomialInv`, :func:`cdfNegBinomialInv`

