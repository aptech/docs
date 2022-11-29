Data Exploration
=============================
Descriptive statistic table
---------------------------------
The :func:`dstatmt` procedure generates a summary table of descriptive statistics. It computes following statistics for every numeric column:

* Mean
* Standard deviation
* Variance
* Minimum
* Maximum
* Valid cases
* Missing cases

It works directly with matrices and dataframes and will print a complete summary table to the **Comand** window.

Example: Summary statistics from a datafile
+++++++++++++++++++++++++++++++++++++++++++++

::

  // Create file name with full path
  file_name = getGAUSSHome() $+ "examples/fueleconomy.dat";

  /*
  ** Compute statistics for all variables in the dataset
  ** The 'call' keyword disregards return values from the function
  */
  call  dstatmt(file_name);

This prints the following results

::

  ----------------------------------------------------------------------------------------------------
  Variable                    Mean     Std Dev      Variance     Minimum     Maximum     Valid Missing
  ----------------------------------------------------------------------------------------------------

  annual_fuel_cost           2.537      0.6533        0.4267        1.05         5.7       978    0
  engine_displacement        3.233       1.376         1.892           1         8.4       978    0


The :func:`dstatmt` function can also be used on a subset of variables, rather than the entire dataset.

Example: Summary statistics for select variables
++++++++++++++++++++++++++++++++++++++++++++++++++

::

  // Create file name with full path
  fname = getGAUSSHome $+ "examples/nba_ht_wt.xls";
  nba_ht_wt = loadd(fname,
      "str(Player) + cat(Pos) + Height + Weight + Age + str(School) + str(BDate)");

  /*
  ** Compute statistics for all variables in the dataset
  ** The 'call' keyword disregards return values from the function
  */
  call  dstatmt(nba_ht_wt, "Height"$|"Weight"$|"Age");

This prints the following output:

::

  ----------------------------------------------------------------------------------------
  Variable        Mean     Std Dev      Variance     Minimum     Maximum     Valid Missing
  ----------------------------------------------------------------------------------------

  Height         79.07       3.454         11.93          69          87       505    0
  Weight         220.7       26.64         709.9         157         290       505    0
  Age            26.19       4.325         18.71          15          40       505    0

Individual descriptive statistics
-----------------------------------

+--------------------------+---------------------+--------------------+
| Statistic                | Matrices            | Arrays             |
+==========================+=====================+====================+
| Mean                     | :func:`meanc`       | :func:`amean`      |
+--------------------------+---------------------+--------------------+
| Median                   | :func:`median`      |                    |
+--------------------------+---------------------+--------------------+
| Mode                     | :func:`modec`       |                    |
+--------------------------+---------------------+--------------------+
| Quantiles                | :func:`quantile`    |                    |
+--------------------------+---------------------+--------------------+
| Sample standard deviation| :func:`stdc`        | :func:`astd`       |
+--------------------------+---------------------+--------------------+
| Pop. Standard deviation  | :func:`stdsc`       | :func:`astds`      |
+--------------------------+---------------------+--------------------+
| Minimum                  | :func:`minc`        | :func:`amin`       |
+--------------------------+---------------------+--------------------+
| Maximum                  | :func:`maxc`        | :func:`amax`       |
+--------------------------+---------------------+--------------------+
| Sum                      | :func:`sumc`        | :func:`asum`       |
|                          | :func:`sumr`        |                    |
+--------------------------+---------------------+--------------------+


Example: Finding mean by column
+++++++++++++++++++++++++++++++++

::

  // Load stock price data
  fname = getGAUSShome $+ "examples/xle_daily.xlsx";
  xle_daily = loadd(fname,
                   "date($Date, '%m/%d/%Y %T.%L') + Adj Close + Volume");

  // Find mean of 'Adj Close' and 'Volume'
  meanc(xle_daily[., "Adj Close" "Volume"]);

The results are printed directly to screen:

::

  68.442841
  14308087.


Panel data descriptive statistics
-----------------------------------
The :func:`aggregate` procedure finds descriptive statistics for each group in panel data. It allows an optional input to specify the name of the categorical variable to be used for grouping.

In order to be used with :func:`aggregate` :

