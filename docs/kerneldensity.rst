
kernelDensity
==============================================

Purpose
----------------
To compute kernel density estimate and plot.


Format
----------------
.. function:: out = kernelDensity(dataset [, kernel, bw, c0])
              out = kernelDensity(dataset, formula [, kernel, bw, c0])

    :param dataset: Name of datafile, dataframe, or data matrix.
    :type dataset: String or matrix

    :param formula: Optional argument, formula string for loading variables from datafile. Default is to load all variables.
    :type dataset: String

    :param kernel: Optional argument, type of kernel. Default = 1.

              =========== ==============
              1           Normal.
              2           Epanechnikov.
              3           Biweight.
              4           Triangular
              5           Rectangular.
              6           Truncated normal.
              7           Parzen.
              8           Cosine.
              9           Triweight.
              10          Tricube.
              11          Logistic.
              12          Sigmoid.
              13          Silverman.
              =========== ==============

              If kernel is scalar, the kernel is the same
              for all parameters.  Default = Normal density.

    :type kernel: Scalar

    :param bw: Optional argument, smoothing coefficient (bandwidth). Should be ExE compatible with the dataset. If `bw` is scalar, the smoothing coefficient will be the same for every data observation. If `bw` is zero, optimal smoothing coefficient will be computed. If `bw`` is a matrix, the smoothing coefficient will be different for each observation. Default = 0.
    :type bw: Scalar, Vector, or Matrix

    :param c0: Instance of :class:`kernelDensityControl` structure containing the following members:

        .. list-table::
            :widths: auto

            * - c0.varNames
              - String array, variable name(s). Default is dataframe headers if included, `"X1"`, `"X2"`, ... otherwise.

            * - c0.NumPoints
              - Scalar, number of points to be computed for plots.

            * - c0.EndPoints
              - Kx2 matrix, lower (in first column) and upper (in second column) endpoints of density.  Default is minimum and maximum, respectively, of the parameter values.  If 1x2 matrix, endpoints will be the same for all parameters.

            * - c0.Truncate
              - Kx2 matrix, lower (in first column) and upper (in second column) truncation limits for truncated normal kernel. If 1x2 matrix, truncations limits will be the same for all plots.  Default is minimum and maximum, respectively.

            * - c0.plotFunctionPtr
              - Scalar, a pointer to a user-defined function used to specify format modifications to the default plot format.

            * - c0.plotOff
              - Scalar, an indicator to turn plotting off. Set to 1 to turn off plotting. Default = 0.

    :type c0: Structure


    :return out: Instance of :class:`KernelDensityResults` structure

        .. csv-table::
            :widths: auto

                  "out.px", "Matrix, abscissae."
                  "out.py", "Matrix, ordinates."
                  "out.sm", "Kx1, or Nxk, or Nx1 smoothing coefficients."

    :rtype out: Structure

Examples
----------------

Basic usage with dataframe
+++++++++++++++++++++++++++++++

::

  /*
  ** Example One:
  ** Basic usage
  */

  // Load data
  fname = getGAUSSHome("examples/winevolatileacidity.csv");
  data = loadd(fname);

  // Call kernelDensity function
  // with default normal density
  struct kernelDensityResults krslt1;
  krslt1 = kernelDensity(data[., "volatile acidity"]);

.. figure:: _static/images/kerneldensity1.jpg
   :scale: 50 %

Basic usage with filename
+++++++++++++++++++++++++++++++

::

  /*
  ** Example Two:
  ** Basic usage with filename
  */

  // Load data
  fname = getGAUSSHome("examples/winevolatileacidity.csv");

  // Call kernelDensity function
  // with default normal density
  call kernelDensity(fname, "volatile acidity");

Basic usage with multiple kernels
++++++++++++++++++++++++++++++++++

::

  /*
  ** Example Three:
  ** Multiple kernels
  ** on same plot
  */

  struct kernelDensityResults krslt2;
  krslt2 = kernelDensity(data[., "volatile acidity"], 1|2|3);

.. figure:: _static/images/kerneldensity3.jpg
   :scale: 50 %

Basic usage with multiple series
+++++++++++++++++++++++++++++++++

::

  /*
  ** Example Four:
  ** Multiple series on different plots
  */

  struct kernelDensityResults krslt3;
  krslt3 = kernelDensity(data, 1);


.. figure:: _static/images/kerneldensity4a.jpg
   :scale: 50 %

.. figure:: _static/images/kerneldensity4b.jpg
   :scale: 50 %

Modifying plot with custom plotControl setting function 
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

  /*
  ** Example Five:
  ** Modifying plot
  */

  struct kernelDensityControl kctl;
  kctl = kernelDensityControlCreate();

  // The ampersand (&) in front of the function
  // name makes it a pointer to the function
  kctl.plotFunctionPtr = &myPlotCustomizations;

  // Basic example of kernel density plot customization
  proc (1) = myPlotCustomizations(struct plotControl myPlot);

    // Set size for graph canvas
    plotCanvasSize("px", 800|600);

    // Turn on and style major grid lines 
    plotSetGridPen(&myPlot, "major", 1, "dimgray", 2);

    //Return modified plotControl structure
    retp(myPlot);

  endp;

  // Set kernel to normal
  kernel = 1;

  // Automatically compute bandwidth
  bw = 0;

  // Call kernelDensity with
  // control structure
  struct kernelDensityResults krslt4;
  krslt4 = kernelDensity(data[., "volatile acidity"], kernel, bw, kctl);

.. figure:: _static/images/kerneldensity5.jpg
   :scale: 50 %


Remarks
-------------
#. The x axis label will be set to the name of the column of the dataframe passed to :func:`kerneldensity`. Use :func:`setcolnames` to modify the name of the variable


