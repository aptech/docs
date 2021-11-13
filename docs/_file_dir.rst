
__FILE_DIR
==============================================

Purpose
----------------

Returns a string containing the full path to the file in which the statement is contained.

Format
----------------
.. function:: path = __FILE_DIR

    :return path: containing the full path to the file which contains the usage of `__FILE_DIR`.

    :rtype path: string

Remarks
-------

-  If `__FILE_DIR` is run inside a program file with either ``F4`` or by selecting **Run Selected Text** from the context menu, it will work the same as if run in a file.
-  `__FILE_DIR` can be run at the command prompt. However, since it is not inside a file it will return the current working directory.
-  `__FILE_DIR` makes sharing code with other people or other computers easier. See the next point for more details.
-  A common use of `__FILE_DIR` is to locate a data file which is in the
   same directory as the code file, but may not be the current working
   directory. For example, the GAUSS example file :file:`gmmfitiv_auto.e` is
   located in the GAUSS examples directory. This example code needs to
   load a dataset which is also located in the GAUSS examples directory.
   For this purpose, it uses the line:

   ::

      // Create fully pathed dataset file name string
      auto_dset = __FILE_DIR $+ "auto.dat";

   This code will set the string "auto.dat" equal to the full path to
   the GAUSS examples directory followed by "auto.dat", regardless of
   your system or installation directory. The actual contents of this
   string will vary depending on your system, but will look similar to
   this:

   ::

      // Mac
      "/Users/YourUserName/gauss/examples/auto.dat"
                      
      // Windows
      "C:\\gauss\\examples\\auto.dat"
                          
      // Linux
      "/home/yourusername/gauss/exmples/auto.dat

-  Note that `__FILE_DIR` is technically a GAUSS define, therefore it
   cannot be appended with parentheses like this:

   ::

       // Adding parentheses to the end is incorrect
      __FILE_DIR();            

.. seealso:: Functions :func:`getGAUSSHome`

