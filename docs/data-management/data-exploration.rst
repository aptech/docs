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

It works directly with matrices and dataframes and will print a complete summary table to the **Program Input/Output** window.

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
  fname = getGAUSSHome $+ "examples\\nba_ht_wt.xls";
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
|Sample standard deviation | :func:`stdc`        | :func:`astd`       |
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
  fname = getGAUSShome $+ "examples\\xle_daily.xlsx";
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
The :func:`aggregate` finds descriptive statistics by group in panel data.

In order to be used with :func:`aggregate`, the panel data matrix should:
- Have group identifiers in the first column.
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

Example: Find median square footage and price by number of bedrooms
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

  // Create file name with full path
  fname = __FILE_DIR $+ "housing.csv";

  // Load three variables from dataset
  X = loadd(fname, "beds + price + size");

  // Compute the median of the sales price
  // and size (sq ft) by the variable in the
  // first column, which is the number of bedrooms.
  x_a = aggregate(X, "median");

The matrix `x_a` contains:

::

  bedrooms            price            sq ft
       2             94.3             1060
       3            132.6           1473.5
       4              179             2000
       5           352.65             3095


Frequency tables and plots
-----------------------------
**Frequency counts**

The :func:`counts` procedure counts the numbers of elements of a vector that fall into specified ranges and can be used to create frequency tables.

For example, to find the frequency of each category for a categorical variable, use :func:`counts` with the unique category keys as cutoffs.

::

  // Load data
  fname = getGAUSSHome $+ "examples\\auto2.dta";
  auto2 = loadd(fname, "str(make) + cat(rep78) + cat(foreign)");

  // Frequency table of rep78
  print "Frequency table of rep78:";

  // Get column labels
  { label, keyvalues } = getcollabels(auto2, "rep78");
  counts(auto2[., "rep78"], keyvalues);

**Frequency plots**

The :func:`plotFreq` will compute and plot frequencies for a categorical variable. A quick plot can be generated using default formatting or an optional `plotControlStructure` can be used for custom formatting.

Example: Plotting category frequency
+++++++++++++++++++++++++++++++++++++

::

  // Load data
  fname = getGAUSSHome $+ "examples//auto2.dta";
  auto2 = loadd(fname);

  // Frequency plot
  plotFreq(auto2, "rep78");

Associations and correlations
----------------------------------

**Computing correlations**

Two GAUSS functions are available for computing correlations of a sample:

+----------------------+------------------------------------------+
| Function             | Description                              |
+======================+=====================+====================+
| :func:`corrms`       | Computes the sample correlation using a  |
|                      | moment matrix as the input.              |
+----------------------+---------------------+--------------------+
| :func:`corrxs`       | Computes the sample correlation using a  |
|                      |data matrix as the input.                 |
+----------------------+---------------------+--------------------+

Example: Finding correlation across country GDP
++++++++++++++++++++++++++++++++++++++++++++++++++++

::

  /*
  ** Import data
  */
  fname = getGAUSSHome $+ "examples\\nba_ht_wt.xls";
  nba_ht_wt = loadd(fname, "str(Player) + cat(Pos) + Height + Weight + Age + str(School) + date($BDate, '%m/%d/%Y %T.%L')");


  // Calculate correlation of
  // height and weight
  corrxs(nba_ht_wt[., "Height" "Weight"]);

This prints the correlations to screen:

::

  1.0000000       0.82071923
  0.82071923        1.0000000


.. note:: . The :func:`corrms` and `corrxs` functions compute the standardized version of the correlation matrix. To compute an unbiased estimate which divides by *N-1*, rather than *N*, use :func:`corrm` or :func:`corrx`.
