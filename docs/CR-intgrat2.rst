
intgrat2
==============================================

Purpose
----------------

Integrates the following double integral, using user-defined functions *f*, *g1* and *g2* and scalars *a* and *b*:

.. math::

   \int_{a}^{b}\int_{g_2(x)}^{g_1(x)} f(x,y)dydx

Format
----------------
.. function:: y = intgrat2(&f, xl, gl)

    :param &f: pointer to the procedure containing the function to be integrated.
    :type &f: scalar

    :param xl: the limits of *x*. These must be scalar limits.
    :type xl: 2x1 or 2xN matrix

    :param gl: Function pointers to functions defining the limits of *y*.

        For *xl* and *gl*, the first row is the upper limit and the second row is the lower limit. *N* integrations are computed.

    :type gl: 2x1 or 2xN matrix

    :returns: **y** (*Nx1 vector*) of the estimated integral(s) of :math:`f(x, y)`, evaluated between the limits given by *xl* and *gl*.

Global Input
------------

+-----------------+-----------------------------------------------------+
| \_intord        | scalar, the order of the integration. The larger    |
|                 | \_intord, the more precise the final result will    |
|                 | be. \_intord may be set to 2, 3, 4, 6, 8, 12, 16,   |
|                 | 20, 24, 32, 40.                                     |
|                 | Default = 12.                                       |
+-----------------+-----------------------------------------------------+


Remarks
-------

The user-defined functions specified by *f* and *gl* must either

#. Return a scalar constant

         - or -

#. Return a vector of function values. :func:`intgrat2` will pass to
   user-defined functions a vector or matrix for *x* and *y* and expect a
   vector or matrix to be returned. Use ``.*`` and ``./`` instead of ``*`` and ``/``.


Examples
----------------

::

    proc (1) = f(x, y);
      retp((cos(x) + 1).*(sin(y) + 1));
    endp;

    proc (1) = g1(x);
       retp(sqrt(1 - x^2));
    endp;

    proc (1) = g2(x);
       retp(0);
    endp;

    // Limits
    xl = 1|-1;

    // Create vector of function pointers
    g0 = &g1|&g2;

    // Order of integration
    _intord = 40;

    // Integrate
    y = intgrat2(&f, xl, g0);

This will integrate the function

::

    f(x, y) = (cos(x) + 1)(sin(y) + 1)

over the upper half of the unit circle. Note the use of the ``.*`` operator instead of just ``*`` in the
definition of :math:`f(x, y)`. This allows *f* to return a vector or matrix of function values.

Source
------

intgrat.src

Globals
------------

*_intord*, *_intq12*, *_intq16*, *_intq2*, *_intq20*, *_intq24*, *_intq3*,
*_intq32*, *_intq4*, *_intq40*, *_intq6*, *_intq8*

.. seealso:: Functions :func:`intgrat3`, :func:`intquad1`, :func:`intquad2`, :func:`intquad3`, :func:`intsimp`
