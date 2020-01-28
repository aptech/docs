
getpath
==============================================

Purpose
----------------

Returns an expanded filename including the drive and path.

Format
----------------
.. function:: fname = getpath(pfname)

    :param pfname: partial filename with only partial or missing path information.
    :type pfname: string

    :return fname: filename with full drive and path.

    :rtype fname: string

Examples
----------------

::

    // Get path of `temp.e`
    y = getpath("temp.e");
    print y;

::

    C:\gauss\temp.e

assuming that ``C:\gauss`` is the current directory.

Remarks
-------

This function handles relative path references.


Source
------

getpath.src
