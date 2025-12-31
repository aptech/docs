
Data types
==================

Dataframes
--------------

General
++++++++++++++++

=========================     ==========================================================================
:doc:`../asdf`                Converts a matrix or string array to a dataframe, and optionally sets the column names.
:doc:`../asmatrix`            Converts a dataframe to a matrix.
:doc:`../dfappend`            Vertically conacatenates (or stacks) two dataframes.
:doc:`../dfname`              Sets the variable names of the columns of a dataframe.
:doc:`../dftype`              Sets the types (numeric, categorical, date or string) of a dataframe.
:doc:`../getcolnames`         Returns the names of the columns (or variables) in a GAUSS dataframe.
:doc:`../getcoltypes`         Returns the types for the columns (or variables) in a GAUSS dataframe.
:doc:`../hasmetadata`         Checks to see if a symbol is a dataframe.
:doc:`../setcolmetadata`      Sets the variable names and types for the columns of a dataframe.
:doc:`../setcolnames`         Sets the variable names the columns of a dataframe.
=========================     ==========================================================================


Date variables
++++++++++++++++++++++

============================     ==========================================================================
:doc:`../asdate`                 Converts vectors in Posix time or string dates to a GAUSS date variable and optionally sets the date display format.
:doc:`../dtdayname`              Extracts the day from a date/time variable as a string name.
:doc:`../dtdayofmonth`           Extracts the day of the month from a date/time variable as a decimal number (1-31).
:doc:`../dtdayofweek`            Extracts the day of the week from a date/time variable as a decimal number. 
:doc:`../dtdayofyear`            Extracts the day of the year from a date/time variable as a decimal number (1-366). 
:doc:`../dthour`                  Extracts the hour from a date/time variable as a number (1-12 or 1-24).
:doc:`../dtminute`                Extracts the minute from a date/time variable as a number (0-59).
:doc:`../dtmonth`                 Extracts the month from a date/time variable as a decimal number(1-12).
:doc:`../dtmonthname`             Extracts the month from a date/time variable as a string name.
:doc:`../dtquarter`               Extracts the quarter from a date/time variable (1-4).
:doc:`../dtsecond`                Extracts the seconds from a date/time variable as a number (0-59).
:doc:`../dtweek`                  Extracts the week from a date/time variable as a number (0-53).
:doc:`../dtyear`                  Extracts the year from a date/time variable as a number.
:doc:`../getcoldateformats`      Gets BSD strftime format specifiers for specified columns of a dataframe.
:doc:`../setcoldateformats`      Specifies how GAUSS should display dates using the BSD strftime format specifiers. Note that this will also convert the type of the columns specified by column to Date.
============================     ==========================================================================

String and categorical variables
+++++++++++++++++++++++++++++++++++++

===============================     ==========================================================================
:doc:`../dropcategories`            Removes categories from the variable and the meta data. Resets the keyvalues and labels for the variable.
:doc:`../dropunusedcategories`      Removes categories from the meta data of a dataframe that are not present in the current variable.
:doc:`../endswith`                  Returns a 1 if a string ends with a specified pattern.
:doc:`../getcategories`             Returns the unique set of column labels as a dataframe.
:doc:`../getcollabels`              Returns the unique set of column labels and corresponding key values for a categorical variable.
:doc:`../recodecatlabels`           Change categorical variable labels.
:doc:`../reordercatlabels`          Change the order of categorical variable labels.
:doc:`../setbasecat`                Sets a category in a categorical variable to be the base case.
:doc:`../setbasecat`                Sets a category in a categorical variable to be the base case.
:doc:`../startswith`                Returns a 1 if a string starts with a specified pattern.
===============================     ==========================================================================



Matrices
----------------

Matrix creation
++++++++++++++++++++++

==================         ==================================================================
:doc:`../eye`              Creates identity matrix.
:doc:`../matalloc`         Allocates a matrix with unspecified contents.
:doc:`../matinit`          Allocates a matrix with specified fill value.
:doc:`../ones`             Creates a matrix of ones.
:doc:`../zeros`            Creates a matrix of zeros.
==================         ==================================================================

Size and range
++++++++++++++++++++++

