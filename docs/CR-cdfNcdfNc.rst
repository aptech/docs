
cdfn, cdfnc
==============================================

Purpose
----------------
:func:`cdfn` computes the cumulative distribution function
(cdf) of the Normal distribution. :func:`cdfnc` computes 1
minus the cdf of the Normal distribution.

Format
----------------
.. function:: n = cdfn(x[, mu, sigma])
              n = cdfnc(x)

    :param x: Values at which to evaluate the normal cumulative distribution function or the complement of the normal cdf.
    :type x: NxK matrix

    :param mu: Optional input, mean parameter.
    :type mu: scalar

    :param std: Optional input, standard deviation.
    :type std: scalar

    :return p: Each element in *p* is the normal cumulative distribution function evaluated at the corresponding element in *x*.

    :rtype p: NxK matrix

    :return pc: Each element in *pc* is the complement of the normal cumulative distribution function evaluated at the corresponding element in *x*.

    :rtype pc: NxK matrix

Remarks
------------

Note that:

::

   cdfn(x) + cdfnc(x) = 1

However, many applications expect :code:`cdfn(x)` to approach 1 but never
actually reach it. Because of this, we have capped the return value of
:func:`cdfn` at :math:`1 - machine\:\ epsilon`, or approximately :math:`1 - 1.11e-16`. As the
relative error of :func:`cdfn` is about :math:`\pm 5e-15` for :code:`cdfn(x)` around 1, this does
not invalidate the result. What it does mean is that for :math:`abs(x) >
\approx 8.2924`, the identity does not hold true. If you have a need
for the uncapped value of :func:`cdfn`, the following code will return it:

::

   p = cdfn(x);
   if p >= 1-eps;
      p = 1;
   endif;

where the value of machine epsilon is obtained as follows:

::

   x = 1;
   do while 1-x /= 1;
      eps = x;
      x = x/2;
   endo;

Note that this is an alternate definition of machine epsilon. Machine
epsilon is usually defined as the smallest number such that
:math:`1 + machine\:\ epsilon > 1`, which is about 2.23e-16. This defines machine
epsilon as the smallest number such that :math:`1 - machine\:\ epsilon < 1`, or
about 1.11e-16.

The :func:`erf` and :func:`erfc` functions are also provided, and may sometimes be more
useful than :func:`cdfn` and :func:`cdfnc`.

Examples
----------------

Example 1: Basic use
+++++++++++++

::

    // Value to compute
    x = 0.5;

    p = cdfn(x);
    pc = cdfnc(x);

After above code,

::

    p =  0.69146246
    pc = 0.30853754

Example 2: Specify mean and standard deviation
+++++++++++++++++++++++++++++++++++

::

    // Value
    x = 0.5;

    // Mean
    mu = 1.1;

    // Standard deviation
    std = 3;

    p = cdfn(x, mu, std);

After above code,

::

    p = 0.42074029

Example 3
++++++++++

::

    // Value
    x = { -2 -1 0 1 2 };

    p = cdfn(x);
    pc = cdfnc(x);

After above code,

::

    x  = -2.0000000 -1.0000000 0.0000000 1.0000000 2.0000000
    p  =  0.0227501 0.15865525 0.5000000 0.8413447 0.9772498
    pc =  0.9772498 0.84134475 0.5000000 0.1586552 0.0227501

.. seealso:: Functions :func:`erf`, :func:`erfc`, :func:`cdfBeta`, :func:`cdfChic`, :func:`cdfTc`, :func:`cdfFc`, :func:`gamma`
