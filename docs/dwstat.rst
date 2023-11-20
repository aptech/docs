
dwstat
==============================================

Purpose
----------------

Computes the Durbin-Watson statistic.

Format
----------------
.. function:: dw = DWstat(resid)

    :param resid: Residuals.
    :type resid: Tx1 vector

    :return dw: Durbin-Watson statistic.
    :rtype dw: Scalar

Examples
----------------

::

    // Generate random residuals
    rndseed 8098;
    resid = rndn(150, 1);
    
    // Calculate DW statistic
    dw = DWstat(resid);

The code above computes the following statistic:

::

    dw = 2.1413366

Source
------

fgls.src
