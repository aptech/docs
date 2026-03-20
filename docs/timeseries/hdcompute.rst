hdCompute
=========

Purpose
-------
Compute historical decomposition of observed series into structural shock contributions.

Format
------

.. function:: hd = hdCompute(result)
              hd = hdCompute(result, n_steps)

   :param result: an instance of a :class:`varResult` or :class:`bvarResult` structure.
   :type result: struct

   :param n_steps: Optional, number of MA steps for the decomposition. Default = T-p (full sample).
   :type n_steps: scalar

   :param var_names: Optional keyword, override variable names.
   :type var_names: Mx1 string array

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :return hd: An instance of an :class:`hdResult` structure containing:

       .. include:: include/hdresult.rst

   :rtype hd: struct

Examples
--------

Full Historical Decomposition
+++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));

    result = varFit(data, 4, var_names="GDP"$|"CPI"$|"FFR", quiet=1);

    struct hdResult hd;
    hd = hdCompute(result);

Shock Contributions to a Variable
++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));
    result = varFit(data, 4, var_names="GDP"$|"CPI"$|"FFR", quiet=1);
    hd = hdCompute(result, quiet=1);

    // FFR shock (shock 3) contribution to GDP (variable 1) over time
    ffr_to_gdp = hd.hd[3][., 1];
    print "FFR shock contribution to GDP:";
    print ffr_to_gdp;

    // CPI shock (shock 2) contribution to GDP
    cpi_to_gdp = hd.hd[2][., 1];

Verify Decomposition Sums to Observed
++++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));
    result = varFit(data, 4, var_names="GDP"$|"CPI"$|"FFR", quiet=1);
    hd = hdCompute(result, quiet=1);

    // Reconstruct GDP from shock contributions + initial conditions
    gdp_reconstructed = hd.initial[., 1];
    for j (1, hd.m, 1);
        gdp_reconstructed = gdp_reconstructed + hd.hd[j][., 1];
    endfor;

    // Compare with observed GDP (should match within numerical precision)
    gdp_observed = result.y[result.p+1:rows(result.y), 1];
    print "Max reconstruction error:" maxc(abs(gdp_reconstructed - gdp_observed));

Extract Structural Shocks
+++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));
    result = varFit(data, 4, quiet=1);
    hd = hdCompute(result, quiet=1);

    // Structural (orthogonalized) shocks
    print "Structural shocks:";
    print hd.shocks[1:5, .];

Remarks
-------

**Historical decomposition** expresses each observed variable as the sum of
contributions from each structural shock plus initial conditions:

.. math::

   y_t = \sum_{j=1}^{m} \text{contribution}_{j,t} + \text{initial}_t

The contributions are computed by filtering the structural shocks through the
MA(:math:`\infty`) representation (truncated at *n_steps*).

**Structural shocks** are obtained by applying the Cholesky decomposition of
:math:`\Sigma` to the reduced-form residuals: :math:`\varepsilon_t = P^{-1} u_t`
where :math:`\Sigma = PP'`.

**Interpretation:** ``hd.hd[j][t, i]`` answers the question: "How much of
variable i's value at time t is attributable to the cumulative effect of
shock j up to time t?"

**For BVAR,** the decomposition is computed at the posterior mean of B and
:math:`\Sigma`.

Model
-----

The observed series is decomposed as:

.. math::

   y_t = \underbrace{\sum_{j=1}^{m} \sum_{s=p+1}^{t} \Theta_{t-s} P^{-1} \hat{u}_s}_{\text{cumulative shock contributions}} + \underbrace{y_t^{\text{init}}}_{\text{initial conditions}}

where :math:`\Theta_h` is the structural IRF at horizon h, :math:`P = \text{chol}(\Sigma)'`,
and :math:`\hat{u}_t` are the reduced-form residuals. The structural shocks are
:math:`\hat\varepsilon_t = P^{-1} \hat{u}_t`.

The contribution of shock :math:`j` to variable :math:`i` at time :math:`t` is:

.. math::

   \text{hd}_{j,t,i} = \sum_{s=p+1}^{t} \Theta_{t-s}[i,j] \cdot \hat\varepsilon_{j,s}


Algorithm
---------

1. Compute structural shocks :math:`\hat\varepsilon_t = P^{-1} \hat{u}_t` for all :math:`t`.
2. Compute IRF matrices :math:`\Theta_0, \ldots, \Theta_{T-p-1}`.
3. For each time :math:`t`, accumulate shock contributions via MA convolution.
4. Compute initial conditions as the residual: :math:`y_t^{\text{init}} = y_t - \sum_j \text{hd}_{j,t}`.

**Complexity:** :math:`O(T^2 m^2)` — quadratic in sample size due to the convolution.


Troubleshooting
---------------

**Reconstruction error is not zero:**
The decomposition should reconstruct the observed series exactly (to machine precision).
If the error exceeds :math:`10^{-10}`, there may be a mismatch between the estimation
result and the data. Re-estimate the model.

**One shock dominates the decomposition:**
Same as FEVD — check the variable ordering and consider alternative identification.


References
----------

- Lutkepohl, H. (2005). *New Introduction to Multiple Time Series Analysis*. Springer. Section 2.3.4.
- Kilian, L. and H. Lutkepohl (2017). *Structural Vector Autoregressive Analysis*. Cambridge University Press.


Library
-------
timeseries

Source
------
hd.src

.. seealso:: Functions :func:`irfCompute`, :func:`fevdCompute`, :func:`varFit`, :func:`bvarFit`
