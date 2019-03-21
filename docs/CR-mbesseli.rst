
mbesseli
==============================================

Purpose
----------------

Computes modified and exponentially scaled modified Bessels of the first kind of the nth order.

Format
----------------
.. function:: mbesseli(x, n, alpha) 
			  mbesseli0(x) 
			  mbesseli1(x) 
			  mbesselei(x, n, alpha) 
			  mbesselei0(x) 
			  mbesselei1(x)

    :param x: abscissae.
    :type x: Kx1 vector

    :param n: highest order.
    :type n: scalar

    :param alpha: 0 <= alpha < 1.
    :type alpha: scalar

    :returns: y (*KxN matrix*), evaluations of the modified Bessel or the exponentially scaled modified Bessel
        of the first kind of the nth order.

Examples
----------------
This example produces estimates for the "circular" response regression model (Fisher, N.I. Statistical Analysis of
Circular Data. NY: Cambridge University Press, 1993.), where the
dependent variable varies between -π and π in a circular manner. The model is

::

    y = μ + G(XB)

B
x
y
G
XB
The log-likelihood for this model is from Fisher, N.I. ... 1993, 159:

::

    log⁡L=−N×ln⁡(I0(κ))+κ⁢NΣi⁢cos⁡(yi−μ−G(XiB))

To generate estimates it is necessary to maximize this function using
an iterative method.  QNewton is used here.
κ is required to be nonnegative and therefore in the example
below, the exponential of this parameter is estimated instead. Also,
the exponentially scaled modified Bessel is used to improve numerical
properties of the calculations.
The arctan function is used in G() to map XB to the [ -π, π ] interval
as suggested by Fisher, N.I. ... 1993, 158.

::

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
     
    loadm data;
    y0 = data[.,1];
    x0 = data[.,2:cols(data)];
     
    b0 = 2*ones(cols(x0),1);
     
    { b,fct,grd,ret } = QNewton(&lpr,b0);
     
    cov = invpd(hessp(&lpr,b));
     
    print "estimates standard errors";
    print;
    print b~sqrt(diag(cov));

Source
++++++

ribesl.src

.. seealso:: Functions :func:`besselj`, :func:`besselk`, :func:`bessely`

bessel
