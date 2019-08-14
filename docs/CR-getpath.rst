
getpath
==============================================

Purpose
----------------

Returns an expanded filename including the drive and path.

Format
----------------
.. function:: getpath(pfname)

    :param pfname: partial filename with only partial or missing path information.
    :type pfname: string

    :returns: **fname** (*string*) - filename with full drive and path.

Remarks
-------

This function handles relative path references.


Examples
----------------

::

    // Get path of `temp.e`
    y = getpath("temp.e");
    print y;

::

    C:\gauss\temp.e

assuming that ``C:\gauss`` is the current directory.

Source
------

getpath.src
