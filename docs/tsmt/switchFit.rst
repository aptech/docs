=========
switchFit
=========

10.0.54switchFit
================

Purpose
-------

.. container::
   :name: Purpose

   Estimates the parameters of the Markov switching regression model.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   swo = switchFit(y, num_states, num_lags, swc);
   swo = switchFit(y, x, num_states, num_lags, swc);
   swo = switchFit(dataset, formula, num_states, num_lags);
   swo = switchFit(dataset, formula, num_states, num_lags, swc);

Input
-----

.. container::
   :name: Input

   +------------+-----------------+-----------------+-----------------+
   | y          | N×1 vector,     |                 |                 |
   |            | data.           |                 |                 |
   +------------+-----------------+-----------------+-----------------+
   | x          | N×k vector,     |                 |                 |
   |            | independent     |                 |                 |
   |            | data.           |                 |                 |
   +------------+-----------------+-----------------+-----------------+
   | dataset    | string, name of |                 |                 |
   |            | data set or     |                 |                 |
   |            | null string.    |                 |                 |
   +------------+-----------------+-----------------+-----------------+
   | formula    | string, formula |                 |                 |
   |            | string of the   |                 |                 |
   |            | model.          |                 |                 |
   |            | E.g. "y ~ X1 +  |                 |                 |
   |            | X2" 'y' is the  |                 |                 |
   |            | name of         |                 |                 |
   |            | dependent       |                 |                 |
   |            | variable, 'X1'  |                 |                 |
   |            | and 'X2' are    |                 |                 |
   |            | names of        |                 |                 |
   |            | independent     |                 |                 |
   |            | variables;      |                 |                 |
   |            | E.g. "y ~ ." ,  |                 |                 |
   |            | '.' means       |                 |                 |
   |            | including all   |                 |                 |
   |            | variables       |                 |                 |
   |            | except          |                 |                 |
   |            | dependent       |                 |                 |
   |            | variable 'y';   |                 |                 |
   +------------+-----------------+-----------------+-----------------+
   | num_states | scalar, number  |                 |                 |
   |            | of states.      |                 |                 |
   +------------+-----------------+-----------------+-----------------+
   | num_lags   | scalar, number  |                 |                 |
   |            | of lagged       |                 |                 |
   |            | values of the   |                 |                 |
   |            | dependent       |                 |                 |
   |            | variable.       |                 |                 |
   +------------+-----------------+-----------------+-----------------+
   | swc        | An instance of  |                 |                 |
   |            | a               |                 |                 |
   |            | switchFitCo     |                 |                 |
   |            | ntrolstructure. |                 |                 |
   |            | The following   |                 |                 |
   |            | members of swc  |                 |                 |
   |            | are referenced  |                 |                 |
   |            | within this     |                 |                 |
   |            | routine:        |                 |                 |
   +------------+-----------------+-----------------+-----------------+
   |            | sw              | scalar, if      |                 |
   |            | c.constVariance | nonzero, error  |                 |
   |            |                 | variances are   |                 |
   |            |                 | constant across |                 |
   |            |                 | states,         |                 |
   |            |                 | otherwise if    |                 |
   |            |                 | zero, not.      |                 |
   +------------+-----------------+-----------------+-----------------+
   |            | swc             | scalar, if      |                 |
   |            | .relevantStates | nonzero, lagged |                 |
   |            |                 | states are      |                 |
   |            |                 | relevant for    |                 |
   |            |                 | time series     |                 |
   |            |                 | variable,       |                 |
   |            |                 | otherwise if    |                 |
   |            |                 | zero, only the  |                 |
   |            |                 | current state   |                 |
   |            |                 | is relevant.    |                 |
   +------------+-----------------+-----------------+-----------------+
   |            | swc.aBayes      | scalar, if      |                 |
   |            |                 | nonzero, "a"    |                 |
   |            |                 | parameter       |                 |
   |            |                 | controlling the |                 |
   |            |                 | Bayesian prior  |                 |
   |            |                 | as described in |                 |
   |            |                 | James D.        |                 |
   |            |                 | Hamilton, 1991, |                 |
   |            |                 | "A              |                 |
   |            |                 | quasi-Bayesian  |                 |
   |            |                 | approach to     |                 |
   |            |                 | estimating      |                 |
   |            |                 | parameters for  |                 |
   |            |                 | mixtures of     |                 |
   |            |                 | Normal          |                 |
   |            |                 | distributions," |                 |
   |            |                 | Journal of      |                 |
   |            |                 | Business and    |                 |
   |            |                 | Economic        |                 |
   |            |                 | Statistics,     |                 |
   |            |                 | 9:27-39.        |                 |
   +------------+-----------------+-----------------+-----------------+
   |            | swc.bBayes      | scalar, if      |                 |
   |            |                 | nonzero, "b"    |                 |
   |            |                 | parameter       |                 |
   |            |                 | controlling the |                 |
   |            |                 | Bayesian prior. |                 |
   +------------+-----------------+-----------------+-----------------+
   |            | swc.cBayes      | scalar, if      |                 |
   |            |                 | nonzero, "c"    |                 |
   |            |                 | parameter       |                 |
   |            |                 | controlling the |                 |
   |            |                 | Bayesian prior. |                 |
   +------------+-----------------+-----------------+-----------------+
   |            | s               | scalar, pointer |                 |
   |            | wc.userTransEqp | to              |                 |
   |            |                 | user-provided   |                 |
   |            |                 | function for    |                 |
   |            |                 | setting         |                 |
   |            |                 | equality        |                 |
   |            |                 | constraints on  |                 |
   |            |                 | transition      |                 |
   |            |                 | probability     |                 |
   |            |                 | matrix.         |                 |
   +------------+-----------------+-----------------+-----------------+
   |            | swc.start       | instance of a   |                 |
   |            |                 | PV structure    |                 |
   |            |                 | containing      |                 |
   |            |                 | start values.   |                 |
   +------------+-----------------+-----------------+-----------------+
   |            |                 | beta0           | 1, num_states   |
   |            |                 |                 | by 1 vector,    |
   |            |                 |                 | constants.      |
   +------------+-----------------+-----------------+-----------------+
   |            |                 | beta            | 2, num_states   |
   |            |                 |                 | by K,           |
   |            |                 |                 | coefficients on |
   |            |                 |                 | K independent   |
   |            |                 |                 | variables if    |
   |            |                 |                 | any.            |
   +------------+-----------------+-----------------+-----------------+
   |            |                 | phi             | 3, num_lags by  |
   |            |                 |                 | 1 vector,       |
   |            |                 |                 | autoregression  |
   |            |                 |                 | coefficients.   |
   +------------+-----------------+-----------------+-----------------+
   |            |                 | sigma           | 4, scalar or    |
   |            |                 |                 | num_states by 1 |
   |            |                 |                 | vector, error   |
   |            |                 |                 | variances. If   |
   |            |                 |                 | swc.            |
   |            |                 |                 | constVarianceis |
   |            |                 |                 | zero, it is a   |
   |            |                 |                 | scalar,         |
   |            |                 |                 | otherwise it is |
   |            |                 |                 | a vector.       |
   +------------+-----------------+-----------------+-----------------+
   |            |                 | p               | 5, num_states   |
   |            |                 |                 | by num_states   |
   |            |                 |                 | matrix,         |
   |            |                 |                 | transition      |
   |            |                 |                 | probabilities.  |
   +------------+-----------------+-----------------+-----------------+
   |            |                 | For example:    |                 |
   |            |                 |                 |                 |
   |            |                 | ::              |                 |
   |            |                 |                 |                 |
   |            |                 |    swc.         |                 |
   |            |                 | start = pvPacki |                 |
   |            |                 |                 |                 |
   |            |                 | (swc.start, 3|- |                 |
   |            |                 | 3, "beta0", 1); |                 |
   |            |                 |    swc.         |                 |
   |            |                 | start = pvPacki |                 |
   |            |                 |                 |                 |
   |            |                 |   (swc.start,.1 |                 |
   |            |                 | |.01,"Phi", 3); |                 |
   |            |                 |    swc.         |                 |
   |            |                 | start = pvPacki |                 |
   |            |                 |                 |                 |
   |            |                 |    (swc.start,  |                 |
   |            |                 | 1, "Sigma", 4); |                 |
   |            |                 |    swc.         |                 |
   |            |                 | start = pvPacki |                 |
   |            |                 |                 |                 |
   |            |                 |        (swc.sta |                 |
   |            |                 | rt, (.8˜.1)|(.2 |                 |
   |            |                 | ˜.9), "P", 5);  |                 |
   +------------+-----------------+-----------------+-----------------+
   |            | swc.ctl         | instance of an  |                 |
   |            |                 | sq              |                 |
   |            |                 | psolvemtControl |                 |
   |            |                 | structure.      |                 |
   +------------+-----------------+-----------------+-----------------+
   |            |                 | swc.ctl.covType | scalar, if 2,   |
   |            |                 |                 | QML standard    |
   |            |                 |                 | errors are      |
   |            |                 |                 | computed, if 0, |
   |            |                 |                 | none; otherwise |
   |            |                 |                 | Wald-type.      |
   +------------+-----------------+-----------------+-----------------+
   |            |                 | swc             | scalar,         |
   |            |                 | .ctl.printIters | iteration       |
   |            |                 |                 | information     |
   |            |                 |                 | printed every   |
   |            |                 |                 | swc.ct          |
   |            |                 |                 | l.printIters-th |
   |            |                 |                 | iteration.      |
   +------------+-----------------+-----------------+-----------------+
   |            |                 | See             |                 |
   |            |                 | documentation   |                 |
   |            |                 | for             |                 |
   |            |                 | sq              |                 |
   |            |                 | psolvemtControl |                 |
   |            |                 | for further     |                 |
   |            |                 | information     |                 |
   |            |                 | regarding       |                 |
   |            |                 | members of this |                 |
   |            |                 | structure.      |                 |
   +------------+-----------------+-----------------+-----------------+
   |            | swc.header      | string,         |                 |
   |            |                 | specifies the   |                 |
   |            |                 | format for the  |                 |
   |            |                 | output header.  |                 |
   |            |                 | swc.header can  |                 |
   |            |                 | contain zero or |                 |
   |            |                 | more of the     |                 |
   |            |                 | following       |                 |
   |            |                 | characters:     |                 |
   +------------+-----------------+-----------------+-----------------+
   |            |                 | t               | title is to be  |
   |            |                 |                 | printed.        |
   +------------+-----------------+-----------------+-----------------+
   |            |                 | l               | lines are to    |
   |            |                 |                 | bracket the     |
   |            |                 |                 | title.          |
   +------------+-----------------+-----------------+-----------------+
   |            |                 | d               | a date and time |
   |            |                 |                 | is to be        |
   |            |                 |                 | printed.        |
   +------------+-----------------+-----------------+-----------------+
   |            |                 | v               | version number  |
   |            |                 |                 | of program is   |
   |            |                 |                 | to be printed.  |
   +------------+-----------------+-----------------+-----------------+
   |            |                 | f               | file name being |
   |            |                 |                 | analyzed is to  |
   |            |                 |                 | be printed.     |
   +------------+-----------------+-----------------+-----------------+
   |            |                 | Example:        |                 |
   |            |                 |                 |                 |
   |            |                 | ::              |                 |
   |            |                 |                 |                 |
   |            |                 |    swc.         |                 |
   |            |                 | header = "tld"; |                 |
   |            |                 |                 |                 |
   |            |                 | If              |                 |
   |            |                 | s               |                 |
   |            |                 | wc.header = "", |                 |
   |            |                 | no header is    |                 |
   |            |                 | printed.        |                 |
   |            |                 | Def             |                 |
   |            |                 | ault = "tldvf". |                 |
   +------------+-----------------+-----------------+-----------------+
   |            | swc.output      | scalar, if      |                 |
   |            |                 | nonzero,        |                 |
   |            |                 | results are     |                 |
   |            |                 | printed to      |                 |
   |            |                 | screen. Default |                 |
   |            |                 | = 1 .           |                 |
   +------------+-----------------+-----------------+-----------------+

