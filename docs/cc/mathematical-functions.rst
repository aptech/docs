
Mathematical functions
===========================

Scientific functions
--------------------------------------------

=====================       ===========================================
:doc:`abs`                  Returns absolute value of argument.
:doc:`arccos`               Computes inverse cosine.
:doc:`arcsin`               Computes inverse sine.
:doc:`atan`                 Computes inverse tangent.
:doc:`atan2`                Computes angle given a point x,y.
:doc:`besselj`              Computes Bessel function, first kind.
:doc:`besselk`              Computes the modified Bessel function of the second kind, :math:`K_n(x)`.
:doc:`bessely`              Computes Bessel function, second kind.
:doc:`beta`                 Computes the complete Beta function, also called the Euler integral.
:doc:`boxcox`               Computes the Box-Cox function.
:doc:`cos`                  Computes cosine.
:doc:`cosh`                 Computes hyperbolic cosine.
:doc:`curve`                Computes a one-dimensional smoothing curve.
:doc:`digamma`              Computes the digamma function.
:doc:`exp`                  Computes the exponential function of x.
:doc:`fmod`                 Computes the floating-point remainder of x/y.
:doc:`gamma`                Computes gamma function value.
:doc:`gammacplx`            Computes gamma function for complex inputs.
:doc:`gammaii`              Compute the inverse incomplete gamma function.
:doc:`ln`                   Computes the natural log of each element.
:doc:`lnfact`               Computes natural log of factorial function.
:doc:`lngamma`              Computes the natural log of the gamma function.
:doc:`log`                  Computes the log (base 10) of each element.
:doc:`mbesseli`             Computes modified and exponentially scaled modified Bessels of the first kind of the nth order.
:doc:`pi`                   Returns :math:`\pi`.
:doc:`polygamma`            Computes the polygamma function of order n.
:doc:`psi`                  Computes the psi (or digamma) function.
:doc:`sin`                  Computes sine.
:doc:`sinh`                 Computes the hyperbolic sine.
:doc:`spline`               Computes a two-dimensional interpolatory spline.
:doc:`sqrt`                 Computes the square root of each element.
:doc:`tan`                  Computes tangent.
:doc:`tanh`                 Computes hyperbolic tangent.
:doc:`tocart`               Converts from polar to Cartesian coordinates.
:doc:`topolar`              Converts from Cartesian to polar coordinates.
:doc:`trigamma`             Computes trigamma function.
:doc:`zeta`                 Computes the Rieman zeta function.
=====================       ===========================================

Differentiation and Integration
--------------------------------------------

=====================          ===========================================
:doc:`gradp`                   Computes first derivative of a function; gradcplx allows for complex arguments.
:doc:`hessp`                   Computes second derivative of a function; hesscplx allows for complex arguments.
:doc:`integrate1d`             Integrates a user-defined function over a user-defined range, using adaptive quadrature.
:doc:`intgrat2`                Integrates a 2-dimensional function over an user-defined region.
:doc:`intgrat3`                Integrates a 3-dimensional function over an user-defined region.
:doc:`intquad1`                Integrates a 1-dimensional function.
:doc:`intquad2`                Integrates a 2-dimensional function over an user-defined rectangular region.
:doc:`intquad3`                Integrates a 3-dimensional function over an user-defined rectangular region.
:doc:`intsimp`                 Integrates by Simpson's method.
=====================          ===========================================

The following are differentiation functions with advanced options.

=====================          ===========================================
:doc:`gradMTm`                 Computes numerical gradient with mask.
:doc:`gradMTT`                 Computes numerical gradient using available threads.
:doc:`gradMTTm`                Computes numerical gradient with mask using available threads.
:doc:`gradcplx`                Computes first derivative of a function with complex arguments.
:doc:`hessMTg`                 Computes numerical Hessian using gradient procedure.
:doc:`hessMTgw`                Computes numerical Hessian using gradient procedure with weights.
:doc:`hessMTm`                 Computes numerical Hessian with mask.
:doc:`hessMTmw`                Computes numerical Hessian with mask and weights.
:doc:`hessMTT`                 Computes numerical Hessian using available threads.
:doc:`hessMTTg`                Computes numerical Hessian using gradient procedure with available threads.
:doc:`hessMTTgw`               Computes numerical Hessian using gradient procedure with weights and using available threads.
:doc:`hessMTTm`                Computes numerical Hessian with mask and available threads.
:doc:`hessMTw`                 Computes numerical Hessian with weights.
:doc:`hesscplx`                Computes second derivative of a function with complex arguments.
=====================          ===========================================


