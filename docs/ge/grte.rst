Using the GAUSS Run-Time Engine (GRTE)
======================================

The **GAUSS Run-Time Engine (GRTE)** allows you to create distributable applications that take advantage of the computational speed and power of **GAUSS**.

Creating a Distributable Application 
-----------------------------------------

To use the **GAUSS Engine** in an application on Windows, you must link the application with **mteng.lib**, and your application directory must contain **mteng.dll**. On Linux, link the application with **-lmteng** and make sure that **libmteng.so** is in your application directory. On both platforms, your application will run only if a valid license file with the **MTENG** feature can

be found in your application directory. This license is linked to a particular **hostid**, so it will run only on your development machine.

To create a distributable application, you must use the **GRTE**:

- **Windows:** Link your application with **mtengrt.lib** (instead of **mteng.lib**) and distribute **mtengrt.dll** with your application.

- **Linux:** Link your application with **-lmtengrt** (instead of **-lmteng**), and distribute **libmtengrt.so** with your application.

- **macOS:** Link your application with **-lmtengrt** (instead of **-lmteng**), and distribute **libmtengrt.dylib** with your application.

For the application to run, you must also distribute a license file with the **MTGRTE** feature, named **g.gkf** in your application directory.

Applications that use the **GRTE** will not be able to create globals in a **GAUSS** workspace. Therefore, any global variables or procedures that are needed by the application must be compiled with the **GAUSS Engine** into a **.gcg** file that is distributed with the application. You may use either the compile command from the command line interface, **engauss**, or the **GC** compiler to compile a **GAUSS** program containing global declarations.

Deployment Overview
~~~~~~~~~~~~~~~~~~~~~~~~~

The following table summarizes the GRTE deployment bundle for a headless (no GUI) application. Qt is **not required** for headless deployments -- stub libraries are provided that eliminate all Qt dependencies.

+-------------------------------+----------+----------------------------------------------+
| Component                     | Bundled? | Notes                                        |
+===============================+==========+==============================================+
| ``mtengrt`` shared library    | Yes      | Primary engine (GRTE variant)                |
+-------------------------------+----------+----------------------------------------------+
| ``libgauss``                  | Yes      | Core mathematical functions                  |
+-------------------------------+----------+----------------------------------------------+
| ``libgla``                    | Yes      | BLAS/LAPACK (self-contained, no system       |
|                               |          | BLAS/LAPACK/MKL dependency)                  |
+-------------------------------+----------+----------------------------------------------+
| Graphics/database stubs       | Yes      | ``libgsgraphics_stubs`` + ``libcql_stubs``   |
|                               |          | replace Qt with no-ops for headless use      |
+-------------------------------+----------+----------------------------------------------+
| ``libreadstat``               | Yes      | Statistical file format support              |
+-------------------------------+----------+----------------------------------------------+
| ``libcityhash``               | Yes      | Internal hashing                             |
+-------------------------------+----------+----------------------------------------------+
| ``libhdf5``                   | Yes      | HDF5 data format support                     |
+-------------------------------+----------+----------------------------------------------+
| ``libxl``                     | Yes      | Excel file support                           |
+-------------------------------+----------+----------------------------------------------+
| ``libtbb``, ``libtbbmalloc``  | Yes      | Threading (Intel TBB)                        |
+-------------------------------+----------+----------------------------------------------+
| ``gauss.cfg``                 | Yes      | Runtime configuration (text file)            |
+-------------------------------+----------+----------------------------------------------+
| ``g.gkf``                     | Required | Authorization token for GRTE                 |
+-------------------------------+----------+----------------------------------------------+
| ``.gcg`` compiled files       | Required | Pre-compiled GAUSS programs                  |
+-------------------------------+----------+----------------------------------------------+
| Qt frameworks                 | **No**   | Not needed for headless deployment           |
+-------------------------------+----------+----------------------------------------------+
| System BLAS/LAPACK/MKL        | **No**   | Fully bundled in ``libgla``                  |
+-------------------------------+----------+----------------------------------------------+

