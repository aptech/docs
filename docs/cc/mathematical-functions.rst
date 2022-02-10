
Mathematical functions
===========================

Scientific functions
--------------------------------------------

=====================       ===========================================
:doc:`../abs`                  Returns absolute value of argument.
:doc:`../arccos`               Computes inverse cosine.
:doc:`../arcsin`               Computes inverse sine.
:doc:`../atan`                 Computes inverse tangent.
:doc:`../atan2`                Computes angle given a point :math:`x`,:math:`y`.
:doc:`../besselj`              Computes Bessel function, first kind.
:doc:`../besselk`              Computes the modified Bessel function of the second kind, :math:`K_n(x)`.
:doc:`../bessely`              Computes Bessel function, second kind.
:doc:`../beta`                 Computes the complete Beta function, also called the Euler integral.
:doc:`../boxcox`               Computes the Box-Cox function.
:doc:`../cos`                  Computes cosine.
:doc:`../cosh`                 Computes hyperbolic cosine.
:doc:`../curve`                Computes a one-dimensional smoothing curve.
:doc:`../digamma`              Computes the digamma function.
:doc:`../exp`                  Computes the exponential function of :math:`x`.
:doc:`../fmod`                 Computes the floating-point remainder of :math:`x/y`.
:doc:`../gamma`                Computes gamma function value.
:doc:`../gammacplx`            Computes gamma function for complex inputs.
:doc:`../gammaii`              Compute the inverse incomplete gamma function.
:doc:`../ln`                   Computes the natural log of each element.
:doc:`../lnfact`               Computes natural log of factorial function.
:doc:`../lngamma`              Computes the natural log of the gamma function.
:doc:`../log`                  Computes the log (base 10) of each element.
:doc:`../mbesseli`             Computes modified and exponentially scaled modified Bessels of the first kind of the nth order.
:doc:`../pi`                   Returns the constant, :math:`\pi`.
:doc:`../polygamma`            Computes the polygamma function of order :math:`n`.
:doc:`../psi`                  Computes the psi (or digamma) function.
:doc:`../sin`                  Computes sine.
:doc:`../sinh`                 Computes the hyperbolic sine.
:doc:`../spline`               Computes a two-dimensional interpolatory spline.
:doc:`../sqrt`                 Computes the square root of each element.
:doc:`../tan`                  Computes tangent.
:doc:`../tanh`                 Computes hyperbolic tangent.
:doc:`../tocart`               Converts from polar to Cartesian coordinates.
:doc:`../topolar`              Converts from Cartesian to polar coordinates.
:doc:`../trigamma`             Computes trigamma function.
:doc:`../zeta`                 Computes the Rieman zeta function.
=====================       ===========================================

Differentiation and Integration
--------------------------------------------

=========================        ===========================================
:doc:`../gradpgradcplx`           Computes first derivative of a function.
:doc:`../hessphesscplx`           Computes second derivative of a function.
:doc:`../integrate1d`             Integrates a user-defined function over a user-defined range, using adaptive quadrature.
:doc:`../intgrat2`                Integrates a 2-dimensional function over an user-defined region.
:doc:`../intgrat3`                Integrates a 3-dimensional function over an user-defined region.
:doc:`../intquad1`                Integrates a 1-dimensional function.
:doc:`../intquad2`                Integrates a 2-dimensional function over an user-defined rectangular region.
:doc:`../intquad3`                Integrates a 3-dimensional function over an user-defined rectangular region.
:doc:`../intsimp`                 Integrates by Simpson's method.
=========================        ===========================================

The following are differentiation functions with advanced options.

=====================          ===========================================
:doc:`../gradmtm`                 Computes numerical gradient with mask.
:doc:`../gradmtt`                 Computes numerical gradient using available threads.
:doc:`../gradmttm`                Computes numerical gradient with mask using available threads.
:doc:`../hessmtg`                 Computes numerical Hessian using gradient procedure.
:doc:`../hessmtgw`                Computes numerical Hessian using gradient procedure with weights.
:doc:`../hessmtm`                 Computes numerical Hessian with mask.
:doc:`../hessmtmw`                Computes numerical Hessian with mask and weights.
:doc:`../hessmtt`                 Computes numerical Hessian using available threads.
:doc:`../hessmttg`                Computes numerical Hessian using gradient procedure with available threads.
:doc:`../hessmttgw`               Computes numerical Hessian using gradient procedure with weights and using available threads.
:doc:`../hessmttm`                Computes numerical Hessian with mask and available threads.
:doc:`../hessmtw`                 Computes numerical Hessian with weights.
=====================          ===========================================