==================         ==================================================================
:doc:`../cols`             Returns number of columns in a matrix.
:doc:`../colsf`            Returns number of columns in an open data set.
:doc:`../maxc`             Returns largest element in each column of a matrix.
:doc:`../minc`             Returns smallest element in each column of a matrix.
:doc:`../rows`             Returns number of rows in a matrix.
:doc:`../rowsf`            Returns number of rows in an open data set.
==================         ==================================================================

Other
++++++++++++++++++++++

=======================         ==================================================================
:doc:`../diag`                  Extracts the diagonal of a matrix.
:doc:`../diagrv`                Puts a column vector into the diagonal of a matrix.
:doc:`../lowmatlowmat1`         Returns the lower triangle of a matrix with the main diagonal or a diagonal of ones.
:doc:`../upmatupmat1`           Returns the upper triangle of a matrix with the main diagonal or a diagonal of ones.
=======================         ==================================================================

Complex numbers
+++++++++++++++++++++

==================         ==================================================================
:doc:`../complex`              Creates a complex matrix from two real matrices.
:doc:`../hasimag`              Tests whether the imaginary part of a complex matrix is negligible.
:doc:`../imag`                 Returns the imaginary part of a complex matrix.
:doc:`../iscplx`               Tests whether a matrix is complex.
:doc:`../real`                 Returns the real part of a complex matrix.
==================         ==================================================================


N-Dimensional arrays
-------------------------

Array creation
+++++++++++++++++++++

=====================      ==================================================================
:doc:`../aconcat`          Concatenates conformable matrices and arrays in a user-specified dimension.
:doc:`../aeye`             Creates an N-dimensional array in which the planes described by the two trailing dimensions of the array are equal to the identity.
:doc:`../areshape`         Reshapes a scalar, matrix, or array into an array of user-specified size.
:doc:`../arrayalloc`       Creates an N-dimensional array with unspecified contents.
:doc:`../arrayinit`        Creates an N-dimensional array with a specified fill value.
:doc:`../mattoarray`       Converts a matrix to a type array.
:doc:`../squeeze`          Remove any singleton dimensions from a multi-dimensional array.
=====================      ==================================================================

Size and range
+++++++++++++++++

====================       ==================================================================
:doc:`../amax`             Moves across one dimension of an N-dimensional array and finds the largest element.
:doc:`../amin`             Moves across one dimension of an N-dimensional array and finds the smallest element.
:doc:`../getdims`          Gets the number of dimensions in an array.
:doc:`../getorders`        Gets the vector of orders corresponding to an array.
====================       ==================================================================


Selection and indexing
+++++++++++++++++++++++++

========================       ==================================================================
:doc:`../arrayindex`           Converts a scalar vector index to a vector of indices for an N-dimensional array.
:doc:`../getarray`             Gets a contiguous subarray from an N-dimensional array.
:doc:`../getmatrix`            Gets a contiguous matrix from an N-dimensional array.
:doc:`../getmatrix4d`          Gets a contiguous matrix from a 4-dimensional array.
:doc:`../getscalar3d`          Gets a scalar from a 3-dimensional array.
:doc:`../getscalar4d`          Gets a scalar from a 4-dimensional array.
:doc:`../loopnextindex`        Increments an index vector to the next logical index and jumps to the specified label if the index did not wrap to the beginning.
:doc:`../nextindex`            Returns the index of the next element or subarray in an array.
:doc:`../previousindex`        Returns the index of the previous element or subarray in an array.
:doc:`../singleindex`          Converts a vector of indices for an N-dimensional array to a scalar vector index.
:doc:`../walkindex`            Walks the index of an array forward or backward through a specified dimension.
========================       ==================================================================

Transform
+++++++++++++

======================         ==================================================================
:doc:`../aconcat`              Concatenates conformable matrices and arrays in a user-specified dimension.
:doc:`../areshape`             Reshapes a scalar, matrix, or array into an array of user-specified size.
:doc:`../atranspose`           Transposes an N-dimensional array.
:doc:`../arraytomat`           Changes an array to type matrix.
:doc:`../putarray`             Puts a contiguous subarray into an N-dimensional array and returns the resulting array.
======================         ==================================================================


Other
+++++++

======================         ==================================================================
:doc:`../amean`                Computes the mean across one dimension of an N-dimensional array.
:doc:`../asum`                 Computes the sum across one dimension of an N-dimensional array.
:doc:`../astd`                 Computes the standard deviation of the elements across one dimension of an N-dimensional array.
======================         ==================================================================
