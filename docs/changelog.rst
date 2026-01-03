==========
Change Log
==========

The following is a list of changes from the previous version of GAUSS.

26.0.0
------

#. New function: :func:`pdBalance`, balances a panel so that each group has the same number of observations by either filling or removing observations.
#. New function: :func:`endswith`, returns a 1 if an element of a dataframe or string array ends with a specified pattern.
#. Enhanced functionality: :func:`aggregate` can now group data by more than one variable.
#. Enhanced functionality: :func:`strrindx` can now accept a vector `what` input.
#. Enhanced functionality: :func:`sortc` now accepts an optional `sort_order` parameter to sort in ascending (1) or descending (-1) order.
#. Enhanced functionality: :func:`sortmc` now accepts an optional `sort_order` parameter to sort in ascending (1) or descending (-1) order.
#. Bug fix: :func:`dbnomics_series` would return an error when trying to return multiple variables.
#. Bug fix: :func:`loadd` would not allow more than 95 GAUSS dataset (.gdat) files in certain instances.

25.0.1
------

#. Enhancement: Remove non-numeric types from :func:`pdSummary` computations and print note that non-numeric types have been removed. 
#. Expanded functionality: Add optional style input to :func:`plotSetLegendBorder` for setting line style for legend border.
#. Expanded functionality: Implement option to turn legend border off using :func:`plotSetLegendBorder`. 
#. Graphics: :func:`plotBar` now supports formula strings and automatically handles dataframe input to generate the appropriate axis and legend labels.
#. Graphics: :func:`plotBar` and :func:`plotAddBar` now supports dates as the x-axis labels. 
#. Bug fix: subtraction with sparse matrices would sometimes cause an error of 'could not create sparse marix'.
#. Bug fix: Some use cases of :func:`pdSummary` with limited varlists could error with `incompatible type`.
#. Bug fix: Some cases of :func:`pdSize` would error when empty categories were encountered. 
#. Bug fix: In certain cases the subtraction operator could report an error with sparse matrices.

25.0.0
------
#. New function: :func:`pdAllBalanced` checks if panel data is strongly balanced, i.e., if each individual has the same time periods. It intelligently detects group and date variables, while also providing the flexibility for users to specify these variables as needed.
#. New function: :func:`pdAllConsecutive` checks if all groups in panel are consecutive without gaps.
#. New function: :func:`pdDiff` computes differences of panel datasets. It intelligently detects group and date variables automatically, while also providing the flexibility for users to specify these variables as needed.
#. New function: :func:`pdIsBalanced` checks whether the groups in a panel dataset span the maximum time period of the panel. It intelligently detects group and date variables, while also providing the flexibility for users to specify these variables as needed.
#. New function: :func:`pdIsConsecutive` checks whether the groups in a panel dataset cover a consecutive time span without gaps. It intelligently detects group and date variables, while also providing the flexibility for users to specify these variables as needed.
#. New function: :func:`pdLag` compute lags of panel data. It intelligently detects group and date variables, while also providing the flexibility for users to specify these variables as needed.
#. New function: :func:`pdSummary` generates comprehensive summaries of panel datasets, including overall, between-group, and within-group statistics. It intelligently detects group and date variables, while also providing the flexibility for users to specify these variables as needed.
#. New function: :func:`pdSort` sorts panel data using intelligently detected group and date variables.
#. New function: :func:`pdTimeSpans` reports the time spans for each variable in a panel.
#. New function: :func:`waldTest` performs a Wald test of joint hypothesis on model parameters.
#. New function: :func:`qfitSlopeTest` performs tests of slope equality across quantiles after :func:`quantileFit`.  
#. Graphics: :func:`plotFreq` now supports formula string keyword, :class:`by` for splitting data by a specified categorical or string variable and generating the appropriate legend items.
#. Expanded functionality of :func:`tabulate` with option to find column and row percentages.
#. Enhanced functionality of :func:`frequency` to use metadata to detect and print variable names when using dataframes. 
#. Enhanced functionality of :func:`gmmFitIV` to use metadata to detect and print variable names when using dataframes. 
#. Enhanced result printouts for :func:`gmmFit`, :func:`gmmFitIV`, :func:`olsmt`, :func:`glm`, and :func:`quantileFit` to ensure consistency, expand model descriptions, and model diagnostics. 
#. New ability to estimate linear models separately for each subset based on a categorical variable with the :class:`by` keyword and :func:`gmmFitIV`.
#. Speed up of :func:`counts` with new option to specify that incoming data is sorted.
#. Bug fix: :func:`dfwider` would fail with an error if the ``id_cols`` control structure member was used in an unnecessary, but correct manner.
#. Bug fix: :func:`tabulate` would reports inaccurate error message when no tilde was present in formula string.
#. Bug fix: :func:`gmmfit` incorrectly computed J-statistic, now uses moments from user-specified moment function for computation of J-statistic.
#. Bug fix: :func:`spline` could go in an infinite loop in some rare cases.
#. Bug fix: :func:`vec` could crash in a specific case with a column vector dataframe.
#. Bug fix: :func:`saved` would save dataframe columns as their numeric key value when saving to Excel files.
#. Bug fix: The Package Manager would fail to install by default on Windows 11.

24.0.5
------

#. Bug fix: Crash could occur on Windows systems with certain network proxy configurations.

24.0.4
------

#. New function: :func:`dropunusedcategories` removes any categories from the meta data of a dataframe that are not present in the variable.
#. Bug fix: :func:`dfwider` will now only create columns from categories that are present in the variable, ignoring categories present in meta data, but not in the current sample.
#. Bug fix: :func:`dfwider` would fail with an error if the ``id_cols`` control structure member was used in an unnecessary, but correct manner.
#. Bug fix: :func:`dstatmt` would fail with an error if used with the `by` keyword for a categorical variable that only contained a single category.
#. Bug fix: :func:`dropcategories` would error out if more than one category to drop was passed in.
#. Bug fix: In a specific case the `.$==` operator with a dataframe on the left and a string on the right that was shorter than the dataframe element, but identical for all characters it contained, would be reported as equal.

24.0.3
------

#. Bug fix: Package manager failed to work after updated Conda requirements on Windows.
#. Bug fix: The error widget incorrectly handled backslashes in certain cases.

24.0.2
------

#. Bug fix: :func:`plotAddHbar` and :func:`plotAddVbar` would return an error in certain cases if the input was an *nx2* matrix and the bar was turned 'on' for the last element.
#. Bug fix: :func:`plotScatter` and :func:`plotXY` could assign the y-axis label to be the name of the 'by' variable in the case that the y-label was not previously set and a formula string with the 'by' keyword was used.
#. Bug fix: :func:`h5read` and :func:`h5open` now work with one-dimensional HDF5 datasets.


24.0.1
------

#. Added capability to exclude parts of the *columns* variable names from becoming part of a new variable when using the *names_pattern_split* structure member with :func:`dflonger`.
#. Added support for a negative offset with :func:`upmat`.
#. Bug fix for some specific cases with wide matrices and a large offset with :func:`upmat`.

24.0.0
------

#. New functions :func:`dfLonger` and :func:`dfWider` convert between wide and long form panel data.
#. New ability to compute descriptive statistics on a dataframe for each subset based on a categorical variable with :func:`dstatmt` and  the :class:`by` keyword.
#. New ability to estimate linear models separately for each subset based on a categorical variable with the :class:`by` keyword and :func:`glm` or  :func:`olsmt`.
#. New function :func:`fgls` computes feasible GLS estimation with seven options for estimating the innovation covariance matrix.
#. New function :func:`tabulate` generates and returns two-way tables of frequency.
#. New function :func:`DWstat` computes the Durbin-Watson statistic from residuals. 
#. New function :func:`tracem` computes the trace of a matrix.
#. New function :func:`startsWith` returns a binary matrix with a 1 if the element starts with the specified string, otherwise 0.
#. New convenience function :func:`insertcols` allows you to insert one or more new columns into a matrix or dataframe at a specified location.
#. New function :func:`isStructType` checks whether a GAUSS variable is a structure of a specific type.
#. New function :func:`dtSecond` extracts seconds component as numbers from date/time variables.
#. New function :func:`dtMinute` extracts the minutes from date/time variables as a number (00-59).
#. New function :func:`dtHour` extracts the hours from date/time variables as a number with option to use 12-hr or 24-hr clock.
#. New function :func:`dtDayofWeek` extracts the day of the week from date/time variables as a number with option to use Monday (1-7) or Sunday (0-6) start of week.
#. New function :func:`dtDayofMonth` extracts the day of the month from date/time variables as a number (1-31).
#. New function :func:`dtDayofYear` extracts the day of the year from date/time variables as a number (1-366).
#. New function :func:`dtDayName` extracts the name of the day of week from date/time variables as a string array with option to use full or abbreviated names.
#. New function :func:`dtMonthName` extracts the name of the month from date/time variables as a string array with option to use full or abbreviated names.
#. New function :func:`dtWeek` extracts the week of the year from date/time variables as a number, using Monday as start of the week (1-53).
#. New function :func:`dtMonth` extracts the month from date/time variables as a number.
#. New function :func:`dtQuarter` extracts the quarter from date/time variables as number (1-4).
#. New function :func:`dtYear` extracts the year from date/time variables as a number with century included.
#. New convenience function :func:`getCategories` returns category labels of categorical variable. 
#. New convenience function :func:`dropCategories` removes a category from a dataframe and from the dataframe metadata.
#. New convenience function :func:`isstring` returns a 1 if the input is a string or string array, otherwise 0.
#. New methods forward-fill and backward-fill added to :func:`impute`.
#. Expanded functionality of :func:`frequency` to allow for two-way tables and improved printing. 
#. Expanded functionality of :func:`strindx`. The second input can now have multiple rows and/or columns as long as it is element-by-element conformable with the first input.
#. :func:`upmat` now has the option to specify an offset from the main diagonal, the option to return only the upper triangular elements as a vector and is faster for medium and large matrices.
#. New ability to turn density plots off for :func:`kernelDensity` procedure.
#. New option to plot category counts in order from most frequently occurring to least frequently occurring for :func:`plotFreq` procedure. 
#. New option to report category counts in order from most frequently occurring to least frequently occurring for :func:`frequency` procedure. 
#. :func:`plotAddTSHF` no longer requires a ``frequency`` impute which simplifies usage.
#. Speed increase for :func:`packr` with large column vectors.
#. Speed increase for :func:`combinate` with large values of *n*.
#. Bug Fix: :func:`sprintf` could cause a crash in certain cases with very large floating point numbers.
#. Bug Fix:  :func:`svdusv` could have a memory leak in certain situations.
#. Bug Fix: Loading data with :func:`loadd` from a ``.gdat`` file with certain formula strings would fail with an "arguments not conformable error".
#. Bug Fix:  Copy-and-paste with the error widget open could cause a crash on Windows 11.
#. Bug Fix: :func:`strindx` could crash if a dataframe with a missing value was passed in as the first input.
#. Bug Fix: :func:`plotsave` could hang if the *unit* argument was not passed in. The *unit* argument now has a default value of "px".

23.0.4
------

