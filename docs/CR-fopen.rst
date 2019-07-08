
fopen
==============================================

Purpose
----------------

Opens a file.

Format
----------------
.. function:: fopen(filename, omode)

    :param filename: name of file to open.
    :type filename: string

    :param omode: file I/O mode. (See *Remarks*, below.)
    :type omode: string

    :returns: fh (*scalar*) - file handle.

Portability
-----------

**Linux/macOS**

Carriage return-linefeed conversion for files opened in text mode is
unnecessary, because in Linux/macOS a newline is simply a linefeed.

Remarks
-------

filename can contain a path specification.

*omode* is a sequence of characters that specify the mode in which to open
the file. The first character must be one of:

.. csv-table::
    :widths: auto

    "r", "Open an existing file for reading. If the file does not exist, :func:`fopen` fails."
    "w", "Open or create a file for writing. If the file already exists, its current contents will be destroyed."
    "a", "Open or create a file for appending. All output is appended to the end of the file."

To this can be appended a ``+`` and/or a ``b``. The ``+`` indicates the file is to
opened for reading and writing, or update, as follows:

.. csv-table::
    :widths: auto

    "r+", "Open an existing file for update. You can read from or write to any location in the file. If the file does not exist, :func:`fopen` fails."
    "w+", "Open or create a file for update. You can read from or write to any location in the file. If the file already exists, its current contents will be destroyed."
    "a+", "Open or create a file for update. You can read from any location in the file, but all output will be appended to the end of the file."

Finally, the ``b`` indicates whether the file is to be opened in text or
binary mode. If the file is opened in binary mode, the contents of the
file are read verbatim; likewise, anything output to the file is written
verbatim. In text mode (the default), carriage return-linefeed sequences
are converted on input to linefeeds, or newlines. Likewise on output,
newlines are converted to carriage return-linefeeds. Also in text mode,
if a ``Ctrl+Z`` (char 26) is encountered during a read, it is interpreted as
an end-of-file character, and reading ceases. In binary mode, ``Ctrl+Z`` is
read in uninterpreted.

The order of ``+`` and ``b`` is not significant; ``rb+`` and ``r+b`` mean the same
thing.

You can both read from and write to a file opened for update. However,
before switching from one to the other, you must make an :func:`fseek` or :func:`fflush`
call, to flush the file's buffer.

If :func:`fopen` fails, it returns a 0.

Use `close` and :func:`closeall` to close files opened with :func:`fopen`.

.. seealso:: Functions :func:`fseek`, `close`, :func:`closeall`
