# Data Modeling with Postgres

## Introduction

The purpose of this project is to create an ETL (Extract, Transform, Load) pipeline for the **Sparkify** music start-up. Raw **songs** and *songplays** data files are provided in JSON format under the data folder. In this project, we extract data from those files and organize it in our Sparkify database.
Once in the database, data analysts will be able to perform various SQL queries on our data and identify insights.

## Database design/schema

To design the database, we opted for a simple STAR schema. The STAR schema below constists of a FACT table (Song Plays) surrounded by various DIMENSIONS (users, songs, artists and time)

Here is an overview of our schema:

 ![Database design](/DBdesign.JPG)

This design is helpful as it isolates all the key dimensions from each-other. We can easily add a song, user or artist without having to revamp the database. Also, we have a songplays table, which is the center piece of our design. It enables us to query all historical logs with the right level of details.

## Project Steps

We took on the following steps to resolve this project:

1. Create various queries to drop tables, create tables, insert data into tables and find (select) data in the tables.
2. The "create_queries.py" Python script is used to create (refresh) all tables using the sql_queries.py file.
3. Worked in the etly.ipynb Jupyter Notebook to experiment with the data and convert this data into tables.
4. We also used the test.ipynb notebook to validate our actions/queries via SQL commands.

## Instructions

To run the project, simply run the following commands in the shell:
- python create_queries.py
- python etl.py

Note that all connections to our Sparkify database need to be stopped before running those commands. If a notebook is connected to our database, we can "kill" that connection by refreshing/reseting the Jupyter notebook.

Then, within test.ipynb, we can verify how the database was successfully populated.

## Additional Comments

In our initial approach, we used an insert SQL command to add each record to the database. Postgres actually provides a mechanism to insert data in bulk mode. This is the "copy_from" command. It is more efficient since we only need to perform 1 commit command after the bulk insert. The idea is to create dataframes and copy their data to the database using the copy_from command. Unfortunately, we can't copy as such because the object from which the data gets copied from needs to have a read method. Dataframes don't support this. So, we can address this problem by either save dataframes into a csv format and read it to create the various tables. Better, we could create an IO stream (in memory) from the data frames and feed the database using that stream.
