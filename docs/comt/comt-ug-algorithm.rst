Algorithm
=========

COMT uses the Sequential Quadratic Programming method. In this method, the parameters are updated in a series of iterations beginning with starting values that you provide. Let :mat:`\theta_k` be the current parameter values. Then the succeeding values are 

.. math:: 

    \theta_{t+1} = \theta_k + \rho \delta, 

where :math:`\delta` is a :math:`K \times 1` direction vector and :math:`rho`` is a scalar step length.

Define 

.. math::  \Sigma(\theta) = \frac{\partial^2L}{\partial\theta \partial \theta \prime}
.. math::  \Psi(\theta) = \frac{\partial L}{\partial\theta}

and the Jacobians 

.. math::  \dot{G}(\theta) = \frac{\partialG(\theta)}{\partial\theta}
.. math::  \dot{H}(\theta) = \frac{\partialH(\theta)}{\partial\theta}
    
For the purposes of this exposition and without loss of generality, we may assume that the linear constraints and bounds have been incorporated into :math:`G` and :math:`H`.

The direction :math:`\delta` is the solution to the quadratic program. 

.. math::  \text{minimize  } \frac{1}{2}\delta\prime\Sigma(\theta_t)\delta + \Psi(\theta_t)\delta
.. math::  \text{subject to } \dot{G}(\theta_t)\delta + G(\theta_t) = 0
.. math::  \dot{H}(\theta_t)\delta + H(\theta_t) \geq 0


This solution requires that :math:`\Sigma` be positive semi-definite.

In practice, linear constraints are specified separately from the :math:`G` and :math:`H` because their Jacobians are known and easy to compute. And the bounds are more easily handled separately from the linear inequality constraints.

Line Search
-----------

Define the merit function 

.. math::
    m(\theta) = L - \sigma_j \kappa_jg_j(\theta) - \sigma_l \lambda_lh_l(\theta) 
    
where :math:`g` is the j-th row of :math:`G`, :math:`h_l` is the l-th row of :math:`H`, :math:`\kappa` is the vector of Lagrangean coefficients of the equality constraints, and :math:`\lambda`` the vector of Lagrangean coefficients of the inequality constraints.

The line search finds a value of :math:`\rho` that minimizes or decreases :math:`m(\theta_t + \rho\delta)`.

The penalty coefficient, :math:`\mu`, increases at each iteration. The amount of increase in this coefficient is set by the *penalty* member of the instance of the :class:`comtControl` structure.

Trust Radius
------------

By default, a "trust radius" is set around all of the parameters being estimated. Constraints are set for each parameter that bounds the new direction, ensuring the iterations against extreme movements in the estimates. This provides for safer iterations but can add to the total number of iterations to convergence. To turn this off, set the *trustRadius* member of the instance of the :class:`comtControl` structure to a scalar missing value.

The Secant Algorithms
---------------------

The Hessian may be very expensive to compute at every iteration, and poor start values may produce an ill-conditioned Hessian. For these reasons, alternative algorithms are provided in **COMT** for updating the Hessian rather than computing it directly at each iteration. These algorithms, as well as step length methods, may be modified during the execution of **COMT**.

Beginning with an initial estimate of the Hessian or a conformable identity matrix, an update is calculated. The update at each iteration adds more "information" to the estimate of the Hessian, improving its ability to project the direction of the descent. Thus, after several iterations, the secant algorithm should do nearly as well as the Newton iteration with much less computation.

There are two basic types of secant methods: the BFGS (Broyden, Fletcher, Goldfarb, and Shanno) and the DFP (Davidon, Fletcher, and Powell). They are both rank two updates, that is, they are analogous to adding two rows of new data to a previously computed moment matrix. The Cholesky factorization of the estimate of the Hessian is updated using the functions :func:`cholup` and :func:`choldn`.

Secant Methods (BFGS and DFP)
++++++++++++++++++++++++++++++
BFGS is the method of Broyden, Fletcher, Goldfarb, and Shanno, and DFP is the method of Davidon, Fletcher, and Powell. These methods are complementary (Luenberger 1984, page 268). BFGS and DFP are like the NEWTON method in that they use both first and second derivative information. However, in DFP and BFGS the Hessian is approximated, reducing considerably the computational requirements. Because they do not explicitly calculate the second derivatives they are sometimes called quasi-Newton methods. While it takes more iterations than the
NEWTON method, the use of an approximation produces a gain because it can be expected to converge in less overall time (unless analytical second derivatives are available in which case it might be a toss-up).

