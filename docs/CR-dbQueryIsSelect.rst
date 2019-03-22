
dbQueryIsSelect
==============================================

Purpose
----------------

Reports whether the specified query is a ``SELECT`` statement.

Format
----------------
.. function:: dbQueryIsSelect(qid)

    :param qid: query number.
    :type qid: scalar

    :returns: ret (*scalar*), 1 if the query is a ``SELECT`` statement or 0 otherwise.

Examples
----------------

::

    qid = dbExecQuery(db_id, "SELECT * 
        FROM PEOPLE");
    
    dbQueryIsSelect(qid); // True
    
    qid = dbExecQuery(db_id, "INSERT INTO 
        PEOPLE (fname, lname) VALUES 
        ('John', 'Doe');");
    
    dbQueryIsSelect(qid); // False