Linear Algebra
--------------------------------------------

=====================          ===========================================
:doc:`balance`                 Balances a matrix.
:doc:`band`                    Extracts bands from a symmetric banded matrix.
:doc:`bandchol`                Computes the Cholesky decomposition of a positive definite banded matrix.
:doc:`bandcholsol`             Solves the system of equations :math:`Ax = b` for x, given the lower triangle of the Cholesky decomposition of a positive definite banded matrix A.
:doc:`bandltsol`               Solves the system of equations :math:`Ax = b` for x, where A is a lower triangular banded matrix
:doc:`bandrv`                  Creates a symmetric banded matrix, given its compact form.
:doc:`bandsolpd`               Solves the system of equations :math:`Ax = b` for x, where A is a positive definite banded matrix.
:doc:`blockDiag`               Creates a block-diagonal matrix from one or more input matrices
:doc:`chol`                    Computes Cholesky decomposition, :math:`X=U'U`.
:doc:`choldn`                  Performs Cholesky downdate on an upper triangular matrix.
:doc:`cholsol`                 Solves a system of equations given the Cholesky factorization of a matrix.
:doc:`cholup`                  Performs Cholesky update on an upper triangular matrix.
:doc:`cond`                    Computes condition number of a matrix.
:doc:`crout`                   Computes Crout decomposition, :math:`X = LU` (real matrices only).
:doc:`croutp`                  Computes Crout decomposition with row pivoting (real matrices only).
:doc:`det`                     Computes determinant of square matrix.
:doc:`detl`                    Computes determinant of decomposed matrix.
:doc:`dot`                     Returns a scalar dot product of the columns of two matrices.
:doc:`hess`                    Computes upper Hessenberg form of a matrix (real matrices only).
:doc:`inv`                     Inverts a matrix.
:doc:`invpd`                   Inverts a positive definite matrix.
:doc:`invswp`                  Computes a generalized sweep inverse.
:doc:`lapeighb`                Computes eigenvalues only of a real symmetric or complex Hermitian matrix selected by bounds.
:doc:`lapeighi`                Computes eigenvalues only of a real symmetric or complex Hermitian matrix selected by index.
:doc:`lapeighvb`               Computes eigenvalues and eigenvectors of a real symmetric or complex Hermitian matrix selected by bounds.
:doc:`lapeighvi`               Computes selected eigenvalues and eigenvectors of a real symmetric or complex Hermitian matrix.
:doc:`lapgeig`                 Computes generalized eigenvalues for a pair of real or complex general matrices.
:doc:`lapgeigh`                Computes generalized eigenvalues for a pair of real symmetric or Hermitian matrices.
:doc:`lapgeighv`               Computes generalized eigenvalues and eigenvectors for a pair of real symmetric or Hermitian matrices.
:doc:`lapgeigv`                Computes generalized eigenvalues, left eigenvectors, and right eigenvectors for a pair of real or complex general matrices.
:doc:`lapgschur`               Computes the generalized Schur form of a pair of real or complex general matrices.
:doc:`lapgsvdcst`              Computes the generalized singular value decomposition of a pair of real or complex general matrices.
:doc:`lapgsvds`                Computes the generalized singular value decomposition of a pair of real or complex general matrices.
:doc:`lapgsvdst`               Computes the generalized singular value decomposition of a pair of real or complex general matrices.
:doc:`lapsvdcusv`              Computes the singular value decomposition a real or complex rectangular matrix, returns compact u and v.
:doc:`lapsvds`                 Computes the singular values of a real or complex rectangular matrix.
:doc:`lapsvdusv`               Computes the singular value decomposition a real or complex rectangular matrix.
:doc:`ldl`                     Computes the L and D factors of the LDL factorization of a real symmetric matrix.
:doc:`ldlp`                    Computes LDL decomposition with row pivoting of a symmetric matrix.
:doc:`ldlsol`                  Computes Solves the system of equations :math:`LDLTx = b` using a matrix factorized by :doc:`ldlp`.
:doc:`lu`                      Computes LU decomposition with row pivoting (real and complex matrices).
:doc:`lusol`                   Computes Solves the system of equations :math:`LUx = b`.
:doc:`norm`                    Computes one of several specified matrix norms, or a vector p-norm.
:doc:`null`                    Computes orthonormal basis for right null space.
:doc:`null1`                   Computes orthonormal basis for right null space.
:doc:`orth`                    Computes orthonormal basis for column space x.
:doc:`pinv`                    Generalized pseudo-inverse: Moore-Penrose.
:doc:`pinvmt`                  Generalized pseudo-inverse: Moore-Penrose.
:doc:`powerM`                  Computes the power n of a matrix A, as the mathematical equivalent of the matrix product of n copies of A.
:doc:`qqr`                     QR decomposition: returns Q1 and R.
:doc:`qqre`                    QR decomposition: returns Q1, R and a permutation vector, E.
:doc:`qqrep`                   QR decomposition with pivot control: returns Q1, R, and E.
:doc:`qr`                      QR decomposition: returns R.
:doc:`qre`                     QR decomposition: returns R and E.
:doc:`qrep`                    QR decomposition with pivot control: returns R and E.
:doc:`qrsol`                   Solves a system of equations R'x = b given an upper triangular matrix, typically the R matrix from a QR decomposition.
:doc:`qrtsol`                  Solves a system of equations R'x = b given an upper triangular matrix, typically the R matrix from a QR decomposition.
:doc:`qtyr`                    QR decomposition: returns Q'Y and R.
:doc:`qtyre`                   QR decomposition: returns Q'Y, R and E.
:doc:`qtyrep`                  QR decomposition with pivot control: returns Q'Y, R and E.
:doc:`qyr`                     QR decomposition: returns QY and R.
:doc:`qyre`                    QR decomposition: returns QY, R and E.
:doc:`qyrep`                   QR decomposition with pivot control: returns QY, R and E.
:doc:`qz`                      Compute the complex QZ, or generalized Schur, form of a pair of real or complex general matrices with an option to sort the eigenvalues.
:doc:`rank`                    Computes rank of a matrix.
:doc:`rref`                    Computes reduced row echelon form of a matrix.
:doc:`schtoc`                  Reduces any 2x2 blocks on the diagonal of the real Schur form of a matrix returned from schur. The transformation matrix is also updated.
:doc:`schur`                   Computes real or complex Schur decomposition of a matrix.
:doc:`solpd`                   Solves a system of positive definite linear equations.
:doc:`svd`                     Computes the singular values of a matrix.
:doc:`svd1`                    Computes singular value decomposition, :math:`X = USV'`.
:doc:`svd2`                    Computes svd1 with compact U.
:doc:`svdcusv`                 Computes the singular value decomposition of a matrix so that: :math:`X = U S V'` (compact u).
:doc:`svds`                    Computes the singular values of a matrix.
:doc:`svdusv`                  Computes the singular value decomposition of a matrix so that: :math:`X = U S V'`.
:doc:`sylvester`               Computes the solution to the Sylvester matrix equation, :math:`AX + XB = C`.
=====================          ===========================================

