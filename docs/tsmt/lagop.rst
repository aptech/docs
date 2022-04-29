=====
lagop
=====

10.0.31lagop
============

Purpose
-------
Lag polynomial operator function (filter). It produces the moving
   average series formed by the lag polynomial operator.

Library
-------
tsmt

Format
------
y = lagop( x, b, x0, t0, t1 )

Input
-----
+----+----------------------------------------------------------------+
   | x  | Nxk matrix, each of whose columns will be transformed by the   |
   |    | lag polynomial operator. Data in x are considered to be data   |
   |    | for time periods 1 to T.                                       |
   +----+----------------------------------------------------------------+
   | b  | qxk matrix, containing the coefficients of the lag polynomial  |
   |    | operators. If b has only one column, this will be used for all |
   |    | columns in x.                                                  |
   +----+----------------------------------------------------------------+
   | x0 | qxk matrix or 1x1 scalar 0, containing initial values for the  |
   |    | series. A scalar 0 is equivalent to a qxk matrix of 0's. x0 is |
   |    | considered to contain data for time periods -(q-1) to 0.       |
   +----+----------------------------------------------------------------+
   | t0 | Initial time period for the filtered series. If t0 = 0, then   |
   |    | t0 will be set to the first "legitimate" value of the series;  |
   |    | that is, if x0 is qxk and not all 0's, t0 will be set to 1; if |
   |    | x0 is scalar zero (or all 0's), t0 will be set to q + 1; 1 ≤   |
   |    | t0 ≤ T.                                                        |
   +----+----------------------------------------------------------------+
   | t1 | Final time period for the filtered series. However, ift1 = 0,  |
   |    | then t1 will be set to T. 1 ≤ t1 ; T ; t1 ≥ t0.                |
   +----+----------------------------------------------------------------+

Output
------
+---+-----------------------------------------------------------------+
   | y | lxk matrix, where l = t1 - t0 if t1 and t0 are not 0, otherwise |
   |   | l = T - q0, where T = rows(x) and q0 is either 1 or q+1, as     |
   |   | described above in the discussion of t0.                        |
   +---+-----------------------------------------------------------------+

Remarks
-------
This proc calls conv. The basic call is:  conv(1 \| -b, x, t0, t1); 
   Most of the code in this proc computes the correct x, t0, and t1 to
   be passed to conv. Since there is a certain amount of overhead
   involved in this, in some cases it could speed up computation
   substantially just to make a direct call to conv.

Source
------
autregmt.src
