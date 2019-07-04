
DOSWinOpen
==============================================

Purpose
----------------

Opens the DOS compatibility window and gives it the specified title and attributes.

.. WARNING:: This function is no longer supported. This documentation is provided as a reference for understanding legacy code. In many cases, you may simply comment out calls to :func:`DOSWinOpen` and the program will run successfully in the program input/output window.

Format
----------------
.. function:: DOSWinOpen(title, attr)

    :param title: window title.
    :type title: string

    :param attr: window attributes.

        .. csv-table::
            :widths: auto

            "[1]", "window x position"
            "[2]", "window y position"
            "[3]", "text foreground color"
            "[4]", "text background color"
            "[5]", "close action bit flags"
            "", "bit 0 (1's bit)", "issue dialog"
            "", "bit 1 (2's bit)", "close window"
            "", "bit 2 (4's bit)", "stop program"

    :type attr: 5x1 vector or scalar missing

    :returns: **ret** (*scalar*) - success flag, 1 if successful, 0 if not.

Remarks
-------

If title is a null string (``""``) the window will be titled
:code:`"GAUSS-DOS"`.

Defaults are defined for the elements of *attr*. To use the default, set
an element to a missing value. Set *attr* to a scalar missing to use all
defaults. The defaults are defined as follows:

+-----+--------+-------------------------------------------------------+
| [1] | varies | use x position of previous DOS window                 |
+-----+--------+-------------------------------------------------------+
| [2] | varies | use y position of previous DOS window                 |
+-----+--------+-------------------------------------------------------+
| [3] | 7      | white foreground                                      |
+-----+--------+-------------------------------------------------------+
| [4] | 0      | black background                                      |
+-----+--------+-------------------------------------------------------+
| [5] | 6      | 4+2: stop program and close window without confirming |
+-----+--------+-------------------------------------------------------+

If the DOS window is already open, the new title and *attr* will be
applied to it. Elements of *attr* that are missing are not reset to the
default values, but are left as is.

To set the close action flags value (*attr[5]*), just sum the desired bit
values. For example:

::

    stop program (4) + close window (2) + confirm close (1) = 7

The close action flags are only relevant when a user attempts to
interactively close the DOS window while a program is running. If GAUSS
is idle, the window will be closed immediately. Likewise, if a program
calls :func:`DOSWinCloseall`, the window is closed, but the program does not get
terminated.


Examples
----------------

::

    let attr = 50 50 7 0 7;

    if not DOSWinOpen("Legacy Window", attr);
       errorlog "Failed to open DOS window, aborting";
       stop;
    endif;

This example opens the DOS window at screen location (50,50), with white text on a black background. The close action flags are 4 + 2 + 1 (stop program + close window + issue confirm dialog) = 7. Thus, if the user attempts to close the window while a program is running, he/she will be asked for confirmation. Upon confirmation, the window will be closed and the program terminated.

|
