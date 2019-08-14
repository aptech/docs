
sysstate
==============================================

Purpose
----------------

Gets or sets general system parameters.

Format
----------------
.. function:: { rets... } = sysstate(case, y)

    :param case: , path to set.
    :type case: scalar 2-7

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

    :return vi: containing version information:

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

    :type vi: 8x1 numeric vector

Remarks
-------

The available cases are as follows:

+-----------------------------------+-----------------------------------+
| **Case 1**                        | **Version Information** Returns   |
|                                   | the current GAUSS version         |
|                                   | information in an 8-element       |
|                                   | numeric vector.                   |
+-----------------------------------+-----------------------------------+
| **Cases 2-7**                     | **GAUSS System Paths** Gets or    |
|                                   | sets GAUSS system path.           |
+-----------------------------------+-----------------------------------+
| **Case 8**                        | **Complex Number Toggle**         |
|                                   | Controls automatic generation of  |
|                                   | complex numbers in sqrt, ln, and  |
|                                   | log for negative arguments.       |
+-----------------------------------+-----------------------------------+
| **Case 9**                        | **Complex Trailing Character**    |
|                                   | Gets or sets trailing character   |
|                                   | for the imaginary part of a       |
|                                   | complex number.                   |
+-----------------------------------+-----------------------------------+
| **Case 10**                       | **Printer Width** Gets or sets    |
|                                   | lprint width.                     |
+-----------------------------------+-----------------------------------+
| **Case 11**                       | **Auxiliary Output Width** Gets   |
|                                   | or sets the auxiliary output      |
|                                   | width.                            |
+-----------------------------------+-----------------------------------+
| **Case 13**                       | **LU Tolerance** Gets or sets     |
|                                   | singularity tolerance for LU      |
|                                   | decomposition in current thread.  |
+-----------------------------------+-----------------------------------+
| **Case 14**                       | **Cholesky Tolerance** Gets or    |
|                                   | sets singularity tolerance for    |
|                                   | Cholesky decomposition in current |
|                                   | thread.                           |
+-----------------------------------+-----------------------------------+
| **Case 15**                       | **Screen State** Gets or sets     |
|                                   | window state as controlled by     |
|                                   | screen command.                   |
+-----------------------------------+-----------------------------------+
| **Case 18**                       | **Auxiliary Output** Gets         |
|                                   | auxiliary output parameters.      |
+-----------------------------------+-----------------------------------+
| **Case 19**                       | **Get/Set Format** Gets or sets   |
|                                   | format parameters.                |
+-----------------------------------+-----------------------------------+
| **Case 21**                       | **Imaginary Tolerance** Gets or   |
|                                   | sets imaginary tolerance in       |
|                                   | current thread.                   |
+-----------------------------------+-----------------------------------+
| **Case 22**                       | **Source Path** Gets or sets the  |
|                                   | path the compiler will search for |
|                                   | source files.                     |
+-----------------------------------+-----------------------------------+
| **Case 24**                       | **Dynamic Library Directory**     |
|                                   | Gets or sets the path for the     |
|                                   | default dynamic library           |
|                                   | directory.                        |
+-----------------------------------+-----------------------------------+
| **Case 25**                       | **Temporary File Path** Gets or   |
|                                   | sets the path GAUSS will use for  |
|                                   | temporary files.                  |
+-----------------------------------+-----------------------------------+
| **Case 26**                       | **Interface Mode** Returns the    |
|                                   | current interface mode.           |
+-----------------------------------+-----------------------------------+
| **Case 28**                       | **Random Number Generator         |
|                                   | Parameters** Gets or sets         |
|                                   | parameters used by the random     |
|                                   | number generation commands.       |
+-----------------------------------+-----------------------------------+
| **Case 30**                       | **Base Year Toggle** Specifies    |
|                                   | whether year value returned by    |
|                                   | date is to include base year      |
|                                   | (1900) or not.                    |
+-----------------------------------+-----------------------------------+
| **Case 32**                       | **Global LU Tolerance** Gets or   |
|                                   | sets global singularity tolerance |
|                                   | for LU decomposition.             |
+-----------------------------------+-----------------------------------+
| **Case 33**                       | **Global Cholesky Tolerance**     |
|                                   | Gets or sets global singularity   |
|                                   | tolerance for Cholesky            |
|                                   | decomposition.                    |
+-----------------------------------+-----------------------------------+
| **Case 34**                       | **Global Imaginary Tolerance**    |
|                                   | Gets or sets global imaginary     |
|                                   | tolerance.                        |
+-----------------------------------+-----------------------------------+

.. seealso:: Functions :func:`outwidth`, :func:`croutp`, :func:`inv`, :func:`chol`, :func:`solpd`, `screen`, `output`, :func:`format`, :func:`print`, :func:`hasimag`, `dlibrary`, :func:`dllcall`, :func:`rndcon`, :func:`rndn`, :func:`rndu`, :func:`croutp`, :func:`inv`, :func:`chol`, :func:`solpd`, :func:`hasimag`