Eigenvalues
-----------------

=====================          ===========================================
:doc:`eig`                     Computes eigenvalues of general matrix.
:doc:`eigh`                    Computes eigenvalues of complex Hermitian or real symmetric matrix.
:doc:`eighv`                   Computes eigenvalues and eigenvectors of complex Hermitian or real symmetric matrix.
:doc:`eigv`                    Computes eigenvalues and eigenvectors of general matrix.
=====================          ===========================================

Polynomial Operations
--------------------------

=====================          ===========================================
:doc:`polychar`                Computes characteristic polynomial of a square matrix.
:doc:`polyeval`                Evaluates polynomial with given coefficients.
:doc:`polyint`                 Calculates Nth order polynomial interpolation given known point pairs.
:doc:`polymake`                Computes polynomial coefficients from roots.
:doc:`polymat`                 Returns sequence powers of a matrix.
:doc:`polymult`                Multiplies two polynomials together.
:doc:`polyroot`                Computes roots of polynomial from coefficients.
=====================          ===========================================

See also :doc:`recserrc`, :doc:`recsercp`, and :doc:`conv`.

Fourier Transforms
-----------------------

=====================          ===========================================
:doc:`dfft`                    Computes discrete 1-D FFT.
:doc:`dffti`                   Computes inverse discrete 1-D FFT.
:doc:`fft`                     Computes 1- or 2-D FFT.
:doc:`ffti`                    Computes inverse 1- or 2-D FFT.
:doc:`fftm`                    Computes multi-dimensional FFT.
:doc:`fftmi`                   Computes inverse multi-dimensional FFT.
:doc:`fftn`                    Computes 1- or 2-D FFT using prime factor algorithm.
:doc:`rfft`                    Computes real 1- or 2-D FFT.
:doc:`rffti`                   Computes inverse real 1- or 2-D FFT.
:doc:`rfftip`                  Computes inverse real 1- or 2-D FFT from packed format FFT.
:doc:`rfftn`                   Computes real 1- or 2-D FFT using prime factor algorithm.
:doc:`rfftnp`                  Computes real 1- or 2-D FFT using prime factor algorithm, returns packed format FFT.
:doc:`rfftp`                   Computes real 1- or 2-D FFT, returns packed format FFT.
=====================          ===========================================

