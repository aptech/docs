
keep (dataloop)
==============================================

Purpose
----------------

Specifies columns (variables) to be saved to the output data set in a data loop.

Format
----------------
.. function:: keep variable_list

Remarks
-------

Commas are optional in variable_list.

Retains only the specified variables in the output data set. Any
variables referenced must already exist, either as elements of the
source data set, or as the result of a previous make, vector, or code
statement.

If neither keep nor drop is used, the output data set will contain all
variables from the source data set, as well as any newly defined
variables. The effects of multiple keep and drop statements are
cumulative.


Examples
----------------

::

    keep age, pay, sex;

.. seealso:: Functions 
