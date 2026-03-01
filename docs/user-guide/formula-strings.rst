
Formula Strings
===============================================

Formula strings allow you to represent a model or a collection of variables
in a compact, readable way, using the variable names in the dataset. They
are used throughout GAUSS for loading data, specifying regression models,
computing descriptive statistics, and controlling plot layouts.

.. admonition:: Prerequisites

    This page assumes you can load data with :func:`loadd`. If you are new
    to GAUSS, see :doc:`/getting-started/quickstart` first.

::

    // Load two variables by name
    x = loadd(getGAUSSHome("examples/cancer.dat"), "stage + count");

    // Specify a regression model
    call olsmt(getGAUSSHome("examples/credit.dat"), "Limit ~ Income + Rating");

    // Compute descriptive statistics for selected variables
    call dstatmt(getGAUSSHome("examples/auto2.dta"), "mpg + weight + price");

Formula strings work with **dataframes** — matrices that carry column names
and types, returned by :func:`loadd`. Because each column has a name,
formula strings can reference those names directly for subsetting,
estimation, and plotting.


Basic Syntax
-----------------------------------------

A formula string is a quoted string containing variable names and operators.

**Selecting variables for loading or statistics:**

::

    // Load all variables
    df = loadd(fname, ".");

    // Load specific variables
    df = loadd(fname, "Income + Rating + Cards");

    // Load all variables except one
    df = loadd(fname, ". - Cards");

**Specifying a model with dependent and independent variables:**

The tilde ``~`` separates the dependent (response) variable on the left
from the independent (explanatory) variables on the right:

::

    // Limit = alpha + beta_1 * Income + beta_2 * Rating + epsilon
    call olsmt(fname, "Limit ~ Income + Rating");

    // Use all remaining variables as predictors
    call olsmt(fname, "Limit ~ .");


Operators
-----------------------------------------

The following operators are available in formula strings. The examples
assume a dataset containing three variables: **Limit**, **Income**, and
**Rating**.

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Operator
      - Description

    * - ``.`` (dot)
      - Include all variables. When used after ``~``, includes everything
        except the dependent variable.

        ::

            // These two are equivalent
            "Limit ~ Income + Rating"
            "Limit ~ ."

    * - ``+`` (plus)
      - Add a variable.

        ::

            "Income + Rating"

    * - ``-`` (minus)
      - Remove a variable.

        ::

            // These two are equivalent
            "Limit ~ Rating"
            "Limit ~ . - Income"

    * - ``:`` (colon)
      - Create a pure interaction term between two variables (no main effects).

        ::

            "Limit ~ Income:Rating"

    * - ``*`` (asterisk)
      - Include both main effects and the interaction term.

        ::

            // These two are equivalent
            "Limit ~ Income * Rating"
            "Limit ~ Income + Rating + Income:Rating"

    * - ``1`` (one)
      - Represents the intercept. Estimation functions such as :func:`olsmt`
        and :func:`glm` include an intercept by default. Data-loading
        functions such as :func:`loadd` and statistics functions such as
        :func:`dstatmt` do not.

        ::

            // Remove the intercept
            "Limit ~ -1 + Income + Rating"

    * - ``$`` (dollar sign)
      - Indicates that a variable should be loaded as a string. Typically
        used with the ``date`` keyword.

        ::

            // Load 'order_time' as a string and interpret as a date
            "date($order_time)"


Keywords
-----------------------------------------

factor
+++++++++++++++++++++++

The ``factor`` keyword tells GAUSS that a numeric variable represents
categories. In estimation functions such as :func:`olsmt` and :func:`glm`,
GAUSS will automatically create dummy variables for each level, using
the first level as the base case.

::

    // Load data
    fname = getGAUSSHome("examples/auto2.dta");

    // Create dummy variables from 'rep78'
    call olsmt(fname, "mpg ~ weight + factor(rep78)");

The above code prints a regression report with separate coefficient
estimates for each non-base-case level of ``rep78``:

