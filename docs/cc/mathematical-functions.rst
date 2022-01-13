
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
:doc:`besselk`              Computes the modified Bessel function of the second kind, K_n(x).
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
:doc:`pi`                   Returns π.
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
:doc:`gradMT`                  Computes numerical gradient.
:doc:`gradMTm`                 Computes numerical gradient with mask.
:doc:`gradMTT`                 Computes numerical gradient using available threads.
:doc:`gradMTTm`                Computes numerical gradient with mask using available threads.
:doc:`gradp`, :doc:`gradcplx`  Computes first derivative of a function; gradcplx allows for complex arguments.
:doc:`hessMT`                  Computes numerical Hessian.
:doc:`hessMTg`                 Computes numerical Hessian using gradient procedure.
:doc:`hessMTgw`                Computes numerical Hessian using gradient procedure with weights.
:doc:`hessMTm`                 Computes numerical Hessian with mask.
:doc:`hessMTmw`                Computes numerical Hessian with mask and weights.
:doc:`hessMTT`                 Computes numerical Hessian using available threads.
:doc:`hessMTTg`                Computes numerical Hessian using gradient procedure with available threads.
:doc:`hessMTTgw`               Computes numerical Hessian using gradient procedure with weights and using available threads.
:doc:`hessMTTm`                Computes numerical Hessian with mask and available threads.
:doc:`hessMTw`                 Computes numerical Hessian with weights.
:doc:`hessp`, :doc:`hesscplx`  Computes second derivative of a function; hesscplx allows for complex arguments.
:doc:`integrate1d`             Integrates a user-defined function over a user-defined range, using adaptive quadrature.
:doc:`intgrat2`                Integrates a 2-dimensional function over an user-defined region.
:doc:`intgrat3`                Integrates a 3-dimensional function over an user-defined region.
:doc:`intquad1`                Integrates a 1-dimensional function.
:doc:`intquad2`                Integrates a 2-dimensional function over an user-defined rectangular region.
:doc:`intquad3`                Integrates a 3-dimensional function over an user-defined rectangular region.
:doc:`intsimp`                 Integrates by Simpson's method.
=====================          ===========================================


Linear Algebra
--------------------------------------------

