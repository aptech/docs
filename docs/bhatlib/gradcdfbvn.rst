gradcdfbvn
==============================================

Purpose
----------------

Develops gradients with respect to the standard bivariate normal cumulative function. 

Format
----------------
.. function:: { gw1, gw2, grho } = gradcdfbvn(w1, w2, rho)

    :param w1: Abscissae points.
    :type w1: K x 1 vector

    :param w2: Abscissae points.
    :type w2: K x K matrix

    :param rh0: Correlation vector.
    :type rho: K x 1 vector 
    
    :param gw1: Gradients of cdfbvn with respect to w1.
    :type gw1: K x 1 vector 
    
    :param gw2: Gradients of cdfbvn with respect to w2.
    :type gw2: scalar

    :return grho: Gradients of cdfbvn with respect to rho.
    :rtype grho: scalar

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);


Source
------------

gradients-mvn.src
