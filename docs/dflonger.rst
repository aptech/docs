
dfLonger
==============================================

Purpose
----------------
Converts a GAUSS dataframe in wide panel format to long panel format.


Format
----------------
.. function:: df_long = dfLonger(df_wide, columns, names_to, values_to [, ctl])

    :param df_wide: A GAUSS dataframe in wide panel format.
    :type df_wide: Dataframe

    :param columns:  The columns that should be used in the conversion.
    :type columns: String array

    :param names_to: The variable name(s) for the new columns to be created.
    :type names_to: String array

    :param values_to: The name of the new column containing the values.
    :type values_to: String

    :param pctl        An optional pivotControl structure with the following members:

        .. list-table::
            :widths: auto

            * - pctl.names_prefix
              - String, the characters, if any, that should be stripped from the front of the newly created variable names.  Default = "", no prefix.
            * - pctl.names_sep_combine
              - String, the characters, if any, that should be added between the tokens when creating the new variable names. Default = "_".
            * - pctl.values_drop_missing
              - Scalar, 0 or 1. If set to 1, all rows with missing values will be removed. Default = 0.
            * - pctl.id_cols
              - String array, containing the names of the variables that should be used to determine a unique observation. Default = "", meaning the combination of all variables other than those specified by ``names_to`` and ``values_from`` will be used.

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


.. seealso:: Functions :func:`dfwider`
