# Project Title: SQL Introduction

## Overview
Welcome to the SQL Introduction project! In this project, you will delve into the world of databases, specifically focusing on MySQL. The project covers fundamental concepts such as creating databases, tables, and executing various SQL queries. By the end of this project, you'll have a solid understanding of databases, relational databases, and MySQL.

## Table of Contents
1. [Concepts](#concepts)
2. [Resources](#resources)
3. [Learning Objectives](#learning-objectives)
4. [Requirements](#requirements)
5. [Installation](#installation)
6. [Tasks](#tasks)
    - [Task 0: List Databases](#task-0-list-databases)
    - [Task 1: Create a Database](#task-1-create-a-database)
    - [Task 2: Delete a Database](#task-2-delete-a-database)
    - [Task 3: List Tables](#task-3-list-tables)
    - [Task 4: First Table](#task-4-first-table)
    - [Task 5: Full Description](#task-5-full-description)
    - [Task 6: List All in Table](#task-6-list-all-in-table)
    - [Task 7: First Add](#task-7-first-add)
    - [Task 8: Count 89](#task-8-count-89)
    - [Task 9: Full Creation](#task-9-full-creation)
    - [Task 10: List by Best](#task-10-list-by-best)
    - [Task 11: Select the Best](#task-11-select-the-best)
    - [Task 12: Cheating is Bad](#task-12-cheating-is-bad)
    - [Task 13: Score Too Low](#task-13-score-too-low)
    - [Task 14: Average](#task-14-average)
    - [Task 15: Number by Score](#task-15-number-by-score)
    - [Task 16: Say My Name](#task-16-say-my-name)
    - [Task 18: Temperatures #0](#task-18-temperatures-0)
    - [Task 19: Temperatures #1](#task-19-temperatures-1)
    - [Task 20: Temperatures #2](#task-20-temperatures-2)

## Concepts
- **Databases**: Understanding the basics of databases.
- **MySQL**: Learning the fundamentals of MySQL.
- **SQL**: Getting acquainted with Structured Query Language.
- **DDL and DML**: Exploring Data Definition Language and Data Manipulation Language.

## Resources
Before starting the project, it's recommended to review the following resources:
- [What is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaPeM)
- [A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)
- [Basic SQL Statements: DDL and DML](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php)
- [SQL Technique: Functions](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php)
- [SQL Technique: Subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
- [What makes the big difference between a backtick and an apostrophe?](https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458)
- [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)
- [Installing MySQL in Ubuntu 20.04](https://phoenixnap.com/kb/install-mysql-ubuntu-20-04)

## Learning Objectives
By the end of this project, you are expected to:
- Explain the concepts of databases and relational databases.
- Define SQL and MySQL and understand their roles.
- Create and modify databases and tables.
- Execute SQL queries for selecting, inserting, updating, and deleting data.
- Utilize MySQL functions and understand the significance of subqueries.

## Requirements
- **Allowed Editors**: vi, vim, emacs
- **Operating System**: Ubuntu 20.04 LTS
- **MySQL Version**: 8.0.25
- **File Standards**: All files should end with a new line.
- **SQL Query Comments**: All SQL queries should have comments just before.
- **File Comments**: All files should start with a comment describing the task.
- **Uppercase Keywords**: All SQL keywords should be in uppercase.
- **README.md**: A README.md file at the root of the project folder is mandatory.

## Installation
Follow these steps to install MySQL 8.0 on Ubuntu 20.04 LTS:
```bash
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$ sudo mysql
```

## Tasks

### Task 0: List Databases
```bash
$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
```

### Task 1: Create a Database
```bash
$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
```

### Task 2: Delete a Database
```bash
$ cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
```

### Task 3: List Tables
```bash
$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
```

### Task 4: First Table
```bash
$ cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

### Task 5: Full Description
```bash
$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

### Task 6: List All in Table
```bash
$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

### Task 7: First Add
```bash
$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

### Task 8: Count 89
```bash
$ cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
```

### Task 9: Full Creation
```bash
$ cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

### Task 10: List by Best
```bash
$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

### Task 11: Select the Best
```bash
$ cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

### Task 12: Cheating is Bad
```bash
$ cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

### Task 13: Score Too Low
```bash
$ cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

### Task 14: Average
```bash
$ cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

### Task 15: Number by Score
```bash
$ cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

### Task 16: Say My Name
```bash
$ cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

### Task 17: Go to UTF8
```bash
$ cat 100-move_to_utf8.sql | mysql -hlocalhost -uroot -p
```

### Task 18: Temperature #0
```bash
$ cat 101-avg_temperatures.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

### Task 19: Temperatures #1
```bash
$ cat 102-top_city.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

### Task 20: Temperatures #2
```bash
$ cat 103-max_state.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

Feel free to explore, learn, and master SQL with this project. Happy coding!
