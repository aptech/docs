
Data cleaning
===========================

Size
---------------------------

=====================       ===========================================
:doc:`../cols`              Returns number of columns in a matrix, string array or dataframe.
:doc:`../getdims`           Returns the number of dimensions in a matrix, string array or n-dimensional array.
:doc:`../getorders`         Returns the dimensions corresponding to matrix, string array or n-dimensional array.
:doc:`../rows`              Returns number of rows in a matrix, string array or dataframe.
=====================       ===========================================


Selection
--------------------------------------------

=====================       ===========================================
:doc:`../delcols`           Removes variables from a dataframe specified by index or name.
:doc:`../delif`             Removes rows of data based on a logical expression.
:doc:`../delrows`           Removes observations (rows) from a dataframe by index.
:doc:`../diag`              Extracts the diagonal of a matrix.
:doc:`../getmatrix`         Gets a contiguous matrix from an N-dimensional array.
:doc:`../head`              Returns the first ``n`` rows of a matrix, dataframe or string array.
:doc:`../selif`             Keeps rows of data based on a logical expression.
:doc:`../submat`            Extracts a submatrix from a matrix.
:doc:`../subvec`            Extracts an Nx1 vector of elements from an NxK matrix.
:doc:`../tail`              Returns the last ``n`` rows of a matrix, dataframe or string array.
:doc:`../trimr`             Trims rows from the top or bottom.
=====================       ===========================================

Merging
-------------------
=====================       ===========================================
:doc:`../innerjoin`         Performs a left, or full, outer join on two matrices based upon user-specified key columns.
:doc:`../insertcols`        Inserts one or more new columns into a matrix or dataframe at a specified location.
:doc:`../outerjoin`         Joins two matrices, or dataframes based upon user-specified key columns, with non-matching rows removed.
:doc:`../where`             Returns elements from ``a`` or ``b``, depending on ``condition``.
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


Sorting and set functions
-------------------------------

==========================    ===============================================================
:doc:`../intrsect`            Returns the intersection of two vectors.
:doc:`../setdif`              Returns the unique elements in one vector that are not present in a second vector.
:doc:`../sortc`               Sorts a numeric matrix, character matrix or string array.
:doc:`../sortindsortindc`     Returns the sorted index of x.
:doc:`../sortmc`              Sorts a matrix on multiple columns.
:doc:`../sortrsortrc`         Sorts the columns of a matrix of numeric or character data, with respect to a specified row.
:doc:`../union`               Returns the union of two vectors.
:doc:`../unique`              Sorts and removes duplicate elements from a vector.
:doc:`../uniqindx`            Computes the sorted index of x, leaving out duplicate elements.
==========================    ===============================================================


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

Transform
----------------------------------

=========================      ==================================================================
:doc:`../code`                 Allows a new variable to be created (coded) with different values depending upon which one of a set of logical expressions is true.
:doc:`../dflonger`             Converts a GAUSS dataframe in wide panel format to long panel format.
:doc:`../dfwider`              Converts a GAUSS dataframe in long panel format to wide panel format.
:doc:`../diagrv`               Inserts a vector into the diagonal of a matrix.
:doc:`../dummy`                Creates a set of dummy (0/1) variables by breaking up a variable into specified categories. The highest (rightmost) category is unbounded on the right.
:doc:`../dummybr`              Creates a set of dummy (0/1) variables. The highest (rightmost) category is bounded on the right.
:doc:`../dummydn`              Creates a set of dummy (0/1) variables by breaking up a variable into specified categories. The highest (rightmost) category is unbounded on the right, and a specified column of dummies is dropped.
:doc:`../lagn`                 Lags (or leads) a matrix a specified number of time periods for time series analysis.
:doc:`../lagtrim`              Lags (or leads) a vector a specified number of time periods and removes the incomplete rows.
:doc:`../maxv`                 Performs an element by element comparison of two matrices and returns the maximum value for each element.
:doc:`../minv`                 Performs an element by element comparison of two matrices and returns the minimum value for each element.
:doc:`../order`                Reorder a matrix based on user-specified ordering. Relocates columns to the beginning of the dataset in the order in which the variables are specified.
:doc:`../reclassify`           Replaces specified values of a matrix, array or string array
:doc:`../reclassifycuts`       Replaces values of a matrix or array within specified ranges
:doc:`../rev`                  Reverses the order of rows of a matrix.
:doc:`../reshape`              Reshapes a dataframe, matrix or string array to new dimensions.
:doc:`../rotater`              Rotates the rows of a matrix, wrapping elements as necessary.
:doc:`../shiftc`               Shifts, lags or leads, columns of a matrix, filling in holes with a specified value.
:doc:`../shiftr`               Shifts rows of a matrix, filling in holes with a specified value.
:doc:`../subscat`              Changes the values in a vector depending on the category a particular element falls in.
:doc:`../substute`             Substitutes new values for old values in a matrix, depending on the outcome of a logical expression.
:doc:`../vecvecr`              Stacks columns or rows of a matrix to form a single column.
:doc:`../vech`                 Reshapes the lower triangular portion of a symmetric matrix into a column vector.
:doc:`../xpnd`                 Expands a column vector into a symmetric matrix.
=========================      ==================================================================


Scaling and normalization
----------------------------

==================         ==================================================================
:doc:`../rescale`          Scales the columns of a matrix using a specified centering and scaling method.
==================         ==================================================================
