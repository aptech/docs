======
ecmFit
======

10.0.19ecmFit
=============

Purpose
-------

.. container::
   :name: Purpose

   Calculate and return parameter estimates for an error correction
   model.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   vmo = ecmFit(y, p);
   vmo = ecmFit(y, p, vmc);
   vmo = ecmFit(dataset, formula, p);
   vmo = ecmFit(dataset, formula, p, vmc);

Input
-----

.. container::
   :name: Input

   +---------+------------------+------------------+------------------+
   | y       | N×1 vector,      |                  |                  |
   |         | data.            |                  |                  |
   +---------+------------------+------------------+------------------+
   | dataset | string, name of  |                  |                  |
   |         | data set or null |                  |                  |
   |         | string.          |                  |                  |
   +---------+------------------+------------------+------------------+
   | formula | string, formula  |                  |                  |
   |         | string of the    |                  |                  |
   |         | model.           |                  |                  |
   |         | E.g. "y ~ X1 +   |                  |                  |
   |         | X2" 'y' is the   |                  |                  |
   |         | name of          |                  |                  |
   |         | dependent        |                  |                  |
   |         | variable, 'X1'   |                  |                  |
   |         | and 'X2' are     |                  |                  |
   |         | names of         |                  |                  |
   |         | independent      |                  |                  |
   |         | variables;       |                  |                  |
   |         | E.g. "y ~ ." ,   |                  |                  |
   |         | '.' means        |                  |                  |
   |         | including all    |                  |                  |
   |         | variables except |                  |                  |
   |         | dependent        |                  |                  |
   |         | variable 'y';    |                  |                  |
   +---------+------------------+------------------+------------------+
   | p       | scalar, order of |                  |                  |
   |         | AR process.      |                  |                  |
   +---------+------------------+------------------+------------------+
   | vmc     | Optional input,  |                  |                  |
   |         | an instance of a |                  |                  |
   |         | varmamtC         |                  |                  |
   |         | ontrolstructure. |                  |                  |
   |         | The following    |                  |                  |
   |         | members of vmc   |                  |                  |
   |         | are referenced   |                  |                  |
   |         | within this      |                  |                  |
   |         | routine:         |                  |                  |
   +---------+------------------+------------------+------------------+
   |         | vmc.rho          | scalar, number   |                  |
   |         |                  | of cointegrating |                  |
   |         |                  | relations. Set   |                  |
   |         |                  | to -1 to have    |                  |
   |         |                  | GAUSS estimate   |                  |
   |         |                  | this value.      |                  |
   |         |                  | Default = 0.     |                  |
   +---------+------------------+------------------+------------------+
   |         | vmc.header       | string,          |                  |
   |         |                  | specifies the    |                  |
   |         |                  | format for the   |                  |
   |         |                  | output header.   |                  |
   |         |                  | vmc.header can   |                  |
   |         |                  | contain zero or  |                  |
   |         |                  | more of the      |                  |
   |         |                  | following        |                  |
   |         |                  | characters:      |                  |
   +---------+------------------+------------------+------------------+
   |         |                  | t                | title is to be   |
   |         |                  |                  | printed.         |
   +---------+------------------+------------------+------------------+
   |         |                  | l                | lines are to     |
   |         |                  |                  | bracket the      |
   |         |                  |                  | title.           |
   +---------+------------------+------------------+------------------+
   |         |                  | d                | a date and time  |
   |         |                  |                  | is to be         |
   |         |                  |                  | printed.         |
   +---------+------------------+------------------+------------------+
   |         |                  | v                | version number   |
   |         |                  |                  | of program is to |
   |         |                  |                  | be printed.      |
   +---------+------------------+------------------+------------------+
   |         |                  | f                | file name being  |
   |         |                  |                  | analyzed is to   |
   |         |                  |                  | be printed.      |
   +---------+------------------+------------------+------------------+
   |         |                  | Example:         |                  |
   |         |                  |                  |                  |
   |         |                  | ::               |                  |
   |         |                  |                  |                  |
   |         |                  |    vmc           |                  |
   |         |                  | .header = "tld"; |                  |
   |         |                  |                  |                  |
   |         |                  | If               |                  |
   |         |                  | vmc.header = "", |                  |
   |         |                  | no header is     |                  |
   |         |                  | printed.         |                  |
   |         |                  | De               |                  |
   |         |                  | fault = "tldvf". |                  |
   +---------+------------------+------------------+------------------+
   |         | vmc.indEquations | K×L matrix of    |                  |
   |         |                  | zeros and ones.  |                  |
   |         |                  | Used to set zero |                  |
   |         |                  | restrictions on  |                  |
   |         |                  | the *x*          |                  |
   |         |                  | variables to be  |                  |
   |         |                  | estimated. Used  |                  |
   |         |                  | only if the      |                  |
   |         |                  | number of        |                  |
   |         |                  | equations,       |                  |
   |         |                  | vmc.L, is        |                  |
   |         |                  | greater than     |                  |
   |         |                  | one. Elements    |                  |
   |         |                  | set to one       |                  |
   |         |                  | indicate the     |                  |
   |         |                  | coefficients to  |                  |
   |         |                  | be estimated. If |                  |
   |         |                  | vmc.L = 1, all   |                  |
   |         |                  | coefficients     |                  |
   |         |                  | will be          |                  |
   |         |                  | estimated. If    |                  |
   |         |                  | vmc.L > 1 and    |                  |
   |         |                  | vmc.indEquations |                  |
   |         |                  | is set to a      |                  |
   |         |                  | missing value    |                  |
   |         |                  | (the default),   |                  |
   |         |                  | all coefficients |                  |
   |         |                  | will be          |                  |
   |         |                  | estimated.       |                  |
   +---------+------------------+------------------+------------------+
   |         | vmc.lags         | scalar, number   |                  |
   |         |                  | of lags over     |                  |
   |         |                  | which ACF and    |                  |
   |         |                  | Diagnostics are  |                  |
   |         |                  | calculated.      |                  |
   |         |                  | Default = 12.    |                  |
   +---------+------------------+------------------+------------------+
   |         | vmc.start        | Instance of a PV |                  |
   |         |                  | structure        |                  |
   |         |                  | containing       |                  |
   |         |                  | starting values. |                  |
   |         |                  | See              |                  |
   |         |                  | `VES-Starting    |                  |
   |         |                  | Values           |                  |
   |         |                  |  <VES.7.2-Starti |                  |
   |         |                  | ngValues.htm>`__ |                  |
   |         |                  | for an example.  |                  |
   +---------+------------------+------------------+------------------+
   |         | vmc.nodet        | scalar. Set      |                  |
   |         |                  | vmc.nodet = 1 to |                  |
   |         |                  | suppress the     |                  |
   |         |                  | constant term    |                  |
   |         |                  | from the fitted  |                  |
   |         |                  | regression and   |                  |
   |         |                  | include it in    |                  |
   |         |                  | the              |                  |
   |         |                  | co-integrating   |                  |
   |         |                  | regression;      |                  |
   |         |                  | otherwise, set   |                  |
   |         |                  | vmc.nodet = 0.   |                  |
   |         |                  | Default = 0.     |                  |
   +---------+------------------+------------------+------------------+
   |         | vmc.nwtrunc      | scalar, the      |                  |
   |         |                  | number of        |                  |
   |         |                  | autocorrelations |                  |
   |         |                  | to use in        |                  |
   |         |                  | calculating the  |                  |
   |         |                  | Newey-West       |                  |
   |         |                  | correction. If   |                  |
   |         |                  | vmc.nwtrunc = 0, |                  |
   |         |                  | GAUSS will use a |                  |
   |         |                  | truncation lag   |                  |
   |         |                  | given by Newey   |                  |
   |         |                  | and West,        |                  |
   |         |                  | vmc.nw           |                  |
   |         |                  | trunc\ |image3|. |                  |
   +---------+------------------+------------------+------------------+
   |         | vmc.ctl          | An instance of   |                  |
   |         |                  | an               |                  |
   |         |                  | s                |                  |
   |         |                  | qpsolvemtControl |                  |
   |         |                  | structure.       |                  |
   +---------+------------------+------------------+------------------+
   |         |                  | vmc.ctl.covType  | scalar, if 2,    |
   |         |                  |                  | QML standard     |
   |         |                  |                  | errors are       |
   |         |                  |                  | computed, if 0,  |
   |         |                  |                  | none; otherwise  |
   |         |                  |                  | Wald-type.       |
   +---------+------------------+------------------+------------------+
   |         |                  | vm               | scalar,          |
   |         |                  | c.ctl.printIters | iteration        |
   |         |                  |                  | information      |
   |         |                  |                  | printed every    |
   |         |                  |                  | swc.c            |
   |         |                  |                  | tl.printIters-th |
   |         |                  |                  | iteration.       |
   +---------+------------------+------------------+------------------+
   |         |                  | See              |                  |
   |         |                  | documentation    |                  |
   |         |                  | for              |                  |
   |         |                  | s                |                  |
   |         |                  | qpsolvemtControl |                  |
   |         |                  | for further      |                  |
   |         |                  | information      |                  |
   |         |                  | regarding        |                  |
   |         |                  | members of this  |                  |
   |         |                  | structure.       |                  |
   +---------+------------------+------------------+------------------+
   |         | vmc.olsqtol      | scalar, the      |                  |
   |         |                  | tolerance used   |                  |
   |         |                  | in determining   |                  |
   |         |                  | if diagonal      |                  |
   |         |                  | elements are     |                  |
   |         |                  | approaching zero |                  |
   |         |                  | in olsqrmt.      |                  |
   |         |                  | Default = 1e-14. |                  |
   +---------+------------------+------------------+------------------+
   |         | vmc.output       | scalar, if       |                  |
   |         |                  | nonzero, results |                  |
   |         |                  | are printed to   |                  |
   |         |                  | screen.          |                  |
   |         |                  | Default = 1.     |                  |
   +---------+------------------+------------------+------------------+
   |         | vmc.row          | scalar.          |                  |
   |         |                  | Specifies how    |                  |
   |         |                  | many rows of the |                  |
   |         |                  | dataset are to   |                  |
   |         |                  | be read per      |                  |
   |         |                  | iteration of the |                  |
   |         |                  | read loop. By    |                  |
   |         |                  | default, the     |                  |
   |         |                  | number of rows   |                  |
   |         |                  | to be read is    |                  |
   |         |                  | calculated by    |                  |
   |         |                  | ecmFit.          |                  |
   +---------+------------------+------------------+------------------+
   |         | vmc.scale        | scalar or an L×1 |                  |
   |         |                  | vector, scales   |                  |
   |         |                  | for the time     |                  |
   |         |                  | series. If       |                  |
   |         |                  | scalar, all      |                  |
   |         |                  | series are       |                  |
   |         |                  | multiplied by    |                  |
   |         |                  | the value. If an |                  |
   |         |                  | L×1 vector, each |                  |
   |         |                  | series is        |                  |
   |         |                  | multiplied by    |                  |
   |         |                  | the              |                  |
   |         |                  | corresponding    |                  |
   |         |                  | element of       |                  |
   |         |                  | vmc.scale.       |                  |
   |         |                  | Defa             |                  |
   |         |                  | ult = 4/standard |                  |
   |         |                  | deviation (found |                  |
   |         |                  | to be best by    |                  |
   |         |                  | e                |                  |
   |         |                  | xperimentation). |                  |
   +---------+------------------+------------------+------------------+
   |         | vm               | scalar, set to a |                  |
   |         | c.setConstraints | nonzero value to |                  |
   |         |                  | impose           |                  |
   |         |                  | stationarity and |                  |
   |         |                  | invertibility by |                  |
   |         |                  | constraining     |                  |
   |         |                  | roots of the AR  |                  |
   |         |                  | and MA           |                  |
   |         |                  | characteristic   |                  |
   |         |                  | equations to be  |                  |
   |         |                  | outside the unit |                  |
   |         |                  | circle. Set to   |                  |
   |         |                  | zero to estimate |                  |
   |         |                  | an unconstrained |                  |
   |         |                  | model.           |                  |
   |         |                  | Default = 1.     |                  |
   +---------+------------------+------------------+------------------+
   |         | vmc.title        | string, a title  |                  |
   |         |                  | to be printed at |                  |
   |         |                  | the top of the   |                  |
   |         |                  | output header    |                  |
   |         |                  | (see             |                  |
   |         |                  | vmc.header). By  |                  |
   |         |                  | default, no      |                  |
   |         |                  | title is printed |                  |
   |         |                  | (                |                  |
   |         |                  | vmc.title = ""). |                  |
   +---------+------------------+------------------+------------------+

