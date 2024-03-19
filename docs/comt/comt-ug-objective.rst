The Objective Function
======================

**COMT** is a set of procedures for estimating the parameters of models via the SQP (Sequential Quadratic Programming) method with general constraints on the parameters.

.. math:: \min F\(\Theta\)

Subject to the linear constraints

.. math:: A\(\Theta\) = B
.. math:: C\(\Theta\) \geq D          

 the nonlinear constraints
 
 .. math:: G\(\Theta\) = 0
 .. math:: H\(\Theta\) \geq 0     

  and bounds, 
  
  .. math:: \Theta_L \leq \Theta \leq \Theta_u
  
 :math:`G\(\Theta\)` and :math:`H\(\Theta\)` are functions provided by the user and must be differentiable at least once with respect to the parameters.

The Descent Algorithms
----------------------

**COMT** uses a Sequential Quadratic Programming Method in which the nonlinear constraints, if any, are linearized and added to the linear constraints and then a descent iteration is accomplished by the use of a quadratic programming solve. This method also requires the Hessian, the matrix of second-order derivatives of the objective function with respect to the parameters, and the gradient, the vector of first derivatives. If analytical derivatives are not provided, they can be numerically estimated.

The available methods for estimating the Hessian are a direct numerical estimate, called the Newton method, and the secant methods, BFGS and DFP, where the estimate is an update from the previous iteration starting with a diagonal matrix.