All dependencies can be collected automatically using the provided **deploy.py** script.

.. note::

   On macOS arm64, the engine uses Apple's Accelerate framework for optimized linear algebra. Accelerate is a system framework present on all macOS installations -- no additional distribution is required.

List of Files To Distribute
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are several files which must be distributed with your application in order for the application to be able to use the **GRTE**. The list of files differs between platforms.


Windows 
^^^^^^^^

On Windows, the necessary files are (located in GAUSS installation directory):

1. The **.gcg** file containing compiled declarations of all global variables and procedures needed by the application.

2. Steps 3-6 can be skipped with this method. Use the provided ‘\ **deploy.py**\ ’ Python script to copy the dependencies to a different directory. This script will run with Python 2 or Python 3. GAUSS user code dependencies are not copied automatically.

..

   usage: deploy.py [-h] [--with-graphics] [--with-database] [--with-qt]

   [--dest DEST]

   file

   positional arguments:

   file Binary to distribute

   optional arguments:

   -h, --help show this help message and exit

   --with-graphics Enable graphics functionality. Adds additional dependencies

   --with-database Enable database functionality. Adds additional dependencies

   --with-qt Enables graphics and database functionality. Identical to

   --with-graphics and --with-database. Adds additional

   dependencies

   --dest DEST Output directory to deploy to

An example after building the provided ‘mtcall’ example would be:

C:\\Python34\\python.exe deploy.py mtcall.exe

The files required to run mtcall.exe would now be located in the default deployment directory (‘dist’ in the current working directory).

3. The shared library files: **gauss.dll, readstat.dll, iconv.dll, gla.dll, cityhash.dll, hdf5.dll, zlib.dll, szip.dll, tbb.dll, tbbmalloc.dll, TecIO.dll, libiomp5md.dll, libxl.dll, mtengrt.dll, pthreadVC2.dll,** and **xls.dll.**

4. Database functionality

   a. If your program uses the **GAUSS** database functionality, then you will also need to distribute: **cql.dll**, **Qt5Core.dll** and **Qt5Sql.dll**.

   b. If your program does NOT use the **GAUSS** database functionality, then you can rename **cql_stubs.dll** to **cql.dll** and add this file to your project.

5. The **GAUSS** configuration file, **gauss.cfg**. The distributed copy of **gauss.cfg** must have both the *user_lib* and *gauss_lib* options set to **off**. By default, they are both set to **on**.

6. A license file with the **MTGRTE** feature, which must have a **g.gkf** file name and be located in the directory containing the shared library and configuration files.

7. The target machine will also need the Microsoft Visual C++ 2015 Redistributable Package for your target architecture (32-bit or 64-bit). This can be freely obtained from the Microsoft Download Center.


Linux 
^^^^^^

On Linux, the necessary files are (located in GAUSS installation directory as well as ‘bin’ directory):

1. The **.gcg** file containing compiled declarations of all global variables and procedures needed by the application.

2. Steps 3-6 can be skipped with this method. Use the provided ‘\ **deploy.py**\ ’ Python script to copy the dependencies to a different directory. This script will run with Python 2 or Python 3. GAUSS user code dependencies are not copied automatically.

..

   usage: deploy.py [-h] [--with-graphics] [--with-database] [--with-qt]

   [--dest DEST]

   file

   positional arguments:

   file Binary to distribute

   optional arguments:

   -h, --help show this help message and exit

   --with-graphics Enable graphics functionality. Adds additional dependencies

   --with-database Enable database functionality. Adds additional dependencies

   --with-qt Enables graphics and database functionality. Identical to

   --with-graphics and --with-database. Adds additional

   dependencies

   --dest DEST Output directory to deploy to

An example after building the provided ‘mtcall’ example would be:

python deploy.py mtcall

The files required to run mtcall would now be located in the default deployment directory (‘dist’ in the current working directory).

3. The shared library files **libgauss.so, libreadstat.so, libiconv.so, libgla.so, libcityhash.so, libhdf5.so, libszip.so, libtbb.so, libtbbmalloc.so, libiomp5.so, libmtengrt.so** and **libxl.so.**

