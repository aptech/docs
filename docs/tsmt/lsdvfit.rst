=======
lsdvFit
=======

10.0.34lsdvFit
==============

Purpose
-------

.. container::
   :name: Purpose

   Estimates coefficients of a regression model with autoregressive
   errors of any specified order.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   lout1 = lsdvFit(y, x, series_length, n_lags);
   lout1 = lsdvFit(y, x, series_length, n_lags, lsc);
   lout1 = lsdvFit(dataset, formula, series_length, n_lags);
   lout1 = lsdvFit(dataset, formula, series_length, n_lags, lsc);

Input
-----

.. container::
   :name: Input

   +---------------+-----------------------+-----------------------+---+
   | y             | N×1 vector, data.     |                       |   |
   +---------------+-----------------------+-----------------------+---+
   | x             | N×k vector,           |                       |   |
   |               | independent data.     |                       |   |
   +---------------+-----------------------+-----------------------+---+
   | dataset       | string, name of data  |                       |   |
   |               | set or null string.   |                       |   |
   +---------------+-----------------------+-----------------------+---+
   | formula       | string, formula       |                       |   |
   |               | string of the model.  |                       |   |
   |               | E.g. "y ~ X1 + X2"    |                       |   |
   |               | 'y' is the name of    |                       |   |
   |               | dependent variable,   |                       |   |
   |               | 'X1' and 'X2' are     |                       |   |
   |               | names of independent  |                       |   |
   |               | variables;            |                       |   |
   |               | E.g. "y ~ ." , '.'    |                       |   |
   |               | means including all   |                       |   |
   |               | variables except      |                       |   |
   |               | dependent variable    |                       |   |
   |               | 'y';                  |                       |   |
   +---------------+-----------------------+-----------------------+---+
   | series_length | scalar, number of     |                       |   |
   |               | time periods for each |                       |   |
   |               | case or instance.     |                       |   |
   +---------------+-----------------------+-----------------------+---+
   | num_lags      | scalar, number of     |                       |   |
   |               | lagged values of the  |                       |   |
   |               | dependent variable.   |                       |   |
   +---------------+-----------------------+-----------------------+---+
   | lsc           | Optional input, an    |                       |   |
   |               | instance of a         |                       |   |
   |               | lsdvmtControl         |                       |   |
   |               | structure. The        |                       |   |
   |               | following members of  |                       |   |
   |               | lsc are referenced    |                       |   |
   |               | within this routine:  |                       |   |
   +---------------+-----------------------+-----------------------+---+
   |               | lsc.Constrain         | scalar, if nonzero    |   |
   |               |                       | constraints will be   |   |
   |               |                       | applied to the        |   |
   |               |                       | autoregression        |   |
   |               |                       | coefficients.         |   |
   |               |                       | Default = 1.          |   |
   +---------------+-----------------------+-----------------------+---+
   |               | lsc.scale             | scalar, if nonzero,   |   |
   |               |                       | data are scaled.      |   |
   +---------------+-----------------------+-----------------------+---+
   |               | lsc.output            | scalar, determines    |   |
   |               |                       | the output to be      |   |
   |               |                       | printed.              |   |
   +---------------+-----------------------+-----------------------+---+
   |               | lsc.title             | string, title to be   |   |
   |               |                       | printed at top of     |   |
   |               |                       | header.               |   |
   +---------------+-----------------------+-----------------------+---+

Output
------

