======
vmsjmt
======

10.0.77vmsjmt
=============

Purpose
-------

.. container::
   :name: Purpose

   Computes Johansen's (1988) ML Trace and Maximum Eigenvalue
   statistics.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   { ev, evec, lr1, lr2 } = vmsjmt(x, p, k, nodet);

Input
-----

.. container::
   :name: Input

   +-------+-------------------------------------------------------------+
   | x     | T×L matrix.                                                 |
   +-------+-------------------------------------------------------------+
   | p     | scalar, order of the time-polynomial in the fitted          |
   |       | regression. Set *p* = -1 for no deterministic part, *p* = 0 |
   |       | for a constant term, and *p* = 1 for a constant with trend. |
   +-------+-------------------------------------------------------------+
   | k     | scalar, number of lagged difference terms to use when       |
   |       | computing the estimator.                                    |
   +-------+-------------------------------------------------------------+
   | nodet | scalar. Set nodet = 1 to suppress the constant term from    |
   |       | the fitted regression and include it in the co-integrating  |
   |       | regression; otherwise, set nodet = 0.                       |
   +-------+-------------------------------------------------------------+

Output
------

.. container::
   :name: Output

   +------+--------------------------------------------------------------+
   | ev   | L×1 vector of eigenvalues.                                   |
   +------+--------------------------------------------------------------+
   | evec | L×L matrix of eigenvectors. The first *r* columns are the    |
   |      | unnormalized cointegrating vectors.                          |
   +------+--------------------------------------------------------------+
   | lr1  | L×1 vector of Johansen's likelihood ratio Trace statistics   |
   |      | for the null hypotheses of H0; at most *r* cointegrating     |
   |      | vectors versus H1: not |image5|.                             |
   +------+--------------------------------------------------------------+
   | lr2  | L×1 vector of Johansen's Maximum Eigenvalue Statistics for   |
   |      | the null hypotheses of H0: *r* cointegrating vectors versus  |
   |      | H1: *r*\ +1 cointegrating vectors, |image6|.                 |
   +------+--------------------------------------------------------------+

 

.. container::
   :name: Example

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

      //Specify a VAR(2) model
      p = 2;

      //Number of lagged differences to include in test 
      k = 2;

      //Do not suppress constant term
      nodet = 0;

      { ev, evec, lr1, lr2 } = vmsjmt(y, p, k, nodet);

      print "Eigenvalues :"; 
      ev;
      print;

      print "Eigenvectors :";
      evec;
      print;

      print "Johansen's likelihood ratio trace statistics for r = 0 to L-1 cointegrating vectors :";
      lr1;
      print;

      print "Johansen's  maximum eigenvalue statistic for the null hypothesis of r = 0 to m-1 cointegrating vectors :";
      lr2;
      print;
              

Source
------

.. container:: gfunc
   :name: Source

   varmamt.src

.. |image1| image:: _static/images/Equation741.svg
   :class: mcReset
.. |image2| image:: _static/images/Equation742.svg
   :class: mcReset
.. |image3| image:: _static/images/Equation741.svg
   :class: mcReset
.. |image4| image:: _static/images/Equation742.svg
   :class: mcReset
.. |image5| image:: _static/images/Equation741.svg
   :class: mcReset
.. |image6| image:: _static/images/Equation742.svg
   :class: mcReset