Linear Algebra
--------------------------------------------

=====================          ===========================================
:doc:`../balance`                 Balances a matrix.
:doc:`../band`                    Extracts bands from a symmetric banded matrix.
:doc:`../bandchol`                Computes the Cholesky decomposition of a positive definite banded matrix.
:doc:`../bandcholsol`             Solves the system of equations :math:`Ax = b` for :math:`x`, given the lower triangle of the Cholesky decomposition of a positive definite banded matrix :math:`A`.
:doc:`../bandltsol`               Solves the system of equations :math:`Ax = b` for :math:`x`, where :math:`A` is a lower triangular banded matrix
:doc:`../bandrv`                  Creates a symmetric banded matrix, given its compact form.
:doc:`../bandsolpd`               Solves the system of equations :math:`Ax = b` for :math:`x`, where :math:`A` is a positive definite banded matrix.
:doc:`../blockdiag`               Creates a block-diagonal matrix from one or more input matrices
:doc:`../chol`                    Computes Cholesky decomposition, :math:`X=U'U`.
:doc:`../choldn`                  Performs Cholesky downdate on an upper triangular matrix.
:doc:`../cholsol`                 Solves a system of equations given the Cholesky factorization of a matrix.
:doc:`../cholup`                  Performs Cholesky update on an upper triangular matrix.
:doc:`../cond`                    Computes condition number of a matrix.
:doc:`../crout`                   Computes Crout decomposition, :math:`X = LU` (real matrices only).
:doc:`../croutp`                  Computes Crout decomposition with row pivoting (real matrices only).
:doc:`../det`                     Computes determinant of square matrix.
:doc:`../detl`                    Computes determinant of decomposed matrix.
:doc:`../dot`                     Returns a scalar dot product of the columns of two matrices.
:doc:`../hess`                    Computes upper Hessenberg form of a matrix (real matrices only).
:doc:`../invinvpd`                Inverts a square or positive-definite matrices, respectively.
:doc:`../invswp`                  Computes a generalized sweep inverse.
:doc:`../lapeighb`                Computes eigenvalues only of a real symmetric or complex Hermitian matrix selected by bounds.
:doc:`../lapeighi`                Computes eigenvalues only of a real symmetric or complex Hermitian matrix selected by index.
:doc:`../lapeighvb`               Computes eigenvalues and eigenvectors of a real symmetric or complex Hermitian matrix selected by bounds.
:doc:`../lapeighvi`               Computes selected eigenvalues and eigenvectors of a real symmetric or complex Hermitian matrix.
:doc:`../lapgeig`                 Computes generalized eigenvalues for a pair of real or complex general matrices.
:doc:`../lapgeigh`                Computes generalized eigenvalues for a pair of real symmetric or Hermitian matrices.
:doc:`../lapgeighv`               Computes generalized eigenvalues and eigenvectors for a pair of real symmetric or Hermitian matrices.
:doc:`../lapgeigv`                Computes generalized eigenvalues, left eigenvectors, and right eigenvectors for a pair of real or complex general matrices.
:doc:`../lapgschur`               Computes the generalized Schur form of a pair of real or complex general matrices.
:doc:`../lapgsvdcst`              Computes the generalized singular value decomposition of a pair of real or complex general matrices.
:doc:`../lapgsvds`                Computes the generalized singular value decomposition of a pair of real or complex general matrices.
:doc:`../lapgsvdst`               Computes the generalized singular value decomposition of a pair of real or complex general matrices.
:doc:`../ldl`                     Computes the :math:`L` and :math:`D` factors of the LDL factorization of a real symmetric matrix.
:doc:`../ldlp`                    Computes :math:`LDL` decomposition with row pivoting of a symmetric matrix.
:doc:`../ldlsol`                  Computes Solves the system of equations :math:`LDLTx = b` using a matrix factorized by :doc:`../ldlp`.
:doc:`../lu`                      Computes :math:`LU` decomposition with row pivoting (real and complex matrices).
:doc:`../lusol`                   Computes Solves the system of equations :math:`LUx = b`.
:doc:`../norm`                    Computes one of several specified matrix norms, or a vector p-norm.
:doc:`../null`                    Computes orthonormal basis for right null space.
:doc:`../null1`                   Computes orthonormal basis for right null space.
:doc:`../orth`                    Computes orthonormal basis for column space :math:`x`.
:doc:`../pinv`                    Generalized pseudo-inverse: Moore-Penrose.
:doc:`../pinvmt`                  Generalized pseudo-inverse: Moore-Penrose.
:doc:`../powerm`                  Computes the power :math:`n` of a matrix :math:`A`, as the mathematical equivalent of the matrix product of :math:`n` copies of :math:`A`.
:doc:`../qqr`                     :math:`QR` decomposition: returns :math:`Q_1` and :math:`R`.
:doc:`../qqre`                    :math:`QR` decomposition: returns :math:`Q_1`, :math:`R` and a permutation vector, :math:`E`.
:doc:`../qqrep`                   :math:`QR` decomposition with pivot control: returns :math:`Q_1`, :math:`R`, and :math:`E`.
:doc:`../qr`                      :math:`QR` decomposition: returns :math:`R`.
:doc:`../qre`                     :math:`QR` decomposition: returns :math:`R` and :math:`E`.
:doc:`../qrep`                    :math:`QR` decomposition with pivot control: returns :math:`R` and :math:`E`.
:doc:`../qrsol`                   Solves a system of equations :math:`R'x = b` given an upper triangular matrix, typically the :math:`R` matrix from a :math:`QR` decomposition.
:doc:`../qrtsol`                  Solves a system of equations :math:`Rx = b` given a lower triangular matrix, typically a transposed :math:`R` matrix from a :math:`QR` decomposition.
:doc:`../qtyr`                    :math:`QR` decomposition: returns :math:`Q'Y` and :math:`R`.
:doc:`../qtyre`                   :math:`QR` decomposition: returns :math:`Q'Y`, :math:`R` and :math:`E`.
:doc:`../qtyrep`                  :math:`QR` decomposition with pivot control: returns :math:`Q'Y`, :math:`R` and :math:`E`.
:doc:`../qyr`                     :math:`QR` decomposition: returns :math:`QY` and :math:`R`.
:doc:`../qyre`                    :math:`QR` decomposition: returns :math:`QY`, :math:`R` and :math:`E`.
:doc:`../qyrep`                   :math:`QR` decomposition with pivot control: returns :math:`QY`, :math:`R` and :math:`E`.
:doc:`../qz`                      Compute the complex :math:`QZ`, or generalized Schur, form of a pair of real or complex general matrices with an option to sort the eigenvalues.
:doc:`../rank`                    Computes rank of a matrix.
:doc:`../rref`                    Computes reduced row echelon form of a matrix.
:doc:`../schtoc`                  Reduces any 2x2 blocks on the diagonal of the real Schur form of a matrix returned from schur. The transformation matrix is also updated.
:doc:`../schur`                   Computes real or complex Schur decomposition of a matrix.
:doc:`../solpd`                   Solves a system of positive definite linear equations.
:doc:`../svd`                     Computes the singular values of a matrix.
:doc:`../svd1`                    Computes singular value decomposition, :math:`X = USV'`.
:doc:`../svd2`                    Computes the singular value decomposition :math:`X = USV'` with compact :math:`U`.
:doc:`../svdcusv`                 Computes the singular value decomposition of a matrix so that: :math:`X = U S V'` (compact :math:`U`).
:doc:`../svds`                    Computes the singular values of a matrix.
:doc:`../svdusv`                  Computes the singular value decomposition of a matrix so that: :math:`X = U S V'`.
:doc:`../sylvester`               Computes the solution to the Sylvester matrix equation, :math:`AX + XB = C`.
=====================          ===========================================

