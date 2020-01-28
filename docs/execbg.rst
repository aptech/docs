
execbg
==============================================

Purpose
----------------

Executes an executable program in the background and returns the process id to GAUSS.

Format
----------------
.. function:: pid = execbg(program, comline)

    :param program: the name of the program, including the extension, to be executed.
    :type program: string

    :param comline: the arguments to be placed on the command line of the program being executed.
    :type comline: string

    :return pid: the process id of the executable returned by *program*.

        If :func:`execbg` cannot execute *program*, the error returns
        will be negative:

        .. csv-table::
            :widths: auto

            "-1", "file not found"
            "-2", "the file is not an executable file"
            "-3", "not enough memory"
            "-4", "command line too long"

    :rtype pid: scalar

Examples
----------------

::

    pid = execbg("atog.exe", "comd1.cmd");

    if (pid < 0);
       errorlog "atog failed";
       end;
    endif;

In this example, the ATOG ASCII conversion utility is
executed under the :func:`execbg`. The name of the
command file to be used, :file:`comd1.cmd`, is passed to ATOG
on its command line. The returned value, *pid*, is tested
to see whether ATOG was successful. If not successful the
program terminates after printing an error message. See `ATOG <AT-ATOG.html>`_ .