#. Bug Fix: :func:`loadd` could fail to load a csv file if some particular sections ended with multiple missing values.
#. Bug Fix: :func:`loadd` would fail to load ``.gdat`` files if a formula string transformed a numeric variable to categorical or string.
#. Bug Fix: :func:`saved` would report an error if saving a dataset with only numeric variables.
#. Bug Fix: :func:`kerneldensity` would not respect x-label setting if a plot setting procedure pointer was passed in and was setting plot canvas size automatically.

23.0.3
------

#. Bug Fix: The generated code in the symbol editor could be incorrect in the event a header was both renamed and toggled in a manner that would remove it.
#. Bug Fix: The generated code in the file import dialog could be incorrect when a certain number of headers were toggled and additional modifications were present.
#. Bug Fix: :func:`rescale` was not always retaining column metadata.
#. Bug Fix: Matrix multiply operations will now always drop column metadata.
#. Bug Fix: Custom fonts were being ignored when used in LaTeX labels for ``\\{text}`` tags when plotting.
#. Bug Fix: Specifying ``"vcenter"`` in :func:`plotSetLegend` was also causing horizontal alignment to occur.
#. Bug Fix: :func:`plotSave` now allows a 1x1 string array for the filename argument instead of requiring a string.
#. Bug Fix: Additional validation was added to :func:`trimr`.
#. Bug Fix: :func:`asdf` now allows the *headers* argument to be a string array instead of requiring each header as a separate string argument. 

23.0.2
------

#. Behavior Change: The `kernelDensity` procedure accepts column vector bandwidth to set different bandwidths for each column of the dataset. 
#. Bug Fix: The column sniffing behavior of the import dialog did not match the logic of :func:`loadd`, which could lead to unexpected column types.
#. Bug Fix: Overriding the guessed column type in the import dialog will now correctly use the ``pass`` keyword in the formula string, indicating the column should be passed through unaltered.
#. Bug Fix: The Help Page 'Index' widget will now correctly load certain built-in functions that may have redundant pages elsewhere (e.g. the User Guide).
#. Bug Fix: Selecting a compiled file (extension :file:`.gcg`) in the project view widget will now execute the file instead of attempting to open it as a source file.
#. Bug Fix: (Windows) Reading Excel data from COM using :func:`xlsReadSA` will now store the data sequentially in the underlying datastore. This was causing corrupted string arrays in certain use-cases, such as overwriting a string value in the symbol. This bug is not present if ``#define USECOMEXCEL 1`` is commented out in xls.src.

23.0.1
------

#. :func:`strsect` now supports string arrays.
#. Behavior Change: Date patterns have had their acceptable years modified to 1800 <=> 2200 to reduce the occurrence of false positives. (e.g. detecting a date column with :func:`loadd`)
#. Bug Fix: Automatic type detection could cause loading failure in cases where the column looks like a date but is a pre-defined category column.
#. Bug Fix: In specific cases where a message exceeded a certain size with `errorlog`, a crash could occur on Windows.
#. Bug Fix: The ``fred_api_key`` value was not being read from the :file:`gauss.cfg` file.
#. Bug Fix: Calling :func:`strtof` on a dataframe category/string column with a NaN could cause a crash.
#. Bug Fix: :func:`loadd` will now default to the CSV file type for unrecognized file extensions.

23.0.0
------

#. A new :file:`*.gdat` file type has been introduced with full support for GAUSS dataframes. See :func:`loadd` and :func:`saved`.
#. Added new functions to download and search Federal Reserve Economic Data (FRED) directly into a dataframe. See :func:`fred_load` and :func:`fred_search`.
#. Added new function to download DBnomics data directly into a dataframe. See :func:`dbnomics_series`.
#. Added new function :func:`between` returns a vector with a 1 if the element is in the range or otherwise a zero.
#. Added new function :func:`where` that returns elements from ``a`` or ``b``, depending on ``condition``.
#. Added new function :func:`shiftc` shifts data down the columns of a matrix.
#. Added new function :func:`kerneldensity` for computing and plotting kernel estimates. Added kernels include Normal, Epanechnikov, Biweight, Triangular, Rectangular, Truncate normal, Parzen, Cosine, Triweight, Tricube, Logistic, Sigmoid, and Silverman.
#. Added new function :func:`kurtosis` to compute sample kurtosis.
#. Added new function :func:`skewness` to compute sample skew.
#. Added new function :func:`jarqueBera` to compute Jarque-Bera test for goodness of fit and normality.
#. :func:`quantileFit` now implements kernel estimate of asymptotic covariance. Kernel options include Normal (Gaussian), Epanechnikov, Biweight, Parzen, and Cosine.
#. :func:`quantileFit` now implements bandwidth selection methods. Method options include Hall-Sheather, Bofinger, and Chamberlain.
#. :func:`quantileFit` now computes pseudo R-squared.
#. :func:`quantileFit` output printing improved and expanded to include model characteristics in model header.
#. :func:`quantileFit` now compatible with dataframe and formula string syntax.
#. :func:`clusterSE` and :func:`robustSE` now compatible with dataframe and formula string notation.
#. :func:`clusterSE` and :func:`robustSE` now include optional argument for turning off small sample correction.
#. :func:`loadd` can now read known file types directly from a URL.
#. :func:`loadd` will now automatically detect column types. This can be controlled in :file:`gauss.cfg` with the ``policy_formula_auto_infer`` option.
#. :func:`saved` now supports :file:`*.fmt` files.
#. :func:`getGAUSSHome` can now accept relative paths as an input so they do not have to be appended to the end with the string addition operator.
#. :func:`strctoposix` will now return a missing if the string input matches the current workspace's missing value.
#. :func:`vartypef` now returns all possible dataframe header types instead of strictly numeric/string.
#. Up to 10x speed improvement and 50% decrease in memory usage for :func:`lagn`.
#. :func:`lagn` now retains variable names and column types from the input.
#. Improved performance of date format pattern matching with :func:`loadd`.
#. Improved performance of :func:`indsav` with dataframes.
#. Improved performance for reading large XLS/XLSX files with :func:`loadd` and when previewing files in the file import dialog.
#. Improved performance when viewing large symbols in the symbol editor. Specifically symbols with many columns.
#. Improved performance of all GAUSS ExE operators with temporary matrices (e.g. ``df[., "age"] .> 30``).
#. Improved performance of :func:`reclassify`, especially with a single ``from`` and ``to`` element.
#. Opening ReadStat file types (SAS, Stata, SPSS) now has a progress indicator while loading in the file import dialog.
#. Behavior Change: Unmapped dataframe string/category column values will be represented as string literals instead of a missing for purposes of printing. Note that the string literal will not match a mapped value in an oppossing dataframe in the context of an :func:`outerjoin`.
#. Behavior Change: Negative keys are now allowed for dataframe string/category column types.
#. Behavior Change: The OMP default child count was changed from 2 to 1. This improved performance significantly in cases with `threadfor` loops that performed multi-threaded BLAS/LAPACK functions, such as matrix multiply.
#. Bug Fix: A file buffer containing ``open f = /`` would cause a crash in the syntax parser.
#. Bug Fix: An empty newline at the end of a CSV could show up as row of missings.
#. Bug Fix: Certain edge cases with relative paths could cause ``#include`` to fail.
#. Bug Fix: Certain edge cases in :func:`selif`, :func:`delif`, :func:`copymetadata` and :func:`setcoldateformats` caused a memory leak.
#. Bug Fix: :func:`move` could fail in specific cases.
#. Bug Fix: :func:`asdf` now allows dataframes to be passed as input for string arguments.
#. Bug Fix: Indexing a dataframe with fixed rows and specifying ``.`` for the columns when the column count is 1 would not return a dataframe.
#. Bug Fix: :func:`xlsGetSheetSize` would return :math:`[1, 1]` for sheets that were a row or column vector.
#. Bug Fix: :func:`strctoposix` is now case-insensitive for character literals in the pattern/input.
#. Bug Fix: Formula strings containing newlines would not work correctly.
#. macOS now bundles in OpenSSL with the installer, and all three platforms are now using OpenSSL 1.1.1q.
#. New examples: olsmt_nw.e, kerneldensity_wine.e, quantilefitdf.e

22.2.1
------

#. Bug Fix: Extra spacing could show up between axis labels and numbers in certain cases.
#. Bug Fix: A one-time crash could occur after retrieving an updated license after a subscription renewal.

22.2.0
------

#. Added support for GAUSS subscription-based licenses.
#. Added support for multiple activation keys in the license activation dialog. (GUI)
#. Added support for passing extra arguments to the objective function in :func:`sqpSolve`.
#. Added support for passing extra arguments to the objective function in :func:`QNewton`.
#. Bug Fix: :func:`dbGetTables` returned an error instead of a scalar missing on an empty result set.
#. Bug Fix: :kbd:`F4` shortcut was not interpreting :func:`__FILE_DIR` correctly.
#. Bug Fix: Fixed Forward/Back key shortcuts for navigating file history on macOS.
#. Bug Fix: Custom missing values in the file import dialog could cause GAUSS to crash.
#. Bug Fix: Allowed changing case of dataframe header names in the symbol editor (GUI).
#. Bug Fix: Legend positioning could be slightly off in certain circumstances.
#. Bug Fix: The legend font color could overwrite the marker border color when a plotAdd occurred.
#. Bug Fix: Use current encoding when doing token matching in the editor.
#. Bug Fix: macOS update was not removing existing vwrmp.app before replacement.
#. Bug Fix: Multi-element assignment with a 1x1 matrix on the right-hand side would cause an error.
#. Bug Fix: Indexing a scalar from a dataframe vector in a non-atomic fashion was not returning a dataframe.
#. Bug Fix: Selecting a new date format in the symbol editor would show existing dates that were missing values as the incorrect date until the change was applied.
#. Bug Fix: Fixed support for negative category keys when reading Stata files.

22.1.0
------

