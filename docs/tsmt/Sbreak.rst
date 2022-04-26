======
sbreak
======

10.0.49sbreak
=============

Purpose
-------

.. container::
   :name: Purpose

   Estimates the m-break structural break model.model.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   sbout = sbreak( yt, xt, zt, sbc0 );

Input
-----

.. container::
   :name: Input

   +------+---------------------------+---------------------------+---+
   | yt   | Matrix, dependent data.   |                           |   |
   +------+---------------------------+---------------------------+---+
   | xt   | Matrix, time invariant    |                           |   |
   |      | independent variables.    |                           |   |
   +------+---------------------------+---------------------------+---+
   | zt   | Matrix, time variant      |                           |   |
   |      | independent variables.    |                           |   |
   +------+---------------------------+---------------------------+---+
   | sbc0 | Instance of thesbControl  |                           |   |
   |      | structure containing the  |                           |   |
   |      | following elements:       |                           |   |
   +------+---------------------------+---------------------------+---+
   |      | q                         | Scalar,number of          |   |
   |      |                           | regressors subject to     |   |
   |      |                           | change.                   |   |
   +------+---------------------------+---------------------------+---+
   |      | p                         | Scalar, number of time    |   |
   |      |                           | invariant regressors in   |   |
   |      |                           | x.                        |   |
   +------+---------------------------+---------------------------+---+
   |      | m                         | Scalar, maximum number of |   |
   |      |                           | structural changes.       |   |
   +------+---------------------------+---------------------------+---+
   |      | trim                      | Scalar, trimming value    |   |
   |      |                           | (as a decimal).           |   |
   +------+---------------------------+---------------------------+---+
   |      | h                         | Scalar, minimal length of |   |
   |      |                           | segment (h > p + q)       |   |
   +------+---------------------------+---------------------------+---+
   |      | initialBeta               | Matrix, if initialBeta == |   |
   |      |                           | {} call function to set   |   |
   |      |                           | initial values            |   |
   +------+---------------------------+---------------------------+---+
   |      | maxIters                  | maximum number of         |   |
   |      |                           | iterations                |   |
   +------+---------------------------+---------------------------+---+
   |      | printOutput               | Indicator to print        |   |
   |      |                           | iteration outputs         |   |
   +------+---------------------------+---------------------------+---+
   |      | eps                       | Scalar, convergence       |   |
   |      |                           | criterion                 |   |
   +------+---------------------------+---------------------------+---+

Output
------

.. container::
   :name: Output

   +-------+-----------------------------+-----------------------------+
   | sbOut | Instance of the sbOut       |                             |
   |       | structure containing the    |                             |
   |       | following elements:         |                             |
   +-------+-----------------------------+-----------------------------+
   |       | breakDate                   | Matrix, MxM of date breaks  |
   |       |                             | estimated for possible      |
   |       |                             | number of breaks less than  |
   |       |                             | or equal to m.              |
   +-------+-----------------------------+-----------------------------+
   |       | breakSSR                    | MxM, vector of ssr          |
   |       |                             | associated with all number  |
   |       |                             | of breaks less than or      |
   |       |                             | equal to m.                 |
   +-------+-----------------------------+-----------------------------+

Example
-------

.. container::
   :name: Example

   ::

      new;
      cls;
      library tsmt;

      //DATA INPUT
      //Load y data 
      y = loadd( getGAUSSHome() $+ "pkgs/tsmt/examples/real_intrate.dat", "." );

      //Specify regressors 
      //Time varying coefficients in z
      z = ones( rows(y), 1 );

      //No time invariant regressors
      x = 0;

      //Declare sbControl structure
      struct sbControl sbc0;

      //Initialize instance of structure
      sbc0 = sbControlCreate( );

      //Set individual model parameters
      sbc0.q = 1;                         
      sbc0.m = 5;                        
      sbc0.trim = 0.15;  
      sbc0.h = 0;   
      sbc0.printOutput = 1;
      sbc0.initialBeta = 0.5;
      sbc0.maxIters = 40;

      //Turn on graphing capability
      sbc0.graphOn = 1;
      sbc0.dtstart = dtdate( 1961, 01, 01, 0, 00, 00 );
      sbc0.frequency = 4;

      struct sbOut sbc0ut;
      sbc0ut = sbreak( y, z, x, sbc0 );

References
----------

.. container::
   :name: Reference

   Bai, J and Perron, P. (2003) Computation and analysis of multiple
   structural change models, Journal of Applied Econometrics,18(1),
   1-22.

Source
------

.. container:: gfunc
   :name: Source

   sb.src
