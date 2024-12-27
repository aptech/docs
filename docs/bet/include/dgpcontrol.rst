        .. list-table:: 
           :widths: auto

           * - model
             - String, specifies model type. Must be one of the following GAUSS supported model specifications:
               
               - "Linear" - Univariate or multivariate linear model.
               - "Auto" - Univariate linear model with autoregressive error terms.
               - "HB" - Hierarchical bayes estimation.
               - "Probit" - Binary choice probit model.
               - "Logit" - Binary choice logit model.
           * - numObs
             - Scalar, number of observations to be generated per subject.
           * - numSubjects, NTot
             - Scalar, total number of subjects and total number of observations, respectively.
           * - numMix
             - Scalar, number of mixing components.
           * - trueBeta
             - Matrix, numX x numY, true beta coefficients for linear dependency.
           * - trueSigma
             - Matrix, numX x numY, true standard deviation of error terms.
           * - trueLambda
             - Matrix, numX x numX, upper triangular matrix for HB model standard deviation of coefficients in stage one equation.
           * - trueTheta
             - Matrix, numZ x numX, HB linear dependency coefficients in stage one equation.
           * - Member
             - Description
           * - trueInterceptX
             - Scalar, intercept value for all x equations.
           * - trueTrendX
             - Scalar, coefficient on linear trend in x equation. 
           * - trueInterceptZ 
             - Scalar, intercept value for all z equations.
           * - trueTrendZ
             - Scalar, coefficient on linear trend in z equation. 
