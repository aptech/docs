
lib
==============================================

Purpose
----------------

Builds and updates library files.

.. _lib:
.. index:: lib

Format
----------------

::

    lib library file;
    lib library -flag;
    lib library file -flag1 -flag2;

**Parameters:**

:library: (*literal*) name of library.
:file: (*literal*) optional. name of source file to be updated or added.
:flags: (*literal*) optional. preceded by ``-``, controls operation of library update. To control handling of path information on source filenames:

    .. csv-table::
        :widths: auto

        "``-addpath``", "add paths to entries without paths and expand relative paths."
        "``-gausspath``", "reset all paths using a normal file search."
        "``-leavepath``", "(default) leave all path information untouched."
        "``-nopath``", "drop all path information."

    To specify a library update or a complete library build:

    .. csv-table::
        :widths: auto

        "``-update``", "(default) update the symbol information for the specified file only."
        "``-build``", "update the symbol information for every library entry by compiling the actual source file."
        "``-delete``", "delete a file from the library."
        "``-list``", "list files in a library."

    To control the symbol type information placed in the library file:

    .. csv-table::
        :widths: auto

        "``-strong``", "(default) use strongly typed symbol entries."
        "``-weak``", "save no type information. This should only be used to build a library compatible with a previous version of GAUSS."

    To control location of temporary files for a complete library build:

    .. csv-table::
        :widths: auto

        "``-tmp``", "(default) use the directory pointed to by the *tmp_path* configuration variable. If *tmp_path* is not defined, `lib` will look for a *tmp* environment variable."
        "``-disk``", "use the same directory listed in the *lib_path* configuration variable."

Examples
----------------

Let us suppose that you have a file named :file:`myprocs.gss` located in your GAUSS `src` directory. Let us further suppose that you would like to create a new library named *mylibrary*. You could accomplish that task like this:

::

    lib mylibrary myprocs.gss;

Now that this library has been created, you could add other files in the same manner. To add a file named :file:`mystats.gss` would look like this:

::

    lib mylibrary mystats.gss;

This second command will add the file :file:`mystats.gss` to the *mylibrary* which was created in the first step above. It will not overwrite or replace the library.

You may print the list of files contained in the library by using the ``-list`` flag. Entering the command:

::

    lib mylibrary -list;

at the GAUSS command line will produce the output similar to:

::

    Listing library:  mylibrary.lcg
        myprocs.gss
        mystats.gs

If you add procedures to one of the files in your library, you will need to update the library to reflect these new changes. Continuing with the example from above, if you added some new procedures to the file :file:`mystats.gss`, you could update the *mylibrary* library with the following command:

::

    lib mylibrary mystats.gss -update;

Note that, as in the command above, the ``-update`` flag must be used with a file. To update, or rebuild the references for all files in the library, use the ``-build`` flag.

::

    lib mylibrary -build;

Remarks
-------

The library management functionality offered by the `lib` command can also
be accomplished interactively with windows and buttons, using the
Library Tool in the user interface. See **The Library Tool**, Chapter 1,
for more information on using the Library Tool.

The flags can be shortened to one or two letters, as long as they remain
unique-for example, ``-b`` to ``-build`` a library, ``-li`` to list files in a
library.

If the filenames include a full path, the compilation process is faster
because no unnecessary directory searching is needed during the
autoloading process. The default path handling adds a path to each file
listed in the library and also expands any relative paths so the system
will work from any drive or subdirectory.

When a path is added to a filename containing no path information, the
file is searched for on the current directory and then on each
subdirectory listed in *src_path*. The first path encountered that
contains the file is added to the filename in the library entry.

.. seealso:: Keyword `library`