#. New function :func:`dfappend` vertically stacks dataframes and merges the meta data from string and categorical columns.
#. :func:`sortc` can now accept multiple columns to sort on. :func:`sortmc` can now accept string variable names.
#. New convenience feature: The column input to :func:`reshape` is now optional and if a -1 is passed in for the row or column input, :func:`reshape` will infer the other dimension.
#. New convenience feature: :func:`miss` with no inputs will return a scalar missing value.
#. New functions :func:`head` and :func:`tail` allow convenient previewing of the first or last rows of data.
#. New function :func:`annotationsettextalign` allows specifying alignment of text inside textboxes programmatically.
#. New function :func:`annotationsetlinepen` allows for more convenient setting of annotation line width, color and style.
#. Final inputs to :func:`annotationsetfont` are now optional inputs.
#. New function :func:`plotsetfonts` allows convenient control of font family, size and color for all, or a subset of the text elements in a graph.
#. New function :func:`plotsetmissgap` controls whether a gap in line plots is shown for missing observations.
#. New functions :func:`plotsetactivex` and :func:`plotsetactivey` control which x and y axes (bottom/top, left/right)  subsequent plotSet functions apply to.
#. The legend text item will no longer cyle, meaning it will only be used for the series it was set for.
#. Added support for specifying textbox position relative to the coordinate location in :func:`plotaddtextbox`.
#. Added support for specifying a single x or y-axis to :func:`plotsettextinterpreter`.
#. Added support for space separated string specifiers to :func:`plotsettextinterpreter` for convenience.
#. Added additional optional inputs to :func:`plotsetxrange` and :func:`plotsetyrange` to set the tick inverval and the location of the first tick label.
#. The x-top axis now supports time series data.
#. :func:`plotsetxrange` and :func:`plotsetyrange` can now set the top / bottom x-axes and left / right y-axes separately.
#. Legend properties, such as font and background settings as well as location can now be set in a plotAdd call if the legend has not yet been drawn.
#. Improved the automatic tick spacing for time series plots through :func:`plotxy` and :func:`plottshf`.
#. :func:`plotsetxticcount` and :func:`plotsetyticcount` when set to 0, now provide a convenient way to turn off ticks and tick labels.
#. If line style is set to 0 (off) and then line width and/or color are set, the style will be set to 1 (solid). This allows for enabling lines such as the grid that are disabled by default by specifying only line width or color.
#. All "base" graph profiles in preferences (e.g. "Bar", "XY", "Scatter", etc) will be overwritten when GAUSS is updated. This allows us to push updates and fixes to the default profiles. Permanent changes and settings should be saved to a cloned profile.
#. Added additional optional input to functions :func:`vcm` and :func:`vcx`, allowing control over the degrees-of-freedom adjustment used in the computation.
#. Added additional argument to :func:`outerjoin` to allow a full outer join instead of only left outer join (the default).
#. Added significant performance increase to :func:`indnv` for most cases. If the input is already sorted, :func:`indnv` now accepts an optional argument to specify this for reduced overhead.
#. The main logic of :func:`innerjoin` is now an intrinsic instead of a procedure.
#. Add missing export in gsgraphics_stub shared library for the GAUSS Engine.
#. Nested `for` loops with a duplicate counter identifier will now show a more accurate error message when the compile fails.
#. :func:`copymetadata` now allows repeating columns from the source dataframe as well as specifying a subset of columns to apply to the destination dataframe.
#. Improved layout of graph profile preferences for better viewing compatibility on smaller resolutions.
#. Bug Fix: :func:`plotsetxticinterval` and :func:`plotsetyticinterval` would set the top x-axis or right y-axis respectively when a scalar (rather than 2x1) input was passed in.
#. Bug Fix: Indexing a dataframe in a specific manner resulting in a scalar could sometimes omit the metadata.
#. Bug Fix: Metadata cache would sometimes not be kept when the LRU cache was full.
#. Bug Fix: Reading complex (i.e. with imaginary numbers) datasets with :func:`readr` in certain cases could return the error "read past end of file".
#. Bug Fix: :func:`__FILE_DIR` is now fixed when used in the Command window on Windows.
#. Bug Fix: Manually created libraries were not immediately visible in certain cases. Extra library paths in the GUI are now refreshed on library creation to fix this.
#. Bug Fix: Regression: Filtering dataframe date columns in the symbol editor now works correctly again.
#. Bug Fix: Bar plots were incorrectly adjusting their size based on the line thickness, even when the line style was set to none.
#. Bug Fix: :func:`strsplit` could cause a crash in specific cases.
#. New example files ``plotunemp.e`` illustrates plotting time series variables from a dataframe using :func:`plotXY` and formula strings, ``plot_customlayout_1.e`` shows placing a histogram count of the data above the x-axis and across from the y-axis..
#. Updated example files to use new functionality: ``plotadd1.e``, ``plotaddci.e``, ``plot_bootmean.e``, ``plotadderrorbar2.e``, ``plotar2.e``, ``plotbar.e``, ``plotbox_auto.e``, and more.

22.0.3
------

#. :func:`stocv` now supports dataframe inputs.
#. :func:`satocv` now supports dataframe inputs.
#. :func:`strtof` now supports dataframe inputs.
#. Bug Fix: :func:`ftocv` now correctly strips metadata if a dataframe is provided.
#. Bug Fix: :func:`loadd` now correctly works with CSV and XLS files with ``header_row = 0`` for the control struct member.

22.0.2
------

#. Graphics: Added support for date variables to :func:`plotScatter` and :func:`plotXY`.
#. Graphics: Added support for specifying date intervals to :func:`plotSetXTicInterval`.
#. Optimized changing the format in the symbol editor for extremely large symbols.
#. Add :func:`warninglog` and :func:`warninglogat` keywords to produce warning, similar to :func:`errorlog` and :func:`errorlogat`.
#. Bug Fix: Context menu actions in the symbol editor were erroneously remapped to copy.
#. Bug Fix: When changing to a numeric or string/category type in the symbol editor, the generated code would have an incorrect column if 'Create New Column' was checked.
#. Bug Fix: Passing a dataframe date column as a position argument to a plot with a datetime axis was not keeping the position as a date.
#. Bug Fix: :func:`plotSetGrid` had a regression which dropped support for the deprecated method of specifying 0 (off) or 1 (on) with an integer. This has been restored for backward compatibility.

22.0.1
------

#. Bug Fix: Specifying the GAUSSHOME value with non platform-specific separators would cause globbing to fail when reading gauss.cfg, (eg ``$GAUSSHOME/pkgs/*/src`` on Windows)
#. Bug Fix: Filtering a date column in the File Import dialog or symbol editor was referencing the wrong column type when generating code. The resulting filtering operation was correct, but has been rectified to generate more friendly code.

22.0.0
------

