vecmBetaTest
============

Purpose
-------
Likelihood ratio test of linear restrictions on the cointegrating vectors of a fitted VECM.

Format
------

.. function:: test = vecmBetaTest(vr, h_mat, quiet=0)

   :param vr: an instance of a :class:`vecmResult` structure returned by :func:`vecmFit` or :func:`vecmAuto`, fit without user regressors in ``ctl.xreg``.
   :type vr: struct

   :param h_mat: restriction matrix *H*. It has as many rows as ``vr.beta`` (M, or M+1 in deterministic cases 2 and 4) and *s* linearly independent columns, with *s* at least the rank *r*.
   :type h_mat: kxs matrix

   :param quiet: Optional keyword, 0 prints a short block with the null hypothesis, LR statistic, degrees of freedom and chi-square p-value; 1 prints nothing. Default = 0.
   :type quiet: scalar

   :return test: An instance of an :class:`lrTestResult` structure containing:

       .. include:: include/lrtestresult.rst

   :rtype test: struct

Examples
--------

Test whether unemployment (the fourth series) can be left out of the
cointegrating relation. Under the hypothesis the relation is a combination
of the columns of *H*, which span the first three series only:

::

    new;
    library timeseries;

    // Canadian employment, productivity, real wage and unemployment, 1980Q1-2000Q4
    fname = getGAUSSHome("pkgs/timeseries/examples/data/canada.csv");
    y = loadd(fname);

    struct vecmResult vr;
    vr = vecmFit(y, 1, p=2, det_case=3, quiet=1);

    h_mat = { 1 0 0,
              0 1 0,
              0 0 1,
              0 0 0 };

    struct lrTestResult test;
    test = vecmBetaTest(vr, h_mat);

The procedure prints:

::

    Cointegrating coefficient restriction test
    ================================================================================
    Null hypothesis: Each cointegrating vector is a linear combination of the columns of H (beta = H * phi).
    LR statistic:                 5.0576    Degrees of freedom:                     1
    Chi-square p:                  0.025

The statistic is 5.0576 on 1 degree of freedom, p-value 0.025: at the 5%
level the hypothesis that unemployment does not enter the relation is
rejected.

Remarks
-------

**Hypothesis.** :math:`H_0: \beta = H\varphi`: every cointegrating vector
is a linear combination of the columns of *H*. The same restriction applies
to all *r* vectors. In cases 2 and 4 the last row of *H* refers to the
constant or the trend inside the relations.

**Statistic.** The model is estimated again under the restriction. With
:math:`\hat\lambda_i` the eigenvalues of the unrestricted model and
:math:`\tilde\lambda_i` those of the restricted one,

.. math::

   LR = T \sum_{i=1}^{r} \ln\frac{1-\tilde\lambda_i}{1-\hat\lambda_i},

compared with a chi-square on :math:`r(k-s)` degrees of freedom, where *k*
is the number of rows of *H* (Johansen 1995, section 7.2). *T* is the number
of rows used in estimation. The test assumes the rank *r* is correct.

Multiplying a column of *H* by a nonzero number does not change the
hypothesis or the result.

By default, the procedure prints the null hypothesis ``beta = H * phi``,
LR statistic, degrees of freedom and chi-square p-value. Use ``quiet=1`` to
suppress the block and read the members of *test*.

Models fitted with ``season=s`` are supported. The stored centered
seasonal columns are included in both the unrestricted and restricted
estimation. Their coefficients are unrestricted; the hypothesis still
applies only to the cointegrating vectors.

Fits with user regressors in ``ctl.xreg`` are not supported, including fits
that also contain seasonal dummies.

References
----------

- Johansen, S. (1995). *Likelihood-Based Inference in Cointegrated Vector Autoregressive Models*. Oxford University Press.

Library
-------
timeseries

Source
------
vecm.src

.. seealso:: Functions :func:`vecmFit`, :func:`vecmAlphaTest`, :func:`johansenTest`
