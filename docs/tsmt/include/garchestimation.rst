.. list-table::
   :widths: auto

   * - gout.aic
     - scalar, Akiake criterion.
   * - gout.bic
     - scalar, Bayesian information criterion.
   * - gout.lrs
     - scalar, likelihood ratio statistic.
   * - gout.numObs
     - scalar, number of observations.
   * - gout.df
     - scalar, degrees of freedom.
   * - gout.par
     - instance of PV structure containing parameter estimates.
   * - gout.retcode
     - scalar, return code:

       =========== =================================================================================
       1           Normal convergence.
       2           Forced exit.
       3           Function calculation failed.
       4           Gradient calculation failed.
       5           Hessian calculation failed.
       6           Line search failed.
       7           Error with constraints.
       8           Function complex.
       =========== =================================================================================

   * - gout.moment
     - KxK matrix, moment matrix of parameter estimates.
   * - gout.climits
     - Kx2 matrix, confidence limits.
   * - gout.tsmtDesc
     - An instance of the :class:`tsmtModelDesc` structure containing the following members:
       
       .. include:: include/tsmtmodeldesc.rst

   * - gout.sumStats 
     - An instance of the :class:`tsmtSummaryStats` structure containing the following members:
       
       .. include:: include/tsmtsummarystats.rst