Output
------

.. container::
   :name: Output

   +-----+-------------------+-------------------+-------------------+
   | vmo | An instance of a  |                   |                   |
   |     | varmamtOut        |                   |                   |
   |     | structure         |                   |                   |
   |     | containing the    |                   |                   |
   |     | following         |                   |                   |
   |     | members:          |                   |                   |
   +-----+-------------------+-------------------+-------------------+
   |     | vmo.aa            | L×r matrix of     |                   |
   |     |                   | coefficients,     |                   |
   |     |                   | such that         |                   |
   |     |                   | |image12| (see    |                   |
   |     |                   | remarks below).   |                   |
   +-----+-------------------+-------------------+-------------------+
   |     | vmo.acfm          | L×(p*L) matrix,   |                   |
   |     |                   | the               |                   |
   |     |                   | autocorrelaton    |                   |
   |     |                   | function. The     |                   |
   |     |                   | first *L* columns |                   |
   |     |                   | are the lag *l*   |                   |
   |     |                   | ACF; the last *L* |                   |
   |     |                   | columns are the   |                   |
   |     |                   | lag *p* ACF.      |                   |
   +-----+-------------------+-------------------+-------------------+
   |     | vmo.aic           | L×1 vector, the   |                   |
   |     |                   | Akaike            |                   |
   |     |                   | Information       |                   |
   |     |                   | Criterion.        |                   |
   +-----+-------------------+-------------------+-------------------+
   |     | vmo.arroots       | p×1 vector of AR  |                   |
   |     |                   | roots, possibly   |                   |
   |     |                   | complex.          |                   |
   +-----+-------------------+-------------------+-------------------+
   |     | vmo.bb            | r×L matrix,       |                   |
   |     |                   | eigenvectors      |                   |
   |     |                   | spanning the      |                   |
   |     |                   | cointegrating     |                   |
   |     |                   | space of          |                   |
   |     |                   | dimension *r*.    |                   |
   +-----+-------------------+-------------------+-------------------+
   |     | vmo.bic           | L×1 vector, the   |                   |
   |     |                   | Schwarz Bayesian  |                   |
   |     |                   | Information       |                   |
   |     |                   | Criterion.        |                   |
   +-----+-------------------+-------------------+-------------------+
   |     | vmo.covpar        | Q×Q matrix of     |                   |
   |     |                   | estimated         |                   |
   |     |                   | parameters where  |                   |
   |     |                   | Q is the number   |                   |
   |     |                   | of estimated      |                   |
   |     |                   | parameters. The   |                   |
   |     |                   | parameters are in |                   |
   |     |                   | the row-major     |                   |
   |     |                   | order: |image13|, |                   |
   |     |                   | |image14| to      |                   |
   |     |                   | |image15|, *beta* |                   |
   |     |                   | (if *x* variables |                   |
   |     |                   | were present in   |                   |
   |     |                   | the estimation),  |                   |
   |     |                   | and the           |                   |
   |     |                   | constants.        |                   |
   +-----+-------------------+-------------------+-------------------+
   |     | vmo.fct           | L×1 vector, the   |                   |
   |     |                   | likelihood value. |                   |
   +-----+-------------------+-------------------+-------------------+
   |     | vmo.lagr          | An instance of an |                   |
   |     |                   | s                 |                   |
   |     |                   | qpsolvemtLagrange |                   |
   |     |                   | structure         |                   |
   |     |                   | containing the    |                   |
   |     |                   | following         |                   |
   |     |                   | members:          |                   |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | vmo.lagr.lineq    | linear equality   |
   |     |                   |                   | constraints.      |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | vmo.lagr.nlineq   | nonlinear         |
   |     |                   |                   | equality          |
   |     |                   |                   | constraints.      |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | vmo.lagr.linineq  | linear inequality |
   |     |                   |                   | constraints.      |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | vmo.lagr.nlinineq | nonlinear         |
   |     |                   |                   | inequality        |
   |     |                   |                   | constraints.      |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | vmo.lagr.bounds   | bounds.           |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | When an           |                   |
   |     |                   | inequality or     |                   |
   |     |                   | bounds constraint |                   |
   |     |                   | is active, its    |                   |
   |     |                   | associated        |                   |
   |     |                   | Lagrangean is     |                   |
   |     |                   | nonzero. The      |                   |
   |     |                   | linear            |                   |
   |     |                   | Lagrangeans       |                   |
   |     |                   | precede the       |                   |
   |     |                   | nonlinear         |                   |
   |     |                   | Lagrangeans in    |                   |
   |     |                   | the covariance    |                   |
   |     |                   | matrices.         |                   |
   +-----+-------------------+-------------------+-------------------+
   |     | vmo.lrs           | L×1 vector, the   |                   |
   |     |                   | likelihood ratio  |                   |
   |     |                   | statistic.        |                   |
   +-----+-------------------+-------------------+-------------------+
   |     | vmo.maroots       | q×1 vector of MA  |                   |
   |     |                   | roots, possibly   |                   |
   |     |                   | complex.          |                   |
   +-----+-------------------+-------------------+-------------------+
   |     | vmo.pacfm         | L×p*L) matrix,    |                   |
   |     |                   | the partial       |                   |
   |     |                   | autocorrelation   |                   |
   |     |                   | function,         |                   |
   |     |                   | computed only if  |                   |
   |     |                   | a univariate      |                   |
   |     |                   | model is          |                   |
   |     |                   | estimated. The    |                   |
   |     |                   | first *L* columns |                   |
   |     |                   | are the lag *1*   |                   |
   |     |                   | ACF; the last *L* |                   |
   |     |                   | columns are the   |                   |
   |     |                   | lag *p* ACF.      |                   |
   +-----+-------------------+-------------------+-------------------+
   |     | vmo.par           | An instance of a  |                   |
   |     |                   | PV structure      |                   |
   |     |                   | containing the    |                   |
   |     |                   | parameter         |                   |
   |     |                   | estimates, which  |                   |
   |     |                   | can be retrieved  |                   |
   |     |                   | using pvUnpack.   |                   |
   |     |                   | For example,      |                   |
   |     |                   |                   |                   |
   |     |                   | ::                |                   |
   |     |                   |                   |                   |
   |     |                   |    struct         |                   |
   |     |                   |  varmamtOut vout; |                   |
   |     |                   |    vout           |                   |
   |     |                   | = varmaFit(y, 2); |                   |
   |     |                   |                   |                   |
   |     |                   |   ph = pvUnpack(v |                   |
   |     |                   | out.par, "zeta"); |                   |
   |     |                   |    th = pvUnpack  |                   |
   |     |                   | (vout.par, "pi"); |                   |
   |     |                   |    vc = pvUnpack  |                   |
   |     |                   | (vout.par, "vc"); |                   |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | The complete set  |                   |
   |     |                   | of parameter      |                   |
   |     |                   | matrices and      |                   |
   |     |                   | arrays that can   |                   |
   |     |                   | be unpacked       |                   |
   |     |                   | depending on the  |                   |
   |     |                   | model is:         |                   |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | phi               | L×p×p array,      |
   |     |                   |                   | autoregression    |
   |     |                   |                   | coefficients.     |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | theta             | L×q×q array,      |
   |     |                   |                   | moving average    |
   |     |                   |                   | coefficients.     |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | vc                | L×L residual      |
   |     |                   |                   | covariance        |
   |     |                   |                   | matrix.           |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | beta              | L×K regression    |
   |     |                   |                   | coefficient       |
   |     |                   |                   | matrix.           |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | beta0             | L×1 constant      |
   |     |                   |                   | vector.           |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | zeta              | L×p×ar array of   |
   |     |                   |                   | ecm coefficients. |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | pi                | L×L matrix. *Note |
   |     |                   |                   | that 'pi' is a    |
   |     |                   |                   | reserved word in  |
   |     |                   |                   | GAUSS. Users will |
   |     |                   |                   | need to assign    |
   |     |                   |                   | this to a         |
   |     |                   |                   | different         |
   |     |                   |                   | variable name.*   |
   +-----+-------------------+-------------------+-------------------+
   |     | vmo.portman       | vmc.lags-(p+q)×3  |                   |
   |     |                   | matrix of         |                   |
   |     |                   | portmanteau       |                   |
   |     |                   | statistics for    |                   |
   |     |                   | the multivariate  |                   |
   |     |                   | model and         |                   |
   |     |                   | Ljung-Box         |                   |
   |     |                   | statistics for    |                   |
   |     |                   | the univariate    |                   |
   |     |                   | model. The time   |                   |
   |     |                   | period is in      |                   |
   |     |                   | column one, the   |                   |
   |     |                   | *Qs*              |                   |
   |     |                   | (portmanteau)     |                   |
   |     |                   | statistic in      |                   |
   |     |                   | column two and    |                   |
   |     |                   | the p_value in    |                   |
   |     |                   | column three.     |                   |
   +-----+-------------------+-------------------+-------------------+
   |     | vmo.residuals     | T×L matrix,       |                   |
   |     |                   | residuals.        |                   |
   +-----+-------------------+-------------------+-------------------+
   |     | vmo.retcode       | 2×1 vector,       |                   |
   |     |                   | return code.      |                   |
   |     |                   | First element:    |                   |
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
   |     |                   | Second element:   |                   |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | **0**             | covariance matrix |
   |     |                   |                   | of parameters     |
   |     |                   |                   | failed.           |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | **1**             | ML covariance     |
   |     |                   |                   | matrix.           |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | **2**             | QML covariance    |
   |     |                   |                   | matrix.           |
   +-----+-------------------+-------------------+-------------------+
   |     |                   | **3**             | Cross-Product     |
   |     |                   |                   | covariance        |
   |     |                   |                   | matrix.           |
   +-----+-------------------+-------------------+-------------------+
   |     | vmo.ss            | L×2 matrix, the   |                   |
   |     |                   | sum of squares    |                   |
   |     |                   | for Y in column   |                   |
   |     |                   | one and the sum   |                   |
   |     |                   | of squared error  |                   |
   |     |                   | in column two.    |                   |
   +-----+-------------------+-------------------+-------------------+
   |     | vmo.va            | r×1 vector,       |                   |
   |     |                   | eigenvalues.      |                   |
   +-----+-------------------+-------------------+-------------------+

