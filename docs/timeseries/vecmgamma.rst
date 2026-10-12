vecmGamma
=========

Purpose
-------
Return one short-run coefficient matrix of a fitted VECM.

Format
------

.. function:: g = vecmGamma(vr, i)

   :param vr: an instance of a :class:`vecmResult` structure returned by :func:`vecmFit` or :func:`vecmAuto`.
   :type vr: struct

   :param i: which lagged difference, 1 to ``p-1``.
   :type i: scalar

   :return g: :math:`\Gamma_i`, the coefficients on :math:`\Delta y_{t-i}`. Row *j* belongs to the equation of series *j*.
   :rtype g: MxM matrix

Examples
--------

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/canada.csv");
    y = loadd(fname);

    struct vecmResult vr;
    vr = vecmFit(y, 1, p=2, det_case=3, quiet=1);

    print vecmGamma(vr, 1);

::

      0.76562256       0.16513409     -0.023606252       0.14208335
     -0.29857108       0.14790495       0.12321796      -0.84347705
     -0.19624183     -0.043727644     -0.056962902       0.43511122
     -0.58459494     -0.073088979     -0.029106624      -0.13306833

Remarks
-------

``vr.Gamma`` stores :math:`\Gamma_1` to :math:`\Gamma_{p-1}` stacked by rows;
this function returns rows :math:`(i-1)M+1` to :math:`iM`. A model with
``p = 1`` has no lagged differences.

Library
-------
timeseries

Source
------
vecm.src

.. seealso:: Functions :func:`vecmFit`, :func:`vecmResults`
