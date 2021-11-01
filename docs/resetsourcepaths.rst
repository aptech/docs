
resetsourcepaths
==============================================

Purpose
----------------

Resets the source path to the original GAUSS startup values.

Format
----------------
.. function:: ret = resetsourcepaths()

    :return ret: 1 if reset is successful, 0 otherwise.

    :rtype ret: string

Remarks
-------

The source path is set by the :file:`src_path` configuration variable in your
GAUSS configuration file, :file:`gauss.cfg`.
