Linear Programming MT
============================
Tools to solve small and large scale linear programming problems.

Description
----------------
**Linear Programming MT** is designed to solve small and large scale linear programming problems. **LPMT** exploits sparse matrices and thread-safe execution to tackle even large scale constraint problems with ease. User specified starting values can be initialized to further streamline problems and reduce the number of iterations. ​

**Linear Programming MT** Module solves the standard linear programming problem with the following features:

* **Thread-safe Execution:** Control variables are model matrices are contained in structures allowing thread-safe execution of programs.  
* **Sparse matrices:** Linear Programming MT exploits sparse matrix technology permitting the analysis of problems with very large constraint matrices. The size of a problem that can be analyzed is dependent on the speed and amount of memory on the computer, but problems with two to three thousand constraints and more than six thousand variables have been tested on ordinary PC's.    
* **MPS files:** Procedures are available for translating MPS formatted files.  

Installation
--------------
If you're interested in purchasing **LPMT** Please `contact us <https://www.aptech.com/contact-us>`_ to request pricing and installation information.

If you already own **LPMT** , you can use the `GAUSS Package Manager <https://www.aptech.com/blog/gauss-package-manager-basics/>`_ for quick download and installation.

Requires GAUSS/GAUSS Engine/GAUSS Light v8.0 or higher.

Key Features
------------------------------

Model Controls
++++++++++++++++++++++++

* Upper and lower finite bounds can be provided for variables and constraints.  
* Problem type (minimization or maximization).  
* Constraint types (<=, >=, =).  
* Choice of tolerances.  
* Pivoting rules.  
* Thread-safe execution.  
* Handling of sparse matrices.  
* Compatible with MPS files.  

Computed output
++++++++++++++++++

* The value of the variables and the objective function upon termination, and returns the dual variables.  
* State of each constraint
Uniqueness and quality of solution.  
* Multiple optimal solutions if they exist.  
* Number of iterations required.  
* A final basis.  
* Optional iterations log and/or final report.  