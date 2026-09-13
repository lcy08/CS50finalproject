from datetime import date
import csv
import sys

class Book:
    def __init__(self, title, total_pages):
        self.title = title
        self.total = int(total_pages)

    def __str__(self):
        return f"Your progres for {self.title} is on page {self.read} of {self.total}"

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not title:
            raise ValueError("A book must have a title")
        self._title = title

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total_pages):
        if not total_pages:
            raise ValueError("A book must have a page")
        if total_pages < 0:
            raise ValueError("Negative Total Book Pages")
        self._total = total_pages

    def reading(self, n):
        self.read = int(n)

    def progress(self, n):
        self.read += int(n)

    @property
    def read(self):
        return self._read

    @read.setter
    def read(self, n):
        if n < 0:
            raise TypeError("Your progress must not be negative")
        elif n > self.total:
            raise TypeError(
                "Your progress is passing the total pages, are you done reading the book?"
            )
        self._read = n


def main():
    while True:
        mode = (
        input("Do you want to *create* (c) or do you have previous data (p)? \n")
        .lower()
        .strip()
        )
        if books:=get_books(mode):
            break
        else:
            continue
    if books:
        print(books)
        books.progress(get_pages(books))
    else:
        sys.exit("Failed to create or open the book data")

    rewrite_data(books)
    print(books)

def get_books(mode):
    if mode == "c":
        title = get_title()
        if title in previous_title():
            sys.exit("Book already on the list")
        page = int(input("How many pages does it have? "))

        if create_data(title, page):
            sys.exit(
                "Book has been added to the list, run program again to add progress to the book"
            )
        else:
            sys.exit(
                "Fail to add Book to the list"
            )

    elif mode == "p":
        print("Previous Existed Title")
        prev_title = previous_title()
        for title in prev_title:
            print(f"    {title}")
        title = get_title()
        if title not in previous_title():
            sys.exit("Book not on the previous list, create the book's data first")
        data = load_data(title)
        for row in data[-1:]:
            book = Book(row["Title"], row["page"])
            book.reading(row["on page"])
        return book

    else:
        print("Invalid inputs")
        return False

def previous_title():
    title = []
    with open("books.csv", "r") as file:
        reader = csv.DictReader(file)
        for book in reader:
            title.append(book['Title'])

        return title

def get_title():
    return input("What's the book title? ").title().strip()


def create_data(title, page):
    with open(f"{title}.csv", "w") as file:
        writer = csv.DictWriter(
            file, fieldnames=["Title", "Total Pages", "Current Page", "Date"]
        )
        writer.writeheader()
        writer.writerow(
            {
                "Title": title,
                "Total Pages": page,
                "Current Page": 0,
                "Date": date.today(),
            }
        )

    with open("books.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["Title", "Date Added"])
        writer.writerow({"Title": title, "Date Added": date.today()})

    return True


def load_data(title):
    rows = []
    with open(f"{title}.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append({"Title": row["Title"], "page": row["Total Pages"], "on page": row["Current Page"]})
    return rows

def get_pages(book):
    while True:
        try:
            pages = int(input(f"How many pages u read today for {book.title}? "))
        except ValueError:
            print("Invalid inputs, try number instead")
            continue
        else:
            if pages+book.read > book.total:
                while True:
                    b = (input("Looks like it's passing the total pages, are you done reading the books? (y or n) ").lower().strip())
                    if b == 'y':
                        break
                    elif b == 'n':
                        return get_pages(book)
                    else:
                        print("Invalid input")
                        continue
                pages = book.total-book.read
            return pages

def rewrite_data(book):
    with open(f"{book.title}.csv", "a") as file:
        writer = csv.DictWriter(
            file, fieldnames=["Title", "Total Pages", "Current Page", "Date"]
        )
        writer.writerow(
            {
                "Title": book.title,
                "Total Pages": book.total,
                "Current Page": book.read,
                "Date": date.today(),
            }
        )
    return True

if __name__ == "__main__":
    main()
