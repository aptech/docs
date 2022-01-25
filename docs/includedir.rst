
#includedir
==============================================

Purpose
----------------

Adds folders to the source path relative to the program file or the working directory.

Format
----------------
.. function:: #includedir
              #include rel_path



Examples
----------------

Program file examples
+++++++++++++++++++++++++

For this example, let's assume that the following contents were added to a file named ``main.gss`` in the folder ``C:\Users\Research\Progs``.

::

    #includedir
    #include myfile.src; 


The above code will:

1. Add the folder, ``C:\Users\Research\Progs`` to the front of the GAUSS source path.
2. GAUSS will look for the ``myfile.src`` file in ``C:\Users\Research\Progs``.

Relative path example
+++++++++++++++++++++++

Let's say that we have decided to move all of our ``.src`` files to a sub-folder named ``src`` located inside of ``C:\Users\Research\Progs``. If we change our code to:


::

    #includedir src
    #include myfile.src; 

This time, the code will:


1. Add the folder, ``C:\Users\Research\Progs\src`` to the front of the GAUSS source path.
2. GAUSS will look for the ``myfile.src`` file in ``C:\Users\Research\Progs\src``.


Remarks
------------

* Use :func:`resetsourcepaths` to reset your GAUSS source paths to what they were when you started GAUSS.
* If ``#includedir`` is used from the command window, GAUSS will add the current working directory (or a path relative to the current working directory) to the source path.
* :doc:`include` will look for files first in your current working directory, then check the files in your source path.
* You can view your current source path with the command\:

    ::

        // Print the current source path
        print sysstate(22,0);



.. seealso:: Functions `include`, :func:`resetsourcepaths`