#. Added new preprocessor ``#includedir`` to add current file directory to source path. If executed from the Command Window (PGM), uses current working directory.
#. ``#include`` and ``#includedir`` statements can now be processed with ``F4`` in the GUI.
#. :func:`__FILE_DIR` now works with ``F4`` in the GUI.
#. Added new function :func:`resetsourcepaths` to restore source path to initial value from gauss.cfg.
#. Duplicate header prevention was added for dataframes. This can be toggled via policy in gauss.cfg with the ``policy_check_df_header_dupes`` key.
#. Added new function :func:`asdf` to allow automatic conversion of scalar/matrix/string/string array to a dataframe. Headers can now be specified as N additional arguments, where N is equal to the column count of the input symbol.
#. Added new function :func:`currentprocname` was added to return the name of the current proc. It also accepts 1 argument to return the name of the calling procedure(s) from previous stack frame(s) if desired.
#. Added new function :func:`isunique` to return a scalar denoting whether all rows in a matrix or dataframe are unique.
#. Added new function :func:`isrowunique` to return a vector denoting whether each row is unique.
#. Added new function :func:`dropduplicates` to return the input matrix/dataframe with all duplicate rows removed.
#. Added new function :func:`getduplicates` to return the input matrix/dataframe with only duplicate rows present. The original row number is prepended as the first column to the output of this function.
#. :func:`setcolnames` now has header duplicate checking and auto-renaming if the ``policy_check_df_header_dupes`` policy is enabled in gauss.cfg. This policy is enabled by default.
#. :func:`dfname` was added as an alias for :func:`setcolnames`.
#. :func:`dftype` was added as an alias for :func:`setcoltypes`.
#. :func:`asdate` was added as an alias for :func:`setcoldateformats`.
#. ``%e``, ``%E``, ``%f``, ``%F``, ``%g``, ``%G`` flags were reimplemented for more consistent results with :func:`sprintf`.
#. :func:`dttostr` will now return a string instead of a 1x1 string array.
#. Formula strings now support more than one dependent variable. (fields specified before a ``~`` in a formula string).
#. Added ``%v`` support to :func:`asdate`. This is shorthand for ``%e-%b-%Y``.
#. Added support for the automatic monthly, quarterly, and yearly date-conversions in Stata files (e.g. .dta files).
#. :func:`sprintf` now supports the following base conversion patterns: ``%b`` (binary), ``%o`` (octal), ``%x`` and ``%X`` (hex).
#. :func:`aggregate` now accepts an optional input specifying the column index or name of the variable to aggregate on.
#. Graphics: :func:`plotScatter`, :func:`plotXY` and :func:`plotBox` now support formula strings and automatically handle dataframe input to generate the appropriate axis and legend labels.
#. Graphics: New formula string keyword, :class:`by` splits data to be plotted by  :func:`plotScatter`, :func:`plotXY` and :func:`plotBox` by a specified categorical or string variable and automatically handle dataframe input to generate the appropriate legend items.
#. Graphics: Added support for legends to have their own title with :func:`plotSetLegendTitle`.
#. Graphics: Added new functions for vertical/horizontal lines to span the entire axis: :func:`plotAddVLine`, :func:`plotAddHLine`.
#. Graphics: Added new functions for vertical/horizontal bars to span the entire axis: :func:`plotAddVBar`, :func:`plotAddHBar`.
#. Graphics: :func:`plotAddVBar` and :func:`plotAddHBar` support FRED-style input data. (eg { 1950, 1 }, { 1951, 1 }, { 1952, 0 }, ...).
#. Graphics: Added support for dates in simple string format to :func:`plotSetXRange`.
#. Graphics: Added support for outliers to :func:`plotBox`.
#. Graphics: :func:`plotBox` can now accept a vector of groups as the first data input. The ``y`` variable will be split by the categories in the group vector and plotted as separate boxes.
#. Graphics: Added new function :func:`plotSetJitterRange` to control the jitter range for :func:`plotScatter` and :func:`plotBox` outliers.
#. Graphics: Attributes for each axis can be assigned separately. The existing :func:`plotSetAxesPen` convenience procedure will still assign attributes to all axes simultaneously.
#. Graphics: The font can now be specified for :func:`plotContour` labels.
#. Graphics: Axis tics can now be displayed on the inside of the chart (as opposed to outside only) or hidden completely with the :func:`plotSetTicPosition` function.
#. Graphics: Added new function :func:`plotSetOutlineEnabled` to allow a box outline around the entire chart. Outline attributes are controlled via axis properties using :func:`plotSetAxesPen` or individually with :func:`plotSetXPen` and :func:`plotSetYPen`.
#. Graphics: Axes are now at a higher Z-order than series, so lines will not render on top of the axes lines.
#. :func:`plotSetAxesPen` has a new optional input to set the axes line style.
#. Graphics: New functions :func:`plotSetXGridPen` and :func:`plotSetYGridPen` allow the major and minor ``x`` and ``y`` axis grid lines to be enabled and styled separately.
#. Graphics: New function :func:`plotSetGridPen` allows the major and minor ``x`` and ``y`` axis grid lines to be enabled and styled.
#. Graphics: Graph profile settings in the preferences dialog have been fully refactored to only show properties related to the selected graph category. This should reduce confusion regarding which properties are respected when plotting a graph of the specified type.
#. Graphics: Added support for specifying the bar width (:func:`plotSetBarWidth`) and box width (:func:`plotSetBoxWidth`).
#. Graphics: :func:`plotAddXY` and :func:`plotAddScatter` now support category labels as input for X values, so data can be added to locations specified by a text label, rather than a numeric value.
#. Graphics: Contour is now a new default graph profile instead of being shared with Surface.
#. Graphics: New convenience function :func:`plotSetLinePen` to set the line width, color and style in one call.
#. Graphics: New function :func:`plotCloseAll` closes all open graphs.
#. Graphics: Performance: support was improved for plotting large numbers of points for XY and scatter series.
#. Graphics: Behavior change: the default line thickness for bar plots has been set to zero to be consistent with commonly desired styling for added spanning bars.
#. Graphics: Behavior change: the legend position can be updated with settings from a plotAdd call if no legend items already exist on the graph.
#. Graphics: Bug Fix: Outside middle legend will now always have a vertical orientation.
#. Graphics: Bug Fix: :func:`plotOpenWindow` now retains focus in the widget prior to the call (eg the PGM).
#. Graphics: Bug Fix: :func:`plotAddBarH` would calculate the X offset incorrectly if the input X values were index values instead of labels.
#. Graphics: Bug Fix: Axis properties for :func:`plotPolar` was applying the settings in a reversed manner. X-Axis settings now represent the azimuth with Y-Axis settings representing the radial axis. The input order for :func:`plotPolar` has not changed.
#. Graphics: Bug Fix: :func:`plotTSHF` would not allow a fixed axis range to be specified.
#. Graphics: Bug Fix: :func:`plotTSHF` would sometimes omit axis labels in the case of too few calculated labels. At least 1 will be rendered now.
#. Performance: :func:`movingave` up to 4-6x faster.
#. Performance: :func:`unique` was optimized and should be faster.
#. For convenience you can now assign a scalar value to multiple elements of a matrix or dataframe (eg ``x[1 3 5,2] = 7.3;``).
#. Dataframes: All dataframe functions (:func:`dfname`, :func:`dftype`, :func:`asdate`, etc) can now automatically convert a non-dataframe input to a dataframe. String arrays are automatically converted to a category column.
#. Dataframes: :func:`asdate` now allows omission of the format argument, and will default to ``%Y-%m-%d %H:%M:%S.%L``. All or part of this format can be specified in the input argument.
#. Dataframes: passing a format of ``%s`` to :func:`asdate` will automatically coerce it to a friendly format.
#. Dataframes: Behavior: Overwriting an entire column during an assign will overwrite the LHS metadata if the RHS is also a dataframe.
#. Dataframes: Behavior: Combining dataframes with string arrays using the string combine operator, ``$+`` is now supported.
#. Dataframes: Multiple new functions now support dataframes as input arguments: :func:`strtrim`, :func:`strtriml`, :func:`strtrimr`, :func:`strtrunc`, :func:`strtruncl`, :func:`strtruncr`, :func:`strtruncpad`, :func:`upper`, :func:`lower`, :func:`strindx`, :func:`strreplace`, :func:`strsect`, :func:`indsav`, :func:`indnv`, :func:`contains`, :func:`strsplit`, :func:`strjoin`, :func:`strcombine`, :func:`aggregate`
#. Dataframes: A low-level function :func:`normalizecollabels` was added to automatically refactor string/category columns to remove duplicates and consolidate keys.
#. Dataframes: Added string/string array assignment support to existing string/category columns.
#. Dataframes: Date pattern matching has been relaxed. If a string fully matches a date format pattern completely, the calculated date up until that point is now returned instead of requiring the entire format to be satisfied. Most functions that take a date format pattern now default to allowing full/partial usage of the pattern ``"%Y-%m-%d %H:%M:%S.%L"``.
#. Dataframes: :func:`strctoposix` now returns a dataframe.
#. Dataframes: Symbols viewed in the symbol editor will now show up as a 'Dataframe' in the type field instead of 'Matrix'.
#. Dataframes: Improved behavior when checking for like-column types in a partial row assignment from one dataframe to another.
#. Dataframes: :func:`outerjoin` (left outer join) has been rewritten completely as an intrinsic with full support for dataframes with a significant performance increase.
#. Dataframes: Generated code in the file import dialog now takes advantage of new dataframe behavior to allow more concise code.
#. Dataframes: Specifying custom col labels for string/category columns now uses a :func:`seqa` representation for the values if they are left as their default. (Optimization)
#. Dataframes: :func:`sortc` now allows you to specify columns by name.
#. Dataframes: Empty date formats now default to the default date format of ``%Y-%m-%d``.
#. Dataframes: Any function converting a symbol to a string/category will now sort the labels before generating the keys.
#. Dataframes: Bug Fix: Unsorted indices passed to dataframe functions could cause changes to be incorrectly applied.
#. Dataframes: Bug Fix: Specific cases where a program errored out could potentially remove metadata from a symbol in the workspace.
#. Dataframes: Bug Fix: Metadata was not being applied correctly in specific struct-index assignment cases.
#. Dataframes: Bug Fix: String/Category columns can now be used with the ``%s`` pattern in :func:`sprintf`.
#. Dataframes: Bug Fix: All dataframe and string combinations are now supported for ``$+`` operations.
#. Behavior Change: :func:`aggregate` will now check for and ignore missing values by default. An optional input flag has been added to not check for missing values as in the previous version.
#. Behavior Change: Code generation for dataframe operations in the symbol editor have been optimized to be as concise as possible.
#. Behavior Change: Columns in the symbol editor will attempt to automatically resize to yield a more user-friendly display.
#. Behavior Change: Multiple equality filters of the same type in the dataframe 'Filter' tab are now grouped together to use :func:`rowcontains` for optimized code generation and performance.
#. Behavior Change: Policy ``policy_scalar_df_indexing`` is now enabled by default. This policy was added in 21.0.6 to control behavior for dataframe indexing operations that return a scalar. Resulting scalar will now remain a dataframe by default.
#. Bug Fix: :func:`setcollabels` incorrectly allowed the indices argument to be omitted. This has been fixed, but improved to allow omission of the indices argument if the input argument only has one column. The values used will be [0...N-1] where N is the number of labels.
#. Bug Fix: :func:`move` now makes a copy if the input symbol can't release ownership.
#. Bug Fix: Use system palette when restoring regular font color in textbox of editor/PGM find widgets.
#. Bug Fix: Custom missing values set with :func:`msym` was incorrectly printing the missing value backwards in :func:`sprintf`.
#. Bug Fix: :func:`selif` could return a partial dataframe if the return value was a scalar missing.
#. Bug Fix: If a tab character was the delimiter in the file import dialog, the generated code would include a literal tab character as a string. This has been fixed to escape the tab character in the string (eg ``ctl.delimiter = "\t"``).
#. Bug Fix: :func:`seqadt` and :func:`seqaposix` now correctly allow dataframes to pass through without losing their metadata.
#. Bug Fix: Formula strings that contained a ``:`` or ``*`` character in the argument field (eg ``date($my_date, '%Y-%m %H:%M')``) were being treated as multiplier operations.
#. Bug Fix: Add date cell editing support in the symbol editor.
#. Bug Fix: In the import dialog, generated code was not updating when a custom category label or date format was specified. This bug was visual only, as the correct code was generated when the *Import* button was pressed.
#. Bug Fix: In the import dialog, the input box for the new column name was not noticeably greyed out on macOS when the widget was disabled.
#. Bug Fix: The symbol editor will no longer automatically open the 'Manage' panel for dataframes.
#. Bug Fix: :func:`setcolnames` was incorrectly allowing empty names as input.
#. Bug Fix: A missing/NaN in a string/category column will now display the correct value when printed, instead of an empty string.

21.0.8
------

#. Bug Fix: :func:`plotContour` would render incorrectly if a custom X/Y range was specified.

21.0.7
------

#. Bug Fix: :func:`strctodt` and :func:`strctoposix` would set the finalized date to 1 day prior if the day was not specified in the string.
#. Bug Fix: Deleting a dataframe from the data page while also having the dataframe open in the symbol editor would cause a crash.
#. Bug Fix: Non UTF-8 encoded dataframe category string values could sometimes display incorrectly in the symbol editor.
#. Bug Fix: Autcomplete could trigger in comments or strings if the cursor was at the very end of the file.
#. Bug Fix: The autocomplete popup could show up in the Program Input/Output window (PGM) at inconvenient times, such as input during a :func:`cons` call.
#. Bug Fix: When a specific operator prefixes a symbol, hovering while debugging or trying to watch the symbol with Ctrl+E would retain a leading period character.
#. Bug Fix: :func:`timediffdt` and :func:`timediffposix` were incorrectly returning output as a dataframe.
#. Bug Fix: :func:`aggregate` now correctly returns result as a dataframe.
#. Bug Fix: An empty date format string was allowed in :func:`setcoldateformats`. Now uses default date format in that case.

21.0.6
------

#. Added policy to control behavior for dataframe indexing operations that return a scalar. Resulting scalar can now remain a dataframe.
#. Added dataframe category/string support to :func:`indexcat`, :func:`rowcontains`, :func:`ismember`.
#. Windows: Added MySQL/MariaDB SQL driver.
#. Bug Fix: Printing a dataframe now correctly prints a newline before the headers.
#. Bug Fix: Indexing a data frame with a string array could cause a crash in certain cases.
#. Bug Fix: Specific edge cases could cause incorrect metadata to be applied in indexing operations. Numerical results were not affected.
#. Bug Fix: :func:`strlen` now correctly works with dataframe category/date columns.
#. Bug Fix: Memory leak in :func:`seqaposix` and :func:`seqadt` for certain cases.
#. Bug Fix: Memory leak in :func:`eye` for certain cases.
#. Bug Fix: Dataframe comparisons against a string array operand could crash.

21.0.5
------

#. Add new :func:`plotAddXYFill` function.
#. Update OpenSSL libraries on Linux to 1.1.1j.

21.0.4
------

#. Bug Fix: Fixed edge-case performance issue.

21.0.3
------

#. Bug Fix: :func:`dbGetTables` would crash GAUSS.
#. Bug Fix: :func:`eye` would crash in specific circumstances if a value less than 1 was passed in.

21.0.2
------

#. Bug Fix: :func:`sprintf` had incorrect output in the ``%g`` case with 0's after a decimal and prior to the first significant digit.

21.0.1
------

#. Editor documents now have yellow underline markup for locals and/or arguments that are unused, as well as an icon in the margin.
#. Bug fix: :func:`corrxs` was not correctly copying metadata upon return.

21.0.0
------