::

    Ordinary Least Squares
    =========================================================================================
    Valid cases:                         69          Dependent variable:                 mpg
    Missing cases:                        5          Deletion method:               Listwise
    Total SS:                      2.34e+03          Degrees of freedom:                  63
    R-squared:                        0.672          Rbar-squared:                     0.646
    Residual SS:                        768          Std. err of est:                   3.49
    F(5,63):                           25.8          Probability of F:               4.6e-14
    =========================================================================================
                                     Standard                    Prob       Lower       Upper
    Variable             Estimate       Error     t-value        >|t|       Bound       Bound
    -----------------------------------------------------------------------------------------

    CONSTANT               38.059      3.0934      12.304  2.0913e-18      31.996      44.122
    weight              -0.005503    0.000601     -9.1564  3.4748e-13   -0.006681  -0.0043251
    rep78: Fair           -0.4786       2.765    -0.17309     0.86313     -5.8981      4.9409
    rep78: Average       -0.47156      2.5531     -0.1847     0.85406     -5.4757      4.5326
    rep78: Good          -0.59903      2.6066    -0.22981     0.81898      -5.708      4.5099
    rep78: Excellent       2.0863      2.7248     0.76566     0.44674     -3.2544      7.4269
    =========================================================================================


cat
+++++++++++++++++++++++

The ``cat`` keyword tells GAUSS that a string variable in a file (such as
CSV or XLSX) should be reclassified to integer categories. This is useful
for file types that do not store variable type information.

``cat`` can be combined with ``factor`` to load string data, convert it to
integer categories, and create dummy variables in a single step:

::

    fname = getGAUSSHome("examples/yarn.xlsx");

    // Reclassify 'load' from 'high, med, low' to integers,
    // then create dummy variables for OLS
    call olsmt(fname, "cycles ~ factor(cat(load))");

The output:

::

    Ordinary Least Squares
    ====================================================================================
    Valid cases:                       27          Dependent variable:            cycles
    Missing cases:                      0          Deletion method:                 None
    Total SS:                    2.02e+07          Degrees of freedom:                24
    R-squared:                     0.0866          Rbar-squared:                  0.0105
    Residual SS:                 1.85e+07          Std. err of est:                  877
    F(2,24):                         1.14          Probability of F:               0.337
    ====================================================================================
                                Standard                    Prob       Lower       Upper
    Variable        Estimate       Error     t-value        >|t|       Bound       Bound
    ------------------------------------------------------------------------------------

    CONSTANT          534.44      292.47      1.8273    0.080113     -38.806      1107.7
    load: low         621.56      413.62      1.5027     0.14596     -189.14      1432.3
    load: med         359.11      413.62     0.86821     0.39388     -451.59      1169.8
    ====================================================================================

You can specify a base case explicitly when loading with ``cat``:

::

    fname = getGAUSSHome("examples/yarn.xlsx");

    // Load with 'med' as the base case
    df = loadd(fname, "cycles + cat(load, 'med')");

    // Now 'med' is the reference level in the regression
    call olsmt(df, "cycles ~ factor(load)");


date
+++++++++++++++++++++++

The ``date`` keyword tells GAUSS that a column contains date information.
GAUSS will try to match one of approximately 30 recognized date patterns
and convert the values to POSIX date/time format (seconds since
January 1, 1970).

.. note::

    :func:`loadd` auto-detects dates for most common formats. The ``date``
    keyword is an override for cases where auto-detection fails or you need
    to force a specific interpretation.

::

    fname = getGAUSSHome("examples/yellowstone.csv");

    // The $ tells GAUSS that 'Date' is stored as a string.
    // The date() keyword tells GAUSS to interpret it as a date.
    dates = loadd(fname, "date($Date)");

    // Preview the first 4 dates
    print dates[1:4];

This prints:

::

                Date
          2016/01/01
          2015/01/01
          2014/01/01
          2013/01/01

Dates are stored internally as POSIX date/time values (seconds since
January 1, 1970), but GAUSS displays them in human-readable format
automatically. Use :func:`dtYear`, :func:`dtMonth`, and
:func:`dtDayofWeek` to extract date components.

You can also specify a date format explicitly when GAUSS cannot
auto-detect the pattern:

::

    // Specify the format directly
    dates = loadd(fname, "date($Date, '%Y-%m-%d')");


by
+++++++++++++++++++++++

The ``by`` keyword groups data by the values of a variable. It is
supported by descriptive statistics functions such as :func:`dstatmt`
and plotting functions such as :func:`plotScatter` and :func:`plotXY`.

