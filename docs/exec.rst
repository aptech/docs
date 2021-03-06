
exec
==============================================

Purpose
----------------

Executes an executable program and returns the exit code to GAUSS.

Format
----------------
.. function:: ret = exec(program, comline)

    :param program: the name of the program, including the extension, to be executed.
    :type program: string

    :param comline: the arguments to be placed on the command line of the program being executed.
    :type comline: string

    :return ret: the exit code returned by *program*.

        If exec can't execute *program*,
        the error returns will be negative:

        .. csv-table::
            :widths: auto

            "-1", "file not found"
            "-2", "the file is not an executable file"
            "-3", "not enough memory"
            "-4", "command line too long"

    :rtype ret: scalar

Examples
----------------

::

    ret = exec("atog", "comd1.cmd");

    // If 'ret' is nonzero
    if ret;
       errorlog "atog failed";
       end;
    endif;

In this example the ATOG ASCII conversion utility is
executed under the :func:`exec` function. The name of the
command file to be used, :file:`comd1.cmd`, is passed to
ATOG on its command line. The exit code *ret* returned
by :func:`exec` is tested to see if ATOG was successful;
if not, the program will be terminated after printing
an error message. See `ATOG <AT-ATOG.html>`_ .
