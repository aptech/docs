
Data cleaning
===========================

Remove specific variables or observations
--------------------------------------------

=====================       ===========================================
:doc:`../delcols`              Removes variables from a dataframe specified by index or name.
:doc:`../delif`                Removes rows of data based on a logical expression.
:doc:`../delrows`              Removes observations (rows) from a dataframe by index.
:doc:`../selif`                Keeps rows of data based on a logical expression.
=====================       ===========================================

Duplicate observations
------------------------

==========================      ===========================================
:doc:`../dropduplicates`        Drops duplicate observations from data.
:doc:`../getduplicates`         Identifies duplicate observations and prints report.
:doc:`../isunique`              Checks if all observations in the matrix or dataframe are unique.
==========================      ===========================================

Missing values
-----------------

=======================    ===============================================================
:doc:`../impute`           Replaces missing values in the columns of a matrix by a specified imputation method.
:doc:`../isinfnanmiss`     Returns true if the argument contains an infinity, NaN, or missing value.
:doc:`../ismiss`           Returns 1 if matrix has any missing values, 0 otherwise.
:doc:`../missmissrv`       Converts (or replaces) specified elements in a matrix to GAUSS’s missing value code.
:doc:`../missex`           Converts numeric values to the missing value code according to the values given in a logical expression.
:doc:`../msym`             Controls the symbol printed to represent missing values.
:doc:`../packr`            Deletes the rows of a matrix that contain any missing values.
:doc:`../scalmiss`         Returns 1 if the input is a scalar missing value.
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


Scaling and normalization
----------------------------

==================         ==================================================================
:doc:`../rescale`          Scales the columns of a matrix using a specified centering and scaling method.
==================         ==================================================================

