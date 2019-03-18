
pdfWishartInv
==============================================

Purpose
----------------

Computes the probability density function of the inverse Wishart distribution.

Format
----------------
.. function:: pdfWishartInv(IW, S, df)

    :param IW: p x p positive definite matrix.
        T
    :type IW: TODO

    :param S: p x p positive definite scale matrix.
        Ψ
    :type S: TODO

    :param df: degree of freedom.
        ν
    :type df: Scalar

    :returns: y (*Scalar*), probability density function.

Examples
----------------

::

    new ;
    cls ;								
    rndseed 2223; 
    				
    x = {9.2517907  7.4283670, 
         7.4283670 10.503325 };
    				
    S = {1 .5, .5 1};	
    							
    df = 3;
    
    // pdf of inverse Wishart distribution
    y = pdfWishartInv(x, S, df);	
    
    print y;

After above code,

::

    6.0267322e-007

See also
++++++++

`rndWishart <CR-rndWishart.html#rndWishart>`__\,\ `rndWishartInv <CR-rndWishartInv.html#rndWishartInv>`__

pdf inverse Wishart
