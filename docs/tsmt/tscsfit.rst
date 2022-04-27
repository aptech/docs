tscsFit
=======

Purpose
-------
Estimates the parameters of the pooled time-series cross-section regression model.

Format
------
.. function:: tso = tscsFit(y, x, grp[, tsc])
              tso = tscsFit(dataset, formula, grp[, tsc])

   :param y: data.
   :type y: Nx1 vector

   :param dataset: name of data set or null string.
   :type dataset: string

   :param formula: formula string of the model. E.g. ``"y ~ X1 + X2"`` 'y' is the name of dependent variable, '``X1``' and '``X2``' are names of independent variables; E.g. ``"y ~ ."``, '.' means including all variables except dependent variable 'y';
   :type formula: string

   :param grp: NTx1 of group identifiers.
   :type grp: Matrix

   :param tsc: Optional input. Instance of a tscsmtControl structure. The following members of tsc are referenced within this routine:

      .. list-table::
         :widths: auto

         * - tsc.header
           - string, specifies the format for the output header. tsc.header can contain zero or more of the following characters: 

             .. list-table::
                :widths: auto

                * - t
                  - title is to be printed. 
                * - l
                  - lines are to bracket the title. 
                * - d
                  - a date and time is to be printed. 
                * - v
                  - version number of program is to be printed 
                * - f
                  - file name being analyzed is to be printed

             Example: 
              
             ::
                 
               tsc.header = "tld";
                 
             If :code:`tsc.header = ""`, no header is printed. Default = "tldvf".

         * - tsc.ise
           - scalar. If 1, the ind ividual-specific effects are not printed. Default = 0. 
         * - tsc.output
           - scalar, if nonzero, results are printed to screen. Default = 1. 
         * - tsc.meth
           - scalar, Possible values are: Default = 0.

             :0: Uses the fixed effects estimates of the ind ividual-specific effects to estimate the variance components of the random effects model. Us:e: this option if there are a different number of observations for each cross-sectional unit. Th:e: chi-squared test for the individual error components equal to 0 may not be correct if there are a different number of observations for each individual.
             :1: Uses regression on group means to estimate variance components. 

             Default = 0.

         * - tsc.mnsfn
           - string, the name of a file in which to save the group means of the dataset. By default, tsc.mnsfn = "", so the means are not saved. 
         * - tsc.model
           - scalar, controls the type of models to be estimated. Possible values are: 

             :0: All models are estimated. 
             :1: The random effects (error components model) is not estimated.

         * - tsc.rowfac
           - scalar, "row factor." If tscsFit fails due to insufficient memory while attempting to read a GAUSS dataset, tsc.rowfac may be set 
             to some value between 0 and 1 to read a *proportion* of the original number of rows of the GAUSS dataset. For example, setting 
             
             :: 
                
                tsc.rowfac = 0.8;
                
             causes GAUSS to read in 80% of the rows of the GAUSS dataset that were read when the failure due to insufficient memory occurred. 
             tsc.rowfac has an effect only when tsc.row = 0.
             
             Default = 1.

         * - tsc.stnd
           - scalar. If 1, print standardized estimates of regression parameters. Default = 1. 
         * - tsc.title
           - string, a title to be printed at the top of the output header (see tsc.header). By default, no title is printed (tsc.title = ""). 


   :type tsc: struct

   :return tso: An instance of a :class:`tscsFitOut` structure containing the following members:

      .. list-table::
         :widths: auto

         * - tso.bdv
           - Kx1 vector, regression coefficients from the dummy effects model (excluding individual-variables regression model). 
         * - tso.vcdv
           - KxK matrix, variance-covariance matrix of the dummy variables regression model. 
         * - tso.mdv
           - (K+1)x(K+1) matrix, moment matrix of the transformed variables (including a constant) from the dummy variables regression model. 
         * - tso.bec
           - Kx1 vector, regression coefficients from the random effects regression model. 
         * - tso.vcec
           - KxK matrix, variance-covariance matrix of the random effects regression model.. 
         * - tso.mec
           - (K+1)x(K+1) matrix, moment matrix of the transformed variables (including a constant) from the random effects regression model. 
         * - tso.fixedEffects
           - matrix, fixed effects dummy variable estimates. 
         * - tso.sefixedEffects
           - matrix, standard error of fixed effects dummy variable estimates. 
         * - tso.randomEffects
           - matrix, estimated of random effects. 
         * - tso.y_hat_dv
           - matrix, fixed effects model estimated dependent variable. 
         * - tso.y_hat_ec
           - matrix, random effects model estimated dependent variable. 
         * - tso.res_dv
           - matrix, fixed effects model residuals. 
         * - tso.res_ec
           - matrix, random model effects residuals. 

   :rtype tso: struct

Examples
--------

Formula String
+++++++++++++++

::

   new;
   cls,;
   library tsmt;

   //Declare tscsmt output structure
   struct tscsmtOut tso;

   //Estimate model
   tso = tscsFit( getGAUSSHome() $+ "pkgs/tsmt/examples/grunfeld.dat", "investment~firm_value + capital", "firm");

Data Matrices
+++++++++++++

::

   new;
   cls;
   library tsmt;
     
   //Load data from dataset
   data=loadd(getGAUSSHome() $+ "pkgs/tsmt/examples/munnell");

   //Independent variable
   y = data[., 2];

   //Dependent variable
   x = data[., 3:6];

   //Group variable
   grp = data[.,1];
     
   //Declare tscsmt output structure
   struct tscsmtOut tso;

   //Estimate model
   tso = tscsFit(y, x, grp);

Remarks
-------
The panel data must be contained in a stacked panel GAUSS dataset,
with one variable containing an index for the units. From each
cross-sectional unit all observations must be grouped together. For
example, for the first cross-sectional unit there may be 10 rows in
the dataset, for the second cross-sectional unit there may be another
10 rows, and so on. Each row in the dataset contains measurements on
the endogenous and exogenous variables measured for each observation
along with the index identifying the cross-sectional unit.

The index variable must be a series of integers. While all
observations for each cross-sectional unit must be grouped together,
they do not have to be sorted according to the index.

Library
-------
tsmt

Source
------
tscsmt.src
