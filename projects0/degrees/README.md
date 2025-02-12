# Degree of seperation project

This project is to find the degree of separations between two actors in the movie industry. The data is extracted from the movie database and the actors are connected based on the movies they have acted in.


## How to run

Run this project with the command 

```bash
python degrees.py [foldername]
```

this folder should have three different CSV files, the first `movies.csv` that shows movies, the second `stars.csv` which is a map between people and movies and the third one is `people.csv` that is about people.

After that it asks you two names: 1- Name of source actor, 2- Name of target actor.

Then it finds the shortest path between source to target actor.


## How to test

Test this project using `check50`, first install `check50` using `pip`:

```bash
pip install check50
```

then you can test this program by running following command:

```bash
check50 ai50/projects/2024/x/degrees
```