Eigenvalues
-----------------

=====================          ===========================================
:doc:`../eig`                     Computes eigenvalues of general matrix.
:doc:`../eigh`                    Computes eigenvalues of complex Hermitian or real symmetric matrix.
:doc:`../eighv`                   Computes eigenvalues and eigenvectors of complex Hermitian or real symmetric matrix.
:doc:`../eigv`                    Computes eigenvalues and eigenvectors of general matrix.
=====================          ===========================================

Polynomial Operations
--------------------------

=====================          ===========================================
:doc:`../polychar`                Computes characteristic polynomial of a square matrix.
:doc:`../polyeval`                Evaluates polynomial with given coefficients.
:doc:`../polyint`                 Calculates Nth order polynomial interpolation given known point pairs.
:doc:`../polymake`                Computes polynomial coefficients from roots.
:doc:`../polymat`                 Returns sequence powers of a matrix.
:doc:`../polymult`                Multiplies two polynomials together.
:doc:`../polyroot`                Computes roots of polynomial from coefficients.
=====================          ===========================================

See also :doc:`../recserrc`, :doc:`../recsercp`, and :doc:`../conv`.

Fourier Transforms
-----------------------

=====================          ===========================================
:doc:`../dfft`                    Computes discrete 1-D FFT.
:doc:`../dffti`                   Computes inverse discrete 1-D FFT.
:doc:`../fft`                     Computes 1- or 2-D FFT.
:doc:`../ffti`                    Computes inverse 1- or 2-D FFT.
:doc:`../fftm`                    Computes multi-dimensional FFT.
:doc:`../fftmi`                   Computes inverse multi-dimensional FFT.
:doc:`../fftn`                    Computes 1- or 2-D FFT using prime factor algorithm.
:doc:`../rfft`                    Computes real 1- or 2-D FFT.
:doc:`../rffti`                   Computes inverse real 1- or 2-D FFT.
:doc:`../rfftip`                  Computes inverse real 1- or 2-D FFT from packed format FFT.
:doc:`../rfftn`                   Computes real 1- or 2-D FFT using prime factor algorithm.
:doc:`../rfftnp`                  Computes real 1- or 2-D FFT using prime factor algorithm, returns packed format FFT.
:doc:`../rfftp`                   Computes real 1- or 2-D FFT, returns packed format FFT.
=====================          ===========================================

