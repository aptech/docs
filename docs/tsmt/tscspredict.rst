===========
tscsPredict
===========

10.0.60tscsPredict
==================

Purpose
-------

.. container::
   :name: Purpose

   Estimates forecasts using estimation results obtained from tscsFit.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   f = tscsPredict( tso, y, x, grp );

Input
-----

.. container::
   :name: Input

   === ====================================
   tso Instance of the tscsmtOut structure.  
   y   N×1 vector, dependent data.           
   x   N×1 vector, independent data          
   grp Matrix, NTx1 of group identifiers.    
   === ====================================

Output
------

.. container::
   :name: Output

   +-----+----------------------------+----------------------------+---+
   | tso | Instance of the tscsmtOut  |                            |   |
   |     | structure with the         |                            |   |
   |     | following members filled:  |                            |   |
   +-----+----------------------------+----------------------------+---+
   |     | tso.y_hat_dv               | matrix, fixed effects      |   |
   |     |                            | model estimated dependent  |   |
   |     |                            | variable.                  |   |
   +-----+----------------------------+----------------------------+---+
   |     | tso.y_hat_ec               | matrix, random effects     |   |
   |     |                            | model estimated dependent  |   |
   |     |                            | variable.                  |   |
   +-----+----------------------------+----------------------------+---+
   |     | tso.res_dv                 | matrix, fixed effects      |   |
   |     |                            | model residuals.           |   |
   +-----+----------------------------+----------------------------+---+
   |     | tso.res_ec                 | matrix, random model       |   |
   |     |                            | effects residuals.         |   |
   +-----+----------------------------+----------------------------+---+

Remarks
-------

.. container::
   :name: Remarks

   tscsPredict is run as part of the tscsFit procedure.

Source
------

.. container:: gfunc
   :name: Source

   tscsmt.src
