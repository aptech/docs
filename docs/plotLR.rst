
plotLR
==============================================

Purpose
----------------

Generates summary plot of parameter path and mse path over lambda values.

Format
----------------
.. function:: plotLR(mdl [, mse_test])

    :param mdl: A filled instance of either a `lassoModel` or `ridgeModel` structure.
    :type mdl: struct

    :param mse_test: Optional, vector of MSE values for test data.
    :type mse_test: Nx1 vector


Examples
----------------

::




.. seealso:: Functions :func:`lrPredict`, :func:`lassoFit`, :func:`ridgeFit`
