
plotFreq
==============================================

Purpose
----------------

Generate frequency plot of categorical data.

Format
----------------
.. function:: plotFreq([myPlot, ] x, column [, sort, pct_axis])

    :param myPlot: Optional argument, a :class:`plotControl` structure.
    :type myPlot: Struct

    :param x: data.
    :type x: NxK matrix

    :param column: Categorical variable to be plotted.
    :type column: Scalar or string
    
    :param sort: Optional, indicator to sort from most frequent to least frequent categories. Set to 1 to sort. Default = 0.
    :type column: Scalar

    :param pct_axis: Optional, indicator to plot axis as percentage instead of counts. Set to 1 to plot percentages. Default = 0.
    :type column: Scalar

Examples
----------------

Example 1: Default settings
++++++++++++++++++++++++++++

::

  // Load data
  fname = getGAUSSHome("examples/auto2.dta");
  auto2 = loadd(fname);

  // Frequency plot
  plotFreq(auto2, "rep78");

.. figure:: _static/images/plotfreq1.jpg
    :scale: 50 %

Example 2: Sorted bars
++++++++++++++++++++++++++++

To create a sorted table, use the optional *sort* input:

::

  // Sorted frequency plot of 'rep78'
  plotFreq(auto2, "rep78", 1);

.. figure:: _static/images/plotfreq2.jpg
    :scale: 50 %

Example 3: Plotting percentages
+++++++++++++++++++++++++++++++++

To plot percentage frequencies, use the optional *pct_axis* input. Note that we must also include the optional *sort* input, since optional arguments must be specified in order:

::

  // Unsorted, frequency percentage 
  // plot of 'rep78'
  plotFreq(auto2, "rep78", 0, 1);

.. figure:: _static\images\g25-percent-frequencies.jpg
    :scale: 50 %
    
Example 4: Adding a title
++++++++++++++++++++++++++++

Any frequency plot can be customized using a ``plotControl`` structure:

::

  // Declare plotControl structure
  struct plotControl myPlt;
  myPlt = plotGetDefaults("bar");
  
  // Set title
  plotSetTitle(&myPlt, "Frequency of `Rep78`");

  // Frequency plot
  plotFreq(myPlt, auto2, "rep78", 1);

.. figure:: _static/images/plotfreq3.jpg
    :scale: 50 %

 Example 5: Plotting by group with 'by'
++++++++++++++++++++++++++++++++++++++++

The :func:`plotFreq` function supports the use of the ``by`` keyword for plotting categorical frequencies by groups. 

::

  // Load dataset
  tips2 = loadd("tips2.csv");
 
  // Create a frequency plot of visits per day
  // for each category of smoker (Yes, or No).
  plotFreq(tips2, "day + by(smoker)");

.. figure:: _static\images\g25-plotfreq-day-by-smoker.jpg
    :scale: 50 %

.. seealso:: Functions :func:`plotHist`, :func:`plotHistP`, :func:`plotHistF`
