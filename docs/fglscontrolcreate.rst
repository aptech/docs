
fglsControlCreate
==============================================

Purpose
----------------

Creates default olsmtControl structure.

Format
----------------
.. function:: fctl = fglsControlCreate()

    :return fctl: instance of :class:`fglsControl` struct with members set to default values.

    :rtype c: struct

Examples
----------------
Since structures are strongly typed in GAUSS, each structure must be declared
before it can be used.

::

    // Declare 'fctl' as an olsmtControl structure
    struct fglsControl fctl;

    // Initialize structure 'ctl'
    fctl = fglsControlCreate();

The members of the :class:`fglsControl` structure and their default values are described in the
manual entry for :func:`fgls`.

Source
------

fgls.src

.. seealso:: Functions :func:`fgls`
