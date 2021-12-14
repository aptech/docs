
renamefile
==============================================

Purpose
----------------

Changes file name.

Format
----------------
.. function:: ret = renamefile("oldname","newname")

    :param oldname: existing file name.
    :type oldname: string

    :param newname: new file name.
    :type newname: string

    :return ret: 0 if successful.

    :rtype ret: scalar

Examples
----------------

::

    ret = renamefile("myfile.gss", "mynewfile.gss");

In this example, a file in the current working directory with the name ``"myfile.gss"`` will be renamed ``"mynewfile.gss"`` in the same directory. Full path information may also be included:

::

    // On Windows
    ret = renamefile("c:\\gauss22\\myfile.gss",
      "c:\\gauss22\\mynewfile.gss");

    // On Linux/Mac
    ret = renamefile("/home/user/gauss22/myfile.gss",
      "/home/user/gauss22/mynewfile.gss");
