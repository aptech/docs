varmaPredict
============

Purpose
-------
Calculates forecasts from a VARMAX model.

Format
------
.. function:: f = varmaPredict(vmo, y, x, t)

   :param vmo: An instance of avarmamtOut structure returned by a call to a VARMAX or ECM procedure.
   :type vmo: struct

   :param y: the variables to be forecast.
   :type y: TxL matrix

   :param x: x covering only the forecast horizon, in the order or the scalar zero if there are no x variables.
   :type x: txK matrix

   :param t: the number of periods to forecast.
   :type t: scalar

   :return f: Column one contains the period forecast. The remaining columns contain the forecast values.
   :rtype f: tx(L+1) matrix

Example
-------

::

   new;
   cls;
   library tsmt;

   // Load data
   // Create file name with full path
   fname = getGAUSSHome() $+ "pkgs/tsmt/examples/mink.csv";

   // Load two variables from dataset
   y = loadd(fname, "LogMink + LogMusk");

   // Difference the data
   y = vmdiffmt(y, 1);

   // Declare 'vout' to be a varmamtOut structure
   struct varmamtOut vout;

   // Estimate the parameters of the VAR(2) model
   vout = varmaFit(y, 2);

   // Predict model
   f = varmaPredict(vout, y, 0, 25);

Remarks
-------
The varmaFit and ecmFit procedures estimate centered models and do
not return intercepts. However, varmaPredict allows intercepts, so
that it might be used with the results of other estimation
procedures.

Library
-------
tsmt

Source
------
varmamt.src
