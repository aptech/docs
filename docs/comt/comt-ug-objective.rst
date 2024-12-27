The Objective Function
======================

**COMT** is a set of procedures for estimating the parameters of models via the SQP (Sequential Quadratic Programming) method with general constraints on the parameters.

.. math:: \min F(\theta)

Subject to the linear constraints

.. math:: A(\theta) = B
.. math:: C(\theta) \geq D          

the nonlinear constraints
 
.. math:: G(\theta) = 0
.. math:: H(\theta) \geq 0     

and bounds, 
  
.. math:: \theta_L \leq \theta \leq \theta_u
  
:math:`G(\theta)` and :math:`H(\theta)` are functions provided by the user and must be differentiable at least once with respect to the parameters.

The Descent Algorithms
----------------------

**COMT** uses a Sequential Quadratic Programming Method in which the nonlinear constraints, if any, are linearized and added to the linear constraints and then a descent iteration is accomplished by the use of a quadratic programming solve. This method also requires the Hessian, the matrix of second-order derivatives of the objective function with respect to the parameters, and the gradient, the vector of first derivatives. If analytical derivatives are not provided, they can be numerically estimated.

The available methods for estimating the Hessian are a direct numerical estimate, called the Newton method, and the secant methods, BFGS and DFP, where the estimate is an update from the previous iteration starting with a diagonal matrix.