The secant methods are commonly implemented as updates of the inverse of the Hessian. This is not the best method numerically for the BFGS algorithm (Gill and Murray, 1972). This version of **COMT**, following Gill and Murray (1972), updates the Cholesky factorization of the Hessian instead, using the functions :func:`cholup` and :func:`choldn` for BFGS. The new direction is then computed using :func:`cholsol`, a Cholesky solve, as applied to the updated Cholesky factorization of the Hessian and the gradient.

Line Search Methods
-------------------

Given a direction vector \delta, the updated estimate of the parameters is computed 

.. math:: \theta_{t+1} = \theta_t + \rho\delta, 

where \rho is a constant, usually called the step length, that increases the descent of the function given the direction. **COMT** includes a variety of methods for computing :math:`\rho`. The value of the function to be minimized as a function of :math:`\rho` is 

.. math:: m(\theta_t + \rho\delta)

Given :math:`\theta` and :mat:`delta`, this is a function of a single variable :math:`\rho`. Line search methods attempt to find a value for :math:`\rho` that decreases :math:`m`. STEPBT is a polynomial fitting method, BRENT and HALF are iterative search methods. A fourth method called ONE forces a step length of 1. The default line search method is STEPBT. If this or any selected method fails, then BRENT is tried. If BRENT fails, then HALF is tried. If all of the line search methods fail, then a random search is tried, provided the *randRadius* member of the :class:`comtControl` instance is greater than zero. The default setting for *randRadius* is greater than zero.

Augmented Penalty Line Search Method
++++++++++++++++++++++++++++++++++++++
When the *lineSearch* member of the instance of the :class:`comtControl` structure is set to zero, **COMT** uses an "augmented Lagrangian penalty"' method for the line search described in Conn, Gould, and Toint (2000). The Hessian and gradient for the Quadratic Programming problem in the SQP method is augmented as described in their Section 15.3.1. This method requires that constraints be imposed on the parameters. This method is not available for solving maximum likelihood problems without constraints on parameters.

STEPBT
+++++++++
STEPBT is an implementation of a similarly named algorithm described in Dennis and Schnabel (1983). It first attempts to fit a quadratic function to :math:`m(\theta_t + \rho\delta)` and computes a :math:`rho` that minimizes the quadratic. If that fails, it attempts to fit a cubic function. The cubic function more accurately portrays the :math:`F` which is not likely to be very quadratic but is, however, more costly to compute. STEPBT is the default line search method because it generally produces the best results for the least cost in computational resources.

BRENT
++++++++
This method is a variation on the golden section method due to Brent (1972). In this method, the function is evaluated at a sequence of test values for :math:`rho`. These test values are determined by extrapolation and interpolation using the constant:

.. math:: (\sqrt{5 - 1)/2 = 0.6180 \ldots


This constant is the inverse of the so-called "golden ratio":

.. math:: (\sqrt{5 + 1)/2 = 1.6180 \ldots

and is why the method is called a golden section method. This method is generally more efficient
than STEPBT but requires significantly more function evaluations.

HALF
++++++++++
This method first computes :math:`m(x + \delta)`, i.e., sets :math:`\rho = 1`. If :math:`m(x + \delta) \leq m(x)` then the
step length is set to 1. If not, then it tries :math:`m(x + 0.5\delta)`. The attempted step length is divided
by one half each time the function fails to decrease and exits with the current value when it does decrease. This method usually requires the fewest function evaluations (it often only requires one), but it is the least efficient in that it is not very likely to find the step
length that decreases :math:`m` the most.

Active and Inactive Parameters
-------------------------------

The member *active* of the :class:`comtControl` structure may be used to fix parameters to their start values. *Active* must be set to a vector of the same length as the vector of start values. Elements of active set to zero will fix the corresponding parameter to its starting value, while the parameters corresponding to nonzero elements will be estimated.

For example, to fix the third parameter of a model with five parameters, to its starting value:

::

    // Declare 'ctl' to be a comtControl struct
    struct comtControl ctl;

    // Fill 'ctl' with default settings
    ctl = comtControlCreate();

    // Fix the third parameter to its start value
    // NOTE: This setting will not take effect until
    // 'ctl' is passed in to a call to 'comt'
    ctl.active = { 1, 1, 0, 1, 1 };

This allows estimation of different models without having to modify the function procedure. For example, setting a parameter to be 'inactive' and setting its starting value to zero will eliminate it from the estimation.