Fuzzy Conditional Functions
-----------------------------------

==============================================================                    ===========================================
:doc:`../dotfeqdotfgedotfgtdotfledotfltdotfne`                                    Fuzzy .==, .>=, .>, .<=, .<, .!=
:doc:`../dotfeqmtdotfgemtdotfgtmtdotflemtdotfltmtdotfnemt`                        Fuzzy .==, .>=, .>, .<=, .<, .!=
:doc:`../feqfgefgtflefltfne`                                                      Fuzzy ==, >=, >, <=, <, !=
:doc:`../feqmtfgemtfgtmtflemtfltmtfnemt`                                          Fuzzy ==, >=, >, <=, <, !=
==============================================================                    ===========================================

The mt commands use an fcmptol argument to control the tolerance used for comparison.
The non-mt commands use the global variable _fcmptol to control the tolerance used for comparison. By default, this is 1e-15. The default can be changed by editing the file fcompare.dec.

Statistical Functions
-------------------------

===========================       ===========================================
:doc:`../acf`                      Computes sample autocorrelations.
:doc:`../astd`                     Computes the standard deviation of the elements across one dimension of an N-dimensional array.
:doc:`../astds`                    Computes the 'sample' standard deviation of the elements across one dimension of an N-dimensional array.
:doc:`../chibarsquare`             Computes probability of chi-bar-square statistic.
:doc:`../clusterse`                Computes the White cluster-robust standard errors.
:doc:`../combinate`                Computes combinations of :math:`n` things taken :math:`k` at a time.
:doc:`../combinated`               Writes combinations of :math:`n` things taken :math:`k` at a time to a GAUSS data set.
:doc:`../conscore`                 Computes constrained score statistic and its probability.
:doc:`../conv`                     Computes convolution of two vectors.
:doc:`../corrmcorrvccorrx`         Computes an unbiased estimate of a correlation matrix from a moment matrix, variance-covariance matrix or general matrix.
:doc:`../crossprd`                 Computes cross product.
:doc:`../design`                   Creates a design matrix of 0's and 1's.
:doc:`../dstatmt`                  Computes descriptive statistics of a data set or matrix.
:doc:`../dot`                      Computes a scalar dot product of the columns of two matrices.
:doc:`../gdadstat`                 Computes descriptive statistics on multiple Nx1 variables in a GDA.
:doc:`../gdadstatmat`              Computes descriptive statistics on a selection of columns in a variable in a GDA.
:doc:`../glm`                      Computes generalized linear regression of a matrix.
:doc:`../gmmfit`                   Computes generalized method of moments estimates from user specified moment function.
:doc:`../gmmfitiv`                 Estimate instrumental variables model using the generalized method of moments.
:doc:`../loess`                    Computes coefficients of locally weighted regression.
:doc:`../loessmt`                  Computes coefficients of locally weighted regression.
:doc:`../meanc`                    Computes mean value of each column of a matrix.
:doc:`../median`                   Computes medians of the columns of a matrix.
:doc:`../moment`                   Computes moment matrix (:math:`x'x`) with special handling of missing values.
:doc:`../momentd`                  Computes moment matrix from a data set.
:doc:`../movingave`                Computes moving average of a series.
:doc:`../movingaveexpwgt`          Computes exponentially weighted moving average of a series.
:doc:`../movingavewgt`             Computes weighted moving average of a series.
:doc:`../numcombinations`          Computes number of combinations of :math:`n` things taken :math:`k` at a time.
:doc:`../ols`                      Computes least squares regression of data set or matrix.
:doc:`../olsmt`                    Computes least squares regression of data set or matrix.
:doc:`../olsqr`                    Computes OLS coefficients using :math:`QR` decomposition.
:doc:`../olsqr2`                   Computes OLS coefficients, residuals, and predicted values using :math:`QR` decomposition.
:doc:`../olsqrmt`                  Computes OLS coefficients using :math:`QR` decomposition.
:doc:`../pacf`                     Computes sample partial autocorrelations.
:doc:`../princomp`                 Computes principal components of a data matrix.
:doc:`../quantile`                 Computes quantiles from data in a matrix, given specified probabilities.
:doc:`../quantiled`                Computes quantiles from data in a data set, given specified probabilities.
:doc:`../quantilefit`              Perform linear quantile regression.
:doc:`../quantilefitloc`           Perform local linear or quadratic quantile regression.
:doc:`../robustse`                 Computes the Huber-White heteroscedastic robust standard errors. The procedure uses the "sandwich" variance-covariance estimator with a small sample correction of :math:`(n)/(n-1)`.
:doc:`../stdc`                     Computes standard deviation of the columns of a matrix.
:doc:`../toeplitz`                 Computes Toeplitz matrix from column vector.
:doc:`../varmall`                  Computes the log-likelihood of a Vector ARMA model.
:doc:`../varmares`                 Computes the residuals of a Vector ARMA model.
:doc:`../vcmvcx`                   Computes an unbiased estimate of a variance-covariance matrix from a matrix :math:`x` or a moment matrix, :math:`x'x`.
===========================       ===========================================



Series and Sequence Functions
---------------------------------

=====================       ===========================================
:doc:`../recserar`             Computes autoregressive recursive series.
:doc:`../recsercp`             Computes recursive series involving products.
:doc:`../recserrc`             Computes recursive series involving division.
:doc:`../recservar`            Computes a vector autoregressive recursive.
:doc:`../seqaseqm`             Creates an additive or multiplicative sequence, respectively.
:doc:`../seqadt`               Creates a sequence of dates in DT scalar format.
:doc:`../seqaposix`            Creates a sequence of dates in posix date format, returned as a dataframe date variable.
=====================       ===========================================

Precision Control
---------------------
 
=====================       ===========================================
:doc:`../base10`               Converts number to x.xxx and a power of 10.
:doc:`../ceil`                 Rounds up towards :math:`+\infty`.
:doc:`../fix`                  Rounds towards 0.
:doc:`../floor`                Rounds down towards :math:`-\infty`.
:doc:`../machepsilon`          Returns the smallest number such that :math:`1 + eps > 1`.
:doc:`../round`                Rounds to the nearest integer.
:doc:`../trunc`                Converts numbers to integers by truncating the fractional portion.
=====================       ===========================================
