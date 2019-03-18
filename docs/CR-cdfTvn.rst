
cdfTvn
==============================================

Purpose
----------------

Computes the cumulative distribution function of the
standardized trivariate Normal density (lower tail).

Format
----------------
.. function:: cdfTvn(x1,  x2,  x3,  rho12,  rho23,  rho13)

    :param x1: Nx1 vector of upper limits of integration for variable 1.
    :type x1: TODO

    :param x2: Nx1 vector of upper limits of integration for variable 2.
    :type x2: TODO

    :param x3: Nx1 vector of upper limits of integration for variable 3.
    :type x3: TODO

    :param rho12: scalar or Nx1 vector of correlation coefficients
        between the two variables  x1 and  x2.
    :type rho12: TODO

    :param rho23: scalar or Nx1 vector of correlation coefficients
        between the two variables  x2 and  x3.
    :type rho23: TODO

    :param rho13: scalar or Nx1 vector of correlation coefficients
        between the two variables  x1 and  x3.
    :type rho13: TODO

    :returns: c (*TODO*), Nx1 vector containing the result of the triple integral
        from -∞ to  x1, -∞ to  x2, and -∞ to  x3
        of the standardized trivariate Normal density.

