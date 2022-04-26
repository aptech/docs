==========
identifymt
==========

10.0.27identifymt
=================

Purpose
-------

.. container::
   :name: Purpose

   Computes and prints multivariate autocorrelation functions and
   portmanteau test statistics.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   { acfm, pacfm, qs } = identifymt(p, q, res );

Input
-----

.. container::
   :name: Input

   === ====================================
   p   Scalar, autoregressive order.
   q   Scalar, moving average order.
   res Matrix, T x L, regression residuals.
   === ====================================

Output
------

.. container::
   :name: Output

   +-------+-------------------------------------------------------------+
   | acfm  | Matrix, Lx(p*L) matrix, the autocorrelation function. The   |
   |       | first L columns are the lag 1 ACF. The last L columns are   |
   |       | the lag p ACF.                                              |
   +-------+-------------------------------------------------------------+
   | pacfm | Matrix, Lx(p*L) matrix, the partial autocorrelation         |
   |       | function. The first L columns are the lag 1 PACF. The last  |
   |       | L columns are the lag p PACF.                               |
   +-------+-------------------------------------------------------------+
   | qs    | Matrix, (vmc.lags-(p+q))x3 matrix of portmanteau statistics |
   |       | for the multivariate model and Ljung-Box statistics for the |
   |       | univariate model. The time period is in column one, the Qs  |
   |       | (portmanteau) statistic in column two and the p-value in    |
   |       | column three                                                |
   +-------+-------------------------------------------------------------+

Source
------

.. container:: gfunc
   :name: Source

   varmamt.src
