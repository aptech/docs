vecmAlphaTest
=============

Purpose
-------
Likelihood ratio test that a chosen set of series has zero adjustment to every cointegrating relation of a fitted VECM (joint weak exogeneity).

Format
------

.. function:: test = vecmAlphaTest(vr, var_idx, quiet=0)

   :param vr: an instance of a :class:`vecmResult` structure returned by :func:`vecmFit` or :func:`vecmAuto`, fit without user regressors in ``ctl.xreg`` and with rank at most M-1.
   :type vr: struct

   :param var_idx: nonempty row or column vector of distinct whole-number indices in 1 to M, in the order of the series columns of *y*. A scalar tests one series. Empty, duplicate, fractional and out-of-range entries are refused. For *k* indices, require ``k <= M-r``.
   :type var_idx: kx1 or 1xk vector

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
    LR statistic:                 5.4808    Chi-square df:                         1
    Chi-square p:                  0.019

The statistic is 5.4808 on 1 degree of freedom, p-value 0.019: at the 5%
level the hypothesis that productivity does not adjust to the relation is
rejected.

Test productivity and the real wage jointly at rank one:

::

    tested_indices = { 2 3 };
    test = vecmAlphaTest(vr, tested_indices);

::

    Weak exogeneity test
    ================================================================================
    Null hypothesis: All adjustment coefficients for prod, rw are zero.
    LR statistic:                28.3789    Chi-square df:                         2
    Chi-square p:                < 0.001

This tests zero adjustment for both series in the same model, on two
degrees of freedom. Separate one-series tests do not test this hypothesis.

Remarks
-------

**Hypothesis.** :math:`H_0`: every row of :math:`\alpha` named by *var_idx*
is zero in every cointegrating relation. This tests the chosen series
jointly: none responds to deviations from the cointegrating relations.
A series for which this holds is called weakly exogenous for the
cointegrating vectors. Non-rejection does not establish weak exogeneity.
Weak exogeneity for the long-run parameters does not rule out short-run
feedback.

**Statistic.** The model is estimated again under the restriction and the
likelihood ratio statistic

.. math::

   LR = T \sum_{i=1}^{r} \ln\frac{1-\tilde\lambda_i}{1-\hat\lambda_i}

is compared with a chi-square on *r k* degrees of freedom for *k* tested series, where
:math:`\hat\lambda_i` and :math:`\tilde\lambda_i` are the eigenvalues of
the unrestricted and the restricted model (Johansen 1995, section 8.2).
*T* is the number of rows used in estimation. The test assumes the rank *r*
is correct.

Write :math:`\alpha=A\psi`, where *A* is the M-column identity matrix
with the *k* tested columns removed. Its M-k columns must accommodate
the *r* adjustment relations, so ``r <= M-k``. A single index retains the
one-series test. At full rank no series can be tested.

By default, the procedure prints the null hypothesis, LR statistic, degrees
of freedom and chi-square p-value. The weak-exogeneity block names the tested
series. Use ``quiet=1`` to suppress the block and read the members of *test*.

Models fitted with ``season=s`` are supported. The stored centered
seasonal columns are included in both the unrestricted and restricted
estimation. Their coefficients are unrestricted; the hypothesis still
applies only to the selected rows of the adjustment matrix.

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

.. seealso:: Functions :func:`vecmFit`, :func:`vecmBetaTest`, :func:`johansenTest`