4. Database functionality

a. If your program uses the **GAUSS** database functionality, then you will also need to distribute: **libcql.so**, **libQtCore.so.5** and **libQtSql.so.5**.

b. If your program does NOT use the **GAUSS** database functionality, then you can rename **libcql_stubs.so** to **libcql.so** and add this file to your project.

5. The **GAUSS** configuration file, **gauss.cfg**. The distributed copy of **gauss.cfg** must have both the *user_lib* and *gauss_lib* options set to **off**. By default, they are both set to **on**.

6. A license file with the **MTGRTE** feature, which must have a **g.gkf** file name and be located in the directory containing the shared library and configuration files.


macOS 
^^^^^^

On macOS, the necessary files are (Located in GAUSS installation directory as well as ‘redist’ directory):

1. The **.gcg** file containing compiled declarations of all global variables and procedures needed by the application.

2. Steps 3-6 can be skipped with this method. Use the provided ‘\ **deploy.py**\ ’ Python script to copy the dependencies to a different directory. This script will run with Python 2 or Python 3. GAUSS user code dependencies are not copied automatically.

..

   usage: deploy.py [-h] [--with-graphics] [--with-database] [--with-qt]

   [--dest DEST]

   file

   positional arguments:

   file Binary to distribute

   optional arguments:

   -h, --help show this help message and exit

   --with-graphics Enable graphics functionality. Adds additional dependencies

   --with-database Enable database functionality. Adds additional dependencies

   --with-qt Enables graphics and database functionality. Identical to

   --with-graphics and --with-database. Adds additional

   dependencies

   --dest DEST Output directory to deploy to

An example after building the provided ‘mtcall’ example would be:

python deploy.py mtcall

The files required to run mtcall would now be located in the default deployment directory (‘dist’ in the current working directory).

3. The shared library files **libgauss.dylib, libreadstat.dylib, libiconv.dylib, libgla.dylib, libcityhash.dylib, libhdf5.dylib, libszip.dylib, libtbb.dylib, libtbbmalloc.dylib, libiomp5.dylib, libmtengrt.dylib** and **libxl.dylib.**

4. Database functionality

a. If your program uses the **GAUSS** database functionality, then you will also need to distribute: **libcql.dylib**, **QtCore** and **QtSql**.

b. If your program does NOT use the **GAUSS** database functionality, then you can rename **libcql_stubs.dylib** to **libcql.dylib** and add this file to your project.

5. The **GAUSS** configuration file, **gauss.cfg**. The distributed copy of **gauss.cfg** must have both the *user_lib* and *gauss_lib* options set to **off**. By default, they are both set to **on**.

6. A license file with the **MTGRTE** feature, which must have a **g.gkf** file name and be located in the directory containing the shared library and configuration files.

Setting the Home Directory 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before the end user is able to run the application, the home path for the **GAUSS Run-Time Engine** must be set, so it can find the shared library, configuration, and license files. There are three ways to do this:

1. The end user can set the environment variable **MTENGHOME26** to the path of the directory containing the shared library and configuration files.

2. You can specify the name of a new home environment variable in your application with **GAUSS_SetHomeVar**. The end user would then need to set that environment variable to the path of the directory containing the shared library and configuration files.

3. You can include code in your application that will find the correct path and set it using **GAUSS_SetHome**.

..

   On **Linux**, the following environment variables must be set:

1. The path of the directory containing the shared library files must also be included in the environment variable **LD_LIBRARY_PATH**, or the shared library files must be placed in the canonical system location. To reference shared library files that exist in MTENGHOME26, the following two paths must be added to LD_LIBRARY_PATH:

export LD_LIBRARY_PATH=$MTENGHOME26:$MTENGHOME26/bin

2. If using database functionality (linking against libcql.so) or graphics (libsgsgraphics.so), then the following environment setup is required:

..

   export QT_QPA_PLATFORM=offscreen

   export QT_PLUGIN_PATH=$MTENGHOME26/plugins

