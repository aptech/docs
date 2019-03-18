
sysstate
==============================================

Purpose
----------------

Gets or sets general system parameters.

Format
----------------
.. function:: sysstate(case, y)

    :param case: scalar 2-7, path to set.
    :type case: TODO

    .. csv-table::
        :widths: auto

        "2", ".exe file location."
        "3", "loadexe path."
        "4", "save path."
        "5", "load, loadm path."
        "6", "loadf, loadp path."
        "7", "loads path."

    :param path: or string
        containing the new path.
    :type path: scalar 0 to get path

    :returns: vi (*TODO*), 8x1 numeric vector containing version information:

    .. csv-table::
        :widths: auto

        "[1]", "Major version number."
        "[2]", "Minor version number."
        "[3]", "Revision."
        "[4]", "Machine type."
        "[5]", "Operating system."
        "[6]", "Runtime module."
        "[7]", "Light version."
        "[8]", "Always 0."
        "vi[4] indicates the type of machine on which GAUSS is running:"
        "", "1", "Intel x86"
        "", "2", "Sun SPARC"
        "", "4", "HP 9000"
        "", "7", "Mac 32-bit PowerPC"
        "vi[5] indicates the operating system on which GAUSS is running:"
        "", "3", "Solaris"
        "", "5", "HP-UX"
        "", "9", "Windows"
        "", "10", "Linux"
        "", "12", "Mac OS"