#. GAUSS now supports dataframes with date, categorical, string and numeric columns.
#. :func:`loadd` now returns a dataframe. This is a behavior change that can be reverted by the `#defines` in `policy.dec`.
#. :func:`loadd` now accepts an optional input with support for additional data loading options, such as selecting a row range, specifying Excel sheets, CSV delimiters, the header row, values to interpret as missing values, and the quote character.
#. :func:`loadFileControlCreate` fills a `loadFileControl` structure with the defaults for the new data loading options.
#. Formula string keyword ``cat`` now supports an optional input to set the base case.
#. Formula string keyword ``date`` now supports an optional input to specify the incoming date format.
#. Logical operators (``.<``, ``.>``, ``.<=``, ``.>=``, ``.==``, ``.!=``) support comparisons with date strings and categorical variable labels.
#. :func:`glm` and :func:`olsmt` support dataframes and automatically turn categorical variables in to dummy variables.
#. :func:`dstatmt` supports dataframes and counts missing values by default.
#. :func:`saved` will write, string, categorical and date variables. The variable names argument is now optional.
#. New functions :func:`setcolnames` and :func:`getcolnames` set and return columns names of a matrix, or dataframe.
#. New functions :func:`setcoltypes` and :func:`getcoltypes` set and return the variable types of the columns of a matrix, or dataframe.
#. New function :func:`setcolmetadata` sets column names and variable types for a matrix or dataframe.
#. New function :func:`recodecatlabels` changes the labels displayed for a categorical variable in a dataframe.
#. New function :func:`reordercatlabels` changes the order of the labels displayed for a categorical variable in a dataframe.
#. New function :func:`setbasecat` sets the base category of a categorical variable.
#. New functions :func:`setcollabels` and :func:`getcollabels` set and return the integer key values and string labels of categorical variables in a dataframe.
#. New function :func:`getcollabelvalues` returns the string labels for every observation of a categorical variable as a string array.
#. New function :func:`setcoldateformats` sets the display format of a date variable, :func:`getcoldateformats` returns the display format.
#. New function :func:`hasmetadata` returns a 1 if the input is a dataframe.
#. New function :func:`asmatrix` turns a dataframe into the equivalent matrix.
#. New function :func:`order` reorders columns of a dataframe by name.
#. New function :func:`frequency` computes a frequency table for a categorical variable.
#. The **Data Import Window** now supports variable selection, interactive filtering and automatic code generation.
#. The suffix for duplicate headers in the import dialog now start at _2 instead of _1.
#. **Symbol Editors** support the same variable selection and filtering options added to the **Data Import Window**.
#. Formatting in the **Symbol Editor** is now on a per column basis.
#. Character vectors now show up to 8 characters in the **Symbol Editor** (the length is NOT limited for string arrays or dataframe string and category columns).
#. CSV sniffing in the **Data Import Window** will now only occur for the first 200 rows instead of the entire file to improve performance.
#. The **Project Folders** window now automatically shows contents of the Current Working Directory.
#. The **Project Folders** window now shows new files without need to refresh.
#. The default setting for the run button is now to run the active file. This can be changed in Preferences to be the same as previous versions.
#. **Find Usages** for local variables now reports only instances of the local variable.
#. `CTRL+F1` will now find the declaration of local variables in a procedure.
#. New Preference option to specify the default directory for **File > Open**.
#. Assignments to arrays of structures in `threadFor` loops is now allowed.
#. Bug fix: Memory leak in :func:`lagtrim`.
#. Bug fix: Memory leak in specific situation with :func:`EuropeanBSCall`.
#. Bug fix: `threadFor` would not allow certain cases with multiple references to a slice variable to compile.
#. **Control Var** node on **Data Page** is now collapsed by default.
#. New example files for dataframe 'get' and 'set' functions as well as :func:`frequency` and :func:`plotFreq`.
#. GLM example files updated to use dataframes.

20.0.7
------
#. Bug Fix: :func:`sprintf` had incorrect output in the ``%g`` case with 0's after a decimal and prior to the first significant digit. (Backported)

20.0.6
------
#. macOS: Add environment variable ``QT_MAC_WANTS_LAYER`` to LSEnvironment key to fix hang on startup with Big Sur.

20.0.5
------

#. :func:`strctoposix` and :func:`posixtostrc` now support specifying the quarter (``%q``).
#. Add ability to toggle 'Safe Write' in preferences. This fixes an issue some users may experience when trying to save files in Dropbox/OneDrive/Google Drive, or other similar shared folders.

20.0.4
------

#. Bug Fix: :func:`sprintf` was omitting trailing 0's for ``%f`` case.
#. Bug Fix: A regression caused :func:`plotSurface` to segfault on Windows.
#. Bug Fix: Using cql_stubs.dll with a GAUSS Engine program did not have the correct symbol definitions to be used for deployment.
#. Bug Fix: Some graphics legend items were not appearing in very specific cases.
#. Bug Fix: :func:`plotLogX` and :func:`plotLogY` were incorrectly setting both axes to log scale.
#. Bug Fix: :func:`gmmFit` was not computing Hansen J-stat.
#. Bug Fix: Some Project View folders did not have 'Set to Working Directory' available.
#. Added optional user-specified truncation lags to :func:`gmmFitIV` and :func:`gmmFit`
#. Bug Fix: Updated HAC weight matrix computation method in :func:`gmmFit` and :func:`gmmFitIV`

20.0.3
------

#. Bug Fix: The :func:`olsmt` procedure was not correctly implementing specified weights when data inputs included missing values.
#. Added error log for case of non-compatible covariance specifications with weighted least squares.
#. Added error log for case of improperly specified weights.
#. Added error log for case of non-compatible pairwise deletion option with weighted least squares.
#. Add custom quotation character support to :func:`csvReadM` and :func:`csvReadSA`.
#. Bug Fix: :func:`varget` was not performing a deep copy for structs.
#. Improve performance for enumeration and tooltips on symbol page for very large strings.
#. Bug Fix: :func:`plotAddBar` and :func:`plotAddBarH` could sometimes segfault without a correctly initialized axis.
#. Bug Fix: :func:`plotAddBarH` was not behaving the same as :func:`plotAddBar` with existing labels and custom indices.

20.0.2
------

#. File import dialog now uses ``%g`` formatting by default.
#. Bug fix: Certain editor codecs were not loading correctly on startup when selected in preferences.
#. macOS: Build against Qt 5.12.6.
#. macOS: Upgrade Sparkle to 1.22.
#. Linux: Add new-version check functionality to Linux.

20.0.1
------
#. Added new example files :file:`aggregate_housing.e`, :file:`sprintf_cancer_1.e`, :file:`sprintf_cancer_2.e`.
#. Bug fix: :func:`plotAddHist` could crash if the previous graph did not have a category axis.

20.0.0
------

#. New integrated package manager to download, install and uninstall Aptech provided, or private GAUSS packages.
#. New function, :func:`aggregate` to group data by a column containing group ids, using one of several methods such as mean, median, mode, standard deviation, sum, and variance.
#. New function :func:`sprintf` formats combinations of string and numeric matrices.
#. New function :func:`loaddSA` loads variables from datasets as GAUSS string arrays.
#. New function :func:`dynargsGet` retrieves optional arguments passed into a procedure, or default values.
#. New function :func:`dynargsCount` counts the number of optional arguments passed into a procedure.
#. New function :func:`dynargsTypes` returns a vector indicating the types (i.e. matrix, string, structure) of the optional arguments passed into a procedure.
#. New function :func:`modec` computes the mode of the columns of a matrix.
#. Added option to use custom weights for weighted least squares estimation with :func:`olsmt`.
#. New function :func:`plotXYFill` creates filled area plots between XY lines.
#. New function :func:`plotBarH` creates horizontal bar plots.
#. New function :func:`plotSetYTicInterval` controls y-axis tick label positioning.
#. Added ability for :func:`plotAddBar` to add bars to specified locations.
#. :func:`plotSetLegend` now allows setting the legend location by axis coordinates as well as text location.
#. New function :func:`plotSetLegendBorder` controls the style properties of the legend border.
#. All plot colors now support alpha channel, providing the option to add transparency to any graph item.
#. Added new methods to :func:`impute` function: predictive mean matching, local residual draws and linear prediction.
#. Command reference documentation style updates and new examples.
#. Speed increase for certain cases of ``*X'X*`` with small to medium matrices.
#. Reading and writing :file:`.XLSM` files is now supported for the case where the COM/Excel interface is not used.
#. Increased compatibility for newer style :file:`.XLSX` files for the case where the COM/Excel interface is not used.
#. Bug fixes: several minor bug fixes for reading :file:`.XLSX` files in the case where the COM/Excel interface is not used.
#. Added count of number of open files to **Edit Page** to open file dropdown selection widget.
#. Bug fix: :func:`substute` reported error unnecessarily for specific case with mixed numeric and string input.
#. Bug fix: :func:`xlsReadSA` reported error with string array *vls* input.
#. Bug fix: :func:`reclassify` possible crash when the *from* variable was much smaller than *to*.
#. Changed state variable in example dataset :file:`hsng.dat` to a string variable with state abbreviations.
#. New example file :file:`wls.e` demonstrates weighted least squares estimation.
#. New example file :file:`impute.e` demonstrates several missing value imputation methods.
#. Adding setting ``dataloop_case = on`` to :file:`gauss.cfg`. This setting will instruct the dataloop translator to ignore case in dataloop statements.
#. Upgrade Reprise License Manager (RLM) to 13.0 for all platforms

19.2.2
------

#. Upgrade Reprise License Manager (RLM) to 13.0 for macOS

19.2.1
------

#. Add explicit query-deleting for database calls (eg :func:`dbExecQuery`) with
   :func:`dbQueryDelete` method.
#. Database: Add auto-cleanup of queries and open databases on 'new'
   statement and after ``GAUSS_FreeWorkspace``
#. Bug fix: Fix performance issues with bulk inserts for database
   operations
#. Bug fix: A dangling str-concat operation ($+) could result in a crash
   when using on the command-line
#. Bug fix: :func:`strtof` would result in output matrix twice as large as input
   even in cases of real input.



19.2.0
------

#. Full re-mapping of all key/keyw values to match GAUSS 10 and below
   values. Lookup table available in `key` and `keyw` reference pages.



19.1.2
------

#. Update bundled LaTeX library (MathJax 2.7.5)
#. Bug fix: Formula strings that specified a modifier for a variable now
   always negate the original variable. eg. ``". + ln(x)"`` will now remove
   'x' from the output
#. Bug fix: The `saveall` command could cause a program to crash after the
   save in specific situations.



19.1.1
------

#. Bug fix: Saving files was improved in situations where the file could
   be locked, resulting in being unable to save or extra temporary
   files.



19.1.0
------

#. The Program Input/Output window (PGM) now supports autocomplete for
   active workspace symbols.
#. The Program Input/Output window (PGM) and all editor documents
   support autocomplete and lexing for library symbols not part of
   gauss.lcg.
#. Struct definitions are now included in the library tool list.
#. Add more descriptive messaging to gpkg errors when installing
   packages.
#. Added function :func:`plotSetZRange` to control the range of the Z-axis on
   surface plots.
#. New example files :func:`plotlogx.e` and :func:`plotlogy.e`.
#. Bug fix: :func:`quantileFit` errors for case when weights are included and
   data has missing values.
#. Bug fix: When viewing a struct member with the symbol editor (e.g
   ``Ctrl+E``), the member now correctly scrolls into view in the tree.
#. Bug fix: The 'Format Text' functionality in editor documents now keep
   preprocessor statements fully left-aligned. The 'keyword' token now
   correctly starts an indentation block.
#. Bug fix: Autocomplete pop-up could freeze in certain situations with
   too many token references due to memory leak.
#. Bug fix: Potential freeze when debugging with an undocked graphics
   page and floating symbol watch.
#. Bug fix: Specific case of weights with missing values in data when
   using :func:`quantileFit`.
#. Bug fix: Fix 'Save with Encoding' option from codec selector dialog.
#. Bug fix: Add missing context-menu icons for tab split action when a
   split already exists.
