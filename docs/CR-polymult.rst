
polymult
==============================================

Purpose
----------------

Multiplies polynomials.

Format
----------------
.. function:: c = polymult(c1, c2)

    :param c1: coefficients of the first polynomial
    :type c1: (D1+1)x1 vector

    :param c2: coefficients of the second polynomial
    :type c2: (D2+1)x1 vector

    :returns: c (*(D1+D2)x1 vector*) containing the coefficients of the product of the two polynomials.

Examples
----------------
This example multiplies the polynomials:

.. math::

    (2x + 1)(2x2 + 1)

and returns the answer:

.. math::

    4x3 + 2x2 + 2x + 1

::

    // Assign c1 to represent 2x + 1
    c1 = { 2, 1 };
    
    // Assign c2 to represent 2x2 + 1
    c2 = { 2, 0, 1 };
    c = polymult(c1,c2);

After the code above:

::

        4
    c = 2
        2
        1

Technical Notes
------------

If the degree of *c1* is *D1* (e.g., if :math:`D1=3`, then the polynomial
corresponding to *c1* is cubic), then there must be D1+1 elements in *c1*
(e.g., 4 elements for a cubic). Thus, for instance the coefficients for
the polynomial

.. math::

   5x3 + 6x + 3

would be:

::

   // Using the pipe operator for vertical concatenation
   c1 = 5|0|6|3;

     or

   // Using an array assignment
   c1 = { 5, 0, 6, 3 };

(Note that zeros must be explicitly given if there are powers of *x* missing.)

.. DANGER:: fix equations

Source
------

poly.src

.. seealso:: Functions :func:`polymake`, :func:`polychar`, :func:`polyroot`, :func:`polyeval`

