
psi
==============================================

Purpose
----------------

Computes the Psi (or Digamma) function.

Format
----------------
.. function:: f = psi(z)

    :param z: data. *z* may be complex
    :type z: NxK matrix

    :returns: f (*NxK matrix*)

Remarks
-------

This program uses the analytical derivative of the log of the Lanczos
series approximation for the Gamma function.

References
----------
#. C. Lanczos, SIAM JNA 1, 1964. pp. 86-96.

#. Y. Luke, ''The Special ... approximations,'' 1969 pp. 29-31.

#. Y. Luke, ''Algorithms ... functions,'' 1977.

#. J. Spouge, SIAM JNA 31, 1994. pp. 931.

#. W. Press, ''Numerical Recipes.''

#. S. Chang, ''Computation of special functions,'' 1996.

#. Original code by Paul Godfrey

