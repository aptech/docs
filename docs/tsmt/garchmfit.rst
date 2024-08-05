garchMFit
=========

Purpose
-------
Estimates GARCH-in-mean model.

Format
------
.. function:: gOut = garchMFit(y, p[, q, gctl])
              gOut = garchMFit(dataset, formula, p[, q, gctl])

   :param y: dependent variables.
   :type y: Matrix

   :param x: independent variables.
   :type x: Matrix

   :param dataset: name of data set or null string.
   :type dataset: string

   :param formula: formula string of the model. E.g. "y ~ X1 + X2" 'y' is the name of dependent variable, 'X1' and 'X2' are names of independent variables; E.g. "y ~ ." , '.' means including all variables except dependent variable 'y';
   :type formula: string

   :param p: order of the GARCH parameters.
   :type p: scalar

   :param q: Optional input, order of the ARCH parameters.
   :type q: scalar

   :param gctl: Optional input, :class:`garchControl`` structure.

      .. include:: include/garchcontrol.rst

   :type gCtl: struct

   :return gOut: :class:`garchEstimation` structure.

      .. include:: include/garchestimation.rst

   :rtype out1: struct

Library
-------
tsmt

Source
------
tsgarch.src

.. seealso:: Functions :func:`garchFit`, :func:`garchGJRFit`
