
Interactive Data Import
======================================


The GAUSS **Data Import** window is an interactive environment for loading data from:

* CSV and other text delimited files.
* Excel files (XLS, XLSX).
* GAUSS datasets (DAT) and matrix files (FMT).
* SAS, Stata and SPSS datasets.

as well as performing all aspects of data import, such as:

* Selecting variables and changing their types.
* Selecting observations by range or logical filtering.
* Managing date formats and category labels.
* Previewing data.

.. figure:: ../_static/images/data-import-window-1.jpg


Open the Data Import window
--------------------------------------------

.. figure:: ../_static/images/data-import-project-folder.jpg


You can open the **Data Import** window in three ways:

* Select data **File > Import Data** from the main GAUSS menu bar. 
* From the **Project Folders** window:

    * Double-click on the name of the data file.
    * Right-click the file and select **Import Data** from the context menu.


Change the name of the matrix, or dataframe that is imported
---------------------------------------------------------

.. figure:: ../_static/images/data-import-symbol-name.png
    :scale: 50%

The **Symbol Name** text box in the **Data Import** window controls the name of the new matrix or dataframe that will be created. By default, this will be the name of the data file.


Can I find the code to import my data?
---------------------------------------------------------

.. figure:: ../_static/images/data-import-code-generation.png
    :scale: 50%

The **Data Import** window auto-generates code to perform all the import and filter steps. This is the actual code that is run to import the data. Therefore, you can copy-and-paste this code from the **Command History** to a program file to repeat these steps. 


Managing import options
---------------------------------------------------------

.. figure:: ../_static/images/data-import-import-options-csv.png
    :scale: 50%


The **Import Options** tab lets you specify various aspects of data import, such as:

**Import**

* **Keep Metadata**: If checked, the data will be imported as a dataframe with variable names and column type information (category, date, numeric, string). Otherwise the data will be imported as a matrix or string array.
* **Import As**: This dropdown allows you to import the data as a string array instead of a matrix or dataframe.

**File**

* **Header row**: GAUSS automatically locates the most likely header row. To specify a different header row, enter the row number in the **Header Row** text box. 
* **Sheets** (Excel only) Selects which sheet to load data from. 
* **Separator** (CSV only) Select one of several common data delimiters from a list or set a custom delimitor.
* **Quote** (CSV only) Sets the quote character to a single or double-quote.

**Selection**

* **Row range**: Controls the rows of data to be imported. This should not include the variable names, if present.


Navigation and Data Preview
=================================

How can I bring a variable in my dataset into view to preview?
------------------------------------------------------------------

Select the variable you wish to bring into view and the View  [image of icon here] option will appear. 
Click [image of icon here] View and the preview window will shift to bring that variable into view. This is particularly useful for wide datasets with many variables. 

How can I find specific variables on the variable list?
------------------------------------------------------------------

Type the filter keywords in the Filter box on the Variables tab to search for variables containing certain keywords. 

How can I select multiple of variables?
------------------------------------------------------------------

You can select multiple variables within the Variables tab by clicking on a variable name while pressing the `Control` key.

[image of multiple variables selected on variables list]

How can I select a group of variables?
------------------------------------------------------------------

Click on the name of the first variable in the group. 
Press `Control+Shift` and click on the name of the last variable in the group. 
You may now perform actions on this entire group such as changing the variable types, selecting the variables for import.

				[Image of group of variables selected on variables list]

IMPORTING DATA SUBSET
=================================

How do I select subsets of variables to import?
------------------------------------------------------------------

The **Variables** tab in the **Data Import** window allows you to select which variables in a data set are imported. 
By default, all variables are selected for import.

Clear the variable checkbox if you do not want to import that variable. 

How can I control which rows are imported?
------------------------------------------------------------------

You can specify both the starting and ending row in the **Row Range** text box located in the  **File** pane of the **Import Options** tab. 
Note that GAUSS picks the starting row based on the location of header rows. 

Data Filtering
=================================

How can I filter values to be imported?
------------------------------------------------------------------

[Image of filter tab] 

Use the **Variable** name drop-down list on the **Filter** tab to select a variable to use for filtering.

Select the desired filtering operation from the Operation drop-down lists. This list changes depending on the type of the variable selected.  [INSERT TABLE OF TYPES AND FILTERING OPTIONS]

Enter the filtering condition value in the text box.

Click [IMAGE of Add Condition Button]. Add 

Can I remove a filtering condition?
------------------------------------------------------------------

Click  [IMAGE of Remove Condition Button] Remove to remove a filtering condition.

How can I hide filtered observations from view?
------------------------------------------------------------------

Check the Hide Filtered Rows/Columns options on the Filter tab. 

DATA TYPES AND FORMATS
===========================

Dates
------------------------------------------------------------------

How do I import dates into GAUSS?
------------------------------------------------------------------

GAUSS uses an internal smart date detector to data which represents dates and times. 

If a date variable is not determined by GAUSS as a date, you can select Date from the Type drop-down list on the Variable tab. 
When a variable type is changed to Date, a Specify Date Format dialog automatically opens.

How can I specify my date format?
------------------------------------------------------------------

[Image of the Specify Date Format dialog]

If GAUSS does not automatically detect your date format, you will be asked to manually specify a date format using the Specify Date Format dialog. 
The dialog Specify Date Format dialog provides a list of BSD strftime format specifiers, along with a sample and description. 
Type the desired specifier in the Date Format box or may select specifiers from the BSD specifier list. 

As you build your date format, a sample date will be dynamically created. 

To more quickly locate the desired specifier, you can use the Pattern Filter drop-down list to filter specifiers by categories such as day specifiers, month specifiers, or hour specifiers. 
Our blog “Reading dates and times in GAUSS” provides additional information on this topic. 

String type
------------------------------------------------------------------

How can I change my variable to a string type?
------------------------------------------------------------------

To specify a variable as a string, select String from the Type drop-down list on the Variables tab of the **Data Import** window. 
When a variable is specified as a string type, it attaches string labels to underlying numeric variables. 
This allows you to view string labels when printing your matrix.

Category type
------------------------------------------------------------------

How can I specify my variable to be a category?
------------------------------------------------------------------

To specify that a variable is a categorical variable, select Category from the Type drop-down list on the Variables tab of the **Data Import** window. 

How can I change the category mapping?
------------------------------------------------------------------

When you change a variable to a category, a [image of the hamburger menu] Menu will appear next to the variable. This will open a Modify Column Mapping dialog. 

Enter the desired label in the Renamed Label textbox next to the category label you want to change.
Click [image of OK button in Modify Column Mapping] to apply the new category labels. 

How can I specific categories to be the base case?
------------------------------------------------------------------

Open [image of the hamburger menu] the Menu next to the categorical variable of interest. This will open the Modify Column Mapping dialog.
The Key column indicates the ordering of the categories. The category with the Key equal to zero is used as the base case in all GAUSS estimation procedures. 
To change the base case select the Label of the category you want to be the new base case. 

Click [image of the double arrow button in the modify column mapping dialog] to move the selected category to the base case. 

How can I count the number of categories in my categorical data?
------------------------------------------------------------------
Open [image of the hamburger menu] the Menu next to the categorical variable of interest. This will open the Modify Column Mapping dialog.
The count of categories will be located in the upper right hand corner of the Modify Column Mapping dialog. 
[Image of the Category Count in the Modify Column Mapping]

Numeric type	
------------------------------------------------------------------

How can I convert my data to a numeric variable?
------------------------------------------------------------------

To specify a variable as a numeric variable, select String from the Type drop-down list on the Variables tab of the **Data Import** window. 

