============
varmaPredict
============

10.0.64varmaPredict
===================

Purpose
-------

.. container::
   :name: Purpose

   Calculates forecasts from a VARMAX model.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   f = varmaPredict( vmo, y, x, t );

Input
-----

.. container::
   :name: Input

   +-----+---------------------------------------------------------------+
   | vmo | An instance of avarmamtOutstructure returned by a call to a   |
   |     | VARMAX or ECM procedure.                                      |
   +-----+---------------------------------------------------------------+
   | y   | T×L matrix, the variables to be forecast.                     |
   +-----+---------------------------------------------------------------+
   | x   | t×K matrix of x covering only the forecast horizon, in the    |
   |     | order or the scalar zero if there are no x variables.         |
   +-----+---------------------------------------------------------------+
   | t   | scalar, the number of periods to forecast.                    |
   +-----+---------------------------------------------------------------+

Output
------

.. container::
   :name: Output

   +---+-----------------------------------------------------------------+
   | f | t×(L+1) matrix. Column one contains the period forecast. The    |
   |   | remaining columns contain the forecast values.                  |
   +---+-----------------------------------------------------------------+

Remarks
-------

.. container::
   :name: Remarks

   The varmaFit and ecmFit procedures estimate centered models and do
   not return intercepts. However, varmaPredict allows intercepts, so
   that it might be used with the results of other estimation
   procedures.

Example
-------

.. container::
   :name: Example

   ::

      new;
      cls;
      library tsmt;

      //Load data
      //Create file name with full path
      fname = getGAUSSHome() $+ "pkgs/tsmt/examples/mink.csv";

      //Load two variables from dataset
      y = loadd(fname, "LogMink + LogMusk");

      //Difference the data
      y = vmdiffmt(y, 1);

      //Declare 'vout' to be a varmamtOut structure
      struct varmamtOut vout;

      //Estimate the parameters of the VAR(2) model
      vout = varmaFit(y, 2);

      //Predict model
      f = varmaPredict(vout, y, 0, 25);

Source
------

.. container:: gfunc
   :name: Source

   varmamt.src
