### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
PostgreSQL is a database management system that helps you work with SQL databases.

- What is the difference between SQL and PostgreSQL?
SQL is a language for working with relational databases and PostgreSQL is a database management system that uses SQL to manage the data.

- In `psql`, how do you connect to a database?
psql -d database_name

- What is the difference between `HAVING` and `WHERE`?
WHERE filters individual rows before grouping and specifies conditions that must be met by each row, HAVING filters groups of rows after grouping and filters the output 

- What is the difference between an `INNER` and `OUTER` join?
INNER JOIN returns only the rows that have matching values in both tables, while OUTER JOIN returns all the rows from one table and the matching rows from the other 

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
A LEFT OUTER JOIN returns all the rows from the left table and the matching rows from the right table, while a RIGHT OUTER JOIN returns all the rows from the right table and the matching rows from the left table

- What is an ORM? What do they do?
An ORM (Object-Relational Mapping) maps the objects in an application to the tables in a relational database

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
Requests made using AJAX are typically initiated from the client-side using JavaScript, while requests made using a library like requests are typically initiated from the server-side using Python code.

- What is CSRF? What is the purpose of the CSRF token?
CSRF (Cross-Site Request Forgery) is when somone sends false requests to a website. A CSRF token is a unique identifier that is included in web forms to prevent CSRF attacks by adding a hidden field to the form for authentication.

- What is the purpose of `form.hidden_tag()`?
Creates a hidden field in a form for adding things such as the CSRF token to be included in the form for validation but not shown to the user.
