
code (dataloop)
==============================================

Purpose
----------------

Creates new variables with different values based on a set of logical expressions.

Format
----------------
.. function:: code [[#]] [[$]] var [[default defval]] with
                  val_1 for expression_1,
                  val_2 for expression_2, 
                  ... 
                  val_n for expression_n

    :param var: the new variable name.
    :type var: literal

    :param defval: the default value if none of the expressions are TRUE.
    :type defval: scalar

    :param val: value to be used if corresponding expression is TRUE.
    :type val: scalar

    :param expression: logical scalar-returning expression that returns nonzero TRUE or zero FALSE
    :type expression: scalar

Remarks
-------

If '$' is specified, the new variable will be considered a character
variable. If '#' or nothing is specified, the new variable will be
considered numeric.

The logical expressions must be mutually exclusive, i.e., only one may
return TRUE for a given row (observation).

Any variables referenced must already exist, either as elements of the
source data set, as externs, or as the result of a previous make,
vector, or code statement.

If no default value is specified, 999 is used.

Examples
----------------

::

    code agecat default 5 with
     1 for age < 21,
     2 for age >= 21 and age < 35,
     3 for age >= 35 and age < 50,
     4 for age >= 50 and age < 65;

::

    code $ sex with
    "MALE" for gender == 1,
    "FEMALE" for gender == 0;

.. seealso:: Functions :func:`recode`