Random Numbers
----------------

=====================          ===========================================
:doc:`rndBernoulli`            Computes random numbers with Bernoulli distribution.
:doc:`rndBeta`                 Computes random numbers with beta distribution.
:doc:`rndBinomial`             Computes binomial pseudo-random numbers with the choice of underlying random number generator.
:doc:`rndCauchy`               Computes Cauchy distributed random numbers with a choice of underlying random number generator.
:doc:`rndChiSquare`            Creates pseudo-random numbers with a chi-squared distribution, with an optional non-centrality parameter and a choice of underlying random number generator.
:doc:`rndCreateState`          Creates a new random number stream for a specified generator type from a seed value.
:doc:`rndExp`                  Computes exponentially distributed random numbers with a choice of underlying random number generator.
:doc:`rndGamma`                Computes gamma pseudo-random numbers with a choice of underlying random number generator.
:doc:`rndGeo`                  Computes geometric pseudo-random numbers with a choice of underlying random number generator.
:doc:`rndGumbel`               Computes Gumbel distributed random numbers with a choice of underlying random number generator.
:doc:`rndHyperGeo`             Computes pseudo-random numbers following a hypergeometric distribution with a choice of underlying random number generator.
:doc:`rndi`                    Returns random integers in a specified range.
:doc:`rndKMvm`                 Computes von Mises pseudo-random numbers.
:doc:`rndLaplace`              Computes Laplacian pseudo-random numbers with the choice of underlying random number generator.
:doc:`rndLogNorm`              Computes lognormal pseudo-random numbers with the choice of underlying random number generator.
:doc:`rndMVn`                  Computes multivariate normal random numbers given a covariance matrix.
:doc:`rndMVt`                  Computes multivariate Student-t random numbers given a covariance matrix.
:doc:`rndn`                    Computes normally distributed pseudo-random numbers with a choice of underlying random number generator.
:doc:`rndNegBinomial`          Computes negative binomial pseudo-random numbers with a choice of underlying random number generator.
:doc:`rndPoisson`              Computes Poisson pseudo-random numbers with a choice of underlying random number generator.
:doc:`rndRayleigh`             Computes rayleigh pseudo-random numbers with the choice of underlying random number generator.
:doc:`rndseed`                 Changes seed of the random number generator.
:doc:`rndStateSkip`            To advance a state vector by a specified number of values.
:doc:`rndu`                    Computes uniform random numbers with a choice of underlying random number generator.
:doc:`rndWeibull`              Computes Weibull pseudo-random numbers with the choice of underlying random number generator.
:doc:`rndWishart`              Computes Wishart pseudo-random matrices with the choice of underlying random number generator.
:doc:`rndWishartInv`           Computes inverse Wishart pseudo-random matrices with the choice of underlying random number generator.
=====================          ===========================================

