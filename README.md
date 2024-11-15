# Potential Enigma
This is the first in a series of repos I'll be making where I create a program based on github's recommended reposetory name!

The first repo recommendation is 'potential-enigma'. This is a tougher one, and I'm thinking of turning this into a program that serves difficult riddles to be solved.
This project is in progress, but feel free to contribute in any way you feel approriate!

## How it works
This project conststs of a riddle database, and a script that will serve the riddles to the user. This will be a simple python script that will pick a riddle based on the user input of difficulty, and then serve it to the user. The user will have to solve and return a string input as the awnser, which the script will compare with the database awnser and mark the user as correct or incorrect.

### The "database"
The database is be a simple riddles.json file with four parameters: Riddle ID, Riddle, Riddle awnser, and Difficulty.
The .py will simply fetch the file, choose a random riddle ID, and serve the corresponding riddle to the user.
