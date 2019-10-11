
rndWishart
==============================================

Purpose
----------------

Computes Wishart distributed random numbers given a covariance matrix.

Format
----------------
.. function:: r = rndWishart(numMats, cov, df)
              { r, newstate } = rndWishart(numMats, cov, df, state)

    :param numMats: number of Wishart random matrices to create.
    :type numMats: scalar

    :param cov: NxM covariance matrix
    :type cov: matrix

    :param df: degrees of freedom.
    :type df: scalar

    :param state: Optional argument.

        **scalar case**
        
            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **opaque vector case**
        
            *state* = the state vector returned from a previous call to one of the rnd random number functions.

    :type state: scalar or opaque vector

    :return r: wishart random matrices.

    :rtype r: numMats * rows(cov) x N matrix

    :return newstate: the updated state.

    :rtype newstate: Opaque vector

Examples
----------------

::

    // covariance matrix
    cov = {  1   0.5,
           0.5     1 };
    
    // degrees of freedom
    df = 7;
    
    X = rndWishart(1, cov, df);

::

    X = 7.6019339 4.7744799 
        4.7744799 7.7341260

Remarks
-------

The properties of the pseudo-random numbers in *X* are:

.. DANGER:: fix equations

.. math::

   E(X) = df * cov

   Var(Xij) = df * (cov2ij + covii*covjj)


.. seealso:: Functions :func:`rndWishartInv`, :func:`rndMVn`, :func:`rndCreateState`

