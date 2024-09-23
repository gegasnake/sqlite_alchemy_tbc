# Books & Authors Database with SQLAlchemy

This project demonstrates how to create and manipulate an SQLite database using Python and SQLAlchemy. The database consists of two tables: **Author** and **Book**, with a many-to-many relationship between them. The project uses the `Faker` library to generate random data for authors and books, and various SQLAlchemy ORM queries are used to retrieve and manipulate this data.

## Table of Contents

1. [Requirements](#requirements)
2. [Database Schema](#database-schema)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Features](#features)
6. [Queries](#queries)
7. [License](#license)

## Requirements

- Python 3.x
- SQLAlchemy
- SQLite3
- Faker Library

## Database Schema

### Author Table

| Column        | Type     | Description               |
|---------------|----------|---------------------------|
| `id`          | INTEGER  | Primary key               |
| `first_name`  | TEXT     | First name of the author  |
| `last_name`   | TEXT     | Last name of the author   |
| `birth_date`  | DATE     | Date of birth of the author|
| `birth_place` | TEXT     | Place of birth of the author|

### Book Table

| Column         | Type     | Description               |
|----------------|----------|---------------------------|
| `id`           | INTEGER  | Primary key               |
| `title`        | TEXT     | Title of the book         |
| `category`     | TEXT     | Category of the book      |
| `pages`        | INTEGER  | Number of pages           |
| `publish_date` | DATE     | Date of publication       |

### Association Table (Many-to-Many)

The many-to-many relationship between authors and books is represented using an association table:

| Column        | Type     | Description               |
|---------------|----------|---------------------------|
| `author_id`   | INTEGER  | Foreign key referencing Author |
| `book_id`     | INTEGER  | Foreign key referencing Book   |

## Installation

1. Clone the repository or download the script.

2. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   # run the script
   python main.py


## Usage

After running the script, the SQLite database books_authors.db will be created, containing two tables: Author and Book, along with an association table representing the many-to-many relationship. Randomly generated data for 500 authors and 1000 books will be inserted.

The script will also execute several ORM-based queries, such as:

- Finding the book with the most pages.
- Calculating the average number of pages in books.
- Finding the youngest author.
- Listing authors who haven't written any books.
- Finding the top 5 authors who have written more than 3 books.
- Features
Utilizes SQLAlchemy for ORM-based interaction with the SQLite database.
- Randomly generates 500 authors using the Faker library.
- Randomly generates 1000 books linked to the authors via a many-to-many relationship.
- Provides various SQLAlchemy ORM queries to analyze the data, such as retrieving the book with the most pages and listing authors without books.