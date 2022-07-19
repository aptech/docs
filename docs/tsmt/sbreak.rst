sbreak
======

Purpose
-------
Estimates the m-break structural break model.

Format
------
.. function:: out = sbreak(yt, xt, zt, sbc0)

   :param yt: dependent data.
   :type yt: Matrix

   :param xt: time invariant independent variables.
   :type xt: Matrix

   :param zt: time variant independent variables.
   :type zt: Matrix

   :param sbc0: Instance of :class:`sbControl` structure containing the following elements:

      .. list-table::
         :widths: auto

         * - q
           - Scalar, number of regressors subject to change.
         * - p
           - Scalar, number of time invariant regressors in x.
         * - m
           - Scalar, maximum number of structural changes.
         * - trim
           - Scalar, trimming value (as a decimal).
         * - h
           - Scalar, minimal length of segment (h > p + q)
         * - initialBeta
           - Matrix, if initialBeta == {} call function to set initial values
         * - maxIters
           - maximum number of iterations
         * - printOutput
           - Indicator to print iteration outputs
         * - eps
           - Scalar, convergence criterion

   :type sbc0: struct

   :return out: Instance of the :class:`sbOut` structure containing the following elements:

      .. list-table::
         :widths: auto

         * - breakDate
           - Matrix, MxM of date breaks estimated for possible number of breaks less than or equal to m.
         * - breakSSR
           - MxM, vector of ssr associated with all number of breaks less than or equal to m.

   :rtype out: struct


Examples
--------

::

   new;
   cls;
   library tsmt;

   // DATA INPUT
   // Load y data
   y = loadd( getGAUSSHome() $+ "pkgs/tsmt/examples/real_intrate.dat", "." );

   // Specify regressors
   // Time varying coe ficients in z
   z = ones( rows(y), 1 );

   // No time invariant regressors
   x = 0;

   // Declare sbControl structure
   struct sbControl sbc0;

   // Initialize instance of structure
   sbc0 = sbControlCreate( );

   // Set individual model parameters
   sbc0.q = 1;
   sbc0.m = 5;
   sbc0.trim = 0.15;
   sbc0.h = 0;
   sbc0.printOutput = 1;
   sbc0.initialBeta = 0.5;
   sbc0.maxIters = 40;

   // Turn on graphing capability
   sbc0.graphOn = 1;
   sbc0.dtstart = dtdate( 1961, 01, 01, 0, 00, 00 );
   sbc0.frequency = 4;

   struct sbOut sbcOut;
   sbcOut = sbreak( y, z, x, sbc0 );

References
----------
Bai, J and Perron, P. (2003) Computation and analysis of multiple structural change models, Journal of Applied Econometrics,18(1),1-22.

Library
-------
tsmt

Source
------
sb.src
