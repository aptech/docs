Constrained Optimization MT (COMT)
==================================
A constrained optimization package for GAUSS.

Description
----------------
COMT solves the Nonlinear Programming problem, subject to general constraints on the parameters - linear or nonlinear, equality or inequality, using the Sequential Quadratic Programming method in combination with several descent methods selectable by the user.

COMT's ability to handle general nonlinear functions and nonlinear constraints along with other features, such as the Trust Region Method, allow you to solve a wide range of sophisticated optimization problems. Built on the speed and number crunching ability of the GAUSS platform, COMT quickly computes solutions to large problems, making it ideal for large scale Monte Carlo or Bootstrap optimizations.


Installation
--------------
Please `contact us <https://www.aptech.com/contact-us>`_ with to request pricing and installation information.

If you already own COMT, you can use the `GAUSS Package Manager <https://www.aptech.com/blog/gauss-package-manager-basics/>`_ to install COMT as well.

Requires GAUSS/GAUSS Engine/GAUSS Light v16 or higher.

Key Features
------------------------------

Descent methods
+++++++++++++++++++++++++++++++

* BFGS (Broyden, Fletcher, Goldfarb and Powell)
* Modifed BFGS
* DFP (Davidon, Fletcher and Powell)
* Newton-Raphson

Line search methods
+++++++++++++++++++++++++++++++

* Augmented trust region method
* STEPBT
* Brent’s method
* Half
* Strong Wolfe’s conditions

Constraint types
+++++++++++++++++++++++++++++++

* Linear equality and inequality constraints
* Nonlinear equality and inequality constraints
* Bounded parameters

Available Optimization Controls
--------------------------------
Optimization controls are set to default values that few users ever need to change.  However, COMT is fully customizable and the flexible optimization options can be a great help when tackling more difficult problems.

Control Options
+++++++++++++++++++++++++++++++

.. list-table::
    :widths: auto

    * - Linear equality constraints
      - Optional, simple to specify, linear equality constraints.
    * - Linear inequality constraints
      - Optional, simple to specify, linear inequality constraints.
    * - Nonlinear equality constraints
      - Option to provide a procedure to compute nonlinear equality constraints.
    * - Nonlinear inequality constraints
      - Option to provide a procedure to compute nonlinear inequality constraints.
    * - Parameter bounds
      - Simple parameter bounds of the type: lower_bd ≤ x_i ≤ upper_bd.
    * - Feasible test
      - Controls whether parameters are checked for feasibility during line search.
    * - Trust radius
      - Set the size of the trust radius, or turn off the trust region method.
    * - Descent algorithms
      - BFGS, Modified BFGS, DFP, and Newton.
    * - Algorithm switching
      - Specify descent algorithms to switch between based upon the number of elapsed iterations, a minimum change in the objective function, or line search step size.
    * - Line search method
      - Augmented Lagrangian Penalty, STEPBT (quadratic and cubic curve fit), Brent’s method, half-step, or Strong Wolfe’s Conditions.
    * - Active parameters
      - Control which parameters are active (to be estimated) and which should be fixed to their start value.
    * - Gradient Method
      - Either compute an analytical gradient, or have COMT compute a numerical gradient using the forward, central, or backwards difference method.
    * - Hessian Method
      - Either compute an analytical Hessian, or have COMT compute a numerical Hessian using the forward, central, or backwards difference method.
    * - Gradient check
      - Compares the analytical gradient computed by the user-supplied function with the numerical gradient to check the analytical gradient for correctness.
    * - Random seed
      - Starting seed value used by the random line search method to allow for repeatable code.
    * - Print output
      - Controls whether (or how often) iteration output is printed and whether a final report is printed.
    * - Gradient step
      - Advanced feature: Controls the increment size for computing the step size for numerical first and second derivatives.
    * - Random search radius
      - The radius of the random search if attempted.
    * - Maximum iterations
      - Maximum iterations to converge.
    * - Maximum elapsed time
      - Maximum number of minutes to converge.
    * - Maximum random search attempts
      - Maximum allowed number of random line search attempts.
    * - Convergence tolerance
      - Convergence is achieved when the direction vector changes less than this amount.


.. toctree::
    :maxdepth: 2
    :hidden:
    :caption: Constrained Optimization Documents

    user-guide
    command-reference
    comt-examples