Fuzzy Conditional Functions
-----------------------------------

=====================                    ===========================================
:doc:`dotfeq`                            Fuzzy .==
:doc:`dotfeqmt`                          Fuzzy .==
:doc:`dotfge`                            Fuzzy .>=
:doc:`dotfgemt`                          Fuzzy .>
:doc:`dotfgt`                            Fuzzy .>
:doc:`dotfgtmt`                          Fuzzy .>
:doc:`dotfle`                            Fuzzy .<=
:doc:`dotflemt`                          Fuzzy .<=
:doc:`dotflt`                            Fuzzy .<
:doc:`dotfltmt`                          Fuzzy .<
:doc:`dotfne`                            Fuzzy ./=
:doc:`dotfnemt`                          Fuzzy ./=
:doc:`feq`                               Fuzzy ==
:doc:`feqmt`                             Fuzzy ==
:doc:`fge`                               Fuzzy >=
:doc:`fgemt`                             Fuzzy >=
:doc:`fgt`                               Fuzzy >
:doc:`fgtmt`                             Fuzzy >
:doc:`fle`                               Fuzzy <=
:doc:`flemt`                             Fuzzy <=
:doc:`flt`                               Fuzzy <
:doc:`fltmt`                             Fuzzy <
:doc:`fne`                               Fuzzy /=
:doc:`fnemt`                             Fuzzy /=
=====================                    ===========================================

The mt commands use an fcmptol argument to control the tolerance used for comparison.
The non-mt commands use the global variable _fcmptol to control the tolerance used for comparison. By default, this is 1e-15. The default can be changed by editing the file fcompare.dec.

Statistical Functions
-------------------------

