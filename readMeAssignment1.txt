COMP-348 Assignment 1
Ayman Bohsali
40231988

How to test the program:

-For option 1, enter any username: if this username is one of the names in the list in the file, you will be asked to try another username, until a valid username is entered.
-For option 2, the list of movies will be displayed.
-For option 3, try to rate a movie using any of the given usernames, and when the first request is complete, enter option 3 again and rate a movie with a newly registered username. The rating has to be a double between 1.0 and 5.0, or else it will not be registered.
-For option 4, first try to enter a given username (bob and ashton recommended). For example, if the user enters Bob, the movies recommended should be Pulp Fiction, Forest Gump, The Matrix, and The Silence of the Lambs, each with the predicted ratings depending on the average of the ratings by other users. Movies that are not rated by any user will not be listed.
-For an invalid option input, the program will keep requesting for a valid one until the user enters it.

*For ease of running the program multiple times, when you do option 3 the first time, the user_ratings.txt file will have changed, so you can copy the ratings from the spare_ratings.txt file and replace them with the updated ratings in the original file.