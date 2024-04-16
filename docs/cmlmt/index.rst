Constrained Max Likelihood (CMLMT)
=======================================
A constrained maximum likelihood package for **GAUSS**.

Description
----------------
**CMLMT** provides methods for statistical inference of weighted or unweighted, bounded or unbounded maximum likelihood models with general constraints.

**CMLMT's**  ability to handle general nonlinear functions and nonlinear constraints along with other features, such as the Trust Region Method, allow you to solve a wide range of sophisticated optimization problems. Built on the speed and number crunching ability of the GAUSS platform, **CMLMT**  quickly computes solutions to large problems, making it ideal for large scale Monte Carlo or Bootstrap optimizations.


Installation
--------------
Please `contact us <https://www.aptech.com/contact-us>`_ with to request pricing and installation information.

If you already own **CMLMT** , you can use the `GAUSS Package Manager <https://www.aptech.com/blog/gauss-package-manager-basics/>`_ to install CMLMT.

Key Features
------------------------------

Statistical inference
+++++++++++++++++++++++++++++++

* Hypothesis testing for models with constrained parameters
* Inverted Hessian covariance matrix
* Heteroskedastic-consistent covariance matrix
* Wald confidence limits
* Likelihood ratio statistics
* Bootstrap
* Likelihood profile and Profile ‘t’ traces

Descent methods
+++++++++++++++++++++++++++++++

* BFGS (Broyden, Fletcher, Goldfarb and Powell)
* Newton
* DFP (Davidon, Fletcher and Powell)
* BHHH (Berndt, Hall, Hall, and Hausman)

Line search methods
+++++++++++++++++++++++++++++++

* STEPBT
* Brent’s method
* Half
* Strong Wolfe’s conditions

Constraint types
+++++++++++++++++++++++++++++++

* Linear equality and inequality constraints
* Nonlinear equality and inequality constraints
* Bounded parameters

Advantages
--------------------------------
Flexible
+++++++++++++++++

* Supports arbitrary user-provided nonlinear equality and inequality constraints.
* Linear equality and inequality constraints.
* Bounded parameters.
* Control trust region radius.
* Specify fixed and free parameters.
* Dynamic algorithm switching.
* Compute all, a subset, or none of the derivatives numerically.
* Easily pass data other than the model parameters as extra input arguments. New!
* Methods to simply create matrices needed for log-likelihood computation from subsets of the parameters.

Efficient
+++++++++++++++

* Threaded and thread-safe.
* Option to avoid computations that are the same for the log-likelihood function and derivatives.
* The tremendous speed of user-defined procedures in **GAUSS** speeds up your estimation.

Trusted
+++++++++++
For more than 30 years, leading researchers have trusted the efficient and numerically sound code in the GAUSS maximum likelihood estimation tools to keep them at the forefront of their fields.

Available Optimization Controls
--------------------------------
Optimization controls are set to default values that few users ever need to change.  However, COMT is fully customizable and the flexible optimization options can be a great help when tackling more difficult problems.

Control Options
+++++++++++++++++++++++++++++++

.. list-table::
   :widths: auto

   * - Nonlinear constraints
     - User defined procedures to create custom nonlinear equality and/or inequality constraints on the parameters.
   * - Linear constraints
     - Linear equality and/or inequality constraints on the parameters.
   * - Parameter bounds
     - Simple parameter bounds of the type: lower_bd ≤ x_i ≤ upper_bd.
   * - Descent algorithms
     - BFGS, DFP, Newton, and BHHH.
   * - Algorithm switching
     - Specify descent algorithms to switch between based upon the number of elapsed iterations, a minimum change in the objective function or line search step size.
   * - Weights
     - Observation weights.
   * - Covariance matrix type
     - Compute a ML covariance matrix, a QML covariance matrix, or none.
   * - Alpha
     - Probability level for statistical tests.
   * - Line search method
     - STEPBT (quadratic and cubic curve fit), Brent’s method, BHHHStep, half-step, or Strong Wolfe’s Conditions.
   * - Trust region
     - Activate or inactivate the trust region method and set the trust region size.
   * - Active parameters
     - Control which parameters are active (to be estimated) and which should be fixed to their start value.
   * - Gradient Method
     - Either compute an analytical gradient, or have CMLMT compute a numerical gradient using the forward, central, or backwards difference method.
   * - Jacobian of the constraints
     - Specify procedures to compute either the Jacobian of the equality or inequality constraints.
   * - Hessian Method
     - Either compute an analytical Hessian, or have CMLMT compute a numerical Hessian using the forward, central, or backwards difference method.
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
    :caption: Constrained Maximum Likelihood 

    user-guide
    command-reference
    cmlmt-examples



