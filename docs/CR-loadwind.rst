
loadwind
==============================================

Purpose
----------------

Load a previously saved graphic panel configuration. Note: This function is for use with the deprecated PQG graphics.

Format
----------------
.. function:: loadwind(namestr)

    :param namestr: name of file to be loaded.
    :type namestr: string

    :returns: err (*scalar*), 0 if successful, 1 if graphic panel matrix
        is invalid. Note that the current graphic panel configuration will
        be overwritten in either case.