unset QT_QPA_PLATFORMTHEME

The grte01 and grte02 Executables 
--------------------------------------

The **GAUSS Run-Time Engine** is shipped with two complete examples demonstrating how you may create and distribute an application that uses the functionality of **GAUSS**. These examples can be found in the main directory of your **GAUSS Engine**

installation directory. The main directory contains a **README** file, which gives instructions on building and running the examples.

Building the Executable 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The **grte01** and **grte02** examples are made up of five files:

1. **grte01.c** -the example application code for **grte01**.

2. **grte02.c** -the example application code for **grte02**.

3. **grte01.gau** -the **GAUSS** program file containing declarations of all of the global variables and procedures that are used in **grte01**.

4. **grte02.gau** -the **GAUSS** program file containing declarations of all of the global variables and procedures that are used in **grte02**.

5. Makefile - the Makefile needed to build the **grte01** and **grte02** executables.

To build the application, you must make the **grte01** and **grte02** executables and compile **grte01.gau** and **grte02.gau** into **grte01.gcg** and **grte02.gcg** respectively. You may use either the compile command from the command line interface, **engauss**, or the GUI version, gauss, or the **GC** compiler to compile the **.gau** file.

Including the Necessary Files 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After building the example applications, you should create a directory named **distribute** and copy all of the files needed to run the application into **distribute** as follows:


Windows 
^^^^^^^^

1. Copy or move **grte01.exe, grte02.exe, grte02.gcg,** and **grte01.gcg** into **distribute**.

2. Copy the shared library files **gauss.dll, readstat.dll, iconv.dll, gla.dll, cityhash.dll, hdf5.dll, zlib.dll, szip.dll, tbb.dll, tbbmalloc.dll, TecIO.dll, libiomp5md.dll, libxl.dll, mtengrt.dll, pthreadVC2.dll,** and **xls.dll,** as well as the **GAUSS** configuration file, **gauss.cfg**, from your **GAUSS Engine** installation directory into **distribute**. Then set both the *user_lib* and *gauss_lib* options in the **distribute** copy of **gauss.cfg** to **off**.

3. Copy your **GAUSS Run-Time Engine** license file (which should be called **g.gkf**) into the **distribute** directory.


Linux 
^^^^^^

1. Copy or move **grte01, grte02, grte02.gcg,** and **grte01.gcg** into **distribute**.

2. Copy the shared library files **libgauss.so, libreadstat.so, libiconv.so, libgla.so, libcityhash.so, libhdf5.so, libszip.so, libtbb.so, libtbbmalloc.so, libiomp5.so, libmtengrt.so** and **libxl.so**, as well as the **GAUSS** configuration file, **gauss.cfg**, from your **GAUSS Engine** installation directory into **distribute**. Then set both the *user\_ lib* and *gauss\_ lib* options in the distribute copy of **gauss.cfg** to **off**.

3. Copy your **GAUSS Run-Time Engine** license file (which should be called **g.gkf**) into the **distribute** directory.


macOS
^^^^^

1. Copy or move **grte01, grte02, grte02.gcg,** and **grte01.gcg** into **distribute**.

2. Copy the shared library files **libgauss.dylib, libreadstat.dylib, libiconv.dylib, libgla.dylib, libcityhash.dylib, libhdf5.dylib, libszip.dylib, libtbb.dylib, libtbbmalloc.dylib, libiomp5.dylib, libmtengrt.dylib** and **libxl.dylib**, as well as the **GAUSS** configuration file, **gauss.cfg**, from your **GAUSS Engine** installation directory into **distribute**. Then set both the *user\_ lib* and *gauss\_ lib* options in the distribute copy of **gauss.cfg** to **off**.

3. Copy your **GAUSS Run-Time Engine** license file (which should be called **g.gkf**) into the **distribute** directory.

Running the Executable 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After copying the files as specified above, the **distribute** directory should contain all of the files needed to run the **grte01**

and **grte02** executables. This will allow the example to run if it is moved to another location.
