
Data types
==================


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

==================         ==================================================================
:doc:`../diag`             Extracts the diagonal of a matrix.
:doc:`../diagrv`           Puts a column vector into the diagonal of a matrix.
:doc:`../lowmat`           Returns the main diagonal and lower triangle.
:doc:`../lowmat1`          Returns a main diagonal of 1's and the lower triangle.
:doc:`../upmat`            Returns the main diagonal and lower triangle.
:doc:`../upmat1`           Returns a main diagonal of 1's and the lower triangle.
==================         ==================================================================

Complex numbers
+++++++++++++++++++++

==================         ==================================================================
:doc:`../complex'              Creates a complex matrix from two real matrices.
:doc:`../hasimag'              Tests whether the imaginary part of a complex matrix is negligible.
:doc:`../imag'                 Returns the imaginary part of a complex matrix.
:doc:`../iscplx'               Tests whether a matrix is complex.
:doc:`../real'                 Returns the real part of a complex matrix.
==================         ==================================================================


N-Dimensional arrays
-------------------------

Array creation
+++++++++++++++++++++

==================         ==================================================================
:doc:`../aconcat`          Concatenates conformable matrices and arrays in a user-specified dimension.
:doc:`../aeye`             Creates an N-dimensional array in which the planes described by the two trailing dimensions of the array are equal to the identity.
:doc:`../areshape`         Reshapes a scalar, matrix, or array into an array of user-specified size.
:doc:`../arrayalloc`       Creates an N-dimensional array with unspecified contents.
:doc:`../arrayinit`        Creates an N-dimensional array with a specified fill value.
:doc:`../mattoarray`       Converts a matrix to a type array.
:doc:`../squeeze`          Remove any singleton dimensions from a multi-dimensional array.
==================         ==================================================================

Size and range
+++++++++++++++++

==================         ==================================================================
:doc:`../amax`             Moves across one dimension of an N-dimensional array and finds the largest element.
:doc:`../amin`             Moves across one dimension of an N-dimensional array and finds the smallest element.
:doc:`../getdims`          Gets the number of dimensions in an array.
:doc:`../getorders`        Gets the vector of orders corresponding to an array.
==================         ==================================================================


Selection and indexing
+++++++++++++++++++++++++

========================       ==================================================================
:doc:`../arrayindex`           Converts a scalar vector index to a vector of indices for an N-dimensional array.
:doc:`../getarray`             Gets a contiguous subarray from an N-dimensional array.
:doc:`../getmatrix`            Gets a contiguous matrix from an N-dimensional array.
:doc:`../getmatrix4D`          Gets a contiguous matrix from a 4-dimensional array.
:doc:`../getscalar3D`          Gets a scalar from a 3-dimensional array.
:doc:`../getscalar4D`          Gets a scalar from a 4-dimensional array.
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
