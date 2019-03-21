
cdir
==============================================

Purpose
----------------

Returns the current directory.

Format
----------------
.. function:: cdir(s)

    :param s: if the first character is 'A'-'Z' and the second character is a colon ':', then that drive
        will be used. If not, the current default drive will be used.
    :type s: string

    :returns: y (string), containing the drive and full path name of the current directory on the specified drive.

Remarks
-------

If the current directory is the root directory, the returned string will
end with a backslash, otherwise it will not.

A null string or scalar zero can be passed in as an argument to obtain
the current drive and path name.


Examples
----------------
If the current working directory is C:\gauss:

::

    x = cdir(0);
    y = cdir("d:");
    print x;
    print y;

The code above will return:

::

    C:\gauss
    d:

