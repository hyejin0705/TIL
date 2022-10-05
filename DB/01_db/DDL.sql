CREATE TABLE contacts (
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL UNIQUE
);

-- 
-- rename a table
ALTER TABLE contacts RENAME TO new_contacts;


-- rename a column
ALTER TABLE new_contacts RENAME COLUMN name TO last_name;

-- add a new column to a table
ALTER TABLE new_contacts 
ADD COLUMN address TEXT NOT NULL;


-- delete a column
ALTER TABLE new_contacts 
DROP COLUMN address;


DROP TABLE new_contacts;