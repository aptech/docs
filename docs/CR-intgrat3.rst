
intgrat3
==============================================

Purpose
----------------

Integrates the following triple integral, using user-defined functions and scalars for bounds:

.. math::

   \int_{a}^{b}\int_{g_2(x)}^{g_1(x)} \int_{gh_2(x, y)}^{h_1(x, y)}f(x, y, z)dzdydx

.. DANGER:: FIX EQUATION

Format
----------------
.. function:: intgrat3(&f, xl, gl, hl)

    :param &f: pointer to the procedure containing the function to be integrated. *f* is a function of *(x, y, z)*.
    :type &f: scalar

    :param xl: the limits of *x*. These must be scalar limits.
    :type xl: 2x1 or 2xN matrix

    :param gl: function pointers. These procedures are functions of *x*.
    :type gl: 2x1 or 2xN matrix

    :param hl: function pointers. These procedures are functions of *x* and *y*.
    :type hl: 2x1 or 2xN matrix

    :returns: y (*Nx1 vector*) of the estimated integral(s) of :math:`f(x, y, z)` evaluated between the limits given by *xl*, *gl* and *hl*.

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

User-defined functions *f*, and those used in *gl* and *hl* must either:

#. Return a scalar constant

         - or -

#. Return a vector of function values. :func:`intgrat3` will pass to
   user-defined functions a vector or matrix for *x* and *y* and expect a
   vector or matrix to be returned. Use ``.*`` and ``./`` operators instead of
   just ``*`` and ``/``.


Examples
----------------

::

    proc f(x, y, z);
    retp(2);
    endp;

    proc g1(x);
       retp(sqrt(25 - x^2));
    endp;

    proc g2(x);
       retp(-g1(x));
    endp;

    proc h1(x, y);
       retp(sqrt(25 - x^2 - y^2));
    endp;

    proc h2(x, y);
       retp(-h1(x, y));
    endp;

    xl = 5|-5;
    g0 = &g1|&g2;
    h0 = &h1|&h2;

    _intord = 40;

    y = intgrat3(&f, xl, g0, h0);

This will integrate the function :math:`f(x, y, z)` over the sphere of
radius 5. The result will be approximately twice the volume of a
sphere of radius 5.

Source
------

intgrat.src

Globals
------------

*_intord*, *_intq12*, *_intq16*, *_intq2*, *_intq20*, *_intq24*, *_intq3*,
*_intq32*, *_intq4*, *_intq40*, *_intq6*, *_intq8*

.. seealso:: Functions :func:`intgrat2`, :func:`intquad1`, :func:`intquad2`, :func:`intquad3`, :func:`intsimp`
