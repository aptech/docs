
cdir
==============================================

Purpose
----------------

Returns the current directory.

Format
----------------
.. function:: y = cdir(s)

    :param s: A null string, or a scalar 0.
    :type s: string, or scalar

    :return dir: containing the drive and full path name of the current directory on the specified drive.

    :rtype dir: string

Remarks
-------

If the current directory is the root directory, the returned string will
end with a backslash, otherwise it will not.

A null string or scalar zero can be passed in as an argument to obtain
the current drive and path name.


Examples
----------------

Windows Example
+++++++++++++++

If the current working directory is ``C:\gauss``:

::

    // Get current directory
    dir = cdir(0);

After the code above, *dir* will equal:

::

    C:\gauss

macOS Example
+++++++++++++++

If the current working directory is ``/Users/Research/gauss``:

::

    // Get current directory
    dir = cdir(0);

After the code above, *dir* will equal:

::

    /Users/Research/gauss
