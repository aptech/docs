
lncdfn
==============================================

Purpose
----------------

Computes natural log of Normal cumulative distribution function.

Format
----------------
.. function:: lnp = lncdfn(x)

    :param x: values at which to evaluate the cumulative distribution function.
    :type x: NxK matrix or N-dimensional array

    :return lnp: The natural log of the normal cumulative distribution function

        .. math:: ln\big(Pr(X < x)\big)

    :rtype lnp: NxK matrix or N-dimensional array

Examples
----------------

::

        // Starting x
        x = { 0.0506, 0.1886, 0.3781, 0.5763 };

        // Call the cdfN2
        print lncdfn(x);

After the above code:

::

  -0.65358
  -0.55374
  -0.43491
  -0.33157

Source
------

lncdfn.src
