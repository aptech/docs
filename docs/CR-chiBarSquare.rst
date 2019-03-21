
chiBarSquare
==============================================

Purpose
----------------

Compute compute the probability for a chi-bar square statistic from an hypothesis involving parameters under constraints.

Format
----------------
.. function:: chiBarSquare(SL, H, a, b, c, d, bounds)

    :param SL: chi-bar square statistic
    :type SL: scalar

    :param H: positive covariance matrix
    :type H: KxK matrix

    :param a: linear equality constraint coefficients
    :type a: MxK matrix

    :param b: linear equality constraint constants
        
        These arguments specify the linear equality
        constraints of the following type:
        
        .. math::  a * X = b
        
        where *x* is the :math:`Kx1` parameter vector.
    :type b: Mx1 vector

    :param c: linear inequality constraint coefficients.
    :type c: MxK matrix

    :param d: linear inequality constraint constants.
        
        These arguments specify the linear inequality
        constraints of the following type:
        
        .. math::  c * X >= d

        where *x* is the :math:`Kx1` parameter vector.
    :type d: Mx1 vector

    :param bounds: bounds on parameters. The first column
        contains the lower bounds, and the second column the
        upper bounds.
    :type bounds: Kx2 matrix

    :returns: SLprob (*scalar*), probability of *SL*.

Remarks
-------

See Silvapulle and Sen, *Constrained Statistical Inference*, page 75 for
further details about this function. Let

.. math::  Zpx1 N(0,V)

where *V* is a positive definite covariance matrix. Define

.. math::  x−2(V,C)=Z′V−1Z−min⁡θϵC⁢   (Z−θ)′ V−1(Z−θ) 

*C* is a closed convex cone describing a set of constraints. ChiBarSquare
computes the probability of this statistic given *V* and *C*.

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
------------

hypotest.src

