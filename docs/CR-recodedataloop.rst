
recode (dataloop)
==============================================

Purpose
----------------

Changes the value of a variable with different values based on a set of logical expressions.

.. _recodedataloop
.. index:: recode(dataloop)

Format
----------------

::

    recode var with 
    //   or
    recode # var with
    //   or
    recode $ var with

    val1 for expression_1,
    val2 for expression_2,
      .
      .
      .
    valn for expression_n;

**Parameters**

:var: (*literal*) the new variable name.

:val: (*scalar*) value to be used if corresponding expression is TRUE.

:expression: (*scalar*) logical scalar-returning expression that returns nonzero TRUE or zero FALSE

Remarks
-------

If '``$``' is specified, the variable will be considered a character
variable. If '``#``' is specified, the variable will be considered numeric.
If neither is specified, the type of the variable will be left
unchanged.

The logical expressions must be mutually exclusive, that is only one may
return TRUE for a given row (observation).

If none of the expressions is TRUE for a given row (observation), its
value will remain unchanged.

Any variables referenced must already exist, either as elements of the
source dataset, as `extern`'s, or as the result of a previous `make`,
`vector`, or `code` statement.


Examples
----------------

::

    recode age with
          1 for age < 21,
          2 for age >= 21 and age < 35,
          3 for age >= 35 and age < 50,
          4 for age >= 50 and age < 65,
          5 for age >= 65;

::

    recode $ sex with
          "MALE" for sex =\,= 1,
          "FEMALE" for sex =\,= 0;

::

    recode # sex with
          1 for sex $=\,= "MALE",
          0 for sex $=\,= "FEMALE";

.. seealso:: Functions `code`

