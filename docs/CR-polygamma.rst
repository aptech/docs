
polygamma
==============================================

Purpose
----------------

Computes the polygamma function.

Format
----------------
.. function:: f = polygamma(z, n)

    :param z: z may be complex
    :type z: NxK matrix

    :param n: If *n* is 0 then *f* will be the Digamma function.
        If *n* = 1,2,3, etc., then *f* will be the tri-, tetra-, penta-, s-, etc., Gamma function.
        Real (*n*) must be positive.
    :type n: The order of the function

    :return f: *f* may be complex.
    :rtype f: NxK matrix

Remarks
-------

The :func:`polygamma` function of order *n* is defined by the equation:

.. math:: $\psi^{(n)}(z) = \\frac{d^n}{dz^n}\psi(z) = \\frac{d^{n+1}}{dz^{n+1}}ln\Gamma(z)$

.. DANGER:: fix equation if needed

This program uses the partial fraction expansion of the derivative of
the log of the Lanczos series approximation for the Gamma function.
Accurate to about 12 digits.

Examples
----------------

Example 1: Basic usage
++++++++++++++++++++++

::

    // Both calls are equivalent
    f = digamma(1);
    f2 = polygamma(1, 0);

After the code above, both *f* and *f2* should be equal to :math:`-g`, where *g* represents the Euler-Mascheroni constant:

::

    -0.57721566

Compute the pentagamma function
+++++++++++++++++++++++++++++++

::

    f = polygamma(1.5, 4);

After the code above, f should be equal to:

::

    -3.47425

Complex input
+++++++++++++

::

    // Set 'z' equal to complex number -45.6-29.4i
    z = { -45.6 - 29.4i };
    polygamma(z, 101);

::

    12.501909 + 9.0829590i


Example 4
+++++++++

::

    z = { -11.5 - 0.577007813568142i };
    polygamma(z,10);

will return the value:

::

    -4.984e-06 + 8.217e-07i

References
------------

#. C. Lanczos, SIAM JNA 1, 1964. pp. 86-96.

#. Y. Luke, "The Special ... approximations," 1969 pp. 29-31.

#. Y. Luke, "Algorithms ... functions," 1977.

#. J. Spouge, SIAM JNA 31, 1994. pp. 931.

#. W. Press, "Numerical Recipes."

#. S. Chang, "Computation of special functions," 1996.

#. Abramowitz & Stegun, section eq 6.4.6

#. Original code by Paul Godfrey

gamma polygamma trigamma
