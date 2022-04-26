========
garchFit
========

10.0.20garchFit
===============

Purpose
-------

.. container::
   :name: Purpose

   Estimates univariate GARCH model.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   out1 = garchFit(y, p);
   out1 = garchFit(y, p, c0);
   out1 = garchFit(y, p, q);
   out1 = garchFit(y, p, q, c0);
   out1 = garchFit(dataset, formula, p);
   out1 = garchFit(dataset, formula, p, c0);
   out1 = garchFit(dataset, formula, p, q);
   out1 = garchFit(dataset, formula, p, q, c0);

Input
-----

.. container::
   :name: Input

   +---------+----------------------------+----------------------------+
   | y       | Matrix, dependent          |                            |
   |         | variables.                 |                            |
   +---------+----------------------------+----------------------------+
   | x       | Matrix, independent        |                            |
   |         | variables.                 |                            |
   +---------+----------------------------+----------------------------+
   | dataset | string, name of data set   |                            |
   |         | or null string.            |                            |
   +---------+----------------------------+----------------------------+
   | formula | string, formula string of  |                            |
   |         | the model.                 |                            |
   |         | E.g. "y ~ X1 + X2" 'y' is  |                            |
   |         | the name of dependent      |                            |
   |         | variable, 'X1' and 'X2'    |                            |
   |         | are names of independent   |                            |
   |         | variables;                 |                            |
   |         | E.g. "y ~ ." , '.' means   |                            |
   |         | including all variables    |                            |
   |         | except dependent variable  |                            |
   |         | 'y';                       |                            |
   +---------+----------------------------+----------------------------+
   | p       | scalar, order of the GARCH |                            |
   |         | parameters.                |                            |
   +---------+----------------------------+----------------------------+
   | q       | >Optional input, scalar,   |                            |
   |         | order of the ARCH          |                            |
   |         | parameters.                |                            |
   +---------+----------------------------+----------------------------+
   | c0      | Optional input,            |                            |
   |         | garchControl structure.    |                            |
   +---------+----------------------------+----------------------------+
   |         | c0.density                 | scalar, density of error   |
   |         |                            | term, 0 - Normal, 1 -      |
   |         |                            | Student's t, 3 - skew      |
   |         |                            | generalized t.             |
   +---------+----------------------------+----------------------------+
   |         | c0.asymmetry               | scalar, if nonzero         |
   |         |                            | assymetry terms are added. |
   +---------+----------------------------+----------------------------+
   |         | c0.inmean                  | scalar, GARCH-in-mean,     |
   |         |                            | square root of conditional |
   |         |                            | variance is included in    |
   |         |                            | the mean equation.         |
   +---------+----------------------------+----------------------------+
   |         | c0.stConstraintsType       | scalar, type of            |
   |         |                            | enforcement of             |
   |         |                            | stationarity requirements, |
   |         |                            | 1 - roots of               |
   |         |                            | characteristic polynomial  |
   |         |                            | constrained outside unit   |
   |         |                            | circle, 2 - arch, GARCH    |
   |         |                            | parameters constrained to  |
   |         |                            | sum to less than one and   |
   |         |                            | greater than zero, 3 -     |
   |         |                            | none.                      |
   +---------+----------------------------+----------------------------+
   |         | c0.cvConstraintsType       | scalar, type of            |
   |         |                            | enforcement of nonnegative |
   |         |                            | conditional variances, 0 - |
   |         |                            | direct constraints, 1 -    |
   |         |                            | Nelson & Cao constraints.  |
   +---------+----------------------------+----------------------------+
   |         | c0.covType                 | scalar, type of covariance |
   |         |                            | matrix of parameters, 1 -  |
   |         |                            | ML, 2 - QML, 3 - none.     |
   +---------+----------------------------+----------------------------+

Output
------

.. container::
   :name: Output

   +------+-------------------+-------------------+-------------------+
   | out1 | garchEstimation   |                   |                   |
   |      | structure         |                   |                   |
   |      | containing the    |                   |                   |
   |      | following         |                   |                   |
   |      | members:          |                   |                   |
   +------+-------------------+-------------------+-------------------+
   |      | out1.aic          | scalar, Akiake    |                   |
   |      |                   | criterion.        |                   |
   +------+-------------------+-------------------+-------------------+
   |      | out1.bic          | scalar, Bayesian  |                   |
   |      |                   | information       |                   |
   |      |                   | criterion.        |                   |
   +------+-------------------+-------------------+-------------------+
   |      | out1.lrs          | scalar,           |                   |
   |      |                   | likelihood ratio  |                   |
   |      |                   | statistic.        |                   |
   +------+-------------------+-------------------+-------------------+
   |      | out1.numObs       | scalar, number of |                   |
   |      |                   | observations.     |                   |
   +------+-------------------+-------------------+-------------------+
   |      | out1.df           | scalar, degrees   |                   |
   |      |                   | of freedom.       |                   |
   +------+-------------------+-------------------+-------------------+
   |      | out1.par          | instance of PV    |                   |
   |      |                   | structure         |                   |
   |      |                   | containing        |                   |
   |      |                   | parameter         |                   |
   |      |                   | estimates.        |                   |
   +------+-------------------+-------------------+-------------------+
   |      | out1.retcode      | scalar, return    |                   |
   |      |                   | code.             |                   |
   +------+-------------------+-------------------+-------------------+
   |      |                   | 1                 | normal            |
   |      |                   |                   | convergence.      |
   +------+-------------------+-------------------+-------------------+
   |      |                   | 2                 | forced exit.      |
   +------+-------------------+-------------------+-------------------+
   |      |                   | 3                 | function          |
   |      |                   |                   | calculation       |
   |      |                   |                   | failed.           |
   +------+-------------------+-------------------+-------------------+
   |      |                   | 4                 | gradient          |
   |      |                   |                   | calculation       |
   |      |                   |                   | failed.           |
   +------+-------------------+-------------------+-------------------+
   |      |                   | 5                 | Hessian           |
   |      |                   |                   | calculation       |
   |      |                   |                   | failed.           |
   +------+-------------------+-------------------+-------------------+
   |      |                   | 6                 | line search       |
   |      |                   |                   | failed.           |
   +------+-------------------+-------------------+-------------------+
   |      |                   | 7                 | error with        |
   |      |                   |                   | constraints.      |
   +------+-------------------+-------------------+-------------------+
   |      |                   | 8                 | function complex. |
   +------+-------------------+-------------------+-------------------+
   |      | out1.moment       | K×K matrix,       |                   |
   |      |                   | moment matrix of  |                   |
   |      |                   | parameter         |                   |
   |      |                   | estimates.        |                   |
   +------+-------------------+-------------------+-------------------+
   |      | out1.climits      | K×2 matrix,       |                   |
   |      |                   | confidence        |                   |
   |      |                   | limits.           |                   |
   +------+-------------------+-------------------+-------------------+

Example
-------

.. container::
   :name: Example

   ::

      new;
      cls,;
      library tsmt;

      y = loadd( getGAUSSHome() $+ "pkgs/tsmt/examples/garch.dat");

      struct garchEstimation f0;
      f0 = garchFit(y, 1, 1);
        

Source
------

.. container:: gfunc
   :name: Source

   tsgarch.src