Remarks
-------

.. container::
   :name: Remarks

   Errors are assumed to be distributed N(0, Q).

Example
-------

.. container::
   :name: Example

   ::

      new;
      cls,;
      library tsmt;

      //Load data
      fname = getGAUSSHome() $+ "pkgs/tsmt/examples/ecmmt.csv";
      y = csvReadM(fname, 1, 2);

      y = vmdiffmt(y, 1);

      //Declare varmamt control structure
      struct varmamtControl vmc;

      //Initialize control structure with default values
      vmc = varmamtControlCreate;

      //No contraints
      vmc.setConstraints = 0;

      //Set up start values
      phi = { 0.05 -0.05, 0 0.01, 0.1 -0.07, 0.05 -0.04 };
      vmc.start = pvcreate();
      vmc.start = pvPacki(vmc.start,areshape(phi, 2|2|2), "phi", 1);
      vmc.start = pvPacksi(vmc.start, xpnd(15.9521|14.2525|15.9908), "vc", 3);

      //Call ecmFit
      struct varmamtOut vout;
      vout = ecmFit(y , 1, vmc); 

Source
------

.. container:: gfunc
   :name: Source

   varmamt.src

.. |image1| image:: _static/images/Equation693.svg
   :class: _inline_math_MCEquation1 mcReset
