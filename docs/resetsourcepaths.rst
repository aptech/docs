
resetsourcepaths
==============================================

Purpose
----------------

Resets the source path to the original GAUSS startup values.

Format
----------------
.. function:: resetsourcepaths()

Remarks
-------

The source path is set by the :file:`src_path` configuration variable in your
GAUSS configuration file, :file:`gauss.cfg`.

Examples
--------

::

    // Reset the source path to the gauss.cfg defaults
    resetsourcepaths();
