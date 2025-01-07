
Panel Data
===========================

Size
---------------------------

==========================       ===========================================
:doc:`../pdallbalanced`          Returns an indicator of whether all groups in a panel dataset covers the maximum time span.
:doc:`../pdallconsecutive`       Returns an indicator of whether all groups in a panel dataset covers consecutive time periods.
:doc:`../pdisbalanced`           Returns an indicator of whether each group in a panel dataset covers the maximum time span.
:doc:`../pdisconsecutive`        Returns an indicator of whether each group in a panel dataset covers consecutive time periods.
:doc:`../pdsize`                 Returns the number of groups, number of time observations for each group, an indicator of strong balance.
:doc:`../pdtimespans`            Returns the start date and end date of each requested variable.
==========================       ===========================================


Tranformation
--------------------------------------------

========================        ===========================================
:doc:`../aggregate`             Aggregates the data in the columns of a matrix or dataframe based upon a column containing group ids with a choice of method.
:doc:`../dflonger`              Converts a GAUSS dataframe in long panel format to wide panel format.
:doc:`../dfwider`               Converts a GAUSS dataframe in wide panel format to long panel format.
:doc:`../pddiff`                Computes time series differences of panel data.
:doc:`../pdlag`                 Computes time series lags of panel data.
:doc:`../reclassify`            Replaces specified values of a matrix, array or string array.
:doc:`../reclassifycuts`        Replaces values of a matrix or array within specified ranges.
========================        ===========================================

Merging and Sorting
-------------------
=====================           ===========================================
:doc:`../dfappend`              Vertically concatenates (or stacks) two dataframes.
:doc:`../innerjoin`             Performs a left, or full, outer join on two matrices based upon user-specified key columns.
:doc:`../insertcols`            Inserts one or more new columns into a matrix or dataframe at a specified location.
:doc:`../outerjoin`             Joins two matrices, or dataframes based upon user-specified key columns, with non-matching rows removed.
:doc:`../pdsort`                Sorts panel data based on automatically detected group and date variable.
:doc:`../sortmc`                Sorts a matrix on multiple columns.
:doc:`../where`                 Returns elements from ``a`` or ``b``, depending on ``condition``.
=====================           ===========================================

Duplicate observations
------------------------

==========================      ===========================================
:doc:`../dropduplicates`        Drops duplicate observations from data.
:doc:`../getduplicates`         Identifies duplicate observations and prints report.
:doc:`../isunique`              Checks if all observations in the matrix or dataframe are unique.
:doc:`../isrowunique`           Returns a binary vector with a one for every row that is unique, otherwise a zero.
==========================      ===========================================

Summary Statistics
------------------------

==========================      ===========================================
:doc:`../aggregate`             Aggregates the data in the columns of a matrix or dataframe based upon a column containing group ids with a choice of method.
:doc:`../pdsummary`             Returns summary statistics for panel data, including overall, between-group, and within-group statistics.
==========================      ===========================================

Tabulation
-------------------------

==========================      ===========================================
:doc:`../frequency`             Generates frequency table.
:doc:`../plotfreq`              Creates frequency plot for specified categorical variable. 
:doc:`../tabulate`              Computes and returns two-way tables of frequencies.
==========================      ===========================================

Missing values
-----------------

=======================    ===============================================================
:doc:`../isinfnanmiss`     Returns true if the argument contains an infinity, NaN, or missing value.
:doc:`../ismiss`           Returns 1 if matrix has any missing values, 0 otherwise.
:doc:`../missmissrv`       Creates a scalar missing value, or converts (or replaces) specified elements in a matrix to GAUSS’s missing value code.
:doc:`../missex`           Converts numeric values to the missing value code according to the values given in a logical expression.
:doc:`../msym`             Controls the symbol printed to represent missing values.
:doc:`../packr`            Deletes the rows of a matrix that contain any missing values.
:doc:`../scalmiss`         Returns 1 if the input is a scalar missing value.
=======================    ===============================================================

Searching
--------------

=======================    ===============================================================
:doc:`../between`          Indicates whether elements in a matrix fall between a specified lower and upper bound. 
:doc:`../contains`         Indicates whether one matrix, multidimensional array or string array contains any elements from another symbol.
:doc:`../counts`           Returns number of elements of a vector falling in specified ranges.
:doc:`../countwts`         Returns weighted count of elements of a vector falling in specified ranges.
:doc:`../indexcat`         Returns indices of elements falling within a specified range.
:doc:`../indnv`            Checks one numeric vector against another and returns the indices of the elements of the first vector in the second vector.
:doc:`../isempty`          Checks whether a symbol is an empty matrix.
:doc:`../ismember`         Checks whether each element of a matrix or string array matches any element from a separate symbol.
:doc:`../maxindc`          Returns row number of largest element in each column of a matrix.
:doc:`../minindc`          Returns row number of smallest element in each column of a matrix.
:doc:`../rowcontains`      Checks whether any element in the row of a matrix or string array matches any element from a separate symbol.
=======================    ===============================================================


String and categorical variables
------------------------------------

===========================      ==================================================================
:doc:`../getcollabels`           Returns the unique set of column labels and corresponding key values for a categorical variable.
:doc:`../recodecatlabels`        Replaces the labels in a categorical variable of a dataframe.
:doc:`../reordercatlabels`       Changes the order of the labels in a categorical variable of a dataframe.
:doc:`../setbasecat`             Sets a specified category to be the base case for a categorical variable.
===========================      ==================================================================

These functions can be used to fix errors in categorical labels.

=====================      ==================================================================
:doc:`../strreplace`       Replaces a substring within a categorical label or string element.
:doc:`../strtof`           Converts a string or categorical variable of a dataframe to a numeric variable.
:doc:`../strtrim`          Strips all white space characters from the left and right side of each element in a categorical variable or  string array.
:doc:`../strtriml`         Strips all white space characters from the left side of each element in a categorical variable or  string array.
:doc:`../strtrimr`         Strips all white space characters from the right side of each element in a categorical variable or  string array.
=====================      ==================================================================

