
zeta
==============================================

Purpose
----------------
Computes the Riemann Zeta function.

Format
----------------
.. function:: f = zeta(z)

    :param z: data. *z* may be complex
    :type z: NxK matrix

    :return f: 

    :rtype f: NxK matrix

Example
--------

::

    f = zeta(2);

After the above code, *f* will equal:

::

    1.6449341

which is equivalent to :math:`\frac{\pi^2}{6}`.

Remarks
-------

The Riemann zeta function is represented by the equation:

.. math::

    \zeta(s) = \frac{1}{\Gamma(s)} \int_0^\infty \frac{x^{s-1}}{e^x-1} dx

Euler MacLaurin series.

References
----------

#. Jon Breslaw, 2009