#. Bug fix: Linux startup script writing empty file named '0' in current
   working directory.
#. Bug fix: Proc detection for editor documents in certain cases where
   proc name or arguments contain underscores.
#. Bug fix: Accidentally resetting legend orientation in :func:`plotSetLegend`.
#. Bug fix: Rare crash when plotting.
#. Bug fix: Reading files with :func:`loadd` could fail to read mixed columns in
   rare cases.
#. Bug fix: Legend position now only uses original position on a :func:`plotAdd`
   even if initial plot call had no legend.
#. Bug fix: Parent graph could have incorrect sizing after a :func:`plotAdd` if
   legend position was outside.



19.0.2
------

#. Speed up of approximately 33% to :func:`quantileFit`.
#. Improved formatting of output tables for :func:`dstat`, :func:`dstatmt` and :func:`olsmt`.
#. Added ability for plotSetYTicLabel to control the tick label
   formatting of the right y-axis.
#. Bug fix: possible crash in certain cases when passing scalar input to
   :func:`invpd`.
#. Bug fix: output table printing returned error when variable names
   were not specified in :func:`quantileFit`.
#. Bug fix: X-tick labels did not start at the first label position
   specified by :func:`plotSetXTicInterval` in certain cases for non-time series
   data.
#. New example program ``plottshf_yellowstone.e`` shows how to: plot monthly
   data with :func:`plotTSHF`, set labels and format the tick labels for the
   left and right Y-axes, control the location and frequency of x-axis
   tick labels, select observations from a matrix based on data and
   specify the graph size programmatically.
#. New example programs ``plotbox_auto.e``, and ``quantilefit3.e``.
#. Bug fix: Allow curve attribute control in graphics page settings
   widget for box plots with ``groupingBehavior`` set to 1.



19.0.1
------

#. Update ``scatter1.e example``.
#. Fix action list 'Current File' action.



19.0.0
------

#. New online license activation allows for convenient license
   activation from a product key.
#. New function :func:`quantileFitLoc` performs local linear and quadratic
   quantile regressions.
#. New function :func:`quantileFit` performs quantile regression.
#. New function :func:`qfitControlCreate` creates default ``qfitControl`` structure.
#. Added option for clustered standard errors and robust standard errors
   to :func:`olsmt` and :func:`quantileFit`.
#. New function :func:`clusterSE` for computing clustered standard errors.
#. New function :func:`robustSE` for computing heteroscedastic-robust standard
   errors.
#. New 'date' keyword for formula strings simplifies reading dates from
   CSV files.
#. New '$' keyword for formula strings reading and processing string
   columns.
#. New function :func:`norm` computes the matrix 1, 2 (Spectral), Infinity,
   Frobenius and Nuclear norms or the vector p-norm.
#. New function :func:`lagTrim` returns a matrix containing specified lags
   and/or leads with incomplete rows removed.
#. New function :func:`recserVAR` performs efficient simulation of a VAR
   process.
#. :func:`lagn` can now accept an optional argument to specify the fill value
   for the missing observations.
#. :func:`saved` can now conveniently create datasets in Excel or CSV format.
#. :func:`plotTS` can now plot daily data.
#. X-tick locations can now be controlled with :func:`plotSetXTicInterval` for
   XY, Scatter, Contour and Histogram plots.
#. New function :func:`plotTSHF` and :func:`plotAddTSHF` creates time series plots for
   high frequency and irregularly spaced data.
#. New functions :func:`plotTSLog` and :func:`plotAddTSLog` create time series plots
   with the y-axis in log space.
#. New function :func:`plotSetGroupingBehavior` to control whether box plots are
   drawn as separate boxes or part of a group--which controls color
   behavior and spacing.
#. New function :func:`plotSetYTicLabel` controls the format and angle of y-axis
   tick labels.
#. New function :func:`plotSetLegendBkd` controls the opacity and color of the
   legend background.
#. Behavior change: The following default graph settings have changed:
   the grid is off, the axes lines and font text color are now set to
   black.
#. Added option for Run and Debug buttons to run the Current File
   (**Tools > Preferences > Command > Behavior**).
#. New function :func:`impute` fills in missing data with a choice of imputation
   methods.
#. Outer vector product is up to 400% faster, using the \* operator.
#. Matrix inverse with :func:`inv` is 20%-400% faster for matrices with sizes
   around 40x40 to 110x110.
#. The log 10 and natural log functions, :func:`log` and :func:`ln`, take 15% to 60%
   less computation time for matrices and arrays with more than
   approximately 50 or more elements.
#. :func:`amult` performs matrix multiply with multi-dimensional arrays 20% to
   3,500% faster for arrays with approximately 50 or more elements.
#. :func:`exp` is 20% to 800% faster for matrices and arrays with more than
   approximately 50 or more elements.
#. :func:`dot` is faster.
#. ``X'y`` is faster when ``X`` is a matrix and ``y`` is a vector.
#. Matrix multiplication is faster and uses less memory when X is a
   non-square matrix.
#. New function :func:`dttostrc` converts DT Scalars to string dates with many
   new date formatting options.
#. New function :func:`strctodt` converts string dates to DT Scalars with many
   new date formatting options.
#. New function :func:`posixtostrc` converts seconds since the Epoch to string
   dates with many new date formatting options.
#. New function :func:`strctoposix` converts string dates to seconds since the
   Epoch with many new date formatting options.
#. New function :func:`dttoposix` converts DT Scalar dates to seconds since the
   Epoch.
#. New functions :func:`timedeltadt` and :func:`timedeltaposix` add or subtract from DT
   scalar or Posix date/time values in terms of user specified time
   units.
#. New functions :func:`timediffdt` and :func:`timediffposix` compute the difference
   between dates in either DT scalar or Posix date/time values in terms
   of user specified time units.
#. New functions :func:`seqadt` and :func:`seqaposix` create sequences of dates in
   either DT scalar or Posix date/time format with a user specified time
   increment.
#. Added support for high-frequency data to Posix date/times.
#. Final input to :func:`strsect` is now optional. New two input case: :func:`strsect`
   will copy from the start index to the end of the string.
#. Final input to :func:`strindx` and :func:`strrindx` is now optional. New two input
   case: :func:`strindx` will start searching from the first character, while
   :func:`strrindx` will search from the last character.
#. :func:`sqpSolvemt` now has the option to compute covariance matrix from
   cross-product of gradient.
#. Date strings returned from :func:`xlsReadSA` (as well as :func:`loadd`) that use
   LibXL or ``xls.dll`` (Windows-only) now return date with time information
   in fixed format pattern ``"MM/DD/YYYY HH:MI:SS.SSS"``.
#. New GUI control. Right-click on a program tab and change your working
   directory to the directory of that file.
#. New GUI control. Right-click on a program tab and copy the directory
   containing that file to the clipboard.
#. HiDPI scaling is enabled by default.
#. Updated navigation bar and new icons throughout the application.
#. All icons now have HiDPI support (eg Retina displays).
#. User interface styling updated to use flat elements.
#. New preference (**Tools > Preferences > Edit > Default Encoding**)
   controls default file encoding for files opened in the GAUSS editor.
#. New option to set file encoding for individual files (**Edit > Select
   Encoding**).
#. Bug fix: improved automatic tick label location selection for data
   separated by very small intervals.
#. Bug fix: multi-dimensional array matrix multiplication in certain
   cases with complex matrices would return an error message instead of
   computing the product.
#. Bug fix: possible crash when opening files with very long lines.
#. Bug fix: Fix :func:`plotBox` with only 1 value.
#. New example files: ``plottshf.e``, ``robustse.e``, ``quantilebs.e``,
   ``quantilefit1.e``, ``quantilefitloc1.e``.
#. Bug fix: Fix source browser not highlighting match in rare cases.
#. Bug fix: Fix issue with incorrect format type passed to :func:`satostrc`.
#. Bug fix: Fix source browser replace for \\r\n line endings in files
   not currently open.
#. OpenSSL dependencies are now bundled (Linux & Windows).


18.1.5
------

#. Bug fix: Regression fix: :func:`varput` was not working with char literals
   for symbol name.
#. Bug fix: Fix rare stack overflow for stopping programs with certain
   multi-dimensional structs.
#. Bug fix: Fix memory issue with news check from 18.1.4.



18.1.4
------

#. UI: Check for news from Aptech on startup.
#. UI: Show full value for strings and string arrays in debug tooltips.
#. UI: Add tooltips to debug watch widget.
#. Perform better validation and whitespace trimming for formula
   strings.
#. Specifying 'factor' or 'cat' in formula string now negates the
   original variable.
#. Bug fix: in :func:`ols`, constant was not added to variable labels for :func:`ols`
   report in certain case.
#. Bug fix: :func:`olsqr` `trap` case was not setting `scalerror` for 2 out / 3 in
   case.
#. Bug fix: Assigning `struct` string member from 1x1 string array was
   broken.
#. Bug fix: Recoded symbol debug tooltips. Sometimes columns didn't
   align correctly. This has been fixed.
#. Bug fix: XLS files that didn't have a lowercase extension did not
   load correctly in import dialog.
#. Bug fix: :func:`varget` now supports 1x1 string arrays.
#. Bug fix: assigning to `struct` string member would crash in specific
   cases.



18.1.3
------

#. Minor bug fixes, documentation and example updates.



18.1.2
------

#. Updates for examples ``glmbinomial1.e``, ``glmgamma1.e`` and ``glmnormal1.e`` to
   use formula string notation.



18.1.1
------

#. Bug fix loading structs via GDA files.
#. :func:`saveStruct` and :func:`loadStruct` now work with files greater than 2GB on
   Windows (up to 4GB).
#. Bug fix: :func:`sampleData` could hang if 'size' parameter was less than 0.
#. Bug fix: Update file access flags on Windows to prevent occasional
   failure reading/writing files on network drives.



18.1.0
------

#. Add auto-update to macOS and Windows.
#. Add tooltip to color selection buttons in UI.
#. Added options to sort eigenvalues to the :func:`schur` function.
#. Bug fix: Fix package installation when both legacy xml and new
   package json are both present.
#. Bug fix: Support > 2GB read/writes on macOS and Linux.
#. Bug fix: Added ability to debug functions with :func:`threadfor` statements.
#. Other bug fixes.



18.0.1
------

#. Allow spaces in file names and paths in GAUSS library files.
#. Bug fix: Fix for incorrect error report when passing large numbers of
   extra dynamic arguments to :func:`gmmFit`.
#. Bug fix: Fixed incorrect error report with literal integer indexing
   of :func:`threadfor` temporary variables in certain cases.
#. Bug fix: Fix for possible compile time stack overflow with nested
   structure definitions.



18.0.0
------

#. Added initial version of package manager (gpkg) CLI. Supports
   installation/removal of GAUSS application package(s).
#. Added ability to read SAS and STATA datasets with :func:`loadd` and any
   function that takes a formula string, such as :func:`dstatmt`, :func:`glm`, :func:`gmmFitIV`.
#. Formula strings can now apply transformations from GAUSS procedures,
   such as :func:`ln` and :func:`exp` as well as interaction terms.