=====================       ===========================================
:doc:`acf`                  Computes sample autocorrelations.
:doc:`astd`                 Computes the standard deviation of the elements across one dimension of an N-dimensional array.
:doc:`astds`                Computes the 'sample' standard deviation of the elements across one dimension of an N-dimensional array.
:doc:`chiBarSquare`         Computes probability of chi-bar-square statistic.
:doc:`clusterse`            Computes the White cluster-robust standard errors.
:doc:`combinate`            Computes combinations of n things taken k at a time.
:doc:`combinated`           Writes combinations of n things taken k at a time to a GAUSS data set.
:doc:`conScore`             Computes constrained score statistic and its probability.
:doc:`conv`                 Computes convolution of two vectors.
:doc:`corrm`                Computes correlation matrix of a moment matrix.
:doc:`corrms`               Computes sample correlation matrix of a moment matrix.
:doc:`corrvc`               Computes correlation matrix from a variance- covariance matrix.
:doc:`corrx`                Computes correlation matrix.
:doc:`corrxs`               Computes sample correlation matrix.
:doc:`crossprd`             Computes cross product.
:doc:`design`               Creates a design matrix of 0's and 1's.
:doc:`dstatmt`              Computes descriptive statistics of a data set or matrix.
:doc:`dot`                  Computes a scalar dot product of the columns of two matrices.
:doc:`gdaDStat`             Computes descriptive statistics on multiple Nx1 variables in a GDA.
:doc:`gdaDStatMat`          Computes descriptive statistics on a selection of columns in a variable in a GDA.
:doc:`glm`                  Computes generalized linear regression of a matrix.
:doc:`gmmFit`               Computes generalized method of moments estimates from user specified moment function.
:doc:`gmmFitIV`             Estimate instrumental variables model using the generalized method of moments.
:doc:`loess`                Computes coefficients of locally weighted regression.
:doc:`loessmt`              Computes coefficients of locally weighted regression.
:doc:`meanc`                Computes mean value of each column of a matrix.
:doc:`median`               Computes medians of the columns of a matrix.
:doc:`moment`               Computes moment matrix (:math:`x'x`) with special handling of missing values.
:doc:`momentd`              Computes moment matrix from a data set.
:doc:`movingave`            Computes moving average of a series.
:doc:`movingaveExpwgt`      Computes exponentially weighted moving average of a series.
:doc:`movingaveWgt`         Computes weighted moving average of a series.
:doc:`numCombinations`      Computes number of combinations of n things taken k at a time.
:doc:`ols`                  Computes least squares regression of data set or matrix.
:doc:`olsmt`                Computes least squares regression of data set or matrix.
:doc:`olsqr`                Computes OLS coefficients using QR decomposition.
:doc:`olsqr2`               Computes OLS coefficients, residuals, and predicted values using QR decomposition.
:doc:`olsqrmt`              Computes OLS coefficients using QR decomposition.
:doc:`pacf`                 Computes sample partial autocorrelations.
:doc:`princomp`             Computes principal components of a data matrix.
:doc:`quantile`             Computes quantiles from data in a matrix, given specified probabilities.
:doc:`quantiled`            Computes quantiles from data in a data set, given specified probabilities.
:doc:`quantileFit`          Perform linear quantile regression.
:doc:`quantileFitLoc`       Perform local linear or quadratic quantile regression.
:doc:`rndvm`                Computes von Mises pseudo-random numbers.
:doc:`robustse`             Computes the Huber-White heteroscedastic robust standard errors. The procedure uses the "sandwich" variance-covariance estimator with a small sample correction of :math:`(n)/(n-1)`.
:doc:`stdc`                 Computes standard deviation of the columns of a matrix.
:doc:`toeplitz`             Computes Toeplitz matrix from column vector.
:doc:`varCovM`              Computes the population variance-covariance matrix from a moment matrix.
:doc:`varCovMS`             Computes a sample variance-covariance matrix from a moment matrix.
:doc:`varCovX`              Computes the population variance-covariance matrix from a data matrix.
:doc:`varCovXS`             Computes a sample variance-covariance matrix from a data matrix.
:doc:`varmall`              Computes the log-likelihood of a Vector ARMA model.
:doc:`varmares`             Computes the residuals of a Vector ARMA model.
:doc:`vcm`                  Computes a variance-covariance matrix from a moment matrix.
:doc:`vcx`                  Computes a variance-covariance matrix from a data matrix.
=====================       ===========================================

Optimization and Solution
-----------------------------

=====================       ===========================================
:doc:`eqSolve`              Solves a system of nonlinear equations.
:doc:`eqSolvemt`            Solves a system of nonlinear equations.
:doc:`eqSolveSet`           Sets global input used by eqSolve to default values.
:doc:`ldlsol`               Solves LDLTx = b using a matrix factorized by :doc:`ldlp`.
:doc:`linsolve`             Solves Ax = b using the inverse function.
:doc:`ltrisol`              Computes the solution of Lx = b where L is a lower triangular matrix.
:doc:`lusol`                Computes the solution of LUx = b where L is a lower triangular matrix and U is an upper triangular matrix.
:doc:`QNewton`              Optimizes a function using the BFGS descent algorithm.
:doc:`QNewtonmt`            Minimizes an arbitrary function.
:doc:`QProg`                Solves the quadratic programming problem.
:doc:`QProgmt`              Solves the quadratic programming problem.
:doc:`sqpSolve`             Solves the nonlinear programming problem using a sequential quadratic programming method.
:doc:`sqpSolveMT`           Solves the nonlinear programming problem using a sequential quadratic programming method.
:doc:`sqpSolveSet`          Resets global variables used by sqpSolve to default values.
:doc:`utrisol`              Computes the solution of Ux = b where U is an upper triangular matrix.
=====================       ===========================================

