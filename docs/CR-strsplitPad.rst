
strsplitPad
==============================================

Purpose
----------------
Splits a string vector into a string array of the individual tokens. Pads on the right with null strings.

Format
----------------
.. function:: strsplitPad(sv, n_cols)

    :param sv: Nx1 string array.
    :type sv: TODO

    :param n_cols: number of columns of output string array.
    :type n_cols: scalar

    :returns: sa (*TODO*), Nx n_cols string array.

Examples
----------------

::

    string sv = {
       "alpha beta gamma",
       "delta, epsilon, zeta, eta",
       "theta iota kappa"
    };
     
     sa = strsplitPad(sv, 4);

After the code above, sa will be equal to:

::

    "alpha"    "beta" "gamma"    ""
                    "delta" "epsilon"  "zeta" "eta"
                    "theta"    "iota" "kappa"    ""

.. seealso:: Functions :func:`strsplit`
