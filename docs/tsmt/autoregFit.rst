==========
autoregFit
==========

10.0.10autoregFit
=================

Purpose
-------

.. container::
   :name: Purpose

   Estimates coefficients of a regression model with autoregressive
   errors of any specified order.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   aro = autoregFit(y, x, lagvars, order);
   aro = autoregFit(y, x, lagvars, order, arc);
   aro = autoregFit(dataset, formula, lagvars, order);
   aro = autoregFit(dataset, formula, lagvars, order, arc);

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
   | lagvars | K×1 vector, the  |                  |                  |
   |         | number of        |                  |                  |
   |         | periods to lag   |                  |                  |
   |         | the variables    |                  |                  |
   |         | inindvars. If    |                  |                  |
   |         | there are no     |                  |                  |
   |         | lagged           |                  |                  |
   |         | variables, set   |                  |                  |
   |         | to scalar 0. The |                  |                  |
   |         | variables        |                  |                  |
   |         | inindvars will   |                  |                  |
   |         | be lagged the    |                  |                  |
   |         | number of        |                  |                  |
   |         | periods          |                  |                  |
   |         | indicated in the |                  |                  |
   |         | corresponding    |                  |                  |
   |         | entries          |                  |                  |
   |         | inlagvars. The   |                  |                  |
   |         | dependent        |                  |                  |
   |         | variable in      |                  |                  |
   |         | depvar can be    |                  |                  |
   |         | included in      |                  |                  |
   |         | indvars can be   |                  |                  |
   |         | repeated if each |                  |                  |
   |         | corresponding    |                  |                  |
   |         | entry in lagvars |                  |                  |
   |         | is a different   |                  |                  |
   |         | value.           |                  |                  |
   +---------+------------------+------------------+------------------+
   | order   | scalar, order of |                  |                  |
   |         | the              |                  |                  |
   |         | autoregressive   |                  |                  |
   |         | process; must be |                  |                  |
   |         | greater than 0   |                  |                  |
   |         | and less than    |                  |                  |
   |         | the number of    |                  |                  |
   |         | observations.    |                  |                  |
   +---------+------------------+------------------+------------------+
   | arc     | Optional input,  |                  |                  |
   |         | an instance of   |                  |                  |
   |         | anautomtC        |                  |                  |
   |         | ontrolstructure. |                  |                  |
   |         | The following    |                  |                  |
   |         | members ofarc    |                  |                  |
   |         | are referenced   |                  |                  |
   |         | within this      |                  |                  |
   |         | routine:         |                  |                  |
   +---------+------------------+------------------+------------------+
   |         | arc.const        | scalar. If 1,    |                  |
   |         |                  | constant will be |                  |
   |         |                  | used in model;   |                  |
   |         |                  | else not.        |                  |
   |         |                  | Default = 1.     |                  |
   +---------+------------------+------------------+------------------+
   |         | arc.header       | string,          |                  |
   |         |                  | specifies the    |                  |
   |         |                  | format for the   |                  |
   |         |                  | output header.   |                  |
   |         |                  | arc.header can   |                  |
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
   |         |                  | f                | file name of     |
   |         |                  |                  | program is to be |
   |         |                  |                  | printed          |
   +---------+------------------+------------------+------------------+
   |         |                  | Example:         |                  |
   |         |                  |                  |                  |
   |         |                  | ::               |                  |
   |         |                  |                  |                  |
   |         |                  |    arc           |                  |
   |         |                  | .header = "tld"; |                  |
   |         |                  |                  |                  |
   |         |                  | If               |                  |
   |         |                  | arc.header = "", |                  |
   |         |                  | no header is     |                  |
   |         |                  | printed.         |                  |
   |         |                  | De               |                  |
   |         |                  | fault = "tldvf". |                  |
   +---------+------------------+------------------+------------------+
   |         | arc.init         | scalar. If 1,    |                  |
   |         |                  | only initial     |                  |
   |         |                  | estimates will   |                  |
   |         |                  | be computed.     |                  |
   |         |                  | Default = 0.     |                  |
   +---------+------------------+------------------+------------------+
   |         | arc.iter         | scalar. If 0,    |                  |
   |         |                  | iteration        |                  |
   |         |                  | information will |                  |
   |         |                  | not be printed.  |                  |
   |         |                  | If 1, iteration  |                  |
   |         |                  | information will |                  |
   |         |                  | be printed       |                  |
   |         |                  | (arc.outputmust  |                  |
   |         |                  | be nonzero).     |                  |
   |         |                  | Default = 0.     |                  |
   +---------+------------------+------------------+------------------+
   |         | arc.maxvec       | calar, the       |                  |
   |         |                  | maximum number   |                  |
   |         |                  | of elements      |                  |
   |         |                  | allowed in any   |                  |
   |         |                  | one matrix.      |                  |
   |         |                  | Default = 20000. |                  |
   +---------+------------------+------------------+------------------+
   |         | arc.output       | scalar, if       |                  |
   |         |                  | nonzero, results |                  |
   |         |                  | are printed to   |                  |
   |         |                  | screen.          |                  |
   |         |                  | Default = 1.     |                  |
   +---------+------------------+------------------+------------------+
   |         | arc.title        | tring, a title   |                  |
   |         |                  | to be printed at |                  |
   |         |                  | the top of the   |                  |
   |         |                  | output header    |                  |
   |         |                  | (see             |                  |
   |         |                  | arc.header). By  |                  |
   |         |                  | default, no      |                  |
   |         |                  | title is printed |                  |
   |         |                  | (arc.title="").  |                  |
   +---------+------------------+------------------+------------------+
   |         | arc.tol          | scalar,          |                  |
   |         |                  | convergence      |                  |
   |         |                  | tolerance.       |                  |
   |         |                  | Default = 1e-5.  |                  |
   +---------+------------------+------------------+------------------+

