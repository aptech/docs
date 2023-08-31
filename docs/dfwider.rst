
dfWider
==============================================

Purpose
----------------
Converts a GAUSS dataframe in long panel format to wide panel format.


Format
----------------
.. function:: df_wide = dfWider(df_long, names_from, values_from [, ctl])

    :param df_long: A GAUSS dataframe in long panel format.
    :type df_long: Dataframe

    :param names_from: The name(s) of the columns from which the new column names will be created.
    :type names_from: String array

    :param values_from: The values with which to fill the newly created columns.
    :type values_from: String array

    :param pctl        An optional pivotControl structure with the following members:

        .. list-table::
            :widths: auto

            * - pctl.names_prefix
              - String, the characters, if any, that should be added to the front of the newly created variable names.  Default = "", no prefix.
            * - pctl.names_sep_combine
              - String, the characters, if any, that should be added between the tokens when creating the new variable names. Default = "_".
            * - pctl.values_drop_missing
              - Scalar, 0 or 1. If set to 1, all rows with missing values will be removed. Default = 0.
            * - pctl.id_cols
              - String array, containing the names of the variables that should be used to determine a unique observation. Default = "", meaning the combination of all variables other than those specified by ``names_from`` and ``values_from`` will be used.

    :type pctl: struct

    :return df_wide: The input data converted to wide form.

    :rtype df_wide: Dataframe

Examples
----------------

::

    x = ones(3, 2);

The code above assigns *x* to be equal to:

::

    1.0000000        1.0000000
    1.0000000        1.0000000
    1.0000000        1.0000000

Remarks
-------

Non-integer arguments will be truncated to an integer.


.. seealso:: Functions :func:`dflonger`
