
comlog
==============================================

Purpose
----------------

Controls logging of interactive mode commands to a disk file.

Format
----------------
.. function:: comlog [[file=filename]] [[on|off|reset]]

    :param filename: The :code:`file=filename` subcommand selects the file to log interactive mode
                     statements to. This can be any legal file name.
                     
                     If the name of the file is to be taken from a string variable, the name
                     of the string must be preceded by the ^ (caret) operator.

                     There is no default file name.

    :type filename: literal or ^string

Remarks
-------

* :code:`comlog on` turns on command logging to the current file. If the file
  already exists, subsequent commands will be appended.

* :code:`comlog off` closes the log file and turns off command logging.

* :code:`comlog reset` turns on command logging to the current log file, resetting
  the log file by deleting any previous commands.

* Interactive mode statements are always logged into the file specified by
  the ``log_file`` configuration variable in the :file:`gauss.cfg` file, regardless of the state of `comlog`.

* The command :code:`comlog file= filename` selects the file but does not turn on logging.

* The command :code:`comlog off` will turn off logging. The filename will remain
  the same. A subsequent :code:`comlog on` will cause logging to resume. A
  subsequent :code:`comlog reset` will cause the existing contents of the log file
  to be destroyed and a new file created.

* The command :code:`comlog by` itself will cause the name and status of the
  current log file to be printed in the window.

