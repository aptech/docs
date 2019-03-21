
rndChiSquare
==============================================

Purpose
----------------

Creates pseudo-random numbers with a chi-squared distribution, with an optional non-centrality parameter and a choice of underlying random number generator.

Format
----------------
.. function:: rndChiSquare(r, c, df, s_ncp, state) 
			  rndChiSquare(r, c, df, s_ncp) 
			  rndChiSquare(r, c, df)

    :param r: number of rows of resulting matrix.
    :type r: Scalar

    :param c: number of columns of resulting matrix.
    :type c: Scalar

    :param df
                    Scalar, degrees of freedom.: 
    :type df
                    Scalar, degrees of freedom.: TODO

    :param s_ncp: , non-centrality parameter. NOTE: This is the square root of the noncentrality parameter that sometimes goes under the symbol lambda.
    :type s_ncp: Optional argument - scalar

    :param state: 
        
        Scalar case:state = starting seed value only. If -1, GAUSS
        computes the starting seed based on the system clock.
        Opaque vector case:state = the state vector returned from a previous
        call to one of the rnd random number functions.
    :type state: Optional argument - scalar or opaque vector

    :returns: x (*r x c matrix*), chi-square distributed random numbers.

    :returns: newstate (*Opaque vector*), the updated state.

