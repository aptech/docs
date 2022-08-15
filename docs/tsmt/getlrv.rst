======
getlrv
======

10.0.23getlrv
=============

Purpose
-------
Estimate long-run variance following user-selected kernel.

Library
-------
tsmt

Format
------
{LRV, bw} = getlrv(y, kernel, lagMethod, model);

Input
-----
+------------+--------------------------------------------------------+
   | y          | Nx1 vector, data.                                      |
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
=== ===========================
   LRV Matrix, long run variance.
   bw  Scalar, selected bandwidth.
   === ===========================
::

new;
cls;
library tsmt;

// Generate random data
yt = rndn(200, 1);

// Newey-West bandwidth selection
lagMethod = "nw";

// Parzen kernel for estimating variance
kernel = "parzen";

// Constant and no trend
Model = 0;

// Call function
{ LRV, bw } = getLRV(yt, kernel, lagMethod, model);

// Print results
print "Long-run variance : ";; LRV;

Source
------
getlrv.src