::

    // Load data as a dataframe
    df = loadd(getGAUSSHome("examples/auto2.dta"));

    // Compute descriptive statistics for 'mpg', grouped by 'foreign'
    call dstatmt(df, "mpg + by(foreign)");

In plotting functions, ``by`` creates separate series for each group:

::

    // Load the data
    df = loadd(getGAUSSHome("examples/auto2.dta"));

    // Scatter plot of mpg vs weight, colored by 'foreign'
    plotScatter(df, "mpg ~ weight + by(foreign)");


Data Transformations
-----------------------------------------

You can apply any GAUSS function to a variable inside a formula string.
The function must accept a single column vector as input and return a
column vector of the same length.

::

    // Use the natural log of height
    "weight ~ ln(height)"

    // Square root transformation
    "y ~ sqrt(x1) + x2"

    // Lag a variable (for time series)
    "y ~ lag(x)"

You may use any built-in or user-defined GAUSS procedure. Because the
formula string is not parsed until runtime, procedures that are not
referenced elsewhere in the code may not be compiled. If you get the error
``"Undefined proc"``, add an ``external proc`` declaration:

::

    // Declare the procedure so the compiler includes it
    external proc myTransform;

    call olsmt(fname, "y ~ myTransform(x1) + x2");


Model Specification
-----------------------------------------

Multiple variable regression
++++++++++++++++++++++++++++++

For the following examples, assume a dataset containing: **admit**,
**gre**, **gpa**, and **rank**.

.. list-table::
    :widths: 50 50
    :header-rows: 1

    * - Model
      - Formula string

    * - :math:`\text{admit} = \alpha + \beta_1 \text{gre} + \beta_2 \text{gpa} + \beta_3 \text{rank} + \varepsilon`
      - ``"admit ~ ."`` or ``"admit ~ gre + gpa + rank"``

    * - :math:`\text{admit} = \alpha + \beta_1 \text{gre} + \beta_2 \text{gpa} + \varepsilon`
      - ``"admit ~ . - rank"`` or ``"admit ~ gre + gpa"``


Keywords and transformations
++++++++++++++++++++++++++++++

.. list-table::
    :widths: 50 50
    :header-rows: 1

    * - Model
      - Formula string

    * - :math:`\text{admit} = \alpha + \beta_1 \ln(\text{gre}) + \beta_2 D_{\text{rank}=2} + \beta_3 D_{\text{rank}=3} + \beta_4 D_{\text{rank}=4} + \varepsilon`

        Log-transform ``gre`` and create dummy variables from ``rank``
        (level 1 is the base case).
      - ``"admit ~ ln(gre) + factor(rank)"``

    * - :math:`\text{admit} = \alpha + \beta_1 \text{gre} + \beta_2 \text{gpa} + \beta_3 (\text{gre} \times \text{gpa}) + \varepsilon`

        Include main effects and their interaction.
      - ``"admit ~ gre * gpa"``


Controlling the intercept
++++++++++++++++++++++++++++++

Estimation functions include an intercept by default. Remove it with
``-1``:

.. list-table::
    :widths: 50 50
    :header-rows: 1

    * - Model
      - Formula string

    * - :math:`\text{admit} = \beta_1 \text{gre} + \beta_2 \text{gpa} + \beta_3 \text{rank} + \varepsilon`
      - ``"admit ~ . - 1"`` or ``"admit ~ -1 + gre + gpa + rank"``

    * - :math:`\text{admit} = \beta_1 \text{gre} + \beta_2 \text{gpa} + \varepsilon`
      - ``"admit ~ . - 1 - rank"`` or ``"admit ~ -1 + gre + gpa"``


Multiple dependent variables
++++++++++++++++++++++++++++++

Some functions accept multiple dependent variables, separated by
additional tildes:

::

    // Two dependent variables
    "y1 ~ y2 ~ x1 + x2"


Formulas without a dependent variable
++++++++++++++++++++++++++++++++++++++++

Some operations, such as computing descriptive statistics or loading data,
do not have a dependent variable. In these cases, omit the tilde:

.. list-table::
    :widths: 40 60
    :header-rows: 1

    * - Variables to include
      - Formula string

    * - All variables
      - ``"."`` or ``"admit + gre + gpa + rank"``

    * - gre and rank only
      - ``". - admit - gpa"`` or ``"gre + rank"``


Complete Examples
-----------------------------------------

The following examples show complete, runnable code combining formula
strings with common GAUSS workflows. Each uses a built-in dataset.

Example 1: OLS with formula strings
++++++++++++++++++++++++++++++++++++++++

::

    // Load data as a dataframe
    fname = getGAUSSHome("examples/credit.dat");
    df = loadd(fname);

    // Preview the data
    head(df);

    // Estimate: Limit = alpha + beta_1 * Income + beta_2 * Rating + epsilon
    call olsmt(df, "Limit ~ Income + Rating");

.. note::

    The legacy function :func:`ols` still works and accepts the same formula
    string syntax, but :func:`olsmt` is recommended for new code.


Example 2: GLM with categorical variables
+++++++++++++++++++++++++++++++++++++++++++

::

    // Load data and remove missing values
    df = loadd(getGAUSSHome("examples/auto2.dta"), "mpg + weight + rep78");
    df = packr(df);

    // Fit a GLM: mpg depends on weight and categorical rep78
    struct glmOut out;
    out = glm(df, "mpg ~ weight + factor(rep78)", "normal");


Example 3: Loading and transforming data
+++++++++++++++++++++++++++++++++++++++++++

::

    fname = getGAUSSHome("examples/credit.dat");

    // Load selected variables with a transformation
    df = loadd(fname, "Limit + ln(Income) + Rating");

    // View the first few rows
    head(df);


Example 4: Descriptive statistics by group
++++++++++++++++++++++++++++++++++++++++++++

::

    // Load data as a dataframe
    df = loadd(getGAUSSHome("examples/auto2.dta"));

    // Descriptive statistics for mpg and weight, grouped by foreign
    call dstatmt(df, "mpg + weight + by(foreign)");


Example 5: Scatter plot with grouping
++++++++++++++++++++++++++++++++++++++++

::

    // Load data
    df = loadd(getGAUSSHome("examples/auto2.dta"));

    // Scatter plot with groups
    plotScatter(df, "mpg ~ weight + by(foreign)");


Example 6: Quantile regression
++++++++++++++++++++++++++++++++++++++++

::

    fname = getGAUSSHome("examples/credit.dat");

    // Quantile regression at the median
    struct qfitOut out;
    out = quantileFit(fname, "Balance ~ Income + Rating", 0.5);


Rules and Tips
-----------------------------------------

- **Case sensitivity:** Variable names in formula strings are case
  sensitive. ``"Income"`` and ``"income"`` refer to different variables.

- **Transformation requirements:** Any procedure used as a data
  transformation must accept a single column vector and return a column
  vector of the same length.

- **Intercept defaults:** Estimation functions (:func:`olsmt`, :func:`glm`,
  :func:`quantileFit`) add an intercept automatically. Data functions
  (:func:`loadd`) and statistics functions (:func:`dstatmt`) do not.

- **Whitespace:** Spaces around operators are optional but recommended
  for readability. ``"y~x1+x2"`` and ``"y ~ x1 + x2"`` are equivalent.

- **Dataframe column names:** Formula strings use the column names stored
  in the dataframe. Use :func:`getHeaders` to see available names.

- **Files without variable names:** Some data files, such as GAUSS matrix
  files (``.fmt``), do not have column names. Refer to columns by position
  using ``X1``, ``X2``, ``X3``, and so on: ``loadd("mydata.fmt", "X1 + X3")``.

.. tip::

    Use :func:`head` to preview a dataframe after loading. This helps you
    confirm the variable names and types before writing a formula string.


What's Next
-----------------------------------------

- Load your own data with :func:`loadd` and explore the available
  column names with :func:`getHeaders`.
- Run a regression with :func:`olsmt` and examine the output structure.
- Create grouped plots with :func:`plotScatter` and the ``by`` keyword.

.. seealso:: Functions :func:`loadd`, :func:`olsmt`, :func:`glm`, :func:`dstatmt`, :func:`quantileFit`, :func:`plotScatter`, :func:`plotXY`, :func:`plotBar`
