
rndExp
==============================================

Purpose
----------------

Computes exponentially distributed random numbers with a choice of underlying random number generator.

Format
----------------
.. function:: rndExp(rows, cols, scale)

    :param rows: number of rows of resulting matrix.
    :type rows: Scalar

    :param cols: number of columns of resulting matrix.
    :type cols: Scalar

    :param scale:  The scale parameter sometimes called β
    :type scale: Scalar or a matrix that is ExE conformable with the dimensions of the output

    :param state: 
        
        Scalar case:state = starting seed value only. If -1, GAUSS
        
        computes the starting seed based on the system clock.Opaque vector case:state = the state vector returned from a previous
        
        call to one of the rnd random number functions.
    :type state: Optional argument - scalar or opaque vector

    :returns: r (*rows x cols matrix*), exponentially distributed random numbers.

    :returns: newstate (*Opaque vector*), the updated state.



Remarks
-------

The properties of the pseudo-random numbers in x are specified in terms
of the scale parameter sometimes called β. This is the reciprocal of the
rate parameter which is sometimes called λ:

::

   E(x) = scale = β = 1/rate = 1/λ
   Var(x) = scale2 = β2 = 1/rate2 = 1/λ2

.. seealso:: Functions :func:`rndCreateState`, :func:`rndStateSkip`