=====================          ===========================================
balance    Balances a matrix.
band    Extracts bands from a symmetric banded matrix.
bandchol    Computes the Cholesky decomposition of a positive definite banded matrix.
bandcholsol    Solves the system of equations Ax = b for x, given the lower triangle of the Cholesky decomposition of a positive definite banded matrix A.
bandltsol    Solves the system of equations Ax = b for x, where A is a lower triangular banded matrix
bandrv    Creates a symmetric banded matrix, given its compact form.
bandsolpd    Solves the system of equations Ax = b for x, where A is a positive definite banded matrix.
blockDiag    Creates a block-diagonal matrix from one or more input matrices
chol    Computes Cholesky decomposition, X=Y`Y.
choldn    Performs Cholesky downdate on an upper triangular matrix.
cholsol    Solves a system of equations given the Cholesky factorization of a matrix.
cholup    Performs Cholesky update on an upper triangular matrix.
cond    Computes condition number of a matrix.
crout    Computes Crout decomposition, X = LU (real matrices only).
croutp    Computes Crout decomposition with row pivoting (real matrices only).
det    Computes determinant of square matrix.
detl    Computes determinant of decomposed matrix.
dot    Returns a scalar dot product of the columns of two matrices.
hess    Computes upper Hessenberg form of a matrix (real matrices only).
inv    Inverts a matrix.
invpd    Inverts a positive definite matrix.
invswp    Computes a generalized sweep inverse.
lapeighb    Computes eigenvalues only of a real symmetric or complex Hermitian matrix selected by bounds.
lapeighi    Computes eigenvalues only of a real symmetric or complex Hermitian matrix selected by index.
lapeighvb    Computes eigenvalues and eigenvectors of a real symmetric or complex Hermitian matrix selected by bounds.
lapeighvi    Computes selected eigenvalues and eigenvectors of a real symmetric or complex Hermitian matrix.
lapgeig    Computes generalized eigenvalues for a pair of real or complex general matrices.
lapgeigh    Computes generalized eigenvalues for a pair of real symmetric or Hermitian matrices.
lapgeighv    Computes generalized eigenvalues and eigenvectors for a pair of real symmetric or Hermitian matrices.
lapgeigv    Computes generalized eigenvalues, left eigenvectors, and right eigenvectors for a pair of real or complex general matrices.
lapgschur    Computes the generalized Schur form of a pair of real or complex general matrices.
lapgsvdcst    Computes the generalized singular value decomposition of a pair of real or complex general matrices.
lapgsvds    Computes the generalized singular value decomposition of a pair of real or complex general matrices.
lapgsvdst    Computes the generalized singular value decomposition of a pair of real or complex general matrices.
lapsvdcusv    Computes the singular value decomposition a real or complex rectangular matrix, returns compact u and v.
lapsvds    Computes the singular values of a real or complex rectangular matrix.
lapsvdusv    Computes the singular value decomposition a real or complex rectangular matrix.
ldl    Computes the L and D factors of the LDL factorization of a real symmetric matrix.
ldlp    Computes LDL decomposition with row pivoting of a symmetric matrix.
ldlsol    Computes Solves the system of equations LDLTx = b using a matrix factorized by ldlp.
lu    Computes LU decomposition with row pivoting (real and complex matrices).
lusol    Computes Solves the system of equations LUx = b.
norm    Computes one of several specified matrix norms, or a vector p-norm.
null    Computes orthonormal basis for right null space.
null1    Computes orthonormal basis for right null space.
orth    Computes orthonormal basis for column space x.
pinv    Generalized pseudo-inverse: Moore-Penrose.
pinvmt    Generalized pseudo-inverse: Moore-Penrose.
powerM    Computes the power n of a matrix A, as the matrix product of n copies of A.
qqr    QR decomposition: returns Q1 and R.
qqre    QR decomposition: returns Q1, R and a permutation vector, E.
qqrep    QR decomposition with pivot control: returns Q1, R, and E.
qr    QR decomposition: returns R.
qre    QR decomposition: returns R and E.
qrep    QR decomposition with pivot control: returns R and E.
qrsol    Solves a system of equations R'x = b given an upper triangular matrix, typically the R matrix from a QR decomposition.
qrtsol    Solves a system of equations R'x = b given an upper triangular matrix, typically the R matrix from a QR decomposition.
qtyr    QR decomposition: returns Q'Y and R.
qtyre    QR decomposition: returns Q'Y, R and E.
qtyrep    QR decomposition with pivot control: returns Q'Y, R and E.
qyr    QR decomposition: returns QY and R.
qyre    QR decomposition: returns QY, R and E.
qyrep    QR decomposition with pivot control: returns QY, R and E.
qz    Compute the complex QZ, or generalized Schur, form of a pair of real or complex general matrices with an option to sort the eigenvalues.
rank    Computes rank of a matrix.
rref    Computes reduced row echelon form of a matrix.
schtoc    Reduces any 2x2 blocks on the diagonal of the real Schur form of a matrix returned from schur. The transformation matrix is also updated.
schur    Computes real or complex Schur decomposition of a matrix.
solpd    Solves a system of positive definite linear equations.
svd    Computes the singular values of a matrix.
svd1    Computes singular value decomposition, X = USV'.
svd2    Computes svd1 with compact U.
svdcusv    Computes the singular value decomposition of a matrix so that: x = u * s * v' (compact u).
svds    Computes the singular values of a matrix.
svdusv    Computes the singular value decomposition of a matrix so that: x = u * s * v'.
sylvester    Computes the solution to the Sylvester matrix equation, AX + XB = C.
=====================          ===========================================

Eigenvalues
-----------------

=====================          ===========================================
eig    Computes eigenvalues of general matrix.
eigh    Computes eigenvalues of complex Hermitian or real symmetric matrix.
eighv    Computes eigenvalues and eigenvectors of complex Hermitian or real symmetric matrix.
eigv    Computes eigenvalues and eigenvectors of general matrix.
=====================          ===========================================

Polynomial Operations
--------------------------

=====================          ===========================================
polychar    Computes characteristic polynomial of a square matrix.
polyeval    Evaluates polynomial with given coefficients.
polyint    Calculates Nth order polynomial interpolation given known point pairs.
polymake    Computes polynomial coefficients from roots.
polymat    Returns sequence powers of a matrix.
polymult    Multiplies two polynomials together.
polyroot    Computes roots of polynomial from coefficients.
=====================          ===========================================

See also :doc:`recserrc`, :doc:`recsercp`, and :doc:`conv`.

Fourier Transforms
-----------------------

=====================          ===========================================
dfft    Computes discrete 1-D FFT.
dffti    Computes inverse discrete 1-D FFT.
fft    Computes 1- or 2-D FFT.
ffti    Computes inverse 1- or 2-D FFT.
fftm    Computes multi-dimensional FFT.
fftmi    Computes inverse multi-dimensional FFT.
fftn    Computes 1- or 2-D FFT using prime factor algorithm.
rfft    Computes real 1- or 2-D FFT.
rffti    Computes inverse real 1- or 2-D FFT.
rfftip    Computes inverse real 1- or 2-D FFT from packed format FFT.
rfftn    Computes real 1- or 2-D FFT using prime factor algorithm.
rfftnp    Computes real 1- or 2-D FFT using prime factor algorithm, returns packed format FFT.
rfftp    Computes real 1- or 2-D FFT, returns packed format FFT.
=====================          ===========================================

Random Numbers
----------------

=====================          ===========================================
rndBernoulli    Computes random numbers with Bernoulli distribution.
rndBeta    Computes random numbers with beta distribution.
rndBinomial    Computes binomial pseudo-random numbers with the choice of underlying random number generator.
rndCauchy    Computes Cauchy distributed random numbers with a choice of underlying random number generator.
rndChiSquare    Creates pseudo-random numbers with a chi-squared distribution, with an optional non-centrality parameter and a choice of underlying random number generator.
rndCreateState    Creates a new random number stream for a specified generator type from a seed value.
rndExp    Computes exponentially distributed random numbers with a choice of underlying random number generator.
rndGamma    Computes gamma pseudo-random numbers with a choice of underlying random number generator.
rndGeo    Computes geometric pseudo-random numbers with a choice of underlying random number generator.
rndGumbel    Computes Gumbel distributed random numbers with a choice of underlying random number generator.
rndHyperGeo    Computes pseudo-random numbers following a hypergeometric distribution with a choice of underlying random number generator.
rndi    Returns random integers, 0 <= y < 232.
rndKMbeta    Returns uniformly distributed random integers over a user specified range.
rndKMgam    Computes gamma pseudo-random numbers.
rndKMi    Returns random integers, 0 <= y < 232.
rndKMn    Computes standard normal pseudo-random numbers.
rndKMnb    Computes negative binomial pseudo-random numbers.
rndKMp    Computes Poisson pseudo-random numbers.
rndKMu    Computes uniform pseudo-random numbers.
rndKMvm    Computes von Mises pseudo-random numbers.
rndLaplace    Computes Laplacian pseudo-random numbers with the choice of underlying random number generator.
rndLogNorm    Computes lognormal pseudo-random numbers with the choice of underlying random number generator.
rndMVn    Computes multivariate normal random numbers given a covariance matrix.
rndMVt    Computes multivariate Student-t random numbers given a covariance matrix.
rndn    Computes normally distributed pseudo-random numbers with a choice of underlying random number generator.
rndNegBinomial    Computes negative binomial pseudo-random numbers with a choice of underlying random number generator.
rndPoisson    Computes Poisson pseudo-random numbers with a choice of underlying random number generator.
rndRayleigh    Computes rayleigh pseudo-random numbers with the choice of underlying random number generator.
rndseed    Changes seed of the LC random number generator.
rndStateSkip    To advance a state vector by a specified number of values.
rndu    Computes uniform random numbers with a choice of underlying random number generator.
rndWeibull    Computes Weibull pseudo-random numbers with the choice of underlying random number generator.
rndWishart    Computes Wishart pseudo-random matrices with the choice of underlying random number generator.
rndWishartInv    Computes inverse Wishart pseudo-random matrices with the choice of underlying random number generator.
=====================          ===========================================

Fuzzy Conditional Functions
-----------------------------------

=====================       ===========================================
dotfeq    Fuzzy .==
dotfeqmt    Fuzzy .==
dotfge    Fuzzy .>=
dotfgemt    Fuzzy .>
dotfgt    Fuzzy .>
dotfgtmt    Fuzzy .>
dotfle    Fuzzy .<=
dotflemt    Fuzzy .<=
dotflt    Fuzzy .<
dotfltmt    Fuzzy .<
dotfne    Fuzzy ./=
dotfnemt    Fuzzy ./=
feq    Fuzzy ==
feqmt    Fuzzy ==
fge    Fuzzy >=
fgemt    Fuzzy >=
fgt    Fuzzy >
fgtmt    Fuzzy >
fle    Fuzzy <=
flemt    Fuzzy <=
flt    Fuzzy <
fltmt    Fuzzy <
fne    Fuzzy /=
fnemt    Fuzzy /=
=====================       ===========================================
The mt commands use an fcmptol argument to control the tolerance used for comparison.
The non-mt commands use the global variable _fcmptol to control the tolerance used for comparison. By default, this is 1e-15. The default can be changed by editing the file fcompare.dec.

Statistical Functions
-------------------------

=====================       ===========================================
acf    Computes sample autocorrelations.
astd    Computes the standard deviation of the elements across one dimension of an N-dimensional array.
astds    Computes the 'sample' standard deviation of the elements across one dimension of an N-dimensional array.
chiBarSquare    Computes probability of chi-bar-square statistic.
clusterse    Computes the White cluster-robust standard errors.
combinate    Computes combinations of n things taken k at a time.
combinated    Writes combinations of n things taken k at a time to a GAUSS data set.
conScore    Computes constrained score statistic and its probability.
conv    Computes convolution of two vectors.
corrm    Computes correlation matrix of a moment matrix.
corrms    Computes sample correlation matrix of a moment matrix.
corrvc    Computes correlation matrix from a variance- covariance matrix.
corrx    Computes correlation matrix.
corrxs    Computes sample correlation matrix.
crossprd    Computes cross product.
design    Creates a design matrix of 0's and 1's.
dstatmt    Computes descriptive statistics of a data set or matrix.
dot    Computes a scalar dot product of the columns of two matrices.
dstatmtControlCreate    Creates default dstatmtControl structure.
gdaDStat    Computes descriptive statistics on multiple Nx1 variables in a GDA.
gdaDStatMat    Computes descriptive statistics on a selection of columns in a variable in a GDA.
glm    Computes generalized linear regression of a matrix.
gmmControlCreate    Creates default gmmControl structure.
gmmFit    Computes generalized method of moments estimates from user specified moment function.
gmmFitIV    Estimate instrumental variables model using the generalized method of moments.
loess    Computes coefficients of locally weighted regression.
loessmt    Computes coefficients of locally weighted regression.
loessmtControlCreate    Creates default loessmtControl structure.
meanc    Computes mean value of each column of a matrix.
median    Computes medians of the columns of a matrix.
moment    Computes moment matrix (x'x) with special handling of missing values.
momentd    Computes moment matrix from a data set.
movingave    Computes moving average of a series.
movingaveExpwgt    Computes exponentially weighted moving average of a series.
movingaveWgt    Computes weighted moving average of a series.
numCombinations    Computes number of combinations of n things taken k at a time.
ols    Computes least squares regression of data set or matrix.
olsmt    Computes least squares regression of data set or matrix.
olsmtControlCreate    Creates default olsmtControl structure.
olsqr    Computes OLS coefficients using QR decomposition.
olsqr2    Computes OLS coefficients, residuals, and predicted values using QR decomposition.
olsqrmt    Computes OLS coefficients using QR decomposition.
pacf    Computes sample partial autocorrelations.
princomp    Computes principal components of a data matrix.
qfitControlCreate    Creates default qfitControl structure.
quantile    Computes quantiles from data in a matrix, given specified probabilities.
quantiled    Computes quantiles from data in a data set, given specified probabilities.
quantileFit    Perform linear quantile regression.
quantileFitLoc    Perform local linear or quadratic quantile regression.
rndvm    Computes von Mises pseudo-random numbers.
robustse    Computes the Huber-White heteroscedastic robust standard errors. The procedure uses the "sandwich" variance-covariance estimator with a small sample correction of (n)/(n-1).
stdc    Computes standard deviation of the columns of a matrix.
stdsc    Computes the 'sample' standard deviation of the elements in each column of a matrix.
toeplitz    Computes Toeplitz matrix from column vector.
varCovM    Computes the population variance-covariance matrix from a moment matrix.
varCovMS    Computes a sample variance-covariance matrix from a moment matrix.
varCovX    Computes the population variance-covariance matrix from a data matrix.
varCovXS    Computes a sample variance-covariance matrix from a data matrix.
varmall    Computes the log-likelihood of a Vector ARMA model.
varmares    Computes the residuals of a Vector ARMA model.
vcm    Computes a variance-covariance matrix from a moment matrix.
vcms    Computes a sample variance-covariance matrix from a moment matrix.
vcx    Computes a variance-covariance matrix from a data matrix.
vcxs    Computes a sample variance-covariance matrix from a data matrix.
=====================       ===========================================

Optimization and Solution
-----------------------------

=====================       ===========================================
eqSolve    Solves a system of nonlinear equations.
eqSolvemt    Solves a system of nonlinear equations.
eqSolvemtControlCreate    Creates default eqSolvemtControl structure.
eqSolvemtOutCreate    Creates default eqSolvemtOut structure.
eqSolveSet    Sets global input used by eqSolve to default values.
ldlsol    Solves LDLTx = b using a matrix factorized by ldlp.
linsolve    Solves Ax = b using the inverse function.
ltrisol    Computes the solution of Lx = b where L is a lower triangular matrix.
lusol    Computes the solution of LUx = b where L is a lower triangular matrix and U is an upper triangular matrix.
QNewton    Optimizes a function using the BFGS descent algorithm.
QNewtonmt    Minimizes an arbitrary function.
QNewtonmtControlCreate    Creates default QNewtonmtControl structure.
QNewtonmtOutCreate    Creates default QNewtonmtOut structure.
QProg    Solves the quadratic programming problem.
QProgmt    Solves the quadratic programming problem.
QProgmtInCreate    Creates an instance of a structure of type QProgmtInCreate with the maxit member set to a default value.
sqpSolve    Solves the nonlinear programming problem using a sequential quadratic programming method.
sqpSolveMT    Solves the nonlinear programming problem using a sequential quadratic programming method.
sqpSolveMTControlCreate    Creates an instance of a structure of type sqpSolveMTcontrol set to default values.
sqpSolveMTlagrangeCreate    Creates an instance of a structure of type sqpSolveMTlagrange set to default values.
sqpSolveMToutCreate    Creates an instance of a structure of type sqpSolveMTout set to default values.
sqpSolveSet    Resets global variables used by sqpSolve to default values.
utrisol    Computes the solution of Ux = b where U is an upper triangular matrix.
=====================       ===========================================

Statistical Distributions
-----------------------------------

=====================       ===========================================
cdfBeta    Computes integral of beta function.
cdfBetaInv    Computes the quantile or inverse of the beta cumulative distribution function.
cdfBinomial    Computes the binomial cumulative distribution function.
cdfBinomialInv    Computes the binomial quantile or inverse cumulative distribution function.
cdfBvn    Computes lower tail of bivariate Normal cdf.
cdfBvn2    Returns cdfbvn of a bounded rectangle.
cdfBvn2e    Returns cdfbvn of a bounded rectangle.
cdfCauchy    Computes the cumulative distribution function for the Cauchy distribution.
cdfCauchyinv    Computes the Cauchy inverse cumulative distribution function.
cdfChic    Computes complement of cdf of χ2.
cdfChii    Computes χ2 abscissae values given probability and degrees of freedom.
cdfChinc    Computes integral of noncentral χ2.
cdfEmpirical    Computes the cumulative distribution function for the empirical distribution.
cdfExp    Computes the cumulative distribution function for the exponential distribution.
cdfExpInv    Computes the exponential inverse cumulative distribution function.
cdfFc    Computes complement of cdf of F.
cdfFnc    Computes integral of noncentral F.
cdfFncInv    Computes the quantile or inverse of noncentral F cumulative distribution function.
cdfGam    Computes integral of incomplete Γ function.
cdfGenPareto    Computes the cumulative distribution function for the Generalized Pareto distribution.
cdfHyperGeo    Computes the cumulative distribution function of the hypergeometric distribution.
cdfLaplace    Computes the cumulative distribution function for the Laplace distribution.
cdfLaplaceInv    Computes the Laplace inverse cumulative distribution function.
cdfLogNorm    Computes the cumulative distribution function of the log-normal distribution.
cdfMvn    Computes multivariate Normal cdf.
cdfMvnce    Computes the complement of the multivariate Normal cumulative distribution function with error management
cdfMvne    Computes multivariate Normal cumulative distribution function with error management
cdfMvn2e    Computes the multivariate Normal cumulative distribution function with error management over the range [a,b]
cdfMvtce    Computes complement of multivariate Student's t cumulative distribution function with error management
cdfMvte    Computes multivariate Student's t cumulative distribution function with error management
cdfMvt2e    Computes multivariate Student's t cumulative distribution function with error management over [a,b]
cdfN    Computes integral of Normal distribution: lower tail, or cdf.
cdfN2    Computes interval of Normal cdf.
cdfNc    Computes complement of cdf of Normal distribution (upper tail).
cdfNegBinomial    Computes the cumulative distribution function for the negative binomial distribution.
cdfNegBinomialInv    Computes the quantile or inverse negative binomial cumulative distribution function.
cdfNi    Computes the inverse of the cdf of the Normal distribution.
cdfPoisson    Computes the Poisson cumulative distribution function.
cdfPoissonInv    Computes the quantile or inverse Poisson cumulative distribution function.
cdfRayleigh    Computes the Rayleigh cumulative distribution function.
cdfRayleighInv    Computes the Rayleigh inverse cumulative distribution function.
cdfTc    Computes complement of cdf of t-distribution.
cdfTci    Computes the inverse of the complement of the Student's t cdf.
cdfTnc    Computes integral of noncentral t-distribution.
cdfTvn    Computes lower tail of trivariate Normal cdf.
cdfTruncNorm    Computes the cumulative distribution function of the normal distibution over the interval from a to b.
cdfWeibull    Computes the cumulative distribution function for the Weibull distribution.
cdfWeibullInv    Computes the Weibull inverse cumulative distribution function.
erf    Computes Gaussian error function.
erfc    Computes complement of Gaussian error function.
erfccplx    Computes complement of Gaussian error function for complex inputs.
erfcplx    Computes Gaussian error function for complex inputs.
lncdfbvn    Computes natural log of bivariate Normal cdf.
lncdfbvn2    Returns log of cdfbvn of a bounded rectangle.
lncdfmvn    Computes natural log of multivariate Normal cdf.
lncdfn    Computes natural log of Normal cdf.
lncdfn2    Computes natural log of interval of Normal cdf.
lncdfnc    Computes natural log of complement of Normal cdf.
lnpdfmvn    Computes multivariate Normal log-probabilities.
lnpdfmvt    Computes multivariate Student's t log-probabilities.
lnpdfn    Computes Normal log-probabilities.
lnpdft    Computes Student's t log-probabilities.
pdfBinomial    Computes the probability mass function for the binomial distribution.
pdfCauchy    Computes the probability density function for the Cauchy distribution.
pdfexp    Computes the probability density function for the exponential distribution.
pdfGenPareto    Computes the probability density function for the Generalized Pareto distribution.
pdfHyperGeo    Computes the probability mass function for the hypergeometric distribution.
pdfLaplace    Computes the probability density function for the Laplace distribution.
pdflogistic    Computes the probability density function for the logistic distribution.
pdfLogNorm    Computes the probability density function of the log-normal distribution.
pdfn    Computes standard Normal probability density function.
pdfPoisson    Computes the probability mass function for the Poisson distribution.
pdfRayleigh    Computes the probability density function of the Rayleigh distribution.
pdfTruncNorm    Computes the cumulative distribution function of the normal distibution over the interval from a to b.
pdfWeibull    Computes the probability density function of a Weibull random variable.
pdfWishartInv    Computes the probability density function of a inverse Wishart distribution.
=====================       ===========================================

Series and Sequence Functions
---------------------------------

=====================       ===========================================
recserar    Computes autoregressive recursive series.
recsercp    Computes recursive series involving products.
recserrc    Computes recursive series involving division.
recserVAR    Computes a vector autoregressive recursive.
seqa    Creates an additive sequence.
seqadt  Creates a sequence of dates in DT scalar format.
seqm    Creates a multiplicative sequence.
seqaposix  Creates a sequence of dates in posix date format.
=====================       ===========================================

Precision Control
---------------------
 
=====================       ===========================================
base10    Converts number to x.xxx and a power of 10.
ceil    Rounds up towards +∞.
floor    Rounds down towards -∞.
machEpsilon    Returns the smallest number such that 1+ eps>1.
round    Rounds to the nearest integer.
trunc    Converts numbers to integers by truncating the fractional portion.
=====================       ===========================================
