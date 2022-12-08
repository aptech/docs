===========
tscsPredict
===========

10.0.60tscsPredict
==================

Purpose
-------
Estimates forecasts using estimation results obtained from tscsFit.

Library
-------
tsmt

Format
------
f = tscsPredict( tso, y, x, grp );

Input
-----
=== ====================================
tso Instance of the tscsmtOut structure.  
y   Nx1 vector, dependent data.           
x   Nx1 vector, independent data          
grp Matrix, NTx1 of group identifiers.    
=== ====================================

Output
------
+-----+----------------------------+----------------------------+---+
| tso | Instance of the tscsmtOut  |                            |   |
|     | structure with the         |                            |   |
|     | following members filled:  |                            |   |
+-----+----------------------------+----------------------------+---+
|     | tso.y_hat_dv               | matrix, fixed effects      |   |
|     |                            | model estimated dependent  |   |
|     |                            | variable.                  |   |
+-----+----------------------------+----------------------------+---+
|     | tso.y_hat_ec               | matrix, random effects     |   |
|     |                            | model estimated dependent  |   |
|     |                            | variable.                  |   |
+-----+----------------------------+----------------------------+---+
|     | tso.res_dv                 | matrix, fixed effects      |   |
|     |                            | model residuals.           |   |
+-----+----------------------------+----------------------------+---+
|     | tso.res_ec                 | matrix, random model       |   |
|     |                            | effects residuals.         |   |
+-----+----------------------------+----------------------------+---+

Remarks
-------
tscsPredict is run as part of the tscsFit procedure.

Source
------
tscsmt.src
