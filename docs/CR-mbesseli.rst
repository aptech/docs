
mbesseli
==============================================

Purpose
----------------

Computes modified and exponentially scaled modified Bessels of the first kind of the nth order.

Format
----------------
.. function:: y = mbesseli(x, n, alpha)
              y = mbesseli0(x)
              y = mbesseli1(x)
              y = mbesselei(x, n, alpha)
              y = mbesselei0(x)
              y = mbesselei1(x)

    :param x: abscissae.
    :type x: Kx1 vector

    :param n: highest order.
    :type n: scalar

    :param alpha: :math:`0 <= alpha < 1`.
    :type alpha: scalar

    :return y: evaluations of the modified Bessel or the exponentially scaled modified Bessel
        of the first kind of the nth order.

    :rtype y: KxN matrix

Remarks
-------

For the functions that permit you to specify the order, the returned
matrix contains a sequence of modified or exponentially scaled modified
Bessel values of different orders. For the ith row of *y*:

.. math::

   y[i,.] = I_{\alpha}(x[i]) I_{\alpha+1}(x[i])...I_{\alpha+n-1}(x[i])

The remaining functions generate modified Bessels of only the specified
order.

The exponentially scaled modified Bessels are related to the unscaled
modifed Bessels in the following way:

::

  mbesselei0(x) = exp(-x) * mbesseli0(x)

The use of the scaled versions of the modified Bessel can improve the
numerical properties of some calculations by keeping the intermediate
numbers small in size.

.. DANGER:: review equations on this page

Examples
----------------
This example produces estimates for the "circular" response regression
model (Fisher, N.I. Statistical Analysis of Circular Data. NY: Cambridge
University Press, 1993.), where the dependent variable varies between
:math:`-π` and :math:`π` in a circular manner. The model is

.. math::

    y = \mu + G(X\beta)

where :math:`\beta` is a vector of regression coefficients, *x* a matrix of
independent variables with a column of 1's included for a constant, and
*y* a vector of "circular" dependent variables, and where :math:`G()` is a
function mapping :math:`X\beta` onto the :math:`[ -π, π ]` interval.

The log-likelihood for this model is from Fisher, N.I. ... 1993, 159:

.. math::

    log⁡L=−N \times ln⁡(I_0(\kappa)) + \kappa ⁢\sum_i^N ⁢cos⁡(y_i−\mu−G(X_i\beta))

To generate estimates it is necessary to maximize this function using
an iterative method. :func:`QNewton` is used here.

:math:`κ` is required to be nonnegative and therefore in the example
below, the exponential of this parameter is estimated instead. Also,
the exponentially scaled modified Bessel is used to improve numerical
properties of the calculations.

The arctan function is used in :math:`G()` to map :math:`X\beta` to the :math:`[ -π, π ]` interval
as suggested by Fisher, N.I. ... 1993, 158.

::

    // Define function
    proc G(u);
       retp(2*atan(u));
    endp;

    proc lpr(b);
       local dev;
       /*
       ** b[1] - kappa
       ** b[2] - mu
       ** b[3] - constant
       ** b[4:rows(b)] - coefficients
       */
       dev = y - b[2]- G(b[3] + x * b[4:rows(b)]);
       retp(rows(dev)*ln(mbesselei0(exp(b[1])) -
          sumc(exp(b[1])*(cos(dev)-1))));
    endp;

    // Load data matrix
    loadm data;

    // Separate x0 and y0
    y0 = data[., 1];
    x0 = data[., 2:cols(data)];

    // Create constant
    b0 = 2*ones(cols(x0), 1);

    // Call optimization procedure
    { b, fct, grd, ret } = QNewton(&lpr, b0);

    cov = invpd(hessp(&lpr, b));

    print "estimates standard errors";
    print;
    print b~sqrt(diag(cov));

Source
------

ribesl.src

.. seealso:: Functions :func:`besselj`, :func:`besselk`, :func:`bessely`
