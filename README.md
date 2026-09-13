# BOOK'S TBR LIST AND READING PROGRESS

Lucky Feliyanto
Indonesia

#### Video Demo: https://youtu.be/i-809MTjO90

#### Description:

It's a simple books tbr listing using csv and have the ability to save reading progression.

Run the program 

```Shell
python project.py
```

First we have to create the book data by using the "c" option. This will create the csv data for the book and add it to the tbr list (`books.csv`). After that we rerun the program and choose "p" option to update the reading progress, the program will be present the list of books first and asking whats the title you would like to update and then ask how many pages you read today for the book. If you update it passing the total pages you submit at the time you create the book's data, the program then ask you "are you done with the book?", if yes then the program update it to the total pages. If no, then the program reprompt the user to input the correct number of pages.

I created a book class to implement a book title, total pages the book have, and the progression of pages the book had. And then I implement the choice of creating or using previous data. This is so the data of the previous run did not overwritten by the data of which is created after the previous run if it had the same name.

And then I created a function to call the previous title from the `books.csv` to give the users a view of what to type if they choose the "p" option.

Then I made a function call get_title, just so I standardize the format of the book title.

create_data function being called by the "c" option create the data, namely, the csv file for individual books and the title list in the `books.csv`.

continue to the load_data function, called by the "p" option. This function return a row of the current file status for the book. So then the last row of data can be use to make the Book properties.

The get_pages function just filtering the input from the users for the question of How many pages they read for the current book loaded. The input should be a number and not passing the book's total pages.

and then finally, the rewrite_data function, use the updated Book properties to append the new data to the book csv file. Appending this data, the author is hoping to implement visualizing the progressiong of the reading the user did from day 0 to the day of finishing the book.

Thank You,
Lucky Feliyanto
