
cdfn, cdfnc
==============================================

Purpose
----------------
:func:`cdfn` computes the cumulative distribution function
(cdf) of the Normal distribution. :func:`cdfnc` computes 1
minus the cdf of the Normal distribution.

Format
----------------
.. function:: cdfn(x[, mu, sigma])
              cdfnc(x)

    :param x: Values at which to evaluate the normal cumulative distribution function or the complement of the normal cdf.
    :type x: NxK matrix

    :param mu: Optional input, mean parameter.
    :type mu: scalar

    :param std: Optional input, standard deviation.
    :type std: scalar

    :returns: **p** (*NxK matrix*) - Each element in *p* is the normal cumulative distribution function evaluated at the corresponding element in *x*.

    :returns: **pc** (*NxK matrix*) - Each element in *pc* is the complement of the normal cumulative distribution function evaluated at the corresponding element in *x*.

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

   n = cdfn(x);
   if n >= 1-eps;
      n = 1;
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

Basic example
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

Specify mean and standard deviation
+++++++++++++++++++++++++++++++++++

::

    // Value
    x = 0.5;

    // Mean
    mu = 1.1;

    // Standard deviation
    std = 3;

    p = cdfn(x, mu, std);


Example 3
++++++++++

After above code,

::

    p = 0.42074029

    // Value
    x = { -2 -1 0 1 2 };

    p = cdfn(x);
    pc = cdfnc(x);

After above code,

::

    x  = -2.0000000 -1.0000000 0.0000000 1.0000000 2.0000000
    p  =  0.0227501 0.15865525 0.5000000 0.8413447 0.9772498
    pc =  0.9772498 0.84134475 0.5000000 0.1586552 0.0227501

Technical Notes
------------

For the integral from :math:`∞` to *x*:

.. csv-table::
    :widths: auto

    ":math:`x \leq -37`", ":func:`cdfn` underflows and 0.0 is returned"
    ":math:`-36 < x < -10`", ":func:`cdfn` has a relative error of approx. ±5e-12"
    ":math:`-10 < x < 0`", ":func:`cdfn` has a relative error of approx. ±1e-13"
    ":math:`0 < x`", ":func:`cdfn` has a relative error of approx. ±5e-15"

For :func:`cdfnc`, i.e., the integral from *x* to :math:`+∞`, use the above accuracies but
change *x* to *-x*.

References
------------

#. Adams, A.G. ''Remark on Algorithm 304 Normal Curve Integral.'' Comm.
   ACM. Vol. 12, No. 10, Oct. 1969, 565-66.

#. Hill, I.D. and S.A. Joyce. ''Algorithm 304 Normal Curve Integral.''
   Comm. ACM. Vol. 10, No. 6, June 1967, 374-75.

#. Holmgren, B. ''Remark on Algorithm 304 Normal Curve Integral.'' Comm.
   ACM. Vol. 13, No. 10, Oct. 1970.

#. Mardia, K.V. and P.J. Zemroch. Tables of the F- and Related
   Distributions with Algorithms. Academic Press, New York, 1978, ISBN
   0-12-471140-5.

.. seealso:: Functions :func:`erf`, :func:`erfc`, :func:`cdfBeta`, :func:`cdfChic`, :func:`cdfTc`, :func:`cdfFc`, :func:`gamma`
