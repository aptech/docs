cmlmtKernelDensity
=====================

Purpose
-------
To compute kernel density estimate and plot for a given dataset using specified kernel types and parameters.

Format
------
.. function:: out = cmlmtKernelDensity(dataset, c0)

    :param dataset: Name of the GAUSS dataset.
    :type dataset: string

    :param c0: Instance of :class:`cmlmtKernelDensityControl` structure with detailed configuration.
    :type c0: struct

        .. list-table::
            :widths: auto

            * - c0.varNames
              - Kx1 string array, names of selected columns for density estimation.
            * - c0.Kernel
              - Kx1 vector specifying the type of kernel used for each parameter. Options include NORMAL (1), EPAN (2), BIWGT (3), TRIANG (4), RECTANG (5), and TNORMAL (6). A scalar value applies the same kernel to all parameters. Default: NORMAL.
            * - c0.NumPoints
              - Scalar defining the number of points to compute for plots. 
            * - c0.EndPoints
              - Kx2 matrix specifying lower and upper endpoints of density for each parameter. A 1x2 matrix applies the same endpoints to all parameters. Defaults to the minimum and maximum of parameter values.
            * - c0.Smoothing
              - Smoothing coefficients for the density estimation, applicable as a Kx1 vector, Nx1 vector, or NxK matrix. A scalar value applies the same coefficient across plots. Default: 0 (automatic calculation).
            * - c0.Truncate
              - Kx2 matrix or 1x2 matrix specifying lower and upper truncation limits for the TNORMAL kernel. Defaults to minimum and maximum values respectively.

    :return out: An instance of the :class:`cmlmtKernelDensityResults` structure.
    :rtype out: struct

        .. list-table::
            :widths: auto

            * - out.px
              - c0.NumPointsx1 vector, abscissae for the density plot.
            * - out.py
              - c0.NumPointsx1 vector, ordinates for the density plot.
            * - out.sm
              - Smoothing coefficients used, returned as Kx1, NxK, or Nx1, based on input configuration.

Example
-------

::

    new;
    library cmlmt;

    // Specify the dataset
    dataset = getGAUSSHome("pkgs/cmlmt/examples/cmlmttobit.dat");

    // Initialize the control structure with default settings
    struct cmlmtKernelDensityControl c0;
    c0 = cmlmtKernelDensityControlCreate();

    // Customize the control structure
    c0.varNames = "Y";
    c0.Kernel = 1; // Use normal kernel
    c0.NumPoints = 100;
    c0.EndPoints = {-3 3};
    c0.Smoothing = 0; // Let the function compute the smoothing coefficient

    // Compute the kernel density estimate and plot
    struct cmlmtKernelDensityResults out;
    out = cmlmtKernelDensity(dataset, c0);

Remarks
-------

- The function generates kernel density plots of the selected parameters using the specified configurations. This method is useful for visualizing the distribution of parameters or data points within a dataset.
