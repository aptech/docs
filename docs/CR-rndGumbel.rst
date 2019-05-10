
rndGumbel
==============================================

Purpose
----------------

Computes Gumbel distributed random numbers with a choice of underlying random number generator.

Format
----------------
.. function:: rndGumbel(rows, cols, scale)
              rndGumbel(rows, cols, location, scale[, state])

.. DANGER:: very format?

    :param rows: number of rows of resulting matrix.
    :type rows: scalar

    :param cols: number of columns of resulting matrix.
    :type cols: scalar

    :param location: scalar or ExE conformable matrix with *rows* and *cols*
    :type location: scalar or matrix

    :param scale: scalar or ExE conformable matrix with *rows* and *cols*
    :type scale: scalar or matrix

    :param state: Optional argument.

        **scalar case**
        
            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **opaque vector case**
        
            *state* = the state vector returned from a previous call to one of the rnd random number functions.

    :type state: scalar or opaque vector

    :returns: r (*rows x cols matrix*), Gumbel distributed random numbers.

    :returns: newstate (*Opaque vector*), the updated state.

Remarks
-------

This function uses the definition of the Gumbel distribution
corresponding to the minimum extreme. The properties of the
pseudo-random numbers in *y* are:

.. DANGER:: fix equations

.. math::

   E(y) = location - γ*scale ≈ location - 0.5772*scale
   γ = Euler-Mascheroni constant
   Var(y) = (π2*scale2)/6

*r* and *c* will be truncated to integers if necessary.

.. seealso:: Functions :func:`rndCreateState`, :func:`rndStateSkip`