Output
------

.. container::
   :name: Output

   +-----+-------------------+-------------------+-------------------+
   | out | An instance of a  |                   |                   |
   |     | switchmtOut       |                   |                   |
   |     | structure         |                   |                   |
   |     | containing the    |                   |                   |
   |     | following         |                   |                   |
   |     | members:          |                   |                   |
   +-----+-------------------+-------------------+-------------------+
   |     | out.par           | instance of a PV  |                   |
   |     |                   | structure         |                   |
   |     |                   | containing the    |                   |
   |     |                   | estimates:        |                   |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | beta0             | 1, num_states×1   |
   |     |                   |                   | vector,           |
   |     |                   |                   | constants.        |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | beta              | 2, num_states×K,  |
   |     |                   |                   | coefficients on K |
   |     |                   |                   | independent       |
   |     |                   |                   | variables if any. |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | phi               | 3, num_lags×1     |
   |     |                   |                   | vector,           |
   |     |                   |                   | autoregression    |
   |     |                   |                   | coefficients.     |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | sigma             | 4, scalar or      |
   |     |                   |                   | num_states×1      |
   |     |                   |                   | vector, error     |
   |     |                   |                   | variances. If     |
   |     |                   |                   | vmc.constVariance |
   |     |                   |                   | is zero, it is a  |
   |     |                   |                   | scalar, otherwise |
   |     |                   |                   | it is a vector.   |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | p                 | 5,                |
   |     |                   |                   | num_              |
   |     |                   |                   | states×num_states |
   |     |                   |                   | matrix,           |
   |     |                   |                   | probabilities.    |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | For example,      |                   |
   |     |                   |                   |                   |
   |     |                   | ::                |                   |
   |     |                   |                   |                   |
   |     |                   |    consts =       |                   |
   |     |                   | pvUnpack(out.par, |                   |
   |     |                   |         "beta0"); |                   |
   |     |                   |                   |                   |
   |     |                   | or                |                   |
   |     |                   |                   |                   |
   |     |                   | ::                |                   |
   |     |                   |                   |                   |
   |     |                   |    consts = pvU   |                   |
   |     |                   | npack(out.par,1); |                   |
   +-----+-------------------+-------------------+-------------------+
   |     | out.covPar        | M×M matrix,       |                   |
   |     |                   | covariance matrix |                   |
   |     |                   | of parameters.    |                   |
   +-----+-------------------+-------------------+-------------------+
   |     | out.logl          | scalar,           |                   |
   |     |                   | log-likelihood at |                   |
   |     |                   | maximum.          |                   |
   +-----+-------------------+-------------------+-------------------+
   |     | out.retcode       | return code:      |                   |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | **0**             | normal            |
   |     |                   |                   | convergence.      |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | **1**             | forced exit.      |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | **2**             | maximum number of |
   |     |                   |                   | iterations        |
   |     |                   |                   | exceeded.         |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | **3**             | function          |
   |     |                   |                   | calculation       |
   |     |                   |                   | failed.           |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | **4**             | gradient          |
   |     |                   |                   | calculation       |
   |     |                   |                   | failed.           |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | **5**             | Hessian           |
   |     |                   |                   | calculation       |
   |     |                   |                   | failed.           |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | **6**             | line search       |
   |     |                   |                   | failed.           |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | **7**             | error with        |
   |     |                   |                   | constraints.      |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | **8**             | function complex. |
   +-----+-------------------+-------------------+-------------------+
   |     | out.lagr          | instance of       |                   |
   |     |                   | s                 |                   |
   |     |                   | qpsolvemtLagrange |                   |
   |     |                   | structure.        |                   |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | out.lagr.lineq    | M×1 vector,       |
   |     |                   |                   | Lagrangeans of    |
   |     |                   |                   | linear equality   |
   |     |                   |                   | constraints.      |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | out.lagr.nlineq   | N×1 vector,       |
   |     |                   |                   | Lagrangeans of    |
   |     |                   |                   | nonlinear         |
   |     |                   |                   | equality          |
   |     |                   |                   | constraints.      |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | out.lagr.linineq  | P×1 vector,       |
   |     |                   |                   | Lagrangeans of    |
   |     |                   |                   | linear inequality |
   |     |                   |                   | constraints.      |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | out.lagr.nlinineq | Q×1 vector,       |
   |     |                   |                   | Lagrangeans of    |
   |     |                   |                   | nonlinear         |
   |     |                   |                   | inequality        |
   |     |                   |                   | constraints.      |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | out.lagr.bounds   | K×2 matrix,       |
   |     |                   |                   | Lagrangeans of    |
   |     |                   |                   | bounds.           |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | Whenever a        |                   |
   |     |                   | constraint is     |                   |
   |     |                   | active, its       |                   |
   |     |                   | associated        |                   |
   |     |                   | Lagrangean will   |                   |
   |     |                   | be nonzero. For   |                   |
   |     |                   | any constraint    |                   |
   |     |                   | that is inactive  |                   |
   |     |                   | throughout the    |                   |
   |     |                   | iterations as     |                   |
   |     |                   | well as at        |                   |
   |     |                   | convergence, the  |                   |
   |     |                   | corresponding     |                   |
   |     |                   | Lagrangean matrix |                   |
   |     |                   | will be set to a  |                   |
   |     |                   | scalar missing    |                   |
   |     |                   | value.            |                   |
   +-----+-------------------+-------------------+-------------------+