- Have group identifiers in the first column if the name of the categorical variable for grouping is not specified.
- Be in stacked panel data format.

The function supports the following statistics:

* Mean
* Median
* Mode
* Min
* Max
* Sample standard deviation
* Sum
* Sample variance

Example One: Find median square footage and price by number of bedrooms
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
In this example, the group variable is included in the first column. No categorical variable is specified for grouping.

::

  // Create file name with full path
  fname = getGAUSSHome $+ "examples/housing.csv";

  // Load three variables from dataset
  X = loadd(fname, "beds + price + size");

  // Compute the median of the sales price
  // and size (sq ft) by the variable in the
  // first column, which is the number of bedrooms.
  x_a = aggregate(X, "median");

The matrix *x_a* contains:

::

  bedrooms          price            sq ft
       2             94.3             1060
       3            132.6           1473.5
       4              179             2000
       5           352.65             3095

Example Two: Find the mean mpg and price for foreign vehicles
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
In this example, a categorical variable name is specified for grouping.

::

  // Load data
  auto2 = loadd(getGAUSSHome $+ "examples/auto2.dta");

  // Aggregate data using
  // foreign column as group
  aggregate(auto2[., "price" "mpg" "foreign"], "mean", "foreign");

The aggregated results are printed to the **Command** window:

::

  foreign     price      mpg
  Domestic  6072.423   19.827
  Foreign   6384.682   24.773

Frequency tables and plots
-----------------------------
**Frequency counts**
The :func:`frequency` procedure computes a frequency count of all categories of a categorical variable.

::

  // Load data
  fname = getGAUSSHome $+ "examples/auto2.dta";
  auto2 = loadd(fname);

  // Frequency table
  print "Frequency count for 'rep78':";
  freq_out = frequency(auto2, "rep78");

The above code prints:

::

     Frequency count for 'rep78':
           Label            Count
            Poor                2
            Fair                8
         Average               30
            Good               18
       Excellent               11

As an alternative to :func:`frequency`, the :func:`counts` procedure counts the numbers of elements of a vector that fall into specified ranges and can be used to create frequency tables.

For example, to find the frequency of each category for a categorical variable, use :func:`counts` with the unique category keys as cutoffs.

::

  // Load data
  fname = getGAUSSHome $+ "examples/auto2.dta";
  auto2 = loadd(fname, "str(make) + cat(rep78) + cat(foreign)");

  // Frequency table of rep78
  print "Frequency table of rep78:";

  // Get column labels
  { label, keyvalues } = getcollabels(auto2, "rep78");
  counts(auto2[., "rep78"], keyvalues);

::

  Frequency table of rep78:

       2.0000000
       8.0000000
       30.000000
       18.000000
       11.000000

**Frequency plots**

.. figure:: ../_static/images/plotfreq.jpg
    :scale: 50%

The :func:`plotFreq` will compute and plot frequencies for a categorical variable. A quick plot can be generated using default formatting or an optional ``plotControlStructure`` can be used for custom formatting.

Example: Plotting category frequency
+++++++++++++++++++++++++++++++++++++

::

  // Load data
  fname = getGAUSSHome $+ "examples/auto2.dta";
  auto2 = loadd(fname);

  // Frequency plot
  plotFreq(auto2, "rep78");

Associations and correlations
----------------------------------

**Computing correlations**

Two GAUSS functions are available for computing correlations of a sample:

+----------------------+------------------------------------------+
| Function             | Description                              |
+======================+==========================================+
| :func:`corrms`       | Computes the sample correlation using a  |
|                      | moment matrix as the input.              |
+----------------------+------------------------------------------+
| :func:`corrxs`       | Computes the sample correlation using a  |
|                      | data matrix as the input.                |
+----------------------+------------------------------------------+

Example: Finding correlation of height and weight in NBA players
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

  /*
  ** Import data
  */
  fname = getGAUSSHome $+ "examples/nba_ht_wt.xls";
  nba_ht_wt = loadd(fname, "str(Player) + cat(Pos) + Height + Weight + Age + str(School) + date($BDate, '%m/%d/%Y %T.%L')");


  // Calculate correlation of
  // height and weight
  corr_nba = corrxs(nba_ht_wt[., "Height" "Weight"]);

This prints the correlations to screen:

::

      Height           Weight
   1.0000000       0.82071923
  0.82071923        1.0000000


.. note:: The :func:`corrms` and :func:`corrxs` functions compute the sample correlation matrix. To compute the population correlation matrix use :func:`corrm` or :func:`corrx`.

Finding variance-covariance
----------------------------------
Two GAUSS functions are available for computing correlations of a sample:

+-------------------------+------------------------------------------+
| Function                | Description                              |
+=========================+==========================================+
| :func:`varCovMS`        | Computes the variance-covariance matrix  |
|                         | using a moment matrix as the input.      |
+-------------------------+------------------------------------------+
| :func:`varCovXS`        | Computes the variance-covariance matrix  |
|                         | using a data matrix as the input.        |
+-------------------------+------------------------------------------+

Example: Finding variance/covariance of height and weight in NBA players
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

  /*
  ** Import data
  */
  fname = getGAUSSHome $+ "examples/nba_ht_wt.xls";
  nba_ht_wt = loadd(fname, "str(Player) + cat(Pos) + Height + Weight + Age + str(School) + date($BDate, '%m/%d/%Y %T.%L')");


  // Calculate correlation of
  // height and weight
  corr_nba = corrxs(nba_ht_wt[., "Height" "Weight"]);

  // Calculate variance-covariance
  // of height and weight
  varCovxs(nba_ht_wt[., "Height" "Weight"]);

This prints the following variance/covariance matrix:

::

  11.930245        75.527346
  75.527346        709.85534

.. note:: The :func:`covVarMS` and :func:`covVarXS` functions compute the sample variance/covariance. It is computed as the moment matrix of deviations about the mean divided by the number of observations minus one, *N−1*. For a population covariance matrix which uses *N* rather than *N−1* see :func:`varCovM()` or :func:`varCovX()`.

Exploratory data visualizations
---------------------------------

**Plotting histograms**

Histograms of data can be plotted using one of three functions:

*  The :func:`plotHist` function which computes and graphs a frequency histogram.
*  The :func:`plotHistP` function which computes and graphs a percent frequency histogram.
*  The :func:`plotHistF` function which graphs a histogram given vector of frequency counts.

.. note:: These functions do not currently utilize the categorical labels and :func:`plotFreq` is recommended for categorical variables with labels.

Example: Frequency and percentage histograms
++++++++++++++++++++++++++++++++++++++++++++++

::

  // Create data
  r = rndGamma( 1e4, 1, 3, 2 );

  // Declare plotControl structure
  struct plotControl myPlot;

  // Set plotControl structure to
  // default values
  myPlot = plotGetDefaults( "bar" );

  // Set Title
  fontname = "Helvetica Neue";
  plotSetTitle( &myPlot, "Example Percentage Histogram", fontname, 18 );

  // Set Y label
  plotSetYLabel( &myPlot, "Percentage",  fontname, 14);

  // Use first pane
  // in layout

  plotLayout(1, 2, 1);
  // plot a percentage histogram
  // with the data from 'r' spread
  // into 50 bins.
  plotHistP( myPlot, r, 50 );

  // Set solid fill and completely opaque (i.e. zero transparency)
  plotSetFill( &myPlot, 1, 1);

  // Set Title
  plotSetTitle( &myPlot, "Example Frequency Histogram" );

  // Set Y label
  plotSetYLabel( &myPlot, "Frequency" );

  // Use second pane
  // in layout
  plotLayout(1, 2, 2);

  // Plot a standard histogram
  // with the data from 'r' spread
  // into 80 bins.
  plotHist( myPlot, r, 80 );


**Plotting scatter plots**

The :func:`plotScatter` function creates a quick scatter plot using just an *x* and *y* input. To add custom plotting use the :class:`plotControl` structure.

Example: Plotting the relationship between height and weight in NBA players
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

  // Create file name with full path
  fname = getGAUSSHome $+ "examples/nba_ht_wt.xls";
  nba_ht_wt = loadd(fname,
      "str(Player) + cat(Pos) + Height + Weight + Age + str(School) + str(BDate)");

   // Plot height and weight
   plotScatter(nba_ht_wt[., Height], nba_ht_wt[., weight]);
