========
varmaFit
========

10.0.62varmaFit
===============

Purpose
-------

.. container::
   :name: Purpose

   Computes exact maximum likelihood parameter estimates for a VARMA
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

   vmo = varmaFit( y, p );
   vmo = varmaFit( y, p, d );
   vmo = varmaFit( y, p, d, q );
   vmo = varmaFit( y, p, d, q, vmc );
   vmo = varmaFit( dataset, formula, p );
   vmo = varmaFit( dataset, formula, p, d );
   vmo = varmaFit( dataset, formula, p, d, q );
   vmo = varmaFit( dataset, formula, p, d, q, vmc );

Input
-----

.. container::
   :name: Input

   +---------+------------------+------------------+------------------+
   | y       | N×1 vector,      |                  |                  |
   |         | data.            |                  |                  |
   +---------+------------------+------------------+------------------+
   | x       | N×k vector,      |                  |                  |
   |         | independent      |                  |                  |
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
   |         | p                | scalar, order of |                  |
   |         |                  | AR process.      |                  |
   |         |                  | Default = 0.     |                  |
   +---------+------------------+------------------+------------------+
   |         | d                | Optional input,  |                  |
   |         |                  | scalar, the      |                  |
   |         |                  | order of         |                  |
   |         |                  | differencing to  |                  |
   |         |                  | achieve          |                  |
   |         |                  | stationarity.    |                  |
   |         |                  | Default = 0.     |                  |
   +---------+------------------+------------------+------------------+
   |         | q                | Optional input,  |                  |
   |         |                  | scalar, number   |                  |
   |         |                  | of MA matrices   |                  |
   |         |                  | to be estimated. |                  |
   |         |                  | Default = 0.     |                  |
   +---------+------------------+------------------+------------------+
   | vmc     | Optional input,  |                  |                  |
   |         | an instance of a |                  |                  |
   |         | varmamtControl   |                  |                  |
   |         | structure. The   |                  |                  |
   |         | following        |                  |                  |
   |         | members of vmc   |                  |                  |
   |         | are referenced   |                  |                  |
   |         | within this      |                  |                  |
   |         | routine:         |                  |                  |
   +---------+------------------+------------------+------------------+
   |         | vmc.adforder     | scalar, number   |                  |
   |         |                  | of AR lags in    |                  |
   |         |                  | the ADF test     |                  |
   |         |                  | statistic.       |                  |
   |         |                  | Default = 2.     |                  |
   +---------+------------------+------------------+------------------+
   |         | vmc.critl        | scalar, the      |                  |
   |         |                  | significance     |                  |
   |         |                  | levels defining  |                  |
   |         |                  | p-values.        |                  |
   |         |                  | Default = .95.   |                  |
   +---------+------------------+------------------+------------------+
   |         | vmc.ctl          | instance of an   |                  |
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
   |         |                  |                  | be printed       |
   +---------+------------------+------------------+------------------+
   |         |                  | Example:         |                  |
   |         |                  |                  |                  |
   |         |                  | ::               |                  |
   |         |                  |                  |                  |
   |         |                  |    vmc           |                  |
   |         |                  | .header = "tld"; |                  |
   |         |                  |                  |                  |
   |         |                  | If               |                  |
   |         |                  | vmc.header = "   |                  |
   |         |                  | ", no header is  |                  |
   |         |                  | printed.         |                  |
   |         |                  | De               |                  |
   |         |                  | fault = "tldvf". |                  |
   +---------+------------------+------------------+------------------+
   |         | vmc.indEquations | K×L matrix of    |                  |
   |         |                  | zeros and ones.  |                  |
   |         |                  | Used to set zero |                  |
   |         |                  | restrictions on  |                  |
   |         |                  | the variables to |                  |
   |         |                  | be estimated.    |                  |
   |         |                  | Only used if the |                  |
   |         |                  | number of        |                  |
   |         |                  | equations, vmc.L |                  |
   |         |                  | is greater than  |                  |
   |         |                  | one. Elements    |                  |
   |         |                  | set to indicate  |                  |
   |         |                  | the coefficients |                  |
   |         |                  | to be estimated. |                  |
   |         |                  | If vmc.L = 1,    |                  |
   |         |                  | all coefficients |                  |
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
   |         |                  | Default = 12.    |                  |
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
   |         |                  | Default = 0.     |                  |
   +---------+------------------+------------------+------------------+
   |         | vmc.nwtrunc      | scalar, the      |                  |
   |         |                  | number of        |                  |
   |         |                  | autocorrelations |                  |
   |         |                  | to use in        |                  |
   |         |                  | calculating the  |                  |
   |         |                  | Newey-West       |                  |
   |         |                  | correction. If   |                  |
   |         |                  | vmc.nwtrunc = 0, |                  |
   |         |                  | GAUSS will use a |                  |
   |         |                  | truncation lag   |                  |
   |         |                  | given by Newey   |                  |
   |         |                  | and West,        |                  |
   |         |                  | vmc.nwtrunc =    |                  |
   |         |                  | |image3|.        |                  |
   +---------+------------------+------------------+------------------+
   |         | vmc.output       | scalar. Set to 0 |                  |
   |         |                  | to suppress all  |                  |
   |         |                  | printing from    |                  |
   |         |                  | varmaFit. Set    |                  |
   |         |                  | vmc.output > 0   |                  |
   |         |                  | to print         |                  |
   |         |                  | results.         |                  |
   |         |                  | Default = 1.     |                  |
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
   |         | vmc.start        | Instance of a PV |                  |
   |         |                  | structure        |                  |
   |         |                  | containing       |                  |
   |         |                  | starting values. |                  |
   |         |                  | See              |                  |
   |         |                  | `VES-Starting    |                  |
   |         |                  | Values           |                  |
   |         |                  |  <VES.7.2-Starti |                  |
   |         |                  | ngValues.htm>`__ |                  |
   |         |                  | for discussion   |                  |
   |         |                  | of setting       |                  |
   |         |                  | starting values. |                  |
   |         |                  | By default,      |                  |
   |         |                  | varmaFit         |                  |
   |         |                  | calculates       |                  |
   |         |                  | starting values. |                  |
   +---------+------------------+------------------+------------------+
   |         | vmc.title        | string, a title  |                  |
   |         |                  | to be printed at |                  |
   |         |                  | the top of the   |                  |
   |         |                  | output header    |                  |
   |         |                  | (see             |                  |
   |         |                  | vmc.header). By  |                  |
   |         |                  | default, no      |                  |
   |         |                  | title is printed |                  |
   |         |                  | (vmc.title = "   |                  |
   |         |                  | ").              |                  |
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
   |     | vmo.acfm          | L×(p*L) matrix,   |                   |
   |     |                   | the               |                   |
   |     |                   | autocorrelation   |                   |
   |     |                   | function. The     |                   |
   |     |                   | first *L* columns |                   |
   |     |                   | are the lag *1*   |                   |
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
   |     | vmo.bic           | L×1 vector, the   |                   |
   |     |                   | Schwarz Bayesian  |                   |
   |     |                   | Information       |                   |
   |     |                   | Criterion.        |                   |
   +-----+-------------------+-------------------+-------------------+
   |     | vmo.covpar        | Q×Q matrix of     |                   |
   |     |                   | estimated         |                   |
   |     |                   | parameters. The   |                   |
   |     |                   | parameters are in |                   |
   |     |                   | the row-major     |                   |
   |     |                   | order: AR(1) to   |                   |
   |     |                   | AR(p), MA(1) to   |                   |
   |     |                   | MA(q), *beta* (if |                   |
   |     |                   | *x* variables     |                   |
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
   |     |                   | vmo.lagr.bounds   | bounds. When an   |
   |     |                   |                   | inequality or     |
   |     |                   |                   | bounds constraint |
   |     |                   |                   | is active, its    |
   |     |                   |                   | associated        |
   |     |                   |                   | Lagrangean is     |
   |     |                   |                   | nonzero. The      |
   |     |                   |                   | linear            |
   |     |                   |                   | Lagrangeans       |
   |     |                   |                   | precede the       |
   |     |                   |                   | nonlinear         |
   |     |                   |                   | Lagrangeans in    |
   |     |                   |                   | the covariance    |
   |     |                   |                   | matrices.         |
   +-----+-------------------+-------------------+-------------------+
   |     | vmo.lrs           | L×1 vector, the   |                   |
   |     |                   | Likelihood Ratio  |                   |
   |     |                   | Statistic.        |                   |
   +-----+-------------------+-------------------+-------------------+
   |     | vmo.maroots       | q×1 vector of MA  |                   |
   |     |                   | roots, possibly   |                   |
   |     |                   | complex.          |                   |
   +-----+-------------------+-------------------+-------------------+
   |     | vmo.pacfm         | L×(p*L) matrix,   |                   |
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
   |     |                   |    vout = var     |                   |
   |     |                   | maFit(vmc, y, 0); |                   |
   |     |                   |    ph = pvUnpack( |                   |
   |     |                   | vout.par, "phi"); |                   |
   |     |                   |                   |                   |
   |     |                   |  th = pvUnpack(vo |                   |
   |     |                   | ut.par, "theta"); |                   |
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
   |     |                   |                   | that pi is a      |
   |     |                   |                   | reserved word in  |
   |     |                   |                   | GAUSS. Users will |
   |     |                   |                   | need to assign    |
   |     |                   |                   | this to a         |
   |     |                   |                   | different         |
   |     |                   |                   | variable name.*   |
   +-----+-------------------+-------------------+-------------------+
   |     | vmo.portman       | vmc.lags-(p+ q)×3 |                   |
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
   |     |                   | the p-value in    |                   |
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
   |     |                   | in column 2.      |                   |
   +-----+-------------------+-------------------+-------------------+

Remarks
-------

.. container::
   :name: Remarks

   Errors are assumed to be distributed N(0, Q). The estimation
   procedure assumes that all series are stationary. Setting
   vmc.SetConstraints to a nonzero value enforces stationarity, by
   constraining the roots of the characteristic equation

   .. image:: GeneratedImages/Equations/Equation711.svg
      :class: mcReset

   to be outside the unit circle (where |image4| are the AR coefficient
   matrices).

   If any estimated parameters in the coefficient matrices are on a
   constraint boundary, the Lagrangeans associated with these parameters
   will be nonzero. These Lagrangeans are stored in vmo.lagr. Standard
   errors are generally not available for parameters on constraint
   boundaries.

Example
-------

.. container::
   :name: Example

   **Example One: Data matrices**
   ::

      new;
      cls;
      library tsmt;

      //Load data
      //Create file name with full path
      fname = getGAUSSHome() $+ "pkgs/tsmt/examples/mink.csv";

      //Load two variables from dataset
      y = loadd(fname, "LogMink + LogMusk");

      //Difference the data
      y = vmdiffmt(y, 1);

      //Number of AR lags
      p = 2; 

      //Declare 'vout' to be a varmamtOut structure
      struct varmamtOut vout;

      //Estimate the parameters of the VAR(2) model
      vout = varmaFit(y, p);

   **Example Two: Formula String**
   ::

      new;
      cls;
      library tsmt;

      //Declare 'vout' to be a varmamtOut structure
      struct varmamtOut vout2;

      //Estimate the parameters of the VAR(2) model
      vout2 = varmaFit( getGAUSSHome() $+ "pkgs/tsmt/examples/var_enders_trans.dat", ".", 3 ); 

Source
------

.. container:: gfunc
   :name: Source

   varmamt.src

.. |image1| image:: GeneratedImages/Equations/Equation710.svg
   :class: mcReset
.. |image2| image:: GeneratedImages/Equations/Equation710.svg
   :class: mcReset
.. |image3| image:: GeneratedImages/Equations/Equation710.svg
   :class: mcReset
.. |image4| image:: GeneratedImages/Equations/Equation712.svg
   :class: mcReset
