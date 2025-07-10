========================================
Data Preparation Guidelines for BHATLIB
========================================

This document provides **clear, step-by-step guidelines** for preparing your data for use with the **BHATLIB** library in GAUSS.

Overview
--------

BHATLIB requires your data to be structured in a clear, consistent way to enable seamless estimation of discrete choice models. This guide will help you prepare your dataset correctly.

File Format
-----------

- Your data file should be in **any format compatible with the GAUSS `loadd` procedure** (e.g., `.csv`, `.gdat`, `.xls`, `.dta`, `etc`.).
- Ensure the file is clean and formatted with **column headers** for easy reference.

Rows: Observations
-------------------

- Each **row should represent one observation (choice situation)**.
- Each row corresponds to an individual’s decision in a specific scenario.

Columns: Alternatives and Choices
----------------------------------

- Create **separate columns for each possible alternative**.
- Use **binary coding** to represent choices:
  
  - The column for the **chosen alternative should be `1`**.
  - All other alternative columns for that row should be `0`.

- Only **one alternative should be marked as `1` per row**.

**Example:**

If a person chooses **transit (TR)** over **driving alone (DA)** or **shared ride (SR)**:

::

    Alt1_ch, Alt2_ch, Alt3_ch
    0,       0,       1

Availability of Alternatives
++++++++++++++++++++++++++++

BHATLIB allows for flexibility in specifying the **availability of alternatives** for each individual.

- **If all alternatives are available to all individuals (no restrictions):**

  - **No additional availability columns are needed in your dataset.**
  - The system will assume all alternatives are fully available for each observation.

- **If availability varies across individuals:**

  - Create **one column per alternative** to indicate availability.
  - Use **binary coding**:
    
    - `1` if the alternative is **available** to that individual.
    - `0` if the alternative is **unavailable**.

  - Example column names: `alt1_avail`, `alt2_avail`, `alt3_avail`, etc.

**Example:**

If **Alt2** is unavailable to a respondent:

::

    alt1_avail, alt2_avail, alt3_avail
    1,          0,          1

Columns: Individual-Specific Variables
---------------------------------------
- You can include additional columns for **individual-specific variables** (e.g., income, age, etc.) that may influence the choice.

Summary Checklist
------------------

✅ Use a **GAUSS `loadd` compatible file** with clear column headers.  
✅ Each **row = one observation/choice situation**.  
✅ Separate columns for each **alternative with binary choice coding** (`1` for chosen, `0` for non-chosen).  
✅ **Only one `1` per row** in choice columns.  
✅ No availability columns needed if all alternatives are available.  
✅ If availability varies, add one **binary availability column per alternative**.

Following these guidelines will ensure that your data is ready for **BHATLIB** analysis without additional restructuring, enabling a smooth and efficient estimation process.

