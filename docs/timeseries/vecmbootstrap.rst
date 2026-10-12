vecmBootstrap
=============

Purpose
-------
Bootstrap p-value for the Johansen trace test of the cointegrating rank. Useful in small samples and when the variance of the shocks changes over time.

Format
------

.. function:: boot = vecmBootstrap(vr)
              boot = vecmBootstrap(vr, r0=0, n_boot=999, seed=42, quiet=0)

   :param vr: an instance of a :class:`vecmResult` structure returned by :func:`vecmFit` or :func:`vecmAuto`, fit without seasonal dummies or regressors. It supplies the data, the lag order and the deterministic terms; its own rank is not used.
   :type vr: struct

   :param r0: Optional keyword, the rank under the null hypothesis, 0 to M-1. The test is of rank at most *r0* against a larger rank. Default = 0.
   :type r0: scalar

   :param n_boot: Optional keyword, number of bootstrap replications. Default = 999.
   :type n_boot: scalar

   :param seed: Optional keyword, seed of the random number generator. The same seed gives the same result. Default = 42.
   :type seed: scalar

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :return boot: An instance of a :class:`bootstrapResult` structure containing:

       .. include:: include/bootstrapresult.rst

   :rtype boot: struct

Examples
--------

::

    new;
    library timeseries;

    // Canadian employment, productivity, real wage and unemployment, 1980Q1-2000Q4
    fname = getGAUSSHome("pkgs/timeseries/examples/data/canada.csv");
    y = loadd(fname);

    struct vecmResult vr;
    vr = vecmFit(y, 1, p=2, det_case=3, quiet=1);

    // Is there any cointegration?
    struct bootstrapResult boot;
    boot = vecmBootstrap(vr, r0=0);

    // Is there more than one relation?
    boot = vecmBootstrap(vr, r0=1);

The two printouts:

::

    ================================================================================
    Wild Bootstrap Johansen Trace Test
    Cavaliere, Rahbek & Taylor (2012, 2014)

    Replications: 999        Seed: 42

    H0: rank <= 0
    Trace statistic:     75.932
    Bootstrap p-value:   0.0040

    Reject H0: rank <= 0 at the 5% level.
    ================================================================================

    ================================================================================
    Wild Bootstrap Johansen Trace Test
    Cavaliere, Rahbek & Taylor (2012, 2014)

    Replications: 999        Seed: 42

    H0: rank <= 1
    Trace statistic:     28.595
    Bootstrap p-value:   0.3520

    Do not reject H0: rank <= 1 at the 5% level.
    ================================================================================

Rank 0 is rejected and rank 1 is not, which agrees with the rank that
:func:`johansenTest` selects from its critical values for these data.

Remarks
-------

**Method.** The procedure follows Cavaliere, Rahbek and Taylor (2012, 2014):

1. Estimate the VECM with rank *r0* (for *r0* = 0, a VAR in differences).
2. Build a bootstrap sample from that model: start from the first *p* rows of
   the data and generate the following rows one at a time from the estimated
   model, with each residual vector multiplied by +1 or -1 at random (a wild
   bootstrap, which keeps the pattern of the residual variances over time).
3. Compute the trace statistic for rank at most *r0* on the bootstrap sample.
4. Repeat *n_boot* times. The p-value is

.. math::

   \frac{1 + \#\{\text{bootstrap statistics} \ge \text{observed statistic}\}}
        {1 + \text{number of valid replications}} .

Unlike the published algorithm, the procedure does not check the roots of
the model estimated in step 1 before simulating from it.

To choose a rank, test *r0* = 0, 1, 2, ... in turn and take the first *r0*
that is not rejected.

**Failed replications.** A replication whose bootstrap sample cannot be
estimated is left out of the p-value and counted in ``boot.n_failed``; a
line of the printout reports the count when it is not zero. If many
replications fail, treat the p-value with caution. If no replication is
valid, the procedure stops with an error.

References
----------

- Cavaliere, G., A. Rahbek and A.M.R. Taylor (2012). "Bootstrap determination of the co-integration rank in vector autoregressive models." *Econometrica*, 80(4), 1721-1740.
- Cavaliere, G., A. Rahbek and A.M.R. Taylor (2014). "Bootstrap determination of the co-integration rank in heteroskedastic VAR models." *Econometric Reviews*, 33(5-6), 606-650.

Library
-------
timeseries

Source
------
vecm.src

.. seealso:: Functions :func:`johansenTest`, :func:`vecmFit`, :func:`vecmAuto`
