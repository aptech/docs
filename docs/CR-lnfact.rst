
lnfact
==============================================

Purpose
----------------

Computes the natural log of the factorial function and can be used to compute log gamma.

Format
----------------
.. function:: lnfact(x)

    :param x: all elements must be positive.
    :type x: NxK matrix or N-dimensional array

    :returns: y (*NxK matrix*), containing the natural log of the factorial of each of the elements in *x*.

Remarks
-------

For integer *x*, this is (approximately) ``ln(x!)``. However, the computation
is done using a formula, and the function is defined for noninteger *x*.

In most formulae in which the factorial operator appears, it is possible
to avoid computing the factorial directly, and to use :func:`lnfact` instead.
The advantage of this is that lnfact does not have the overflow problems
that the factorial (``!``) operator has.

For :math:`x > 1`, this function has at least 6 digit accuracy, for :math:`x > 4` it has
at least 9 digit accuracy, and for :math:`x > 10` it has at least 12 digit
accuracy. For :math:`0 < x < 1`, accuracy is not known completely but is
probably at least 6 digits.

Sometimes log gamma is required instead of log factorial. These
functions are related by:

::

   lngamma(x) = lnfact(x - 1);


Examples
----------------

::

    let x = 100 500 1000;
    y = lnfact(x);

::

        363.73938 
    y = 2611.3305 
        5912.1282

Technical Notes
---------------

For :math:`x > 1`, Stirling's formula is used.

For :math:`0 < x <= 1`, ``ln(gamma(x+1))`` is used.

Source
------

lnfact.src

.. seealso:: Functions :func:`gamma`

