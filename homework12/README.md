Task:

Using ORM framework of your choice, create models classes created in Homework 6 (Teachers, Students, Homework and others). - Target database should be sqlite (filename main.db localted in current directory) - ORM framework should support migrations.

Utilizing that framework capabilities, create
a migration file, creating all necessary database structures.
a migration file (separate) creating at least one record in each created database table
(*) optional task: write standalone script (get_report.py) that retrieves and stores the following information into CSV file report.csv
for all done (completed) homeworks:
Student name (who completed homework) Creation date Teacher name who created homework
Utilize ORM capabilities as much as possible, avoiding executing raw SQL queries.

To run this project:

1.Copy link to this repo `git clone https://github.com/IuliiaLanchuk/hometasksEpam.git develop`

2.Set up used libs in this project: `pip install -r requirements.txt`

3.Download and set up SQLite on your computer. Then, in project be sure you are in the directory with file manage.py.
Then, in terminal run command `sqlite3 db.sqlite3` to connect to database.
Then enter `.tables` to see all tables in this database.
Then you can use SQL queries fo fetch data from database, for example,
`select * from <table_name>;` or others.
Use `exit` to close database connection.

4.To see all data in database you also can use `python manage.py runserver`. Be sure you are in the directory with file manage.py.
In browser go to `http://127.0.0.1:8000/admin`, enter through user `admin`, password 27011996.

5.In '.../my_project/migrations' directory there are all migration files
In case you need to change models, for example, add field or delete model, do changes and then run command
`python manage.py makemigrations`. Be sure you are in the directory with file manage.py. Finally, you need to apply this changes
 to database, so you need to run `python manage.py migrate`.

6.To run standalone script (get_report.py) use command `python get_report.py`. Be sure you are in the directory with file manage.py.