Output
------

.. container::
   :name: Output

   +-----+------------------------------+------------------------------+
   | aro | An instance of an automtOut  |                              |
   |     | structure containing the     |                              |
   |     | following members:           |                              |
   +-----+------------------------------+------------------------------+
   |     | aro.acor                     | (L+1)×1 vector,              |
   |     |                              | autocorrelations.            |
   +-----+------------------------------+------------------------------+
   |     | aro.acov                     | (L+1)×1 vector,              |
   |     |                              | autocovariances.             |
   +-----+------------------------------+------------------------------+
   |     | aro.chisq                    | scalar, -2\* log-likelihood. |
   +-----+------------------------------+------------------------------+
   |     | aro.coefs                    | K×1 vector, estimated        |
   |     |                              | regression coefficients.     |
   +-----+------------------------------+------------------------------+
   |     | aro.phi                      | L×1 vector, lag              |
   |     |                              | coefficients.                |
   +-----+------------------------------+------------------------------+
   |     | aro.rsq                      | scalar, explained variance.  |
   +-----+------------------------------+------------------------------+
   |     | aro.sigsq                    | scalar, variance of white    |
   |     |                              | noise error.                 |
   +-----+------------------------------+------------------------------+
   |     | aro.tobs                     | scalar, number of            |
   |     |                              | observations.                |
   +-----+------------------------------+------------------------------+
   |     | aro.vcb                      | K×K matrix, covariance       |
   |     |                              | matrix of estimated          |
   |     |                              | regression coefficients.     |
   +-----+------------------------------+------------------------------+
   |     | aro.vcphi                    | L×L matrix, covariance       |
   |     |                              | matrix of *phi*.             |
   +-----+------------------------------+------------------------------+
   |     | aro.vsig                     | scalar, variance of          |
   |     |                              | aro.sigsq (variance of the   |
   |     |                              | variance of white noise      |
   |     |                              | error).                      |
   +-----+------------------------------+------------------------------+

Remarks
-------

.. container::
   :name: Remarks

   This program will handle only datasets that fit in memory.

   All autoregressive parameters are estimated up to the specified lag.
   You cannot estimate only the first and fourth lags, for instance.

   The algorithm will fail if the model is not stationary at the
   estimated parameters. Thus, in that sense it automatically tests for
   stationarity.

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
      data = loadd(getGAUSSHome() $+ "pkgs/tsmt/examples/autoregmt.dat");
      y = data[.,1];
      x = data[.,2 3];
              
      //Lag of independent variables
      lag_vars = 0;

      //Autoregressive order
      order = 3;

      //Initialized automtOut structure
      struct automtOut aro;

      //Call autoregFit function
      aro = autoregFit(y, x, lag_vars, order);

   **Example Two: Dataset and formula string**
   ::

      new;
      cls;
      library tsmt;

      //Lag of independent variables
      lag_vars = 0;

      //Autoregressive order
      order = 3;

      //Initialized automtOut structure
      struct automtOut aro;

      //Call autoregFit function
      aro = autoregFit(getGAUSSHome() $+ "pkgs/tsmt/examples/autoregmt.dat", "Y ~ X1 + X2", lag_vars, order);

Source
------

.. container:: gfunc
   :name: Source

   autoregmt.src