#. New keyword, 'factor', in formula strings will load specified columns
   as a set of dummy variables.
#. New keyword, 'cat', in formula strings will load specified string
   columns and transform them to a vector of numeric categories.
#. New function :func:`setBlockSize` to set the size of each chunk of data that
   is read from a dataset that does not fit in memory.
#. New function :func:`getHeaders` to return the variable names from any
   supported data set type.
#. New function :func:`gmmFit` computes generalized method of moments estimates
   from user specified moment function.
#. New function :func:`gmmFitIV` estimates instrumental variables models using
   the generalized method of moments.
#. New function :func:`gmmControlCreate` creates default :class:`gmmControl` structure.
#. New function :func:`plotCanvasSize` to programmatically control the size of
   graph canvas.
#. New function :func:`plotSetTicLabelFont` to programmatically control the
   font, font-size and font-color of X and Y tic labels.
#. Speed up of chained concatenation operations and scalar indexing
   operations by 2-4x.
#. Speed up of x'y for the vector-vector case by 25% to 800% for vectors
   longer than approximately 50 elements.
#. Speed up of 15-30% for :func:`dstat`, :func:`dstatmt` and :func:`ols` for large matrix
   inputs.
#. Speed up run-time scalar performance on macOS. Smaller speed-up for
   all symbol types on all platforms.
#. Speed up contour plot processing.
#. New functions :func:`innerJoin` and :func:`outerJoin` for joining matrices on
   specified columns.
#. New function :func:`delcols` to remove specified columns from a matrix.
#. New function :func:`contains` indicates whether a matrix, multi-dimensional
   array or string array contains one or more elements from the second
   input.
#. New functions :func:`isMember` and :func:`rowContains` indicate whether any element
   of a matrix, or any element of a row of a matrix, 2-dimensional array
   or string array contains one or more elements from the second input.
#. New function :func:`strreplace1` to replace all instances of a substring in a
   string or string array with another substring.
#. New function :func:`squeeze` to remove singleton dimensions from a
   multi-dimensional array.
#. New function :func:`blockDiag` to create a block-diagonal matrix from
   multiple input matrices.
#. New function :func:`besselk` computes the modified Bessel function of the
   second kind.
#. New function :func:`rndRayleigh` to compute Rayleigh distributed random
   numbers.
#. New functions :func:`blendColorPalette`, :func:`getColorPalette`, :func:`getHSLPalette`,
   :func:`getHSLuvPalette` and :func:`listColorPalettes` to simplify the process of
   creating modern, professional and attractive color palettes for
   graphics.
#. Updated default color palettes for 2-D graph types.
#. New define `__FILE_DIR` returns the directory in which the file is
   located.
#. New functions :func:`cdfTruncNorm` and :func:`pdfTruncNorm` to compute the cumulative
   distribution function and the probability density of the truncated
   normal distribution.
#. New functions :func:`cdfLogNorm` and :func:`pdfLogNorm` to compute the cumulative
   distribution and probability density functions of the log-normal
   distribution.
#. Add initialization ability for GAUSS libraries. Placing a file named
   ``[libname]_init.src`` in the same directory as the library lcg file will
   cause that file to be ran when 'library [name]' is referenced.
#. Increase preprocessor #define max length from 40 to 1024.
#. Add globstar wildcard matching to ``gauss.cfg``. See distributed
   ``gauss.cfg`` with pkgs example.
#. Added optional inputs mean and standard deviation to :func:`cdfn`, and :func:`pdfn`.
#. Added support for multi-dimensional array inputs to :func:`pdfn`, :func:`erf`, :func:`erfc`,
   :func:`erfInv`, :func:`erfcInv`, the power operator '^'.
#. Added ability to pass string array as X axis tic labels for :func:`plotXY`
   and :func:`plotScatter`.
#. Added ability to right-click a struct member in a floating symbol
   editor window to open it in another window for the purpose of
   simultaneously viewing more than one member of a structure.
#. The function browser will now located structure definitions as well
   as proc definitions.
#. 'Toggle block comment' can now comment out selections within a single
   line of code as well as adding multi-line comments.
#. Added ability for ExE conformable vector inputs to :func:`europeanBSCall`,
   :func:`europeanBSPut`.
#. Added ability to add scatter, xy and other 2-D plot types to an
   existing contour plot.
#. Updated :func:`olsmt` to make control structure an optional input.
#. Watch window struct tree remembers expansion state and scrollbar
   position on reload (ie debug step in/over etc).
#. Watch window struct vars can now be cloned into their own watch
   window.
#. Preferences are now saved to disk when after 'Apply' or 'OK' has been
   selected instead of when GAUSS exits.
#. Bug fix: Fix `alt+left` Edit Page navigation becoming unresponsive
   sometimes.
#. Bug fix: Watch windows were sometimes not prevented from updating
   during program run, which could cause crash.
#. Bug fix for writer returning 0 on successful writes to HDF5 files,
   rather than number of written rows.
#. Bug fix: :func:`gdaReadStruct` on Linux can now read structs created on
   Windows and Mac.
#. Bug fix: Data Page preview and Debug Page Watch Symbols list took
   more memory than necessary for sparse matrices.
#. Bug fix: Fix minor memory leaks.
#. Added optional input to :func:`cdfEmpirical` to allow specification of the
   number of bins/breakpoints to use.
#. Behavior change: :func:`cdfEmpirical` now returns the breakpoints as well as
   the cumulative probability. This will require use of :func:`cdfEmpirical` to
   assign to two return values.
#. Behavior change: :func:`plotAdd` calls will now inherit curve level settings
   from the initial plot call. This should only be noticeable in cases
   in which a :class:`plotControl` structure is passed in to create the initial
   graph and subsequent :func:`plotAdds` to not use a :class:`plotControl` structure.
   This does not require a code change. See **User Guide > GAUSS
   Graphics > Adding data to existing plots** for more details.
#. Behavior change: Application modules will now be installed under
   ``GAUSSHOME/pkgs/PKG_NAME``, where ``GAUSSHOME`` is your GAUSS installation
   directory and ``PKG_NAME`` is the name of the installed application
   module, i.e. tsmt. This does not require code change. Further, this
   path can be configured through ``gauss.cfg``.
#. Behavior change: Global variable \__row is no longer referenced, use
   :func:`setBlockSize` instead. Note that this will not prevent older code from
   running correctly, but may result in less than optimal sizing of data
   blocks for which are explicitly processed in chunks which were
   previously controlled by \__row.
#. New example programs: ``cdfempirical.e``, ``gmm_auto_ols.e``, ``gmm_hsng1_iv.e``,
   ``gmm_hsng2_iv.e``, ``gmmfitiv_auto.e``, ``gmmfitiv_hsng.e``, ``gmm_tdist.e``.



17.0.5
------

#. Bug fixes.



17.0.4
------

#. Added more complete compile time checks for indexing errors and
   incorrect use of hat operator for strings.
#. Bug fix for possible crash in :func:`sampleData` when requesting a sample
   smaller than 40% of the total observations without replacement.
#. Bug fix crash when loading .plot file with empty LaTeX text boxes.
#. Bug fix for :func:`threadfor` and :func:`threadendfor` not indenting properly in
   editor.
#. Bug fix for :func:`quantiled` returning out-of-memory error with certain
   datasets.
#. Removed unnecessary dependency of Qt shared libraries for GAUSS
   Engine when using ``libcql_stubs.dylib`` on Mac.



17.0.3
------

#. Added support for new graphics with the GAUSS Engine.
#. Added tooltips on hover for elements that are partially out of view
   on the Data Page.
#. Bug fix for cutting off final portion of the last x-axis tick label
   in rare circumstances with time series plots.
#. Bug fix for memory bug in specific case related to unique and string
   array concatenation.
#. Bug fix of possible hang with debugger 'Run to cursor' button.
#. Bug fixes for specific cases with :func:`cdftnc`.
#. Documentation and input check improvements to :func:`polygamma`.



17.0.2
------

#. (Windows) Added GUI license management utility for floating network
   licenses, ``rlmservice.exe``.
#. Bug fix: Fixed possible folder duplication in Source Browser.
#. Bug fix for program files not saving on run, in specific cases.
#. Bug fix for possible underflow in :func:`cdftnc`.
#. Added ability to remove ``tgauss`` dependency on Qt libraries.
#. Other minor documentation enhancements and bug fixes.



17.0.1
------

#. Up to 2-5x speed increase for least squares estimation, using the
   slash operator '/' for non-square coefficient matrices with few
   columns (approximately 1-15) and few rows (approximately 2-100).
#. Bug fix: File import dialog now supports empty sheet names for Excel
   files.
#. Added support for pasting data to the matrix editor from applications
   that use the legacy carriage return only line ending on Mac.



17.0.0
------

#. Increased scalability of :func:`threadFor` and :func:`threadBegin`.
#. GAUSS commands that process datasets can now also process .fmt, and
   .h5 files as well as .dat.
#. New support for HDF5 datasets, allows unlimited sized datasets.
#. Added support for an initial subset of Wilkinson-Rogers formula
   notation for functions such as :func:`dstat`, :func:`dstatmt`, :func:`glm`, :func:`momentd`, :func:`ols`,
   :func:`olsmt` and more.
#. CSV and Excel (.xls, .xlsx) files can be used as datasets for
   functions :func:`quantiled`, :func:`dstatmt`, :func:`glm`, :func:`momentd`, :func:`ols`, :func:`olsmt` and more.
#. New function :func:`cdfEmpirical` for computing the empirical cumulative
   distribution function, and :func:`plotcdfEmpirical` to graph it.
#. New function :func:`plotAddErrorBar` adds error bars to 2-D plots.
#. New function :func:`plotAddSurface` adds additional surfaces to an existing
   surface plot.
#. New function :func:`plotSetLegendFont` to control the font family, size and
   color used in the legend.
#. New function :func:`plotSetZLevels`: user control for the height of levels,
   rather than just the number of contour levels.
#. New function :func:`plotSetContourLabels`: controls whether numeric label
   containing contour level height is drawn, as well as the format of
   the numeric label.
#. New color maps for surface and contour plots.
#. Added option to specify the units and dpi of graphs saved with
   :func:`plotSave`.
#. Added control for the range of the X and Y axes to the graphics
   editor.
#. Added option to control units of graph size and DPI to :func:`plotSave`.
#. Added control for viewing angle, lighting, zoom and toggling
   appearance of the wireframe for surface plots to the graphics editor.
#. New function :func:`sylvester` to compute the solution, X, to the equation AX
   + XB = C.
#. :func:`schur` can now, optionally, return the real or complex Schur form.
#. New function :func:`dot` to compute the dot product of a column or the
   columns of a matrix.
#. New function :func:`powerM` to raise a matrix to a specified power.
#. :func:`getdims` will now return the number of dimensions of a matrix, string
   or string array.
#. :func:`getorders` will now return the number of rows and columns for
   matrices, strings or string arrays.
#. Greatly improved speed and decreased memory usage for :func:`reclassify`.
#. Greatly improved performance of :func:`unique` and :func:`uniquesa` for string
   arrays.
