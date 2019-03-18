
recode (dataloop)
==============================================

Purpose
----------------

Changes the value of a variable with different values based on a set of logical expressions.

Format
----------------
.. function:: recode var with 
			     orrecode # var with   orrecode $ var with val1 for expression_1, val2 for expression_2,  .  .  . valn for expression_n

    :param var: the new variable name.
    :type var: literal

    :param val: value to be used if corresponding
        expression is TRUE.
    :type val: scalar

    :param expression: logical scalar-returning expression
        that returns nonzero TRUE or zero FALSE.
    :type expression: TODO

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

.. seealso:: Functions 
