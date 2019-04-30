
cdfChii
==============================================

Purpose
----------------
Compute chi-square abscissae values given probability and degrees of freedom.

Format
----------------
.. function:: cdfChii(p, n)

    :param p: probabilities.
    :type p: MxN matrix

    :param n: ExE conformable with *p*, degrees of freedom.
    :type n: LxK matrix

    :returns: c (*matrix*), max(M,L) by max(N,K) matrix, abscissae values for chi-squared distribution.

Examples
----------------
The following generates a 3x3 matrix of pseudo-random
numbers with a chi-squared distribution with expected
value of 4:

::

    // Set the rng seed for repeatable random numbers
    rndseed 464578;
    
    // Set the 'probabilities' input equal to a 3x3 matrix of
    // uniform random numbers and the degrees of freedom' input
    // to be a 3x3 matrix with each element equal to '4'
    x = cdfChii(rndu(3,3),4+zeros(3,3));

After the code above:

::

        0.934227 6.231914 4.227479 
    x = 2.647158 1.203957 10.559593 
        5.868060 1.368600 1.963283

Source
-----------

cdfchii.src

.. seealso:: Functions :func:`gammaii`