.. |image2| image:: _static/images/Equation693.svg
   :class: _inline_math_MCEquation1 mcReset
.. |image3| image:: _static/images/Equation693.svg
   :class: _inline_math_MCEquation1 mcReset
.. |image4| image:: _static/images/Equation694.svg
   :class: _inline_math_MCEquation_0 mcReset
.. |image5| image:: _static/images/Equation695.svg
   :class: _inline_math_MCEquation_0 mcReset
.. |image6| image:: _static/images/Equation696.svg
   :class: _inline_math_MCEquation_0 mcReset
.. |image7| image:: _static/images/Equation697.svg
   :class: _inline_math_MCEquation_0 mcReset
.. |image8| image:: _static/images/Equation694.svg
   :class: _inline_math_MCEquation_0 mcReset
.. |image9| image:: _static/images/Equation695.svg
   :class: _inline_math_MCEquation_0 mcReset
.. |image10| image:: _static/images/Equation696.svg
   :class: _inline_math_MCEquation_0 mcReset
.. |image11| image:: _static/images/Equation697.svg
   :class: _inline_math_MCEquation_0 mcReset
.. |image12| image:: _static/images/Equation694.svg
   :class: _inline_math_MCEquation_0 mcReset
.. |image13| image:: _static/images/Equation695.svg
   :class: _inline_math_MCEquation_0 mcReset
.. |image14| image:: _static/images/Equation696.svg
   :class: _inline_math_MCEquation_0 mcReset
.. |image15| image:: _static/images/Equation697.svg
   :class: _inline_math_MCEquation_0 mcReset
