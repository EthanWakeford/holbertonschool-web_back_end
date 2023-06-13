--creates a table onto any database

CREATE TABLE IF NOT EXISTS 'users' (
    id int,
    email varchar(255) NOT NULL ,
    UNIQUE (EMAIL)
    name varchar(255)
);    