Statistical Distributions
-----------------------------------

=====================       ===========================================
:doc:`cdfBeta`              Computes integral of beta function.
:doc:`cdfBetaInv`           Computes the quantile or inverse of the beta cumulative distribution function.
:doc:`cdfBinomial`          Computes the binomial cumulative distribution function.
:doc:`cdfBinomialInv`       Computes the binomial quantile or inverse cumulative distribution function.
:doc:`cdfBvn`               Computes lower tail of bivariate Normal cdf.
:doc:`cdfBvn2`              Returns cdfbvn of a bounded rectangle.
:doc:`cdfBvn2e`             Returns cdfbvn of a bounded rectangle.
:doc:`cdfCauchy`            Computes the cumulative distribution function for the Cauchy distribution.
:doc:`cdfCauchyinv`         Computes the Cauchy inverse cumulative distribution function.
:doc:`cdfChic`              Computes complement of cdf of χ2.
:doc:`cdfChii`              Computes χ2 abscissae values given probability and degrees of freedom.
:doc:`cdfChinc`             Computes integral of noncentral χ2.
:doc:`cdfEmpirical`         Computes the cumulative distribution function for the empirical distribution.
:doc:`cdfExp`               Computes the cumulative distribution function for the exponential distribution.
:doc:`cdfExpInv`            Computes the exponential inverse cumulative distribution function.
:doc:`cdfFc`                Computes complement of cdf of F.
:doc:`cdfFnc`               Computes integral of noncentral F.
:doc:`cdfFncInv`            Computes the quantile or inverse of noncentral F cumulative distribution function.
:doc:`cdfGam`               Computes integral of incomplete Γ function.
:doc:`cdfGenPareto`         Computes the cumulative distribution function for the Generalized Pareto distribution.
:doc:`cdfHyperGeo`          Computes the cumulative distribution function of the hypergeometric distribution.
:doc:`cdfLaplace`           Computes the cumulative distribution function for the Laplace distribution.
:doc:`cdfLaplaceInv`        Computes the Laplace inverse cumulative distribution function.
:doc:`cdfLogNorm`           Computes the cumulative distribution function of the log-normal distribution.
:doc:`cdfMvn`               Computes multivariate Normal cdf.
:doc:`cdfMvnce`             Computes the complement of the multivariate Normal cumulative distribution function with error management
:doc:`cdfMvne`              Computes multivariate Normal cumulative distribution function with error management
:doc:`cdfMvn2e`             Computes the multivariate Normal cumulative distribution function with error management over the range [a,b]
:doc:`cdfMvtce`             Computes complement of multivariate Student's t cumulative distribution function with error management
:doc:`cdfMvte`              Computes multivariate Student's t cumulative distribution function with error management
:doc:`cdfMvt2e`             Computes multivariate Student's t cumulative distribution function with error management over [a,b]
:doc:`cdfN`                 Computes integral of Normal distribution: lower tail, or cdf.
:doc:`cdfN2`                Computes interval of Normal cdf.
:doc:`cdfNc`                Computes complement of cdf of Normal distribution (upper tail).
:doc:`cdfNegBinomial`       Computes the cumulative distribution function for the negative binomial distribution.
:doc:`cdfNegBinomialInv`    Computes the quantile or inverse negative binomial cumulative distribution function.
:doc:`cdfNi`                Computes the inverse of the cdf of the Normal distribution.
:doc:`cdfPoisson`           Computes the Poisson cumulative distribution function.
:doc:`cdfPoissonInv`        Computes the quantile or inverse Poisson cumulative distribution function.
:doc:`cdfRayleigh`          Computes the Rayleigh cumulative distribution function.
:doc:`cdfRayleighInv`       Computes the Rayleigh inverse cumulative distribution function.
:doc:`cdfTc`                Computes complement of cdf of t-distribution.
:doc:`cdfTci`               Computes the inverse of the complement of the Student's t cdf.
:doc:`cdfTnc`               Computes integral of noncentral t-distribution.
:doc:`cdfTvn`               Computes lower tail of trivariate Normal cdf.
:doc:`cdfTruncNorm`         Computes the cumulative distribution function of the normal distibution over the interval from a to b.
:doc:`cdfWeibull`           Computes the cumulative distribution function for the Weibull distribution.
:doc:`cdfWeibullInv`        Computes the Weibull inverse cumulative distribution function.
:doc:`erf`                  Computes Gaussian error function.
:doc:`erfc`                 Computes complement of Gaussian error function.
:doc:`erfccplx`             Computes complement of Gaussian error function for complex inputs.
:doc:`erfcplx`              Computes Gaussian error function for complex inputs.
:doc:`lncdfbvn`             Computes natural log of bivariate Normal cdf.
:doc:`lncdfbvn2`            Returns log of cdfbvn of a bounded rectangle.
:doc:`lncdfmvn`             Computes natural log of multivariate Normal cdf.
:doc:`lncdfn`               Computes natural log of Normal cdf.
:doc:`lncdfn2`              Computes natural log of interval of Normal cdf.
:doc:`lncdfnc`              Computes natural log of complement of Normal cdf.
:doc:`lnpdfmvn`             Computes multivariate Normal log-probabilities.
:doc:`lnpdfmvt`             Computes multivariate Student's t log-probabilities.
:doc:`lnpdfn`               Computes Normal log-probabilities.
:doc:`lnpdft`               Computes Student's t log-probabilities.
:doc:`pdfBinomial`          Computes the probability mass function for the binomial distribution.
:doc:`pdfCauchy`            Computes the probability density function for the Cauchy distribution.
:doc:`pdfexp`               Computes the probability density function for the exponential distribution.
:doc:`pdfGenPareto`         Computes the probability density function for the Generalized Pareto distribution.
:doc:`pdfHyperGeo`          Computes the probability mass function for the hypergeometric distribution.
:doc:`pdfLaplace`           Computes the probability density function for the Laplace distribution.
:doc:`pdflogistic`          Computes the probability density function for the logistic distribution.
:doc:`pdfLogNorm`           Computes the probability density function of the log-normal distribution.
:doc:`pdfn`                 Computes standard Normal probability density function.
:doc:`pdfPoisson`           Computes the probability mass function for the Poisson distribution.
:doc:`pdfRayleigh`          Computes the probability density function of the Rayleigh distribution.
:doc:`pdfTruncNorm`         Computes the cumulative distribution function of the normal distibution over the interval from a to b.
:doc:`pdfWeibull`           Computes the probability density function of a Weibull random variable.
:doc:`pdfWishartInv`        Computes the probability density function of a inverse Wishart distribution.
=====================       ===========================================

Series and Sequence Functions
---------------------------------

=====================       ===========================================
:doc:`recserar`             Computes autoregressive recursive series.
:doc:`recsercp`             Computes recursive series involving products.
:doc:`recserrc`             Computes recursive series involving division.
:doc:`recserVAR`            Computes a vector autoregressive recursive.
:doc:`seqa`                 Creates an additive sequence.
:doc:`seqadt`               Creates a sequence of dates in DT scalar format.
:doc:`seqm`                 Creates a multiplicative sequence.
:doc:`seqaposix`            Creates a sequence of dates in posix date format.
=====================       ===========================================

Precision Control
---------------------
 
=====================       ===========================================
:doc:`base`10               Converts number to x.xxx and a power of 10.
:doc:`ceil`                 Rounds up towards :math:`+\infty`.
:doc:`floor`                Rounds down towards :math:`-\infty`.
:doc:`machEpsilon`          Returns the smallest number such that :math:`1 + eps > 1`.
:doc:`round`                Rounds to the nearest integer.
:doc:`trunc`                Converts numbers to integers by truncating the fractional portion.
=====================       ===========================================
