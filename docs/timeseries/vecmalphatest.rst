vecmAlphaTest
=============

Purpose
-------
Likelihood ratio test that one series does not adjust to the cointegrating relations of a fitted VECM (weak exogeneity).

Format
------

.. function:: test = vecmAlphaTest(vr, var_idx, quiet=0)

   :param vr: an instance of a :class:`vecmResult` structure returned by :func:`vecmFit` or :func:`vecmAuto`, fit without seasonal dummies or regressors and with rank at most M-1.
   :type vr: struct

   :param var_idx: which series to test, 1 to M, in the order of the columns of *y*.
   :type var_idx: scalar

   :param quiet: Optional keyword, 0 prints a short block with the null hypothesis, LR statistic, degrees of freedom and chi-square p-value; 1 prints nothing. Default = 0.
   :type quiet: scalar

   :return test: An instance of an :class:`lrTestResult` structure containing:

       .. include:: include/lrtestresult.rst

   :rtype test: struct

Examples
--------

Test whether productivity (the second series) is weakly exogenous:

::

    new;
    library timeseries;

    // Canadian employment, productivity, real wage and unemployment, 1980Q1-2000Q4
    fname = getGAUSSHome("pkgs/timeseries/examples/data/canada.csv");
    y = loadd(fname);

    struct vecmResult vr;
    vr = vecmFit(y, 1, p=2, det_case=3, quiet=1);

    struct lrTestResult test;
    test = vecmAlphaTest(vr, 2);

The procedure prints:

::

    Weak exogeneity test
    ================================================================================
    Null hypothesis: All adjustment coefficients for prod are zero.
    LR statistic:                 5.4808    Degrees of freedom:                     1
    Chi-square p:                  0.019

The statistic is 5.4808 on 1 degree of freedom, p-value 0.019: at the 5%
level the hypothesis that productivity does not adjust to the relation is
rejected.

Remarks
-------

**Hypothesis.** :math:`H_0`: row *var_idx* of :math:`\alpha` is zero, so
the series does not respond to deviations from the cointegrating relations.
A series for which this holds is called weakly exogenous for the
cointegrating vectors.

**Statistic.** The model is estimated again under the restriction and the
likelihood ratio statistic

.. math::

   LR = T \sum_{i=1}^{r} \ln\frac{1-\tilde\lambda_i}{1-\hat\lambda_i}

is compared with a chi-square on *r* degrees of freedom, where
:math:`\hat\lambda_i` and :math:`\tilde\lambda_i` are the eigenvalues of
the unrestricted and the restricted model (Johansen 1995, section 8.2).
*T* is the number of rows used in estimation. The test assumes the rank *r*
is correct.

One series is tested per call. With rank *r* = *M* no row of
:math:`\alpha` can be zero, so the test is not available at full rank.

By default, the procedure prints the null hypothesis, LR statistic, degrees
of freedom and chi-square p-value. The weak-exogeneity block names the tested
series. Use ``quiet=1`` to suppress the block and read the members of *test*.

References
----------

- Johansen, S. (1995). *Likelihood-Based Inference in Cointegrated Vector Autoregressive Models*. Oxford University Press.

Library
-------
timeseries

Source
------
vecm.src

.. seealso:: Functions :func:`vecmFit`, :func:`vecmBetaTest`, :func:`johansenTest`
