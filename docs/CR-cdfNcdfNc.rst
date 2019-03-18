
cdfn, cdfnc
==============================================

Purpose
----------------
cdfn computes the cumulative distribution function
(cdf) of the Normal distribution. cdfnc computes 1
minus the cdf of the Normal distribution.

Format
----------------
.. function:: cdfn(x) 
			  cdfn(x, mu) 
			  cdfn(x, mu, sigma) 
			  cdfnc(x)

    :param x: NxK matrix.
    :type x: TODO

    :param mu: scalar, mean parameter.
    :type mu: Optional input

    :param sigma: scalar, standard deviation.
    :type sigma: Optional input

    :returns: n (*TODO*), NxK matrix.

    :returns: nc (*TODO*), NxK matrix.

Examples
----------------

Basic example
+++++++++++++

::

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

    x = 0.5;
    mu = 1.1;
    sigma = 3;
    p = cdfn(x,mu,sigma);

After above code,

::

    p = 0.42074029

x = { -2 -1 0 1 2 };
n = cdfn(x);
nc = cdfnc(x);
++++++++++++++++++++++++++++++++++++++++++++++++

After above code,

::

    x  = -2.0000000 -1.0000000 0.0000000 1.0000000 2.0000000
    n  =  0.0227501 0.15865525 0.5000000 0.8413447 0.9772498
    nc =  0.9772498 0.84134475 0.5000000 0.1586552 0.0227501

Remarks
+++++++

n is the integral from -∞ to x of the Normal density function, and nc is
the integral from x to +∞.

Note that:

::

   cdfn(x) + cdfnc(x) = 1

However, many applications expect cdfn(x) to approach 1, but never
actually reach it. Because of this, we have capped the return value of
cdfn at 1 - machine epsilon, or approximately 1 - 1.11e-16. As the
relative error of cdfn is about ±5e-15 for cdfn(x) around 1, this does
not invalidate the result. What it does mean is that for abs(x) >
(approx.) 8.2924, the identity does not hold true. If you have a need
for the uncapped value of cdfn, the following code will return it:

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
1 + machine epsilon > 1, which is about 2.23e-16. This defines machine
epsilon as the smallest number such that 1 -machine epsilon < 1, or
about 1.11e-16.

The erf and erfc functions are also provided, and may sometimes be more
useful than cdfn and cdfnc.

.. seealso:: Functions :func:`erf`, :func:`erfc`, :func:`cdfBeta`, :func:`cdfChic`, :func:`cdfTc`, :func:`cdfFc`, :func:`gamma`

Technical Notes
+++++++++++++++

For the integral from ∞ to x:

+---+---+---+---+---+-----------------------------------------------------+
|   |   | x | < | - | cdfn underflows and 0.0 is returned                 |
|   |   |   | = | 3 |                                                     |
|   |   |   |   | 7 |                                                     |
+---+---+---+---+---+-----------------------------------------------------+
| - | < | x | < | - | cdfn has a relative error of approx. ±5e-12         |
| 3 |   |   |   | 1 |                                                     |
| 6 |   |   |   | 0 |                                                     |
+---+---+---+---+---+-----------------------------------------------------+
| - | < | x | < | 0 | cdfn has a relative error of approx. ±1e-13         |
| 1 |   |   |   |   |                                                     |
| 0 |   |   |   |   |                                                     |
+---+---+---+---+---+-----------------------------------------------------+
| 0 | < | x |   |   | cdfn has a relative error of approx. ±5e-15         |
+---+---+---+---+---+-----------------------------------------------------+

For cdfnc, i.e., the integral from x to +∞, use the above accuracies but
change x to -x.

References
++++++++++

#. Adams, A.G. ''Remark on Algorithm 304 Normal Curve Integral.'' Comm.
   ACM. Vol. 12, No. 10, Oct. 1969, 565-66.

#. Hill, I.D. and S.A. Joyce. ''Algorithm 304 Normal Curve Integral.''
   Comm. ACM. Vol. 10, No. 6, June 1967, 374-75.

#. Holmgren, B. ''Remark on Algorithm 304 Normal Curve Integral.'' Comm.
   ACM. Vol. 13, No. 10, Oct. 1970.

#. Mardia, K.V. and P.J. Zemroch. Tables of the F- and Related
   Distributions with Algorithms. Academic Press, New York, 1978, ISBN
   0-12-471140-5.

complement normal cdf cumulative distribution function
