# Assignment 6 - Bookstore Part I

Name: Lujun Lyu

## Description

This bookstore contains fiction, programming, economics and business, and science books. The SQLite database contains four categories and twelve books. The Python CLI lets users view, search, add, update, and delete books. I also added a search by author feature (option 9).

## Create the database

Open a terminal in this folder and run:

```bash
sqlite3 bookstore.db < createTables.sql
sqlite3 bookstore.db < insertRows.sql
```

These commands reset the tables and load the original sample data. A populated `bookstore.db` is already included.

If the SQLite command-line tool is not installed, the database can also be created using Python:

```bash
python -c "import sqlite3; c=sqlite3.connect('bookstore.db'); c.executescript(open('createTables.sql').read()); c.executescript(open('insertRows.sql').read()); c.close()"
```

## Run the program

```bash
python3 bookstore_cli.py
```

Select an option from the menu. No external Python packages are needed.

The image fields store filenames only. Prices are sample prices in US dollars.
