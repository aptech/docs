
filesa
==============================================

Purpose
----------------

Returns a string array of file names.

Format
----------------
.. function:: fnames = filesa(fspec)

    :param fspec: file specification to search for. Can include path and wildcards.
    :type fspec: string

    :return fnames: all file names that match or null string if none are found.

    :rtype fnames: Nx1 string array

Remarks
-------

*fnames* will contain file names only; any path information that was passed is
dropped.


Examples
----------------

Example 1: List all example files
+++++++++++++++++++++++++++++++++

Print out the list of all files located in the GAUSS examples directory which end with the file extension :file:`.e`.

::
    
    fspec = getGAUSSHome() $+ "examples/*.e";
    print filesa(fspec);

Example 2: Find which start with specific letters
++++++++++++++++++++++++++++++++++++++++++++++++++

This example will search the current working directory for any file which starts with ``ch``.

::

    fnames = filesa("ch*");

Example 3: Create proc to check if a file exists
+++++++++++++++++++++++++++++++++++++++++++++++++

::

    proc exist(filename);
       retp(not filesa(filename) $== "");
    endp;

This procedure will return 1 if the file exists or 0 if not.

.. seealso:: Functions :func:`fileinfo`, :func:`shell`
