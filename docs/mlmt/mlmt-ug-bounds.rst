Bounds
===========
Bounds are a type of linear inequality constraint. For computational convenience, they may be specified separately from the other inequality constraints. To specify bounds, the lower and upper bounds respectively are entered in the first and second columns of a matrix that has the same number of rows as the parameter vector. This matrix is assigned to the *bounds* member of an instance of a :class:`maxlikmtControl` structure.

If the bounds are the same for all of the parameters, only the first row is necessary.

Examples
+++++++++++
To bound four parameters to the ranges:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    // Declare 'ctl' to be a maxlikmtControl struct
    // and fill with default settings
    struct maxlikmtControl ctl;
    ctl = maxlikmtControlCreate();

    // Set separate bounds for each of four parameters
    ctl.bounds = { -10, 10,
                   -10, 0,
                     1, 10,
                     0, 1 };

Suppose all of the parameters are to be bounded between -50 and +50
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    ctl.bounds = {-50, 50};

This specification ensures that all parameters within the model are constrained to operate within the defined bounds, thus adhering to any physical, financial, or other types of constraints that may apply to the parameters being estimated.
