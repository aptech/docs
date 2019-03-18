
DOSWinOpen
==============================================

Purpose
----------------

Opens the DOS compatibility window and gives it the specified title and attributes. NOTE: This function is no longer supported. This documentation is provided as a reference for understanding legacy code. In many cases, you may simply comment out calls to DOSWinOpen and the program will run successfully in the program input/output window.

Format
----------------
.. function:: DOSWinOpen(title, attr)

    :param title: window title.
    :type title: string

    :param attr: window attributes.
    :type attr: 5x1 vector or scalar missing

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

    :returns: ret (*scalar*), success flag, 1 if successful, 0 if not.

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