Example
-------

.. container::
   :name: Remarks

   This example reproduces the results for the French exchange rate in
   “Long Swings in the Exchange Rate: Are They in the Data and Do
   Markets Know It?” by Charles Engel and James D. Hamilton, American
   Economic Review, Sept. 1990.

   ::

      y0 = loadd( getGAUSSHome() $+ "pkgs/tsmt/examples/exdata.dat"); 


      y = y0[.,1];

      //Estimation parameters

      struct switchFitControl c0;
      c0 = switchFitControlCreate();

      c0.constVariance = 0;
      c0.output = 1;
      c0.aBayes = .2;
      c0.bBayes = 1;
      c0.cBayes = .1;

       /*
      ** The log-likelihood is somewhat flat and thus 
      ** the problem requires a good starting point.
      */

      b0 = { 3.3, -2.7 };
      sig = { 10, 37 };
      p = { .8 .2, .2 .8 };

      struct PV st0;
      st0 = pvPacki(pvCreate(), b0, "beta0", 1);
      st0 = pvPacki(st0, sig, "sigma", 4);
      st0 = pvPacki(st0, p, "p", 5);

      c0.start = st0;

      struct switchmtOut out0;
      out0 = switchFit(y, 2, 0, c0);

Source
------

.. container:: gfunc
   :name: Source

   switchmt.src
