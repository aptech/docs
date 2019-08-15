
pdfWishartInv
==============================================

Purpose
----------------

Computes the probability density function of the inverse Wishart distribution.

Format
----------------
.. function:: y = pdfWishartInv(IW, S, df)

    :param IW: 
        T
    :type IW: p x p positive definite matrix

    :param S: 
        Ψ
    :type S: p x p positive definite scale matrix

    :param df: degree of freedom.
        ν
    :type df: Scalar

    :return y: probability density function.

    :rtype y: Scalar

Remarks
-------

pdfWishartInv calculates the probability density function for the
inverse Wishart distribution, which is defined as

::

   f(T)=|Ψ|ν/2|T|ν+p+12⁢2νp2⁢Γp(ν2)exp⁡(−12tr(ΓT−1))


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
