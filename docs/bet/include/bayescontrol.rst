
.. list-table::
   :widths: auto

   * - MCCtl0.model
     - String, specifies model type. Must be one of the following GAUSS supported model specifications:
       
       - "Linear" - Univariate or multivariate linear model.
       - "Auto" - Univariate linear model with autoregressive error terms.
       - "HB" - Hierarchical bayes estimation
       - "Probit" - Binary choice probit model
       - "Logit" - Binary choice logit model
   * - MCCtl0.savedIter
     - Scalar, number of sampler iterations to be saved
   * - MCCtl0.saveSkip
     - Scalar, number of sampler iterations to skip between saving iterations
   * - MCCtl0.burnIter
     - Scalar, number of sampler burn-in iterations
   * - MCCtl0.MLE
     - Scalar, indicator parameter set to one to use MLE to find initial values
   * - MCCtl0.printOut
     - Scalar, indicator parameter set to one to print output details to screen
   * - MCCtl0.graphOut
     - Scalar, indicator parameter set to one to produce post sampler graphs of posterior
   * - MCCtl0.Intercept
     - Scalar, parameter indicating deterministic trends to include in the model:
       
       - 0 for deterministic trends
       - 1 for intercept only
       - 2 for trend and intercept
       - 3 for trend only
   * - MCCtl0.numX
     - Scalar, number of dependent variables, when relevant.
   * - MCCtl0.numZ
     - Scalar, number of first stage Z dependent variables, when relevant.
   * - MCCtl0.numLags
     - Scalar, number of autoregressive lags, when relevant.
   * - MCCtl0.numMix
     - Scalar, number of mixtures components, when relevant.
   * - MCCtl0.numSubjects
     - Scalar, number of subjects, when relevant.
