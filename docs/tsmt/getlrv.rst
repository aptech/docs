======
getlrv
======

10.0.23getlrv
=============

Purpose
-------

.. container::
   :name: Purpose

   Estimate long-run variance following user-selected kernel.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   {LRV, bw} = getlrv(y, kernel, lagMethod, model);

Input
-----

.. container::
   :name: Input

   +------------+--------------------------------------------------------+
   | y          | N×1 vector, data.                                      |
   +------------+--------------------------------------------------------+
   | kernel     | String, kernels used to estimate long-run variance:    |
   |            | "Bartlett", "Parzen", or "Quad".                       |
   +------------+--------------------------------------------------------+
   | lag_method | String, method used to estimate bandwith: "LLC" or     |
   |            | "NW".                                                  |
   +------------+--------------------------------------------------------+
   | model      | scalar, -1 = no constant nor trend; 0 = constant; 1 =  |
   |            | constant and trend.                                    |
   +------------+--------------------------------------------------------+

Output
------

.. container::
   :name: Output

   === ===========================
   LRV Matrix, long run variance.
   bw  Scalar, selected bandwidth.
   === ===========================

.. container::
   :name: Example

   ::

      new;
      cls;
      library tsmt;

      //Generate random data
      yt = rndn(200, 1);

      //Newey-West bandwidth selection
      lagMethod = "nw";

      //Parzen kernel for estimating variance
      kernel = "parzen";

      //Constant and no trend
      Model = 0;

      //Call function
      { LRV, bw } = getLRV(yt, kernel, lagMethod, model);

      //Print results
      print "Long-run variance : ";; LRV;

Source
------

.. container:: gfunc
   :name: Source

   getlrv.src
