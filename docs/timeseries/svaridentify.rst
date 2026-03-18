svarIdentify
============

Purpose
-------
Find a structural rotation satisfying sign restrictions for a single VAR or BVAR estimate.

Format
------

.. function:: sr = svarIdentify(result, ctl)

   :param result: an instance of a :class:`varResult` or :class:`bvarResult` structure.
   :type result: struct

   :param ctl: an instance of an :class:`svarControl` structure with sign restrictions defined. An instance is initialized by calling :func:`svarControlCreate` and the following members can be set:

       .. include:: include/svarcontrol.rst

   :type ctl: struct

   :return sr: An instance of an :class:`svarResult` structure containing:

       .. list-table::
          :widths: auto

          * - sr.p
            - mxm matrix, structural impact matrix P such that :math:`\Sigma = PP'`.

          * - sr.irf
            - :class:`irfResult` struct, identified impulse responses under this rotation.

          * - sr.n_tries
            - Scalar, number of rotation attempts needed to find a valid rotation.

          * - sr.m
            - Scalar, number of variables.

          * - sr.var_names
            - Mx1 string array, variable names.

          * - sr.shock_names
            - Mx1 string array, shock labels.

   :rtype sr: struct

Examples
--------

Monetary Policy SVAR
++++++++++++++++++++

::

    new;
    library timeseries;

    // Load data — ordering determines Cholesky structure
    y = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"), "gdp + cpi + ffr");

    result = varFit(y, 4, var_names="GDP"$|"CPI"$|"FFR", quiet=1);

    // Define sign restrictions
    struct svarControl ctl;
    ctl = svarControlCreate();

    // [variable, shock, horizon, sign]
    // Monetary shock (shock 3): FFR up, GDP down, CPI down at impact
    ctl.sign_restr = { 3 3 0  1,       // FFR positive
                       1 3 0 -1,       // GDP negative
                       2 3 0 -1 };     // CPI negative

    struct svarResult sr;
    sr = svarIdentify(result, ctl);

    print "Structural impact matrix P:";
    print sr.p;
    print "Rotations tried:" sr.n_tries;

Remarks
-------

**Algorithm:**
Draws random orthogonal matrices Q from the Haar measure on O(m) via QR
decomposition of N(0,1) matrices with sign correction (Mezzadri 2007). For
each candidate Q, forms :math:`P = \text{chol}(\Sigma) \cdot Q` and checks
all sign restrictions on the implied IRFs. Returns the first accepted rotation.

**This function finds a single rotation,** which is useful for point estimation
(e.g., from an OLS VAR). For posterior inference with credible bands, use
:func:`svarIrf` with a :class:`bvarResult` or :class:`bvarSvResult`.

**Zero restrictions** are not currently supported. Setting *ctl.zero_restr*
raises an error. Zero restrictions require the ARW2018 null-space algorithm,
which is planned for a future release.

Library
-------
timeseries

Source
------
svar.src

.. seealso:: Functions :func:`svarIrf`, :func:`svarControlCreate`, :func:`irfCompute`