#. Greatly improved performance of :func:`sortc` for column vectors.
#. Greatly improved performance of linear solve using the slash operator
   ``(/)`` for small matrices and X'X matrix multiplication for large
   matrices.
#. Greatly improved performance of :func:`kronecker` product operator (``.*.``)
   when one of the matrices is a column vector.
#. Improved performance of :func:`cdffc` when the ``d1`` parameter is equal to
   one, by 10-1000x.
#. Improved performance of :func:`crossprd` for the case with fewer than 500
   vectors.
#. Added support for complex inputs to :func:`hess` and significant speed up for
   real matrix inputs larger than approximately 30x30.
#. ``tgauss`` can now create new 'plot' graphics.
#. New function :func:`rndWishartInv` for taking draws from the Inverse Wishart
   distribution.
#. New function :func:`pdfWishartInv` computes the probability density function
   of the Inverse Wishart distribution.
#. New function :func:`ldl` computes the LDL decomposition of a positive
   semi-definite matrix and returns separate L and D factors.
#. Added support for generalized linear model function, :func:`glm` for
   inverse-Gaussian distribution and model without an intercept.
#. New function :func:`strtrim` to remove white space from left and right side
   of elements of a string array.
#. Added support for multi-character delimiters to :func:`strsplit`.
#. New function :func:`strjoin` to combine string array elements into a string
   separated by a specified delimiter. This function does NOT add a
   delimiter after the final element as in :func:`strcombine`.
#. Editor now grays out code that is inactive due to a ``#define``.
#. Application Install Wizard can install multiple GAUSS application
   modules at once.
#. Performance improvement: The "forward only" flag
   (:func:`dbQuerySetForwardOnly`) now defaults to true.
#. Bug fix for find-and-replace with UTF-8 multibyte characters.
#. Bug fix: added support for strings to :func:`selif` and :func:`delif` and fixed
   memory bug in :func:`delif`.
#. Bug fix: crash when all points sent to :func:`plotLogX`, :func:`plotLogY` or
   :func:`plotLogLog` were between 10^n and 10^n+1.
#. Bug fix: :func:`errorlog` and :func:`errorlogat` now accept 1x1 string arrays as well
   as strings.
#. Bug fix: :func:`intsimp` would fail with an error when attempting to
   integrate a function that returned only zeros.
#. Bug fix: ability to scroll to right end in program input/output
   window with long lines.
#. New example files: ``dstatmth5.e``, ``glmnormalh5.e``,
   ``plotadddsurf1.e``, ``plotadderrorbar1.e``, ``plotadderrorbar2.e``,
   ``plotarea_ci_latex.e``, ``plotcontour2.e`` and ``plotxy_latex1.e``.



16.0.5
------

#. Bug fixes.



16.0.4
------

#. Data Import Wizard now supports GAUSS Data sets (\*.dat, \*.fmt,
   \*.fst).
#. Debugger now supports loading previous stack frames and viewing
   frame-specific symbols.
#. Improved breakpoint/bookmark behavior.
#. Improved file opening behavior from finder on OSX.
#. Bug fix: Fix various memory leaks.
#. Bug fix: Support :func:`plotAddArea` and :func:`plotAddBar` to existing time-series
   plots.
#. Bug fix: Fix following symlinks for file paths.
#. Bug fix: Fix 'Find Usages' for struct members.
#. Bug fix: Support debug tooltips for struct members.
#. Bug fix: Fix 3D preview, title rendering and exporting for OSX Retina
   devices.
#. Bug fix: Fix previous document shortcut not activating for
   Windows/Linux.
#. Bug fix: Remove 'Delete' option from context menu for undeleteable
   items in graphics page.
#. Bug fix: Improve autocomplete for structs and struct reference
   arguments in procs.



16.0.3
------

#. New function :func:`csvWriteM` writes data to a delimited text file from a
   GAUSS matrix.
#. Added ability to toggle bolding of functions in Edit Page.
#. Bug fix: :func:`plotPolar` now supports line symbols.
#. Bug fix: :func:`plotAddAnnotation` did not maintain correct z-order for added
   annotations.
#. Bug fix: Fix 3D graph export dialog starting size constraints.
#. Bug fix: Fix 'Properties' context menu item on graphics page not
   coming to top.
#. Bug fix: Fix semi-colons in strings, causing Format Text (code
   formatting) option to add line break inside string.
#. Bug fix: Fix starting indent keywords in Edit Page being
   case-sensitive.
#. Bug fix: Properly display long error messages that wrap.
#. Added internal check for, and removal of, completely zero imaginary
   portion of a complex matrix on input to function :func:`lu`.
#. Bug fix: Add complex support for function :func:`lu` on Mac (already
   supported on Windows and Linux).
#. Bug fix: Fix memory leak in function :func:`threadfor` in some specific
   situations.



16.0.2
------

#. Added ability for :func:`csvReadM` and :func:`csvReadSA` to read data from the standard
   input stream (stdin). Pass \__STDIN as the filename argument to
   :func:`csvReadM` and :func:`csvReadSA`.
#. Added ability for :func:`fgets`, :func:`fgetsa`, :func:`fgetsat`, and :func:`fgetst` to read from the
   standard input stream (stdin) . Pass \__STDIN as the file handle to
   :func:`fgets`, :func:`fgetsa`, :func:`fgetsat`, and :func:`fgetst`.
#. Added ability for :func:`fputs` and :func:`fputst` to send data to the standard error
   stream (``stderr``) and the standard output stream (``stdout``). Pass
   ``\__STDERR`` or ``\__STDOUT`` as the file handle to :func:`fputs` and :func:`fputst`.
#. Changed R-squared calculation in :func:`ols` for regression through the
   origin to prevent possibility of negative R-squared.
#. Bug fix: GAUSS source path was not searched when a file name was
   passed to GAUSS on the command line at start up.
#. Bug fix: :func:`csvReadM` and :func:`csvReadSA` skipped final line in CSV file if the
   initial line was blank and :func:`csvRead` was told to skip lines.
#. Bug fix: cons would continue to return the final buffer data after
   hitting EOF.



16.0.1
------

#. Added **Data Import Wizard**.
#. New functions :func:`csvReadM` and :func:`csvReadSA` read data from a delimited text
   file into a GAUSS matrix or string array.
#. New function :func:`glm` calculates the generalized linear model.
#. New function :func:`rescale` provides for scaling columns of a matrix.
#. New function :func:`sampleData` takes samples with or without replacement
   from a GAUSS matrix.
#. New function :func:`qz` computes the sorted complex QZ decomposition.
#. New function :func:`plotSetAxesPen` sets the color and line thickness of the
   axes line.
#. New functions added for data recoding/reclassification: :func:`reclassify`
   and :func:`reclassifyCuts`.
#. Added the following new statistical distribution functions:
   :func:`pdfBinomial`, :func:`pdfPoisson`, :func:`cdfHyperGeo`, :func:`pdfHyperGeo` and :func:`rndHyperGeo`.
#. New function :func:`integrate1d` uses adaptive quadrature to integrate a
   user-defined function over a specified range.
#. Added new compiler command ``#ifmac`` to designate code blocks to be
   compiled and run only on a Mac.
#. Added additional, optional argument to :func:`rndi` to specify the range of
   random integers produced.
#. Added option to pass additional data to integration functions
   :func:`intquad1`, :func:`intquad2` and :func:`intquad3`.
#. Added additional, optional input to :func:`lapgschur` to specify sorting of
   the eigenvalues.
#. Add additional, optional argument to :func:`strsplit` to specify delimiter.
#. Significant speed up to :func:`svd`, :func:`svd1`, :func:`svd2`, :func:`svds`, :func:`svdcusv` and :func:`svdusv`.
#. Significant speed up to :func:`indnv`.
#. Added ability to pass a variable number of arguments to GAUSS
   procedures.
#. Removed requirement to use a DS structure, added option to directly
   pass a variable number of matrices and made control structure
   optional for :func:`eqsolvemt`, :func:`qnewtonmt`, and :func:`sqpsolvemt`.
#. Removed requirement to use DS structure and added option to directly
   pass matrices to all gradient and hessian functions (:func:`gradMT`, :func:`gradMTm`,
   :func:`gradMTT`, :func:`hessMT`, :func:`hessMTm`, :func:`hessMTg`, :func:`hessMTgw`, :func:`hessMTT`, etc).
#. Removed requirement to pass control structure to :func:`dstatmt`.
#. Made inputs other than file name optional for :func:`xlsReadM`, :func:`xlsReadSA`,
   :func:`xlsWrite`, :func:`xlsWriteM`, :func:`xlsWriteSA`, :func:`xlsGetSheetSize`, :func:`spreadSheetReadM`,
   :func:`spreadSheetReadSA`, and :func:`spreadSheetWrite`.
#. ``F4`` hot-key will now run the current statement and then skip to the
   next in addition to running highlighted text.
#. Improved integration of source editor and debugger. Project view
   window, 'find usages', editing source and other source editor
   features are available on debug page.
#. Added multiple new preference options to **Tools > Preferences >
   Debug Page** to control opening and closing of temporary files and
   other debug page behavior.
#. New preference option added to activate autocomplete only manually on
   **Edit Page** (with ``Ctrl+Space``).
#. Added autocomplete and tooltips to program input/output window.
#. Added preference to **Tools > Preferences > Command** to activate
   autocomplete only manually (with ``Ctrl+Space``).
#. Added bolding and separate color control syntax highlighting for all
   GAUSS and user defined procedures (**Tools > Preferences > Edit Page
   > Functions**).
#. Added support for ``Ctrl+E`` to open a symbol selected in the program
   input/output window into a floating symbol editor.
#. Added support for ``F4`` to run highlighted text in program input/output
   window.
#. Added sysstate` cases to assess variable arguments passed in to a
   GAUSS procedure as '...'.
#. Symbol editors remember format preferences until closed instead of
   using default preferences whenever refreshed.
#. Speed up for load time of GAUSS when very large folders are open in
   project view window.
#. Improved behavior of file associations on Mac.
#. Autocomplete no longer pops up when deleting characters or in the
   middle of a word.
#. Bug fix for display of gaps between bars of a histogram when using
   :func:`plotAddHistP` in some cases.
#. Bug fix for situation in which a message box could be hidden and
   unreachable behind a floating symbol editor.
#. Bug fix: autocomplete pop-up window no longer stays visible when page
   loses focus.
#. Bug fix: 'find usages' did not find instances of variables that were
   index assigns (i.e. ``x[5] = 7;``).
#. Bug fix: Dock widgets incorrectly reset to minimum width in some
   instances of page change and restart GAUSS.
#. New example programs: ``glmbinomial1.e``, ``glmbinomial2.e``, ``glmbinomial3.e``,
   ``glmgamma1.e``, ``glmgamma2.e``, ``glmgamma3.e``, ``glmnormal1.e``, ``glmnormal2.e``,
   ``glmpoisson1.e``, ``glmpoisson2.e``, ``qnewtonmt2.e``, ``qnewtonmt3.e``,
   ``qnewtonmt4.e``, ``sqpsolvemt1.e``, ``sqpsolvemt_nlls.e``, ``sqpsolvemt_frontier``.
