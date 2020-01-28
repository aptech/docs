
setvars
==============================================

Purpose
----------------

Reads the variable names from a dataset header and creates global
matrices with the same names.

Format
----------------
.. function:: nvec = setvars(dataset)

    :param dataset: the name of the GAUSS dataset. Do not use a file extension.
    :type dataset: string

    :return nvec: containing the variable names defined in the dataset.

    :rtype nvec: Nx1 character vector

Examples
----------------

::

    nvec = setvars("freq");

Remarks
-------

:func:`setvars` is designed to be used interactively.

Source
------

vars.src

.. seealso:: Functions :func:`makevars`