.. container::
   :name: Output

   +-----+------------------------------+------------------------------+
   | out | An instance of an            |                              |
   |     | lsdvOutstructure. The        |                              |
   |     | following members of out are |                              |
   |     | referenced within this       |                              |
   |     | routine:                     |                              |
   +-----+------------------------------+------------------------------+
   |     | autoCoefficients             | J×1 vector, uncorrected      |
   |     |                              | autoregression coefficients. |
   +-----+------------------------------+------------------------------+
   |     | regCoefficients              | K×1 vector, uncorrected      |
   |     |                              | regression coefficients.     |
   +-----+------------------------------+------------------------------+
   |     | autoCoefficientsCorr         | J×1 vector, bias corrected   |
   |     |                              | autoregression coefficients. |
   +-----+------------------------------+------------------------------+
   |     | regCoefficientsCorr          | K×1 vector, bias corrected   |
   |     |                              | regression coefficients.     |
   +-----+------------------------------+------------------------------+
   |     | autoStderrs                  | J×1 vector, autoregression   |
   |     |                              | coefficient standard errors. |
   +-----+------------------------------+------------------------------+
   |     | regStderrs                   | K×1 vector, regression       |
   |     |                              | coefficient standard errors. |
   +-----+------------------------------+------------------------------+
   |     | covPar                       | K×K matrix, covariance       |
   |     |                              | matrix of parameters         |
   +-----+------------------------------+------------------------------+
   |     | SSresidual                   | scalar, residual sums of     |
   |     |                              | squares.                     |
   +-----+------------------------------+------------------------------+
   |     | SStotal                      | scalar, total sums of        |
   |     |                              | squares.                     |
   +-----+------------------------------+------------------------------+
   |     | SSexplained                  | scalar, explained sums of    |
   |     |                              | squares.                     |
   +-----+------------------------------+------------------------------+
   |     | SSpooledResidual             | scalar, pooled residual sums |
   |     |                              | of squares.                  |
   +-----+------------------------------+------------------------------+
   |     | biasCorr                     | K+J×1 vector, bias           |
   |     |                              | corrections.                 |
   +-----+------------------------------+------------------------------+
   |     | lagrange                     | J×2 matrix, Lagrangeans for  |
   |     |                              | constraints.                 |
   +-----+------------------------------+------------------------------+
   |     | numCases                     | scalar, number of cases.     |
   +-----+------------------------------+------------------------------+
   |     | numMissing                   | scalar, number of            |
   |     |                              | observations with missing    |
   |     |                              | data.                        |
   +-----+------------------------------+------------------------------+
   |     | numDF                        | scalar, number of degrees of |
   |     |                              | freedom.                     |
   +-----+------------------------------+------------------------------+
   |     | numObservations              | scalar, number of            |
   |     |                              | observations.                |
   +-----+------------------------------+------------------------------+
   |     | numParameters                | scalar, number of            |
   |     |                              | parameters.                  |
   +-----+------------------------------+------------------------------+
   |     | numPeriods                   | scalar, number of periods in |
   |     |                              | time series.                 |
   +-----+------------------------------+------------------------------+

Remarks
-------

.. container::
   :name: Remarks

   The data must be contained in a GAUSS dataset cross-sectional unit by
   cross-sectional unit, with one variable containing an index for the
   units. From each cross-sectional unit all observations must be
   grouped together. For example, for the first cross-sectional unit
   there may be 10 rows in the dataset, for the second cross-sectional
   unit there may be another 10 rows, and so on. Each row in the dataset
   contains measurements on the endogenous and exogenous variables
   measured for each observation along with the index identifying the
   cross-sectional unit.

   The index variable must be a series of integers. While all
   observations for each cross-sectional unit must be grouped together,
   they do not have to be sorted according to the index.

Example
-------

.. container::
   :name: Example

   **Example One: Dataset and formula**
   ::

      new;
      library tsmt;
                    
      //Declare lsdvmt control structure
      struct lsdvmtControl c0;
      c0 = lsdvmtControlCreate();             

      //Turn screen output on 
      c0.output = 1;              

      //Scale data before running 
      c0.scale = 0;

       //Declare output structure                                                        
      struct lsdvmtOut out;

      //Call lsdvmt function 
      out = lsdvFit(getGAUSSHome() $+ "pkgs/tsmt/examples/lsdv.dat", "Y~X1+X2+X3", 50, 2, c0);

   **Example Two: Data matrices**
   ::

      new;
      library tsmt;

      //Load data
      data = loadd( getGAUSSHome() $+ "pkgs/tsmt/examples/lsdv.dat");

      //Dependent variable
      y = data[., 1];

      //Independent variable
      x = data[., 2:4];
        
      //Declare lsdvmt control structure
      struct lsdvmtControl c0;
      c0 = lsdvmtControlCreate();             

      //Turn screen output on 
      c0.output = 1;              

      //Scale data before running 
      c0.scale = 0;

       //Declare output structure                                                        
      struct lsdvmtOut out;

      //Call lsdvmt function 
      out = lsdvFit(y, x, 50, 2, c0);

Source
------

.. container:: gfunc
   :name: Source

   lsdvmt.src
