
setvars
==============================================

Purpose
----------------

Reads the variable names from a data set header and creates global
matrices with the same names.

Format
----------------
.. function:: setvars(dataset)

    :param dataset: the name of the GAUSS data set. Do not use
        a file extension.
    :type dataset: string

    :returns: nvec (*Nx1 character vector*), containing the variable names
        defined in the data set.

Examples
----------------

::

    nvec = setvars("freq");

Source
++++++

vars.src

.. seealso:: Functions :func:`makevars`
