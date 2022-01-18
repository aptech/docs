
Data cleaning
===========================

Remove specific variables or observations
--------------------------------------------

=====================       ===========================================
:doc:`../delcols`              Removes variables from a dataframe specified by index or name.
:doc:`../delif`                Removes rows of data based on a logical expression.
:doc:`../delrows`              Removes observations (rows) from a dataframe by index.
:doc:`../selif`                Keeps rows of data based on a logical expression.
:doc:`../trimr'                Trims rows from the top or bottom.
=====================       ===========================================

Duplicate observations
------------------------

==========================      ===========================================
:doc:`../dropduplicates`        Drops duplicate observations from data.
:doc:`../getduplicates`         Identifies duplicate observations and prints report.
:doc:`../isunique`              Checks if all observations in the matrix or dataframe are unique.
:doc:`../isrowunique`           Returns a binary vector with a one for every row that is unique, otherwise a zero.
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

Searching
--------------

=======================    ===============================================================
:doc:`../contains'                Indicates whether one matrix, multidimensional array or string array contains any elements from another symbol.
:doc:`../counts'                  Returns number of elements of a vector falling in specified ranges.
:doc:`../countwts'                Returns weighted count of elements of a vector falling in specified ranges.
:doc:`../indexcat'                Returns indices of elements falling within a specified range.
:doc:`../indnv'                   Checks one numeric vector against another and returns the indices of the elements of the first vector in the second vector.
:doc:`../ismember'                Checks whether each element of a matrix or string array matches any element from a separate symbol.
:doc:`../maxindc'                 Returns row number of largest element in each column of a matrix.
:doc:`../minindc'                 Returns row number of smallest element in each column of a matrix.
:doc:`../rowcontains'             Checks whether any element in the row of a matrix or string array matches any element from a separate symbol.
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

General matrix manipulation
----------------------------------

=====================      ==================================================================
:doc:`../rev'                     Reverses the order of rows of a matrix.
:doc:`../reshape'                 Reshapes a matrix to new dimensions.
:doc:`../rotater'                 Rotates the rows of a matrix, wrapping elements as necessary.
:doc:`../shiftr'                  Shifts rows of a matrix, filling in holes with a specified value.
:doc:`../submat'                  Extracts a submatrix from a matrix.
:doc:`../subvec'                  Extracts an Nx1 vector of elements from an NxK matrix.
:doc:`../vec'                     Stacks columns of a matrix to form a single column.
:doc:`../vech'                    Reshapes the lower triangular portion of a symmetric matrix into a column vector.
:doc:`../vecr'                    Stacks rows of a matrix to form a single column.
:doc:`../xpnd'                    Expands a column vector into a symmetric matrix.
=====================      ==================================================================


Scaling and normalization
----------------------------

==================         ==================================================================
:doc:`../rescale`          Scales the columns of a matrix using a specified centering and scaling method.
==================         ==================================================================

Complex numbers
--------------------
==================         ==================================================================
:doc:`../complex'              Creates a complex matrix from two real matrices.
:doc:`../hasimag'              Tests whether the imaginary part of a complex matrix is negligible.
:doc:`../imag'                 Returns the imaginary part of a complex matrix.
:doc:`../iscplx'               Tests whether a matrix is complex.
:doc:`../real'                 Returns the real part of a complex matrix.
==================         ==================================================================
