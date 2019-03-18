
chiBarSquare
==============================================

Purpose
----------------

Compute compute the probability for a chi-bar square statistic from an hypothesis involving parameters under constraints.

Format
----------------
.. function:: chiBarSquare(SL,  H,  a,  b, c,  d,  bounds)

    :param SL: chi-bar square statistic
    :type SL: scalar

    :param H: positive covariance matrix
    :type H: KxK matrix

    :param a: linear equality constraint coefficients
    :type a: MxK matrix

    :param b: linear equality constraint constants
        
        These arguments specify the linear equality
        constraints of the following type:
        
        a * X = b
        
        where x is the Kx1 parameter vector.
    :type b: Mx1 vector

    :param c: linear inequality constraint coefficients.
    :type c: MxK matrix

    :param d: linear inequality constraint constants.
        
        These arguments specify the linear inequality
        constraints of the following type:
        
        c * X >= d
        where x is the Kx1 parameter vector.
    :type d: Mx1 vector

    :param bounds: bounds on parameters. The first column
        contains the lower bounds, and the second column the
        upper bounds.
    :type bounds: Kx2 matrix

    :returns: SLprob (*scalar*), probability of  SL.

Examples
----------------

::

    V = { 0.0005255598 -0.0006871606 -0.0003191342,
         -0.0006871606 0.0037466205 0.0012285813,
         -0.0003191342 0.0012285813 0.0009081412 };
     
    SL = 3.860509;
    
    Bounds = { 0 200, 0 200, 0 200 };
     
    vi = invpd(v);
     
    SLprob = chiBarSquare(SL,Vi,0,0,0,0,bounds);

After running above code,

::

    SLprob = 0.10885000

Source
++++++

hypotest.src

probability chi bar square statistic
